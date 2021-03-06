import requests
from datetime import datetime
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#-----設定項目

chart_sec = 3600    # １時間足を使用
term = 30           # 過去ｎ日の設定
wait = 0            # ループの待機時間
lot = 1             # BTCの注文枚数
slippage = 0.001    # 手数料・スリッページ


# CryptowatchのAPIを使用する関数
def get_price(min, before=0, after=0):
	price = []
	params = {"periods" : min }
	if before != 0:
		params["before"] = before
	if after != 0:
		params["after"] = after

	response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc",params)
	data = response.json()
	
	if data["result"][str(min)] is not None:
		for i in data["result"][str(min)]:
			if i[1] != 0 and i[2] != 0 and i[3] != 0 and i[4] != 0:
				price.append({ "close_time" : i[0],
					"close_time_dt" : datetime.fromtimestamp(i[0]).strftime('%Y/%m/%d %H:%M'),
					"open_price" : i[1],
					"high_price" : i[2],
					"low_price" : i[3],
					"close_price": i[4] })
		return price
		
	else:
		print("データが存在しません")
		return None


# 時間と高値・安値をログに記録する関数
def log_price( data,flag ):
	log =  "時間： " + datetime.fromtimestamp(data["close_time"]).strftime('%Y/%m/%d %H:%M') + " 高値： " + str(data["high_price"]) + " 安値： " + str(data["low_price"]) + "\n"
	flag["records"]["log"].append(log)
	return flag


# ドンチャンブレイクを判定する関数
def donchian( data,last_data ):
	
	highest = max(i["high_price"] for i in last_data)
	if data["high_price"] > highest:
		return {"side":"BUY","price":highest}
	
	lowest = min(i["low_price"] for i in last_data)
	if data["low_price"] < lowest:
		return {"side":"SELL","price":lowest}
	
	return {"side" : None , "price":0}


# ドンチャンブレイクを判定してエントリー注文を出す関数
def entry_signal( data,last_data,flag ):
	signal = donchian( data,last_data )
	if signal["side"] == "BUY":
		flag["records"]["log"].append("過去{0}足の最高値{1}円を、直近の高値が{2}円でブレイクしました\n".format(term,signal["price"],data["high_price"]))
		flag["records"]["log"].append(str(data["close_price"]) + "円で買いの指値注文を出します\n")

		# ここに買い注文のコードを入れる
		
		flag["order"]["exist"] = True
		flag["order"]["side"] = "BUY"
		flag["order"]["price"] = round(data["close_price"] * lot)

	if signal["side"] == "SELL":
		flag["records"]["log"].append("過去{0}足の最安値{1}円を、直近の安値が{2}円でブレイクしました\n".format(term,signal["price"],data["low_price"]))
		flag["records"]["log"].append(str(data["close_price"]) + "円で売りの指値注文を出します\n")

		# ここに売り注文のコードを入れる
		
		flag["order"]["exist"] = True
		flag["order"]["side"] = "SELL"
		flag["order"]["price"] = round(data["close_price"] * lot)

	return flag



# サーバーに出した注文が約定したか確認する関数
def check_order( flag ):
	
	# 注文状況を確認して通っていたら以下を実行
	# 一定時間で注文が通っていなければキャンセルする
	
	flag["order"]["exist"] = False
	flag["order"]["count"] = 0
	flag["position"]["exist"] = True
	flag["position"]["side"] = flag["order"]["side"]
	flag["position"]["price"] = flag["order"]["price"]
	
	return flag


# 手仕舞いのシグナルが出たら決済の成行注文 + ドテン注文 を出す関数
def close_position( data,last_data,flag ):
	
	flag["position"]["count"] += 1
	signal = donchian( data,last_data )
	
	if flag["position"]["side"] == "BUY":
		if signal["side"] == "SELL":
			flag["records"]["log"].append("過去{0}足の最安値{1}円を、直近の安値が{2}円でブレイクしました\n".format(term,signal["price"],data["low_price"]))
			flag["records"]["log"].append(str(data["close_price"]) + "円あたりで成行注文を出してポジションを決済します\n")
			
			# 決済の成行注文コードを入れる
			
			records( flag,data )
			flag["position"]["exist"] = False
			flag["position"]["count"] = 0
			
			flag["records"]["log"].append("さらに" + str(data["close_price"]) + "円で売りの指値注文を入れてドテンします\n")
			
			# ここに売り注文のコードを入れる
			
			flag["order"]["exist"] = True
			flag["order"]["side"] = "SELL"
			flag["order"]["price"] = round(data["close_price"] * lot)
			

	if flag["position"]["side"] == "SELL":
		if signal["side"] == "BUY":
			flag["records"]["log"].append("過去{0}足の最高値{1}円を、直近の高値が{2}円でブレイクしました\n".format(term,signal["price"],data["high_price"]))
			flag["records"]["log"].append(str(data["close_price"]) + "円あたりで成行注文を出してポジションを決済します\n")
			
			# 決済の成行注文コードを入れる
			
			records( flag,data )
			flag["position"]["exist"] = False
			flag["position"]["count"] = 0
			
			flag["records"]["log"].append("さらに" + str(data["close_price"]) + "円で買いの指値注文を入れてドテンします\n")
			
			# ここに買い注文のコードを入れる
			
			flag["order"]["exist"] = True
			flag["order"]["side"] = "BUY"
			flag["order"]["price"] = round(data["close_price"] * lot)
			
	return flag


# 各トレードのパフォーマンスを記録する関数
def records(flag,data):
	#手仕舞った日時の記録
	flag["records"]["date"].append(data["close_time_dt"])
	
	# 取引手数料等の計算
	entry_price = flag["position"]["price"]
	exit_price = round(data["close_price"] * lot)
	trade_cost = round( exit_price * slippage )
	
	log = "スリッページ・手数料として " + str(trade_cost) + "円を考慮します\n"
	flag["records"]["log"].append(log)
	flag["records"]["slippage"].append(trade_cost)
	
	# 値幅の計算
	buy_profit = exit_price - entry_price - trade_cost
	sell_profit = entry_price - exit_price - trade_cost

	

	# 利益が出てるかの計算
	if flag["position"]["side"] == "BUY":
		flag["records"]["buy-count"] += 1
		flag["records"]["buy-profit"].append( buy_profit )
		flag["records"]["buy-return"].append( round( buy_profit / entry_price * 100, 4 ))
		flag["records"]["buy-holding-periods"].append( flag["position"]["count"] )
		flag["records"]["gross-profit"].append(flag["records"]["gross-profit"][-1]+buy_profit)
		if buy_profit  > 0:
			flag["records"]["buy-winning"] += 1
			log = str(buy_profit) + "円の利益です\n"
			flag["records"]["log"].append(log)
		else:
			log = str(buy_profit) + "円の損失です\n"
			flag["records"]["log"].append(log)
	
	if flag["position"]["side"] == "SELL":
		flag["records"]["sell-count"] += 1
		flag["records"]["sell-profit"].append( sell_profit )
		flag["records"]["sell-return"].append( round( sell_profit / entry_price * 100, 4 ))
		flag["records"]["sell-holding-periods"].append( flag["position"]["count"] )
		flag["records"]["gross-profit"].append(flag["records"]["gross-profit"][-1]+sell_profit)

		if sell_profit > 0:
			flag["records"]["sell-winning"] += 1
			log = str(sell_profit) + "円の利益です\n"
			flag["records"]["log"].append(log)
		else:
			log = str(sell_profit) + "円の損失です\n"
			flag["records"]["log"].append(log)
	
	#ドローダウンの計算
	drawdown = max(flag["records"]["gross-profit"])-flag["records"]["gross-profit"][-1]
	if drawdown > flag["records"]["drawdown"]:
		flag["records"][drawdown] = drawdown

	return flag

# バックテストの集計用の関数
def backtest(flag):
	
	buy_gross_profit = np.sum(flag["records"]["buy-profit"])
	sell_gross_profit = np.sum(flag["records"]["sell-profit"])
	
	print("バックテストの結果")
	print("--------------------------")
	print("買いエントリの成績")
	print("--------------------------")
	print("トレード回数  :  {}回".format(flag["records"]["buy-count"] ))
	print("勝率          :  {}％".format(round(flag["records"]["buy-winning"] / flag["records"]["buy-count"] * 100,1)))
	print("平均リターン  :  {}％".format(round(np.average(flag["records"]["buy-return"]),2)))
	print("総損益        :  {}円".format( np.sum(flag["records"]["buy-profit"]) ))
	print("平均保有期間  :  {}足分".format( round(np.average(flag["records"]["buy-holding-periods"]),1) ))
	
	print("--------------------------")
	print("売りエントリの成績")
	print("--------------------------")
	print("トレード回数  :  {}回".format(flag["records"]["sell-count"] ))
	print("勝率          :  {}％".format(round(flag["records"]["sell-winning"] / flag["records"]["sell-count"] * 100,1)))
	print("平均リターン  :  {}％".format(round(np.average(flag["records"]["sell-return"]),2)))
	print("総損益        :  {}円".format( np.sum(flag["records"]["sell-profit"]) ))
	print("平均保有期間  :  {}足分".format( round(np.average(flag["records"]["sell-holding-periods"]),1) ))
	
	print("--------------------------")
	print("総合の成績")
	print("--------------------------")
	print("総損益        :  {}円".format( np.sum(flag["records"]["sell-profit"]) + np.sum(flag["records"]["buy-profit"]) ))
	print("手数料合計    :  {}円".format( np.sum(flag["records"]["slippage"]) ))
	print(f'最大ドローダウン {-1 * flag["records"]["drawdown"]}円 / {-1 * round(flag["records"]["drawdown"])/max(flag["records"]["gross-profit"]) * 100,1}%')
	print("最大ドローダウン :  {0}円 / {1}％".format(-1 * flag["records"]["drawdown"], -1 * round(flag["records"]["drawdown"]/max(flag["records"]["gross-profit"])*100,1)  ))
	
	# ログファイルの出力
	file =  open("./{0}-log.txt".format(datetime.now().strftime("%Y-%m-%d-%H-%M")),'wt',encoding='utf-8')
	file.writelines(flag["records"]["log"])



# ここからメイン処理

# 価格チャートを取得
price = get_price(chart_sec,after=1483228800)

flag = {
	"order":{
		"exist" : False,
		"side" : "",
		"price" : 0,
		"count" : 0
	},
	"position":{
		"exist" : False,
		"side" : "",
		"price": 0,
		"count":0
	},
	"records":{
		"buy-count": 0,
		"buy-winning" : 0,
		"buy-return":[],
		"buy-profit": [],
		"buy-holding-periods":[],
		
		"sell-count": 0,
		"sell-winning" : 0,
		"sell-return":[],
		"sell-profit":[],
		"sell-holding-periods":[],
		
		"drawdown": 0,
		"date":[], #追加
		"gross-profit":[0], #追加
		"slippage":[],
		"log":[]
	}
}


last_data = []
i = 0
while i < len(price):

	# ドンチャンの判定に使う過去30日分の安値・高値データを準備する
	if len(last_data) < term:
		last_data.append(price[i])
		flag = log_price(price[i],flag)
		time.sleep(wait)
		i += 1
		continue
	
	data = price[i]
	flag = log_price(data,flag)
	
	
	if flag["order"]["exist"]:
		flag = check_order( flag )
	elif flag["position"]["exist"]:
		flag = close_position( data,last_data,flag )
	else:
		flag = entry_signal( data,last_data,flag )
	
	
	# 過去データを30個に保つために先頭を削除
	del last_data[0]
	last_data.append( data )
	i += 1
	time.sleep(wait)


print("--------------------------")
print("テスト期間：")
print("開始時点 : " + str(price[0]["close_time_dt"]))
print("終了時点 : " + str(price[-1]["close_time_dt"]))
print(str(len(price)) + "件のローソク足データで検証")
print("--------------------------")

backtest(flag)

# 損益曲線をプロット
del flag["records"]["gross-profit"][0] # X軸/Y軸のデータ数を揃えるため、先頭の0を削除
date_list = pd.to_datetime( flag["records"]["date"] ) # 日付型に変換

plt.plot( date_list, flag["records"]["gross-profit"] )
plt.xlabel("Date")
plt.ylabel("Balance")
plt.xticks(rotation=50) # X軸の目盛りを50度回転
	
plt.show()