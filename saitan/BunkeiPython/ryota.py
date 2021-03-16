BTCFXのドンチアンチャネルブレイクアウトBOTの実践用コード（Bitflyer用）
170

ryota_0808
2018/05/21 03:46
購入済

はじめまして、リョータです。
このnoteでは、BitflyerのBTCFXでそのまま使えるドンチアン・チャネルブレイクアウトBOTの実践用コードを販売しています。

私のブログの「バックテスト編」「資金管理編」で紹介したバックテスト用コードを実践用に修正したものです。バックテストの検証結果やパラメーター設定の方法なども全てブログで紹介しています。

文系でもわかる！自動売買BOTの始め方
https://ryota-trade.com/

上記のブログでは、pythonの環境構築の方法、APIの使い方、CCXTライブラリの使い方、BOTの作成方法、バックテストの検証方法などを全て無料で公開しています。良かったらブログの方も見てください。以下はBOTの内容です。

BOTの概要
・Bitflyer用のドンチアンチャネルブレイクアウトBOT
・CCXTライブラリを使用
・CryptowatchAPIを使用
（１時間足ではCryptocompareも使用可）

Bitflyer用のドンチアン・チャネルブレイクアウトBOTです。一定期間での最高値・最安値の更新をエントリーの条件とし、逆方向のブレイクアウトを手仕舞い・ドテンの条件とします。また平均ボラティリティから自動的に損切り（ストップ）を入れます。

口座のリスク率に応じてロット数の自動的に調整する機能、２～４回に分けてポジションを積み増しする機能、パラボリックSARを用いてストップ位置をトレイリングする機能が付いています。

設定できる項目
１．使用する時間軸
２．価格APIの取得元（Cryptowatch/Cryptocompare）
３．上値ブレイクアウトの判定期間
４．下値ブレイクアウトの判定期間
５．ブレイクアウトの判定方法（高値・安値／終値のどちらか）
６．平均ボラティリティの計算期間
７．損切のレンジ幅（直近のATRを使用）
８．口座のリスク率
９．レバレッジ倍率設定
10．ポジション積み増しの回数
11．ポジション積み増しの基準レンジ幅
12.  パラボリックSARを使ったトレイリングストップの設定
（初期値・加速度・加速上限）
13.   LINE通知機能、ログファイルの出力機能
14.   移動平均線を使ったトレンドフィルターの設定

※  ポジションの積み増し・トレイリングストップ・トレンドフィルター・ログ出力・LINE通知の機能は無効にできます。

注文の仕様
エントリー・積み増し・損切り・手仕舞いなどの注文はすべて成行注文で実行します。指値注文には対応していません。

注文条件の判定には、基準となる時間軸の確定足と、リアルタイムに形成中の足を使い分けることができます。例えば、１時間足を使用する場合、ブレイクアウトの判断を「終値」でするなら確定足を使い、「高値」「安値」でするなら形成中の足を使います。

ポジションの積み増しや損切りの判定には、リアルタイムで形成中の足を30秒おきに取得して使用します。トレイリングストップの条件の発動は、確定足の最高値・最安値の更新で判定しています。


▽「確定足」と「形成中の足」の意味

画像1

確定足・・・「終値」で何かを判定するときの最新の足（右から２番目）
形成中の足・・・「安値」「高値」で判定するときの最新の足（一番右）

バックテスト結果
バックテストの検証結果などは、私のブログの「バックテスト編」「資金管理編」を読んでいただければ、パラメーターが設定できるようになっているので、良いところも悪いところも、ご自身で納得いくまで徹底的に検証できます。

計算の過程やコードも全て公開しているので、まず先に私のブログを読むことを推奨します。特に「資金管理編」は読んで欲しいです。

参考までにオーソドックスな設定例の検証結果を貼っておきます。
パラメータはご自身で最適なものを研究して使ってください。

検証結果１（2017年9月13日～2018年5月21日）2144％

画像2

【検証の条件】

・１時間足を使用
・上値/下値ともに30期間ブレイクアウト
・ブレイクアウトの判断基準は高値・安値
・平均ボラティリティ（ATR）計算期間 30足
・初期ストップ位置 ２ATR幅
・ポジションの積み増し ４回（1/2ATR幅ごと）
・パラボリックSARの設定（初期値0.02 / 加速度合0.02 / 上限0.2）
・初期資金 30万円
・レバレッジ ３倍
・スリッページ考慮 0.2％（追加ポジション取得時・手仕舞い時に考慮）
・１トレードの上限リスク 口座の４％


【検証の結果】
--------------------------
テスト期間：
開始時点 : 2017/09/13 01:00
終了時点 : 2018/05/21 03:00
6000件のローソク足データで検証
-----------------------------------
総合の成績
-----------------------------------
全トレード数 : 128回
勝率 : 33.6％
平均リターン : 0.71％
平均利益率 : 8.54％
平均損失率 : -3.25％
損益レシオ : 2.62
平均保有期間 : 33.4足分
損切りの回数 : 105回

最大の勝ちトレード : 1669154円
最大の負けトレード : -301529円
最大連敗回数 : 10回
最大ドローダウン : -1009481円 / -18.5％
利益合計 : 10822349円
損失合計 : -4689589円
最終損益 : 6132760円

初期資金 : 300000円
最終資金 : 6432760円
運用成績 : 2144.0％
手数料合計 : -642804円
-----------------------------------
月別の成績
-----------------------------------
2017年9月の成績
-----------------------------------
トレード数 : 8回
月間損益 : -4109円
月末資金 : 295891円
-----------------------------------
2017年10月の成績
-----------------------------------
トレード数 : 16回
月間損益 : 133929円
月末資金 : 429820円
-----------------------------------
2017年11月の成績
-----------------------------------
トレード数 : 15回
月間損益 : 334125円
月末資金 : 763945円
-----------------------------------
2017年12月の成績
-----------------------------------
トレード数 : 9回
月間損益 : 563800円
月末資金 : 1327745円
-----------------------------------
2018年1月の成績
-----------------------------------
トレード数 : 19回
月間損益 : 865642円
月末資金 : 2193387円
-----------------------------------
2018年2月の成績
-----------------------------------
トレード数 : 16回
月間損益 : 768625円
月末資金 : 2962012円
-----------------------------------
2018年3月の成績
-----------------------------------
トレード数 : 14回
月間損益 : 2434229円
月末資金 : 5396241円
-----------------------------------
2018年4月の成績
-----------------------------------
トレード数 : 17回
月間損益 : 335931円
月末資金 : 5732172円
-----------------------------------
2018年5月の成績
-----------------------------------
トレード数 : 14回
月間損益 : 700588円
月末資金 : 6432760円

検証結果２（直近３カ月での検証結果）223.0%

画像3

-----------------------------------
総合の成績
-----------------------------------
全トレード数 : 49回
勝率 : 24.5％
平均リターン : -0.32％
平均利益率 : 7.52％
平均損失率 : -2.86％
損益レシオ : 2.63
平均保有期間 : 31.6足分
損切りの回数 : 42回

最大の勝ちトレード : 172671円
最大の負けトレード : -30480円
最大連敗回数 : 10回
最大ドローダウン : -103324円 / -18.3％
利益合計 : 737185円
損失合計 : -367821円
最終損益 : 369364円

初期資金 : 300000円
最終資金 : 669364円
運用成績 : 223.0％
手数料合計 : -50160円

購入前の注意事項
本コードの内容は、ブログ「文系でもわかる！自動売買BOTの作り方」の付録教材のような位置づけでの販売になります。

そのため、pythonをご自身で勉強する気のない方や、BOTを運用する環境構築の自信がない方、コピペするだけで放置で利益を期待している方は購入しないでください。初心者向けに個別にサポートすることもできません。

あくまでコーディングの例の教材としての価格設定なので、それをご理解いただける方のみご購入ください。もちろん私が実際に運用しているので、動作することは確認済ですが、想定外の不具合が出て対応が可能であればコード修正は対応します。

追記（2021/3）
2018年から３年以上動いているコードなので、それなりの耐用性はあると思いますが、現在は、初心者の方への個別サポートや返信は、ほぼ行っていません。基本的に「エラーが出ても自己解決できる」という意欲の方のみご購入をご検討ください。



以下有料部分です。

------以下有料箇所------


ここから先は有料部分です
ご購入ありがとうございます。
ここから有料箇所です。
まずはソースコードを掲載します。

Bitflyer実践用コード
import requests
from datetime import datetime
from logging import getLogger,Formatter,StreamHandler,FileHandler,INFO
from pprint import pprint
import time
import numpy as np
import ccxt

#-------------設定項目------------------------

wait = 180                   # ループの待機時間
buy_term = 30                # 最高値（上値）ブレイクアウト期間
sell_term = 30               # 最安値（下値）ブレイクアウト期間
chart_sec = 3600             # 使用する時間軸（秒換算）
chart_API = "cryptowatch"    # 価格の取得元を（cryptowatch/cryptocompare）から選択

judge_price={
  "BUY" : "close_price",     # ブレイク判断　高値（high_price)か終値（close_price）を使用
  "SELL": "close_price"      # ブレイク判断　安値 (low_price)か終値（close_price）を使用
}

volatility_term = 5          # 平均ボラティリティの計算に使う期間
stop_range = 2               # 何レンジ幅にストップを入れるか
trade_risk = 0.03            # 1トレードあたり口座の何％まで損失を許容するか
levarage = 3                 # レバレッジ倍率の設定

entry_times = 2              # 何回に分けて追加ポジションを取るか
entry_range = 1              # 何レンジごとに追加ポジションを取るか

trailing_config = "ON"       # ONで有効 OFFで無効
stop_AF = 0.02               # 加速係数
stop_AF_add = 0.02           # 加速係数を増やす度合
stop_AF_max = 0.2            # 加速係数の上限

filter_VER = "OFF"           # フィルター設定／OFFで無効
MA_term = 200                # トレンドフィルターに使う移動平均線の期間

bitflyer = ccxt.bitflyer()
bitflyer.apiKey = ''         # APIキーを設定
bitflyer.secret = ''         # APIシークレットを設定
bitflyer.timeout = 30000     # 通信のタイムアウト時間の設定

line_config = "OFF"          # LINE通知をするかどうかの設定
log_config = "OFF"           # ログファイルを出力するかの設定
log_file_path = ""           # ログを記録するファイル名と出力パス
line_token = ""              # LINE通知を使用する場合はAPIキーを入力

#-------------ログ機能の設定--------------------

# ログ機能の設定箇所
if log_config == "ON":
	logger = getLogger(__name__)
	handlerSh = StreamHandler()
	handlerFile = FileHandler( log_file_path )
	handlerSh.setLevel(INFO)
	handlerFile.setLevel(INFO)
	logger.setLevel(INFO)
	logger.addHandler(handlerSh)
	logger.addHandler(handlerFile)

#-------------注文管理の変数------------------------

flag = {
	"position":{
		"exist" : False,
		"side" : "",
		"price": 0,
		"stop": 0,
		"stop-AF": stop_AF,
		"stop-EP":0,
		"ATR": 0,
		"lot": 0,
		"count":0
	},
	"add-position":{
		"count":0,
		"first-entry-price":0,
		"last-entry-price":0,
		"unit-range":0,
		"unit-size":0,
		"stop":0
	}
}

#-------------売買ロジックの部分の関数--------------

# ドンチャンブレイクを判定する関数
def donchian( data,last_data ):
	
	highest = max(i["high_price"] for i in last_data[ (-1* buy_term): ])
	if data["settled"][ judge_price["BUY"] ] > highest:
		return {"side":"BUY","price":highest}
	
	lowest = min(i["low_price"] for i in last_data[ (-1* sell_term): ])
	if data["settled"][ judge_price["SELL"] ] < lowest:
		return {"side":"SELL","price":lowest}
	
	return {"side" : None , "price":0}

# ドンチャンブレイクを判定してエントリー注文を出す関数
def entry_signal( data,last_data,flag ):

	if flag["position"]["exist"] == True:
		return flag

	signal = donchian( data,last_data )
	if signal["side"] == "BUY":
		print_log("過去{0}足の最高値{1}円を、直近の価格が{2}円でブレイクしました".format(buy_term,signal["price"],data["settled"][judge_price["BUY"]]))
		# フィルター条件を確認
		if filter( signal ) == False:
			print_log("フィルターのエントリー条件を満たさなかったため、エントリーしません")
			return flag
		
		lot,stop,flag = calculate_lot( last_data,data,flag )
		if lot >= 0.01:
			print_log("{0}円あたりに{1}BTCで買いの成行注文を出します".format(data["settled"]["close_price"],lot))
			
			# ここに買い注文のコードを入れる
			price = bitflyer_market( "BUY", lot )
			
			print_log("{0}円にストップを入れます".format(price - stop))
			flag["position"]["lot"],flag["position"]["stop"] = lot,stop
			flag["position"]["exist"] = True
			flag["position"]["side"] = "BUY"
			flag["position"]["price"] = price
		else:
			print_log("注文可能枚数{}が、最低注文単位に満たなかったので注文を見送ります".format(lot))

	if signal["side"] == "SELL":
		print_log("過去{0}足の最安値{1}円を、直近の価格が{2}円でブレイクしました".format(sell_term,signal["price"],data["settled"][judge_price["SELL"]]))
		# フィルター条件を確認
		if filter( signal ) == False:
			print_log("フィルターのエントリー条件を満たさなかったため、エントリーしません")
			return flag
		
		lot,stop,flag = calculate_lot( last_data,data,flag )
		if lot >= 0.01:
			print_log("{0}円あたりに{1}BTCの売りの成行注文を出します".format(data["settled"]["close_price"],lot))
			
			# ここに売り注文のコードを入れる
			price = bitflyer_market( "SELL", lot )
			
			print_log("{0}円にストップを入れます".format(price + stop))
			flag["position"]["lot"],flag["position"]["stop"] = lot,stop
			flag["position"]["exist"] = True
			flag["position"]["side"] = "SELL"
			flag["position"]["price"] = price
		else:
			print_log("注文可能枚数{}が、最低注文単位に満たなかったので注文を見送ります".format(lot))

	return flag

# 損切ラインにかかったら成行注文で決済する関数
def stop_position( data,flag ):

	# トレイリングストップを実行
	if trailing_config == "ON":
		flag = trail_stop( data,flag )
	
	if flag["position"]["side"] == "BUY":
		stop_price = flag["position"]["price"] - flag["position"]["stop"]
		if data["forming"]["low_price"] < stop_price:
			print_log("{0}円の損切ラインに引っかかりました。".format( stop_price ))
			print_log(str(data["forming"]["low_price"]) + "円あたりで成行注文を出してポジションを決済します")
			
			# 決済の成行注文コードを入れる
			bitflyer_market( "SELL" , flag["position"]["lot"] )
			
			flag["position"]["exist"] = False
			flag["position"]["count"] = 0
			flag["position"]["stop-AF"] = stop_AF
			flag["position"]["stop-EP"] = 0
			flag["add-position"]["count"] = 0
	
	
	if flag["position"]["side"] == "SELL":
		stop_price = flag["position"]["price"] + flag["position"]["stop"]
		if data["forming"]["high_price"] > stop_price:
			print_log("{0}円の損切ラインに引っかかりました。".format( stop_price ))
			print_log(str(data["forming"]["high_price"]) + "円あたりで成行注文を出してポジションを決済します")
			
			# 決済の成行注文コードを入れる
			bitflyer_market( "BUY" , flag["position"]["lot"] )
			
			flag["position"]["exist"] = False
			flag["position"]["count"] = 0
			flag["position"]["stop-AF"] = stop_AF
			flag["position"]["stop-EP"] = 0
			flag["add-position"]["count"] = 0
			
	return flag

# 手仕舞いのシグナルが出たら決済の成行注文 + ドテン注文 を出す関数
def close_position( data,last_data,flag ):
	
	if flag["position"]["exist"] == False:
		return flag
	
	flag["position"]["count"] += 1
	signal = donchian( data,last_data )
	
	if flag["position"]["side"] == "BUY":
		if signal["side"] == "SELL":
			print_log("過去{0}足の最安値{1}円を、直近の価格が{2}円でブレイクしました".format(sell_term,signal["price"],data["settled"][judge_price["SELL"]]))
			print_log(str(data["settled"]["close_price"]) + "円あたりで成行注文を出してポジションを決済します")
			
			# 決済の成行注文コードを入れる
			bitflyer_market( "SELL" , flag["position"]["lot"] )
			
			flag["position"]["exist"] = False
			flag["position"]["count"] = 0
			flag["position"]["stop-AF"] = stop_AF
			flag["position"]["stop-EP"] = 0
			flag["add-position"]["count"] = 0
			
			
			# ドテン注文の箇所
			# フィルター条件を確認
			if filter( signal ) == False:
				print_log("フィルターのエントリー条件を満たさなかったため、エントリーしません")
				return flag
			
			
			lot,stop,flag = calculate_lot( last_data,data,flag )
			if lot >= 0.01:
				print_log("さらに{0}円あたりに{1}BTCの売りの成行注文を入れてドテン出します".format(data["settled"]["close_price"],lot))
				
				# ここに売り注文のコードを入れる
				price = bitflyer_market( "SELL", lot )
				
				print_log("{0}円にストップを入れます".format(price + stop))
				flag["position"]["lot"],flag["position"]["stop"] = lot,stop
				flag["position"]["exist"] = True
				flag["position"]["side"] = "SELL"
				flag["position"]["price"] = price
			
			

	if flag["position"]["side"] == "SELL":
		if signal["side"] == "BUY":
			print_log("過去{0}足の最高値{1}円を、直近の価格が{2}円でブレイクしました".format(buy_term,signal["price"],data["settled"][judge_price["BUY"]]))
			print_log(str(data["settled"]["close_price"]) + "円あたりで成行注文を出してポジションを決済します")
			
			# 決済の成行注文コードを入れる
			bitflyer_market( "BUY" , flag["position"]["lot"] )
			
			flag["position"]["exist"] = False
			flag["position"]["count"] = 0
			flag["position"]["stop-AF"] = stop_AF
			flag["position"]["stop-EP"] = 0
			flag["add-position"]["count"] = 0
			
			
			# ドテン注文の箇所
			# フィルター条件を確認
			if filter( signal ) == False:
				print_log("フィルターのエントリー条件を満たさなかったため、エントリーしません")
				return flag
			
			
			lot,stop,flag = calculate_lot( last_data,data,flag )
			if lot >= 0.01:
				print_log("さらに{0}円あたりで{1}BTCの買いの成行注文を入れてドテンします".format(data["settled"]["close_price"],lot))
				
				# ここに買い注文のコードを入れる
				price = bitflyer_market( "BUY", lot )
				
				print_log("{0}円にストップを入れます".format(price - stop))
				flag["position"]["lot"],flag["position"]["stop"] = lot,stop
				flag["position"]["exist"] = True
				flag["position"]["side"] = "BUY"
				flag["position"]["price"] = price

	return flag

#-------------トレンドフィルターの関数--------------

# トレンドフィルターの関数
def filter( signal ):
	
	if filter_VER == "OFF":
		return True
	
	if filter_VER == "A":
		if len(last_data) < MA_term:
			return True
		if data["settled"]["close_price"] > calculate_MA(MA_term) and signal["side"] == "BUY":
			return True
		if data["settled"]["close_price"] < calculate_MA(MA_term) and signal["side"] == "SELL":
			return True

	if filter_VER == "B":
		if len(last_data) < MA_term:
			return True
		if calculate_MA(MA_term) > calculate_MA(MA_term,-1) and signal["side"] == "BUY":
			return True
		if calculate_MA(MA_term) < calculate_MA(MA_term,-1) and signal["side"] == "SELL":
			return True
	return False

# 単純移動平均を計算する関数
def calculate_MA( value,before=None ):
	if before is None:
		MA = sum(i["close_price"] for i in last_data[-1*value:]) / value
	else:
		MA = sum(i["close_price"] for i in last_data[-1*value + before: before]) / value
	return round(MA)

#-------------資金管理の関数--------------

# 注文ロットを計算する関数
def calculate_lot( last_data,data,flag ):

	# 口座残高を取得する
	balance = bitflyer_collateral()

	# 最初のエントリーの場合
	if flag["add-position"]["count"] == 0:
		
		# １回の注文単位（ロット数）と、追加ポジの基準レンジを計算する
		volatility = calculate_volatility( last_data )
		stop = stop_range * volatility
		calc_lot = np.floor( balance * trade_risk / stop * 100 ) / 100
		
		flag["add-position"]["unit-size"] = np.floor( calc_lot / entry_times * 100 ) / 100
		flag["add-position"]["unit-range"] = round( volatility * entry_range )
		flag["add-position"]["stop"] = stop
		flag["position"]["ATR"] = round( volatility )
		
		print_log("現在のアカウント残高は{}円です".format( balance ))
		print_log("許容リスクから購入できる枚数は最大{}BTCまでです".format( calc_lot ))
		print_log("{0}回に分けて{1}BTCずつ注文します".format( entry_times, flag["add-position"]["unit-size"] ))
		
	
	# ストップ幅には、最初のエントリー時に計算したボラティリティを使う
	stop = flag["add-position"]["stop"]
	
	# 実際に購入可能な枚数を計算する
	able_lot = np.floor( balance * levarage / data["forming"]["close_price"] * 100 ) / 100
	lot = min(able_lot, flag["add-position"]["unit-size"])
	
	print_log("証拠金から購入できる枚数は最大{}BTCまでです".format( able_lot ))
	return lot,stop,flag

# 複数回に分けて追加ポジションを取る関数
def add_position( data,flag ):
	
	# ポジションがない場合は何もしない
	if flag["position"]["exist"] == False:
		return flag
	
	# 最初（１回目）のエントリー価格を記録
	if flag["add-position"]["count"] == 0:
		flag["add-position"]["first-entry-price"] = flag["position"]["price"]
		flag["add-position"]["last-entry-price"] = flag["position"]["price"]
		flag["add-position"]["count"] += 1
	
	# 以下の場合は、追加ポジションを取らない
	if flag["add-position"]["count"] >= entry_times:
		return flag
	
	# この関数の中で使う変数を用意
	first_entry_price = flag["add-position"]["first-entry-price"]
	last_entry_price = flag["add-position"]["last-entry-price"]
	unit_range = flag["add-position"]["unit-range"]
	current_price = data["forming"]["close_price"]
	
	
	# 価格がエントリー方向に基準レンジ分だけ進んだか判定する
	should_add_position = False
	if flag["position"]["side"] == "BUY" and (current_price - last_entry_price) > unit_range:
		should_add_position = True
	elif flag["position"]["side"] == "SELL" and (last_entry_price - current_price) > unit_range:
		should_add_position = True
	
	
	# 基準レンジ分進んでいれば追加注文を出す
	if should_add_position == True:
		print_log("前回のエントリー価格{0}円からブレイクアウトの方向に{1}ATR（{2}円）以上動きました".format( last_entry_price, entry_range, round( unit_range ) ))
		print_log("{0}/{1}回目の追加注文を出します".format(flag["add-position"]["count"] + 1, entry_times))
		
		# 注文サイズを計算
		lot,stop,flag = calculate_lot( last_data,data,flag )
		if lot < 0.01:
			print_log("注文可能枚数{}が、最低注文単位に満たなかったので注文を見送ります".format(lot))
			flag["add-position"]["count"] += 1
			return flag
		
		# 追加注文を出す
		if flag["position"]["side"] == "BUY":
			
			# ここに買い注文のコードを入れる
			print_log("現在のポジションに追加して{}BTCの買い注文を出します".format(lot))
			entry_price = bitflyer_market( "BUY", lot )
			
			
		if flag["position"]["side"] == "SELL":

			# ここに売り注文のコードを入れる
			print_log("現在のポジションに追加して{}BTCの売り注文を出します".format(lot))
			entry_price = bitflyer_market( "SELL", lot )
		
		
		# ポジション全体の情報を更新する
		flag["position"]["stop"] = stop
		flag["position"]["price"] = int(round(( flag["position"]["price"] * flag["position"]["lot"] + entry_price * lot ) / ( flag["position"]["lot"] + lot )))
		flag["position"]["lot"] = np.round( (flag["position"]["lot"] + lot) * 100 ) / 100		

		if flag["position"]["side"] == "BUY":
			print_log("{0}円の位置にストップを更新します".format(flag["position"]["price"] - stop))
		elif flag["position"]["side"] == "SELL":
			print_log("{0}円の位置にストップを更新します".format(flag["position"]["price"] + stop))
		print_log("現在のポジションの取得単価は{}円です".format(flag["position"]["price"]))
		print_log("現在のポジションサイズは{}BTCです".format(flag["position"]["lot"]))
		
		flag["add-position"]["count"] += 1
		flag["add-position"]["last-entry-price"] = entry_price
	
	return flag

# トレイリングストップの関数
def trail_stop( data,flag ):

	# まだ追加ポジションの取得中であれば何もしない
	if flag["add-position"]["count"] < entry_times:
		return flag
	
	# 高値／安値がエントリー価格からいくら離れたか計算
	if flag["position"]["side"] == "BUY":
		moved_range = round( data["settled"]["high_price"] - flag["position"]["price"] )
	if flag["position"]["side"] == "SELL":
		moved_range = round( flag["position"]["price"] - data["settled"]["low_price"] )
	
	# 最高値・最安値を更新したか調べる
	if moved_range < 0 or flag["position"]["stop-EP"] >= moved_range:
		return flag
	else:
		flag["position"]["stop-EP"] = moved_range
	
	# 加速係数に応じて損切りラインを動かす
	flag["position"]["stop"] = round(flag["position"]["stop"] - ( moved_range + flag["position"]["stop"] ) * flag["position"]["stop-AF"])
		
	# 加速係数を更新
	flag["position"]["stop-AF"] = round( flag["position"]["stop-AF"] + stop_AF_add ,2 )
	if flag["position"]["stop-AF"] >= stop_AF_max:
		flag["position"]["stop-AF"] = stop_AF_max
	
	# ログ出力
	if flag["position"]["side"] == "BUY":
		print_log("トレイリングストップの発動：ストップ位置を{}円に動かして、加速係数を{}に更新します".format( round(flag["position"]["price"] - flag["position"]["stop"]) , flag["position"]["stop-AF"] ))
	else:
		print_log("トレイリングストップの発動：ストップ位置を{}円に動かして、加速係数を{}に更新します".format( round(flag["position"]["price"] + flag["position"]["stop"]) , flag["position"]["stop-AF"] ))
	
	return flag

#-------------価格APIの関数--------------

# BTCFXのチャート価格をAPIで取得する関数（実行時の取得用）
def get_price(min, before=0, after=0):
	
	# Cryptowatchを使用する場合
	if chart_API == "cryptowatch":
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
			print_log("データが存在しません")
			return None

	# CryptoCompareを使用する場合（１時間足のみ対応）
	if chart_API == "cryptocompare":
		price = []
		params = {"fsym":"BTC","tsym":"JPY","e":"bitflyerfx","limit":2000 }
		
		response = requests.get("https://min-api.cryptocompare.com/data/histohour",params, timeout = 10)
		data = response.json()
		
		if data["Response"] == "Success":
			for i in data["Data"]:
				price.append({ "close_time" : i["time"],
					"close_time_dt" : datetime.fromtimestamp(i["time"]).strftime('%Y/%m/%d %H:%M'),
					"open_price" : i["open"],
					"high_price" : i["high"],
					"low_price" : i["low"],
					"close_price": i["close"] })
			return price
			
		else:
			print_log("データが存在しません")
			return None

# BTCFXのチャート価格をAPIで取得する関数（リアルタイム用）
def get_realtime_price(min):

	# Cryptowatchを使用する場合
	if chart_API == "cryptowatch":
		params = {"periods" : min }
		while True:
			try:
				response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc", params, timeout = 10)
				response.raise_for_status()
				data = response.json()
				return {
						"settled" : { 
							"close_time" : data["result"][str(min)][-2][0],
							"open_price" : data["result"][str(min)][-2][1],
							"high_price" : data["result"][str(min)][-2][2],
							"low_price" : data["result"][str(min)][-2][3],
							"close_price": data["result"][str(min)][-2][4]
							},
						"forming" : { "close_time" : data["result"][str(min)][-1][0],
							"open_price" : data["result"][str(min)][-1][1],
							"high_price" : data["result"][str(min)][-1][2],
							"low_price" : data["result"][str(min)][-1][3],
							"close_price": data["result"][str(min)][-1][4]
							}
						}
			
			except requests.exceptions.RequestException as e:
				print_log("Cryptowatchの価格取得でエラー発生 : " + str(e))
				print_log("{}秒待機してやり直します".format(wait))
				time.sleep(wait)

	# CryptoCompareを使用する場合（１時間足のみ対応）
	if chart_API == "cryptocompare":
		params = {"fsym":"BTC","tsym":"JPY","e":"bitflyerfx" }
		
		while True:
			try:
				response = requests.get("https://min-api.cryptocompare.com/data/histohour", params, timeout = 10)
				response.raise_for_status()
				data = response.json()
				time.sleep(5)
				
				response2 = requests.get("https://min-api.cryptocompare.com/data/histominute", params ,timeout = 10)
				response2.raise_for_status()
				data2 = response2.json()
				
			except requests.exceptions.RequestException as e:
				print_log("Cryptocompareの価格取得でエラー発生 : " + str(e))
				print_log("{}秒待機してやり直します".format(wait))
				time.sleep(wait)
				continue
			
			return {
				"settled" : { 
					"close_time" : data["Data"][-2]["time"],
					"open_price" : data["Data"][-2]["open"],
					"high_price" : data["Data"][-2]["high"],
					"low_price" : data["Data"][-2]["low"],
					"close_price": data["Data"][-2]["close"]
					},
				"forming" : { 
					"close_time" : data2["Data"][-1]["time"],
					"open_price" : data2["Data"][-1]["open"],
					"high_price" : data2["Data"][-1]["high"],
					"low_price" : data2["Data"][-1]["low"],
					"close_price": data2["Data"][-1]["close"]
					}
			}

#-------------その他の補助関数--------------

# 時間と高値・安値・終値を表示する関数
def print_price( data ):
	print_log( "時間： " + datetime.fromtimestamp(data["close_time"]).strftime('%Y/%m/%d %H:%M') + " 高値： " + str(data["high_price"]) + " 安値： " + str(data["low_price"]) + " 終値： " + str(data["close_price"]) )

# １期間の平均ボラティリティを計算する
def calculate_volatility( last_data ):

	high_sum = sum(i["high_price"] for i in last_data[-1 * volatility_term :])
	low_sum  = sum(i["low_price"]  for i in last_data[-1 * volatility_term :])
	volatility = round((high_sum - low_sum) / volatility_term)
	print_log("現在の{0}期間の平均ボラティリティは{1}円です".format( volatility_term, volatility ))
	return volatility

# ログファイルの出力やLINE通知の関数
def print_log( text ):
	
	# LINE通知する場合
	if line_config == "ON":
		url = "https://notify-api.line.me/api/notify"
		data = {"message" : str(text)}
		headers = {"Authorization": "Bearer " + line_token}
		try: 
			requests.post(url, data=data, headers=headers)
		except requests.exceptions.RequestException as e:
			if log_config == "ON":
				logger.info( str(e) )
			else:
				print( str(e) )
	
	# コマンドラインへの出力とファイル保存
	if log_config == "ON":
		logger.info( text )
	else:
		print( text )

#-------------トラブル対策用の関数--------------

def find_unexpected_pos( flag ):
	
	if flag["position"]["exist"] == True:
		return flag
	count = 0
	while True:
		price,size,side = bitflyer_check_positions()
		if size == 0:
			return flag
		
		print_log("把握していないポジションが見つかりました")
		print_log("反映の遅延でないことを確認するため様子を見ています")
		count += 1
		
		if count > 5:
			print_log("把握していないポジションが見つかったためポジションを復活させます")
			
			flag["position"]["exist"] = True
			flag["position"]["side"] = side
			flag["position"]["lot"] = size
			flag["position"]["price"] = price
			flag["position"]["stop-AF"] = stop_AF
			flag["position"]["stop-EP"] = 0
			flag["add-position"]["count"] = entry_times
			
			if flag["position"]["ATR"] == 0:
				flag["position"]["ATR"] = calculate_volatility( last_data )
				flag["position"]["stop"] = flag["position"]["ATR"] * stop_range
			pprint(flag)
			return flag
		time.sleep(30)

#-------------Bitflyerと通信する関数--------------

# 成行注文をする関数
def bitflyer_market(side,lot):
	while True:
		try:
			order = bitflyer.create_order(
				symbol = 'BTC/JPY',
				type='market',
				side= side,
				amount= lot,
				params = { "product_code" : "FX_BTC_JPY" })
			print_log("--------------------")
			print_log( order )
			print_log("--------------------")
			order_id = order["id"]
			time.sleep(30)
			
			# 執行状況を確認
			average_price = bitflyer_check_market_order( order_id, lot )
			return average_price
			
		except ccxt.BaseError as e:
			print_log("Bitflyerの注文APIでエラー発生 : " + str(e))
			print_log("注文が失敗しました")
			print_log("30秒待機してやり直します")
			time.sleep(30)

# 成行注文の執行状況を確認する関数
def bitflyer_check_market_order( id,lot ):
	while True:
		try:
			size = []
			price = []
			
			executions = bitflyer.private_get_getexecutions( params = { "product_code" : "FX_BTC_JPY" })
			for exec in executions:
				if exec["child_order_acceptance_id"] == id:
					size.append( exec["size"] )
					price.append( exec["price"] )
			
			# 全部約定するまで待つ
			if round(sum(size),2) != lot:
				time.sleep(20)
				print_log("注文がすべて約定するのを待っています")
			else:
				# 平均価格を計算する
				average_price = round(sum( price[i] * size[i] for i in range(len(price)) ) / sum(size))
				print_log("すべての成行注文が執行されました")
				print_log("執行価格は平均 {}円です".format(average_price))
				return average_price
				
		except ccxt.BaseError as e:
			print_log("BitflyerのAPIで問題発生 : " + str(e))
			print_log("20秒待機してやり直します")
			time.sleep(20)

# 口座残高を取得する関数
def bitflyer_collateral():
	while True:
		try:
			collateral = bitflyer.private_get_getcollateral()
			spendable_collateral = np.floor(collateral["collateral"] - collateral["require_collateral"])
			print_log("現在のアカウント残高は{}円です".format( int(collateral["collateral"]) ))
			print_log("新規注文に利用可能な証拠金の額は{}円です".format( int(spendable_collateral) ))
			return int( spendable_collateral )
			
		except ccxt.BaseError as e:
			print_log("BitflyerのAPIでの口座残高取得に失敗しました ： " + str(e))
			print_log("20秒待機してやり直します")
			time.sleep(20)

# ポジション情報を取得する関数
def bitflyer_check_positions():
	failed = 0
	while True:
		try:
			size = []
			price = []
			positions = bitflyer.private_get_getpositions( params = { "product_code" : "FX_BTC_JPY" })
			if not positions:
				#print_log("現在ポジションは存在しません")
				return 0,0,None
			for pos in positions:
				size.append( pos["size"] )
				price.append( pos["price"] )
				side = pos["side"]
			
			# 平均建値を計算する
			average_price = round(sum( price[i] * size[i] for i in range(len(price)) ) / sum(size))
			sum_size = round(sum(size),2)
			#print_log("保有中の建玉：合計{}つ\n平均建値：{}円\n合計サイズ：{}BTC\n方向：{}".format(len(price),average_price,sum_size,side))
			
			# 価格・サイズ・方向を返す
			return average_price,sum_size,side
				
		except ccxt.BaseError as e:
			failed += 1
			if failed > 10:
				print_log("Bitflyerのポジション取得APIでエラーに10回失敗しました : " + str(e))
				print_log("20秒待機してやり直します")
			time.sleep(20)

#------------ここからメイン処理の記述--------------

# 最低限、保持が必要なローソク足の期間を準備

need_term = max(buy_term,sell_term,volatility_term,MA_term)
print_log("{}期間分のデータの準備中".format(need_term))

price = get_price(chart_sec)
last_data = price[-1*need_term-2:-2]
print_price(last_data[-1])
print_log("--{}秒待機--".format(wait))
time.sleep(wait)

print_log("---実行開始---")

while True:

	# 最新のローソク足を取得して表示
	data = get_realtime_price( chart_sec )
	if data["settled"]["close_time"] > last_data[-1]["close_time"]:
		print_price( data["settled"] )
	
	# ポジションがある場合
	if flag["position"]["exist"]:
		flag = stop_position( data,flag )
		flag = close_position( data,last_data,flag )
		flag = add_position( data,flag )
	
	# ポジションがない場合
	else:
		flag = find_unexpected_pos( flag )
		flag = entry_signal( data,last_data,flag )
	
	# 確定足が更新された場合
	if data["settled"]["close_time"] > last_data[-1]["close_time"]:
		last_data.append( data["settled"] )
		if len(last_data) > need_term:
			del last_data[0]
	
	time.sleep(wait)
以上がソースコードです。
テキストエディタに貼り付けて使うときはUTF-8で保存してください。

使い方の説明
最初にCCXTとnumpyをpipでインストールしてください。Anacondaで環境構築した方は、numpyはデフォルトでインストールされています。

あとはBitflyerのAPIキーとAPIシークレットを設定してコマンドプロンプトから実行するだけです。動作や仕様に関してわからない箇所は、私のブログを参考にしていただくか、なかなか自己解決できなければご質問ください。

プログラムを勉強中の方は、教材コードなのでただコピペして実行するのではなく、できれば実行する前にコードを１読してください。わからない箇所があってもいいので、どの関数で何をしようとしているのかおおまかに掴んでみてください。


パラメーターの設定方法
wait（待機時間）・・・Cryptowatchへのリクエスト頻度やBitflyerの再処理までの待機時間です。2021年現在、Cryptowatch/Cryptocompareともに、API周りの使用回数制限が厳しくなってきているので、デフォルトは180秒を推奨しています。もしそれでエラーが出るようなら、240秒、360秒を検証してください。または有料APIを検討してください。

buy_term/sell_term ・・・特に理由のない限り、上値・下値ブレイクアウトともに同じ期間を使用した方がいいと思います。違う期間を設定すると、買いバイアス・売りバイアスがかかります。私は30期間か40期間がおすすめです。

chart_sec・・・使用する時間軸の設定です。秒単位で指定してください。
例えば、１時間足なら3600、30分足なら1800、15分足なら900です。
データの存在しない時間軸を指定するとエラーになります。

chart_API　・・・BTCFXの価格データの取得元（API）をcryptowatchかcryptocompareから選択できます。現時点ではcryptowatchを推奨していますが、多くの方が使っているので混雑状況によってはサーバが不安定になることがあります。その場合は、サブの取得元としてcryptocompareに切り替え可能です。
※ 小文字で指定してください
※ cryptocompareは１時間足での利用のみ対応しています。

judge_price ・・・ 上値ブレイクアウトの判定に高値を使用する場合は high_price を、終値を使用する場合には close_price を指定します。下値ブレイクアウト判定に安値を使用する場合は、low_price を、終値を使用する場合は、close_priceを指定します。

volatility_term ・・・ 初期ストップを決める基準となるATR（平均ボラティリティ）を計算する期間です。

stop_range ・・・何ATR幅に初期の損切り（ストップ）を置くかの設定値です。初期設定値は２レンジ幅です。

trade_risk　・・・　１回のトレードで口座の何％のリスクを取るか、です。安定を望むなら１～２％、ハイリスク・ハイリターンを狙うなら３～５％程度に設定してください。５％を超える数値は破産リスクが高いので推奨されません。

※ 注１）trade_riskは、ポジション取得時のサイズ計算に使用される理論上の許容リスクであり、実際に損切注文のときに生じるスリッページやサーバー障害による損失をコントロールするものではありません。なので、実際に許容できるリスク率よりは低めに設定してください。具体的なリスク率の意味は本編ブログの資金管理編を読んでください。

※注２）ポジションの積み増し（分割エントリー）を有効にしていれば、口座リスク率が大きくても、ある程度、ドローダウンを押さえられます。１度に口座の５％分の金額でエントリーするのと、４回に分けて分割エントリーして合計で口座の５％の金額のリスクを取るのとでは、実際のリスクはかなり違うので、仕様を理解して使用してください。

levarage ・・・　実際にBitflyerで設定しているのと同じレバレッジ率を設定してください。レバレッジをかけない場合は１にしてください。

注１）実際にBitflyer側で設定しているレバレッジ率より高いレバレッジを指定することはできません。おかしな挙動になります。
注２）実際にBitflyer側で設定しているレバレッジ率より低いレバレッジを指定することはできますが、分割エントリーを有効にしている場合、少し計算値がズレるので推奨されません。詳しい理由は、以下の購入者質問ページを参考にしてください。

entry_times ・・・ 何回に分けてポジションの積み増しをするかの設定値です。バックテストの検証結果からは、２回～４回の積み増しがお勧めです。なお１に設定すれば、無効にできます。

entry_range ・・・ 何レンジごとにポジションを積みますかです。一番いいのは、「0.5レンジごとに２回に分けて取得」か、「0.5レンジごとに４回に分けて取得」かのどちらかです。バックテストでは４回が良い結果でしたが、スリッページの影響を懸念するなら、「0.5レンジずつ２回」がいいと思います。

trailing_confit ・・・ONで上記のトレイリングストップが有効になります。OFFで無効にできます。

stop_AF/stop_AF_add/stop_AF_max ・・・ 本ブログ記事でも掲載の通り、0.03に設定するのが最もうまく機能するように見えます。教科書通りに運用するなら0.02が定石です。より高い数値を設定するほど、利食いが早くなります。

filter_VER ・・・エントリー時にトレンドフィルターを使うかどうかの設定です。OFFでフィルターを無効にできます。フィルターを利用する場合は、AかBを設定してください。デフォルトでは、AとBの２種類を用意しています。

（A）上値ブレイクアウトでは、N期間の単純移動平均線より現在の終値が上にある場合のみエントリーする（上昇トレンドの確認）。下値ブレイクアウトはその逆。
（B）上値ブレイクアウトでは、N期間の単純移動平均の値が、前々足よりも前足の方が上にある場合（＝移動平均線の傾きが上）のみエントリーする。下値ブレイクアウトはその逆。


※ 例えば、フィルターAをONにする場合は、設定値を filter = "A" にしてください。初期値ではOFFになっています。
※ 各トレンドフィルターの意味とバックテスト結果は本編ブログ第９回で解説しています。教材コードなので、そのまま使ってもいいですが、ご自身の作りたいフィルターにカスタマイズして使うといいと思います。

MA_term ・・・上記のトレンドフィルターで利用する移動平均線の期間を指定できます。例）200期間の単純移動平均の場合、MA_term = 200

bitflyer.apiKey / bitflyer.secret ・・・BitflyerFXのAPIキーとシークレットを入力してください。
bitflyer.timeout ・・・Bitflyerのサーバーと通信するときのタイムアウトの判定時間を指定できます。タイムアウトエラーは二重注文などの原因になるので、少し長めに設定することが推奨されます。デフォルトは30秒です

line_config ・・・LINEへの通知を有効にするかどうかの設定です。通知する場合はONにしてください。教材コードでは、コマンドラインへの標準出力の内容を全てそのままLINEにも通知します。仕様を変えたい場合はご自身でカスタマイズしてください。

line_token ・・・LINE通知機能を使うには、LINEの開発者トークンの入力が必要です。詳しくは本編ブログを読んでください。

log_config ・・・ ログ機能を有効にするかどうかの設定です。ONにした場合、コマンドラインへの標準出力と同じ内容を、指定したフォルダにテキストファイルとして出力・保存します。

log_file_path ・・・ ログ機能を有効にする場合に、ログファイルを吐き出す場所とそのファイル名を指定します。
例）Windows環境（VPSも同じ）の場合
log_file_path = "c:/Pydoc/donchanBOT.log"

パラメータ設定の実際例
2018/7/13    私は現在は以下のパラメーターを中心に使っています。
現時点で、私が一番いいと思って設定しているパラメーターですが、皆さんは十分に懐疑的になった上で、鵜呑みにせず、ご自身で検証しながら判断してください。


wait = 180
buy_term = 30
sell_term = 30
chart_sec = 3600
judge_price ={ "BUY":"close_price","SELL":"close_price" }
volatility_term = 5 # 平均レンジ（ボラティリティ）を計算する期間
stop_range = 2
trade_risk = 0.02 # 1トレードあたり口座の何％リスクを取るか
levarage = 3 # レバレッジ倍率

entry_times = 2 # 何回に分けて追加ポジションを取るか
entry_range = 0.5 # 何レンジごとに追加ポジションを取るか

trailing_config = "ON"
stop_AF = 0.02 # 加速係数
stop_AF_add = 0.02 # 加速係数を増やす度合
stop_AF_max = 0.2 # 加速係数の上限

filter_VER = "A"　# トレンドフィルターのVer
MA_term = 200    # フィルターに使う移動平均線の期間

※ 2021年3月追記
現在、私が使用しているパラメーターは公開していません。上記は比較的、オーソドックスで当たり障りのないパラメーター設定なので、参考の基準値（デフォルト設定）として使ってください。



リアルタイムで形成中の足と確定足
CryptowatchからAPIで価格を取得するときに、以下のように最新価格のデータを格納しています。

▽Cryptowatchから最新価格を取得するコード

# CryptowatchのAPIを使用する関数（リアルタイム用）
def get_realtime_price(min):
	params = {"periods" : min }
	while True:
		try:
			response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc", params, timeout = 5)
			response.raise_for_status()
			data = response.json()
			return {
					"settled" : { 
						"close_time" : data["result"][str(min)][-2][0],
						"open_price" : data["result"][str(min)][-2][1],
						"high_price" : data["result"][str(min)][-2][2],
						"low_price" : data["result"][str(min)][-2][3],
						"close_price": data["result"][str(min)][-2][4]
						},
					"forming" : { "close_time" : data["result"][str(min)][-1][0],
						"open_price" : data["result"][str(min)][-1][1],
						"high_price" : data["result"][str(min)][-1][2],
						"low_price" : data["result"][str(min)][-1][3],
						"close_price": data["result"][str(min)][-1][4]
						}
					}
		except requests.exceptions.RequestException as e:
			print("Cryptowatchの価格取得でエラー発生 : ",e)
			print("{}秒待機してやり直します".format(wait))
			time.sleep(wait)
ここでは、リアルタイムで形成中の足（[-1]）と、すでに直近の１時間で確定した足（[-2]）とを、それぞれdata["forming"]とdata["settled"]に格納しています。

（例）
data["forming"]["high_price"]  ・・・リアルタイムで形成中の高値。常に変化しているので、30秒おきに取得して損切りや追加ポジションの取得判定に使用。コマンドプロンプトへの出力はしない。

data["settled"]["close_price"] ・・・すでに確定している直近の最新の１時間足。１時間に１度しか更新されないので、更新されればコマンドプロンプトに出力。エントリー条件や手仕舞い条件の判定に使用。

各関数には、data変数を丸ごと渡していて、形成中の足と確定足のどちらを判断に利用するかは、各関数が内部で決めています。（例えば、損切りの関数は、data を受け取って、data["forming"]["low_price"]が損切ラインにかかってないかをチェックしています）

どの箇所でどちらを使用しているかは、各関数の中のdataを確認すればわかります。ご自身で変更していただくこともできます。例えば、ブレイクアウトの判定足をリアルタイムで形成中の足にすることもできます。

ブレイクアウトの判定足の変更
▽エントリーの判定を「リアルタイムで形成中の足」にしたい場合

# ドンチャンブレイクを判定する関数
def donchian( data,last_data ):
	
	highest = max(i["high_price"] for i in last_data[ (-1* buy_term): ])
	if data["forming"][ judge_price["BUY"] ] > highest:
		return {"side":"BUY","price":highest}
	
	lowest = min(i["low_price"] for i in last_data[ (-1* sell_term): ])
	if data["forming"][ judge_price["SELL"] ] < lowest:
		return {"side":"SELL","price":lowest}
	
	return {"side" : None , "price":0}
data["settled"]となっていたところを、data["forming"]に変えれば、リアルタイムの足で判定してエントリーできます。

ブレイクアウトの判定を終値で行いたい場合は、１つ前の足（確定足）で判断するので変更は不要です。一方、「リアルタイムの足がブレイクアウトのラインに掛かったらすぐエントリーしたい」という場合は、上記の変更を行ってください。

※ 形成中の足を判断に使う場合は、必ず「終値」を使ってください。
終値以外を使うと、永遠にエントリーと損切りを繰り返してループしてしまうなどのバグの原因となります。


調整のために一時BOTを止めるときのテクニック
特に解説するほどでもないかもしれませんが、BOTがポジションを持っている状態で、パラメーターの設定変更やコードの修正をしたくなった場合は、BOTを１度止めて修正をおこなった後、flag["position"] を以下のように設定してBOTを再実行すれば、ポジションを持った状態から再スタートできます。

（例）

	"position":{
		"exist" : True,
		"side" : "BUY",
		"price": 101528,
		"stop":20764,
		"stop-AF": stop_AF,
		"stop-EP":0,
		"ATR":10382,
		"lot":1.05,
		"count":0
	},
	"add-position":{
		"count":4,
		"first-entry-price":0,
		"last-entry-price":0,
		"unit-range":0,
		"unit-size":0,
		"stop":0
	},
つまり、BOTを一時停止させても、flag["position"]["exist"]をTrueで再開すれば、そのまま継続して運用できます。

ただしこの時にエントリー価格やロット数、ボラティリティ値（ATR）などの数字を覚えていないと再設定できません。これらの数字はprint()によってコマンドプロンプトに出力されているので、BOTを止めるときに忘れずにメモしておきましょう。

また間違って追加ポジションを取得しないように、countを設定値以上にしてから再稼働してください。例えば、４回に分けて分割エントリーする設定であれば、ポジションを持った状態でBOTを再稼働させるには、countを4以上にして再スタートさせる必要があります。

※ 追記）
トラブル対策関数を追加したため、何もせずにBOTの稼働を再開させても、自動的に現在のポジションの平均建値・サイズを自動取得できるようになりました。ただし、ストップ位置や平均ボラティリティ（ATR）の計算は、実行再開時のもので再計算されます。またトレイリングSTOPを途中から再開させることはできません。

よくある質問
（１）ブレイクアウトしてるのにエントリーしない？

ブレイクアウトの判定には「確定足」を使っています。このnoteで言う「確定足」と「リアルタイムで形成中の足」は以下を指しています。

画像4

確定足・・・もう終値が確定した足（右から２番目）
形成中の足・・・リアルタイムで終値が変動していて、まだ安値・高値も変わる可能性のある足（一番右）

ブレイクアウトの判定は「確定足」で行っています。確定足の終値を使うか安値を使うかは設定で変更できます。ただしブレイクアウトのラインは、判定方法の設定に関わらず、過去ｎ期間の「最高値」または「最安値」となります。これは上ヒゲや下ヒゲのラインを意味します。

なお、ブレイクアウトの判定を「リアルタイムで形成中の足」に変更したければ、することもできます。上の解説に記載があります。

（２）コマンド（ログ）に表示される時間が１時間ずれてる気がする

画像5

コマンドプロンプトに出力されているのは、すでに終値が固まった足（確定足）で、表示されている時間は、その足が確定した時間です。１つ前の足が確定した時間とセットで表示されてると思ってください。

例えば、１時間足を使用している場合、７時01分～59分までの足（チャートで見る一番右の足）は、最終的に８時０分に固まって 08:00 として出力されます。これが8時として表示されるのは、Cryptowatchのデータの仕様です。

一番最新の足も30秒に１回取得していますが、こちらは取得のたびに値が変わるので、いちいち出力はしていません。裏側で「損切り」「ポジションの追加取得」などの判定に使用しています。

購入後の動作について

購入前の注意書きの通り、原則として個別サポートはできないのですが、質問や報告をする場所がないのも問題なので、最初の稼働やエントリーまでで自己解決できないことがあれば、以下のページにコメントいただければ可能な範囲で対応します。

質問ページ（コメントを下さい）
https://ryota-trade.com/?p=5059
パス
fabeOYTbs3wQTKbL

※ コメントにアドレスが必須になっていますが、アドレスは、test@yahoo.co.jp等でも構いません。

※ 2021年3月追記
こちらのページは現在、多忙のためほとんど見れておらず、個別に返信もできていません。「エラーが出たときの自力での対処方法」を追記したので、そちらを参考にしてください。また過去にいただいた質問と回答がたくさんあるので、そちらも参考にしてください。



コード修正情報
5/22 19時
23行目 トレイリングストップのON/OFFを指定できるように修正しました。278行目 ポジション積み増しの関数（add_position()）に以下の行を追加しました。

# 注文サイズを計算
lot,stop,flag = calculate_lot( last_data,data,flag )
if lot < 0.01:
		print("注文可能枚数{}が、最低注文単位に満たなかったので注文を見送ります".format(lot))
		flag["add-position"]["count"] += 1 # 追加
元のままでも深刻な問題はありませんが、もし理論サイズより証拠金が不足した場合に、ずっとコマンドプロンプトに「最低注文単に満たなかったので...」と出力され続ける場合があるので、良かったら更新をお願いします。

463行目 約定を判定する関数の小数点の計算に、四捨五入しないと一致しないケースがあることが確認されたため、小数点以下２桁でround()を追記しました。

5/29 20時
456行目、629行目　Bitflyerのサーバー問題の対策（二重注文の対策）の関数を追加しました。二重注文の問題についてはこちらの記事を参考にしてください。

5/31 10時
設定値　Bitflyerのサーバー混雑時のタイムアウト対策としてタイムアウト時間を設定できるようにしました。CCXTのデフォルトが10秒ですが、少し長め（30秒以上）に設定すると意味があるかもしれません。

設定値　BitflyerFXの価格データの取得先APIとして、cryptocompareを選択できるようにしました。基本的にcryptowatchが推奨ですが、もしサーバー混雑や障害等で使えなくなった場合はサブとして使用できます。
※ 小文字で指定してください。

7/13 
形成中の足を判断に使う場合の注意点（終値を使うこと）の追記
公開時の推奨パラメーターの修正

7/15
トレンドフィルター機能、LINE通知機能、ログファイルの出力機能を追加しました。全てOFFに設定すれば、従来のバージョンと同じように動作します。

・277行目 トレンドフィルターの関数
具体的なフィルターの仕様は本編ブログを読んでください。教材コードなので、そのまま使ってもいいですが、ご自身が作りたいフィルターの雛形として使ってください。

・594行目 ログファイル出力・LINE通知の関数
すべてのprint文を、print_log()という関数に置き換えました。ログの設定値をOFFにすれば、全て通常のprint文（標準出力）として実行されます。
※ LINE通知機能を追加したため、初期実行時には準備中のローソク足をすべて表示するのではなく、直近の１足のみ表示するよう変更しています。

7/17
640行目 pprint文を間違ってpprint_log()に置換していたので修正しました。

7/22
51行目 ログ機能をONにしている場合のみ、loggingの設定が読みこまれるようif文を追加しました。

8/05
全ての例外処理の記述箇所について、pring_log()への引数の渡し方が間違っていたので修正しました。また784行目で200件以上データを溜めれない仕様になっていたので修正しました。


2019/5/3
LINE通知の失敗が原因で Connection aborted, OSError("10054")が出て停止することがあったので、598行目以下に例外処理を追記しました。

2021/3/11
CryptowatchAPIについての記載追加、一部の注意事項の更新、
CryptowatchAPIの使用回数制限、Cryptocompareの使用回数制限が変更されたので、noteコードのデフォルトのループ間隔を180秒にしました。

CryptowatchのBitflyerFX価格取得APIの使用回数制限について



※ 更新の差分確認用（１つ前のバージョンのコード）

import requests
from datetime import datetime
from logging import getLogger,Formatter,StreamHandler,FileHandler,INFO
from pprint import pprint
import time
import numpy as np
import ccxt

#-------------設定項目------------------------

wait = 30                    # ループの待機時間（30秒推奨）
buy_term = 30                # 最高値（上値）ブレイクアウト期間
sell_term = 30               # 最安値（下値）ブレイクアウト期間
chart_sec = 3600             # 使用する時間軸（秒換算）
chart_API = "cryptowatch"    # 価格の取得元を（cryptowatch/cryptocompare）から選択

judge_price={
  "BUY" : "close_price",     # ブレイク判断　高値（high_price)か終値（close_price）を使用
  "SELL": "close_price"      # ブレイク判断　安値 (low_price)か終値（close_price）を使用
}

volatility_term = 5          # 平均ボラティリティの計算に使う期間
stop_range = 2               # 何レンジ幅にストップを入れるか
trade_risk = 0.03            # 1トレードあたり口座の何％まで損失を許容するか
levarage = 3                 # レバレッジ倍率の設定

entry_times = 2              # 何回に分けて追加ポジションを取るか
entry_range = 1              # 何レンジごとに追加ポジションを取るか

trailing_config = "ON"       # ONで有効 OFFで無効
stop_AF = 0.02               # 加速係数
stop_AF_add = 0.02           # 加速係数を増やす度合
stop_AF_max = 0.2            # 加速係数の上限

filter_VER = "OFF"           # フィルター設定／OFFで無効
MA_term = 200                # トレンドフィルターに使う移動平均線の期間

bitflyer = ccxt.bitflyer()
bitflyer.apiKey = ''         # APIキーを設定
bitflyer.secret = ''         # APIシークレットを設定
bitflyer.timeout = 30000     # 通信のタイムアウト時間の設定

line_config = "OFF"          # LINE通知をするかどうかの設定
log_config = "OFF"           # ログファイルを出力するかの設定
log_file_path = ""           # ログを記録するファイル名と出力パス
line_token = ""              # LINE通知を使用する場合はAPIキーを入力

#-------------ログ機能の設定--------------------

# ログ機能の設定箇所
if log_config == "ON":
	logger = getLogger(__name__)
	handlerSh = StreamHandler()
	handlerFile = FileHandler( log_file_path )
	handlerSh.setLevel(INFO)
	handlerFile.setLevel(INFO)
	logger.setLevel(INFO)
	logger.addHandler(handlerSh)
	logger.addHandler(handlerFile)

#-------------注文管理の変数------------------------

flag = {
	"position":{
		"exist" : False,
		"side" : "",
		"price": 0,
		"stop": 0,
		"stop-AF": stop_AF,
		"stop-EP":0,
		"ATR": 0,
		"lot": 0,
		"count":0
	},
	"add-position":{
		"count":0,
		"first-entry-price":0,
		"last-entry-price":0,
		"unit-range":0,
		"unit-size":0,
		"stop":0
	}
}

#-------------売買ロジックの部分の関数--------------

# ドンチャンブレイクを判定する関数
def donchian( data,last_data ):
	
	highest = max(i["high_price"] for i in last_data[ (-1* buy_term): ])
	if data["settled"][ judge_price["BUY"] ] > highest:
		return {"side":"BUY","price":highest}
	
	lowest = min(i["low_price"] for i in last_data[ (-1* sell_term): ])
	if data["settled"][ judge_price["SELL"] ] < lowest:
		return {"side":"SELL","price":lowest}
	
	return {"side" : None , "price":0}

# ドンチャンブレイクを判定してエントリー注文を出す関数
def entry_signal( data,last_data,flag ):

	if flag["position"]["exist"] == True:
		return flag

	signal = donchian( data,last_data )
	if signal["side"] == "BUY":
		print_log("過去{0}足の最高値{1}円を、直近の価格が{2}円でブレイクしました".format(buy_term,signal["price"],data["settled"][judge_price["BUY"]]))
		# フィルター条件を確認
		if filter( signal ) == False:
			print_log("フィルターのエントリー条件を満たさなかったため、エントリーしません")
			return flag
		
		lot,stop,flag = calculate_lot( last_data,data,flag )
		if lot >= 0.01:
			print_log("{0}円あたりに{1}BTCで買いの成行注文を出します".format(data["settled"]["close_price"],lot))
			
			# ここに買い注文のコードを入れる
			price = bitflyer_market( "BUY", lot )
			
			print_log("{0}円にストップを入れます".format(price - stop))
			flag["position"]["lot"],flag["position"]["stop"] = lot,stop
			flag["position"]["exist"] = True
			flag["position"]["side"] = "BUY"
			flag["position"]["price"] = price
		else:
			print_log("注文可能枚数{}が、最低注文単位に満たなかったので注文を見送ります".format(lot))

	if signal["side"] == "SELL":
		print_log("過去{0}足の最安値{1}円を、直近の価格が{2}円でブレイクしました".format(sell_term,signal["price"],data["settled"][judge_price["SELL"]]))
		# フィルター条件を確認
		if filter( signal ) == False:
			print_log("フィルターのエントリー条件を満たさなかったため、エントリーしません")
			return flag
		
		lot,stop,flag = calculate_lot( last_data,data,flag )
		if lot >= 0.01:
			print_log("{0}円あたりに{1}BTCの売りの成行注文を出します".format(data["settled"]["close_price"],lot))
			
			# ここに売り注文のコードを入れる
			price = bitflyer_market( "SELL", lot )
			
			print_log("{0}円にストップを入れます".format(price + stop))
			flag["position"]["lot"],flag["position"]["stop"] = lot,stop
			flag["position"]["exist"] = True
			flag["position"]["side"] = "SELL"
			flag["position"]["price"] = price
		else:
			print_log("注文可能枚数{}が、最低注文単位に満たなかったので注文を見送ります".format(lot))

	return flag

# 損切ラインにかかったら成行注文で決済する関数
def stop_position( data,flag ):

	# トレイリングストップを実行
	if trailing_config == "ON":
		flag = trail_stop( data,flag )
	
	if flag["position"]["side"] == "BUY":
		stop_price = flag["position"]["price"] - flag["position"]["stop"]
		if data["forming"]["low_price"] < stop_price:
			print_log("{0}円の損切ラインに引っかかりました。".format( stop_price ))
			print_log(str(data["forming"]["low_price"]) + "円あたりで成行注文を出してポジションを決済します")
			
			# 決済の成行注文コードを入れる
			bitflyer_market( "SELL" , flag["position"]["lot"] )
			
			flag["position"]["exist"] = False
			flag["position"]["count"] = 0
			flag["position"]["stop-AF"] = stop_AF
			flag["position"]["stop-EP"] = 0
			flag["add-position"]["count"] = 0
	
	
	if flag["position"]["side"] == "SELL":
		stop_price = flag["position"]["price"] + flag["position"]["stop"]
		if data["forming"]["high_price"] > stop_price:
			print_log("{0}円の損切ラインに引っかかりました。".format( stop_price ))
			print_log(str(data["forming"]["high_price"]) + "円あたりで成行注文を出してポジションを決済します")
			
			# 決済の成行注文コードを入れる
			bitflyer_market( "BUY" , flag["position"]["lot"] )
			
			flag["position"]["exist"] = False
			flag["position"]["count"] = 0
			flag["position"]["stop-AF"] = stop_AF
			flag["position"]["stop-EP"] = 0
			flag["add-position"]["count"] = 0
			
	return flag

# 手仕舞いのシグナルが出たら決済の成行注文 + ドテン注文 を出す関数
def close_position( data,last_data,flag ):
	
	if flag["position"]["exist"] == False:
		return flag
	
	flag["position"]["count"] += 1
	signal = donchian( data,last_data )
	
	if flag["position"]["side"] == "BUY":
		if signal["side"] == "SELL":
			print_log("過去{0}足の最安値{1}円を、直近の価格が{2}円でブレイクしました".format(sell_term,signal["price"],data["settled"][judge_price["SELL"]]))
			print_log(str(data["settled"]["close_price"]) + "円あたりで成行注文を出してポジションを決済します")
			
			# 決済の成行注文コードを入れる
			bitflyer_market( "SELL" , flag["position"]["lot"] )
			
			flag["position"]["exist"] = False
			flag["position"]["count"] = 0
			flag["position"]["stop-AF"] = stop_AF
			flag["position"]["stop-EP"] = 0
			flag["add-position"]["count"] = 0
			
			
			# ドテン注文の箇所
			# フィルター条件を確認
			if filter( signal ) == False:
				print_log("フィルターのエントリー条件を満たさなかったため、エントリーしません")
				return flag
			
			
			lot,stop,flag = calculate_lot( last_data,data,flag )
			if lot >= 0.01:
				print_log("さらに{0}円あたりに{1}BTCの売りの成行注文を入れてドテン出します".format(data["settled"]["close_price"],lot))
				
				# ここに売り注文のコードを入れる
				price = bitflyer_market( "SELL", lot )
				
				print_log("{0}円にストップを入れます".format(price + stop))
				flag["position"]["lot"],flag["position"]["stop"] = lot,stop
				flag["position"]["exist"] = True
				flag["position"]["side"] = "SELL"
				flag["position"]["price"] = price
			
			

	if flag["position"]["side"] == "SELL":
		if signal["side"] == "BUY":
			print_log("過去{0}足の最高値{1}円を、直近の価格が{2}円でブレイクしました".format(buy_term,signal["price"],data["settled"][judge_price["BUY"]]))
			print_log(str(data["settled"]["close_price"]) + "円あたりで成行注文を出してポジションを決済します")
			
			# 決済の成行注文コードを入れる
			bitflyer_market( "BUY" , flag["position"]["lot"] )
			
			flag["position"]["exist"] = False
			flag["position"]["count"] = 0
			flag["position"]["stop-AF"] = stop_AF
			flag["position"]["stop-EP"] = 0
			flag["add-position"]["count"] = 0
			
			
			# ドテン注文の箇所
			# フィルター条件を確認
			if filter( signal ) == False:
				print_log("フィルターのエントリー条件を満たさなかったため、エントリーしません")
				return flag
			
			
			lot,stop,flag = calculate_lot( last_data,data,flag )
			if lot >= 0.01:
				print_log("さらに{0}円あたりで{1}BTCの買いの成行注文を入れてドテンします".format(data["settled"]["close_price"],lot))
				
				# ここに買い注文のコードを入れる
				price = bitflyer_market( "BUY", lot )
				
				print_log("{0}円にストップを入れます".format(price - stop))
				flag["position"]["lot"],flag["position"]["stop"] = lot,stop
				flag["position"]["exist"] = True
				flag["position"]["side"] = "BUY"
				flag["position"]["price"] = price

	return flag

#-------------トレンドフィルターの関数--------------

# トレンドフィルターの関数
def filter( signal ):
	
	if filter_VER == "OFF":
		return True
	
	if filter_VER == "A":
		if len(last_data) < MA_term:
			return True
		if data["settled"]["close_price"] > calculate_MA(MA_term) and signal["side"] == "BUY":
			return True
		if data["settled"]["close_price"] < calculate_MA(MA_term) and signal["side"] == "SELL":
			return True

	if filter_VER == "B":
		if len(last_data) < MA_term:
			return True
		if calculate_MA(MA_term) > calculate_MA(MA_term,-1) and signal["side"] == "BUY":
			return True
		if calculate_MA(MA_term) < calculate_MA(MA_term,-1) and signal["side"] == "SELL":
			return True
	return False

# 単純移動平均を計算する関数
def calculate_MA( value,before=None ):
	if before is None:
		MA = sum(i["close_price"] for i in last_data[-1*value:]) / value
	else:
		MA = sum(i["close_price"] for i in last_data[-1*value + before: before]) / value
	return round(MA)

#-------------資金管理の関数--------------

# 注文ロットを計算する関数
def calculate_lot( last_data,data,flag ):

	# 口座残高を取得する
	balance = bitflyer_collateral()

	# 最初のエントリーの場合
	if flag["add-position"]["count"] == 0:
		
		# １回の注文単位（ロット数）と、追加ポジの基準レンジを計算する
		volatility = calculate_volatility( last_data )
		stop = stop_range * volatility
		calc_lot = np.floor( balance * trade_risk / stop * 100 ) / 100
		
		flag["add-position"]["unit-size"] = np.floor( calc_lot / entry_times * 100 ) / 100
		flag["add-position"]["unit-range"] = round( volatility * entry_range )
		flag["add-position"]["stop"] = stop
		flag["position"]["ATR"] = round( volatility )
		
		print_log("現在のアカウント残高は{}円です".format( balance ))
		print_log("許容リスクから購入できる枚数は最大{}BTCまでです".format( calc_lot ))
		print_log("{0}回に分けて{1}BTCずつ注文します".format( entry_times, flag["add-position"]["unit-size"] ))
		
	
	# ストップ幅には、最初のエントリー時に計算したボラティリティを使う
	stop = flag["add-position"]["stop"]
	
	# 実際に購入可能な枚数を計算する
	able_lot = np.floor( balance * levarage / data["forming"]["close_price"] * 100 ) / 100
	lot = min(able_lot, flag["add-position"]["unit-size"])
	
	print_log("証拠金から購入できる枚数は最大{}BTCまでです".format( able_lot ))
	return lot,stop,flag

# 複数回に分けて追加ポジションを取る関数
def add_position( data,flag ):
	
	# ポジションがない場合は何もしない
	if flag["position"]["exist"] == False:
		return flag
	
	# 最初（１回目）のエントリー価格を記録
	if flag["add-position"]["count"] == 0:
		flag["add-position"]["first-entry-price"] = flag["position"]["price"]
		flag["add-position"]["last-entry-price"] = flag["position"]["price"]
		flag["add-position"]["count"] += 1
	
	# 以下の場合は、追加ポジションを取らない
	if flag["add-position"]["count"] >= entry_times:
		return flag
	
	# この関数の中で使う変数を用意
	first_entry_price = flag["add-position"]["first-entry-price"]
	last_entry_price = flag["add-position"]["last-entry-price"]
	unit_range = flag["add-position"]["unit-range"]
	current_price = data["forming"]["close_price"]
	
	
	# 価格がエントリー方向に基準レンジ分だけ進んだか判定する
	should_add_position = False
	if flag["position"]["side"] == "BUY" and (current_price - last_entry_price) > unit_range:
		should_add_position = True
	elif flag["position"]["side"] == "SELL" and (last_entry_price - current_price) > unit_range:
		should_add_position = True
	
	
	# 基準レンジ分進んでいれば追加注文を出す
	if should_add_position == True:
		print_log("前回のエントリー価格{0}円からブレイクアウトの方向に{1}ATR（{2}円）以上動きました".format( last_entry_price, entry_range, round( unit_range ) ))
		print_log("{0}/{1}回目の追加注文を出します".format(flag["add-position"]["count"] + 1, entry_times))
		
		# 注文サイズを計算
		lot,stop,flag = calculate_lot( last_data,data,flag )
		if lot < 0.01:
			print_log("注文可能枚数{}が、最低注文単位に満たなかったので注文を見送ります".format(lot))
			flag["add-position"]["count"] += 1
			return flag
		
		# 追加注文を出す
		if flag["position"]["side"] == "BUY":
			
			# ここに買い注文のコードを入れる
			print_log("現在のポジションに追加して{}BTCの買い注文を出します".format(lot))
			entry_price = bitflyer_market( "BUY", lot )
			
			
		if flag["position"]["side"] == "SELL":

			# ここに売り注文のコードを入れる
			print_log("現在のポジションに追加して{}BTCの売り注文を出します".format(lot))
			entry_price = bitflyer_market( "SELL", lot )
		
		
		# ポジション全体の情報を更新する
		flag["position"]["stop"] = stop
		flag["position"]["price"] = int(round(( flag["position"]["price"] * flag["position"]["lot"] + entry_price * lot ) / ( flag["position"]["lot"] + lot )))
		flag["position"]["lot"] = np.round( (flag["position"]["lot"] + lot) * 100 ) / 100		

		if flag["position"]["side"] == "BUY":
			print_log("{0}円の位置にストップを更新します".format(flag["position"]["price"] - stop))
		elif flag["position"]["side"] == "SELL":
			print_log("{0}円の位置にストップを更新します".format(flag["position"]["price"] + stop))
		print_log("現在のポジションの取得単価は{}円です".format(flag["position"]["price"]))
		print_log("現在のポジションサイズは{}BTCです".format(flag["position"]["lot"]))
		
		flag["add-position"]["count"] += 1
		flag["add-position"]["last-entry-price"] = entry_price
	
	return flag

# トレイリングストップの関数
def trail_stop( data,flag ):

	# まだ追加ポジションの取得中であれば何もしない
	if flag["add-position"]["count"] < entry_times:
		return flag
	
	# 高値／安値がエントリー価格からいくら離れたか計算
	if flag["position"]["side"] == "BUY":
		moved_range = round( data["settled"]["high_price"] - flag["position"]["price"] )
	if flag["position"]["side"] == "SELL":
		moved_range = round( flag["position"]["price"] - data["settled"]["low_price"] )
	
	# 最高値・最安値を更新したか調べる
	if moved_range < 0 or flag["position"]["stop-EP"] >= moved_range:
		return flag
	else:
		flag["position"]["stop-EP"] = moved_range
	
	# 加速係数に応じて損切りラインを動かす
	flag["position"]["stop"] = round(flag["position"]["stop"] - ( moved_range + flag["position"]["stop"] ) * flag["position"]["stop-AF"])
		
	# 加速係数を更新
	flag["position"]["stop-AF"] = round( flag["position"]["stop-AF"] + stop_AF_add ,2 )
	if flag["position"]["stop-AF"] >= stop_AF_max:
		flag["position"]["stop-AF"] = stop_AF_max
	
	# ログ出力
	if flag["position"]["side"] == "BUY":
		print_log("トレイリングストップの発動：ストップ位置を{}円に動かして、加速係数を{}に更新します".format( round(flag["position"]["price"] - flag["position"]["stop"]) , flag["position"]["stop-AF"] ))
	else:
		print_log("トレイリングストップの発動：ストップ位置を{}円に動かして、加速係数を{}に更新します".format( round(flag["position"]["price"] + flag["position"]["stop"]) , flag["position"]["stop-AF"] ))
	
	return flag

#-------------価格APIの関数--------------

# BTCFXのチャート価格をAPIで取得する関数（実行時の取得用）
def get_price(min, before=0, after=0):
	
	# Cryptowatchを使用する場合
	if chart_API == "cryptowatch":
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
			print_log("データが存在しません")
			return None

	# CryptoCompareを使用する場合（１時間足のみ対応）
	if chart_API == "cryptocompare":
		price = []
		params = {"fsym":"BTC","tsym":"JPY","e":"bitflyerfx","limit":2000 }
		
		response = requests.get("https://min-api.cryptocompare.com/data/histohour",params, timeout = 10)
		data = response.json()
		
		if data["Response"] == "Success":
			for i in data["Data"]:
				price.append({ "close_time" : i["time"],
					"close_time_dt" : datetime.fromtimestamp(i["time"]).strftime('%Y/%m/%d %H:%M'),
					"open_price" : i["open"],
					"high_price" : i["high"],
					"low_price" : i["low"],
					"close_price": i["close"] })
			return price
			
		else:
			print_log("データが存在しません")
			return None

# BTCFXのチャート価格をAPIで取得する関数（リアルタイム用）
def get_realtime_price(min):

	# Cryptowatchを使用する場合
	if chart_API == "cryptowatch":
		params = {"periods" : min }
		while True:
			try:
				response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc", params, timeout = 10)
				response.raise_for_status()
				data = response.json()
				return {
						"settled" : { 
							"close_time" : data["result"][str(min)][-2][0],
							"open_price" : data["result"][str(min)][-2][1],
							"high_price" : data["result"][str(min)][-2][2],
							"low_price" : data["result"][str(min)][-2][3],
							"close_price": data["result"][str(min)][-2][4]
							},
						"forming" : { "close_time" : data["result"][str(min)][-1][0],
							"open_price" : data["result"][str(min)][-1][1],
							"high_price" : data["result"][str(min)][-1][2],
							"low_price" : data["result"][str(min)][-1][3],
							"close_price": data["result"][str(min)][-1][4]
							}
						}
			
			except requests.exceptions.RequestException as e:
				print_log("Cryptowatchの価格取得でエラー発生 : " + str(e))
				print_log("{}秒待機してやり直します".format(wait))
				time.sleep(wait)

	# CryptoCompareを使用する場合（１時間足のみ対応）
	if chart_API == "cryptocompare":
		params = {"fsym":"BTC","tsym":"JPY","e":"bitflyerfx" }
		
		while True:
			try:
				response = requests.get("https://min-api.cryptocompare.com/data/histohour", params, timeout = 10)
				response.raise_for_status()
				data = response.json()
				time.sleep(5)
				
				response2 = requests.get("https://min-api.cryptocompare.com/data/histominute", params ,timeout = 10)
				response2.raise_for_status()
				data2 = response2.json()
				
			except requests.exceptions.RequestException as e:
				print_log("Cryptocompareの価格取得でエラー発生 : " + str(e))
				print_log("{}秒待機してやり直します".format(wait))
				time.sleep(wait)
				continue
			
			return {
				"settled" : { 
					"close_time" : data["Data"][-2]["time"],
					"open_price" : data["Data"][-2]["open"],
					"high_price" : data["Data"][-2]["high"],
					"low_price" : data["Data"][-2]["low"],
					"close_price": data["Data"][-2]["close"]
					},
				"forming" : { 
					"close_time" : data2["Data"][-1]["time"],
					"open_price" : data2["Data"][-1]["open"],
					"high_price" : data2["Data"][-1]["high"],
					"low_price" : data2["Data"][-1]["low"],
					"close_price": data2["Data"][-1]["close"]
					}
			}

#-------------その他の補助関数--------------

# 時間と高値・安値・終値を表示する関数
def print_price( data ):
	print_log( "時間： " + datetime.fromtimestamp(data["close_time"]).strftime('%Y/%m/%d %H:%M') + " 高値： " + str(data["high_price"]) + " 安値： " + str(data["low_price"]) + " 終値： " + str(data["close_price"]) )

# １期間の平均ボラティリティを計算する
def calculate_volatility( last_data ):

	high_sum = sum(i["high_price"] for i in last_data[-1 * volatility_term :])
	low_sum  = sum(i["low_price"]  for i in last_data[-1 * volatility_term :])
	volatility = round((high_sum - low_sum) / volatility_term)
	print_log("現在の{0}期間の平均ボラティリティは{1}円です".format( volatility_term, volatility ))
	return volatility

# ログファイルの出力やLINE通知の関数
def print_log( text ):
	
	# LINE通知する場合
	if line_config == "ON":
		url = "https://notify-api.line.me/api/notify"
		data = {"message" : text}
		headers = {"Authorization": "Bearer " + line_token} 
		requests.post(url, data=data, headers=headers)
	
	# コマンドラインへの出力とファイル保存
	if log_config == "ON":
		logger.info( text )
	else:
		print( text )

#-------------トラブル対策用の関数--------------

def find_unexpected_pos( flag ):
	
	if flag["position"]["exist"] == True:
		return flag
	count = 0
	while True:
		price,size,side = bitflyer_check_positions()
		if size == 0:
			return flag
		
		print_log("把握していないポジションが見つかりました")
		print_log("反映の遅延でないことを確認するため様子を見ています")
		count += 1
		
		if count > 5:
			print_log("把握していないポジションが見つかったためポジションを復活させます")
			
			flag["position"]["exist"] = True
			flag["position"]["side"] = side
			flag["position"]["lot"] = size
			flag["position"]["price"] = price
			flag["position"]["stop-AF"] = stop_AF
			flag["position"]["stop-EP"] = 0
			flag["add-position"]["count"] = entry_times
			
			if flag["position"]["ATR"] == 0:
				flag["position"]["ATR"] = calculate_volatility( last_data )
				flag["position"]["stop"] = flag["position"]["ATR"] * stop_range
			pprint(flag)
			return flag
		time.sleep(30)

#-------------Bitflyerと通信する関数--------------

# 成行注文をする関数
def bitflyer_market(side,lot):
	while True:
		try:
			order = bitflyer.create_order(
				symbol = 'BTC/JPY',
				type='market',
				side= side,
				amount= lot,
				params = { "product_code" : "FX_BTC_JPY" })
			print_log("--------------------")
			print_log( order )
			print_log("--------------------")
			order_id = order["id"]
			time.sleep(30)
			
			# 執行状況を確認
			average_price = bitflyer_check_market_order( order_id, lot )
			return average_price
			
		except ccxt.BaseError as e:
			print_log("Bitflyerの注文APIでエラー発生 : " + str(e))
			print_log("注文が失敗しました")
			print_log("30秒待機してやり直します")
			time.sleep(30)

# 成行注文の執行状況を確認する関数
def bitflyer_check_market_order( id,lot ):
	while True:
		try:
			size = []
			price = []
			
			executions = bitflyer.private_get_getexecutions( params = { "product_code" : "FX_BTC_JPY" })
			for exec in executions:
				if exec["child_order_acceptance_id"] == id:
					size.append( exec["size"] )
					price.append( exec["price"] )
			
			# 全部約定するまで待つ
			if round(sum(size),2) != lot:
				time.sleep(20)
				print_log("注文がすべて約定するのを待っています")
			else:
				# 平均価格を計算する
				average_price = round(sum( price[i] * size[i] for i in range(len(price)) ) / sum(size))
				print_log("すべての成行注文が執行されました")
				print_log("執行価格は平均 {}円です".format(average_price))
				return average_price
				
		except ccxt.BaseError as e:
			print_log("BitflyerのAPIで問題発生 : " + str(e))
			print_log("20秒待機してやり直します")
			time.sleep(20)

# 口座残高を取得する関数
def bitflyer_collateral():
	while True:
		try:
			collateral = bitflyer.private_get_getcollateral()
			spendable_collateral = np.floor(collateral["collateral"] - collateral["require_collateral"])
			print_log("現在のアカウント残高は{}円です".format( int(collateral["collateral"]) ))
			print_log("新規注文に利用可能な証拠金の額は{}円です".format( int(spendable_collateral) ))
			return int( spendable_collateral )
			
		except ccxt.BaseError as e:
			print_log("BitflyerのAPIでの口座残高取得に失敗しました ： " + str(e))
			print_log("20秒待機してやり直します")
			time.sleep(20)

# ポジション情報を取得する関数
def bitflyer_check_positions():
	failed = 0
	while True:
		try:
			size = []
			price = []
			positions = bitflyer.private_get_getpositions( params = { "product_code" : "FX_BTC_JPY" })
			if not positions:
				#print_log("現在ポジションは存在しません")
				return 0,0,None
			for pos in positions:
				size.append( pos["size"] )
				price.append( pos["price"] )
				side = pos["side"]
			
			# 平均建値を計算する
			average_price = round(sum( price[i] * size[i] for i in range(len(price)) ) / sum(size))
			sum_size = round(sum(size),2)
			#print_log("保有中の建玉：合計{}つ\n平均建値：{}円\n合計サイズ：{}BTC\n方向：{}".format(len(price),average_price,sum_size,side))
			
			# 価格・サイズ・方向を返す
			return average_price,sum_size,side
				
		except ccxt.BaseError as e:
			failed += 1
			if failed > 10:
				print_log("Bitflyerのポジション取得APIでエラーに10回失敗しました : " + str(e))
				print_log("20秒待機してやり直します")
			time.sleep(20)

#------------ここからメイン処理の記述--------------

# 最低限、保持が必要なローソク足の期間を準備

need_term = max(buy_term,sell_term,volatility_term,MA_term)
print_log("{}期間分のデータの準備中".format(need_term))

price = get_price(chart_sec)
last_data = price[-1*need_term-2:-2]
print_price(last_data[-1])
print_log("--{}秒待機--".format(wait))
time.sleep(wait)

print_log("---実行開始---")

while True:

	# 最新のローソク足を取得して表示
	data = get_realtime_price( chart_sec )
	if data["settled"]["close_time"] > last_data[-1]["close_time"]:
		print_price( data["settled"] )
	
	# ポジションがある場合
	if flag["position"]["exist"]:
		flag = stop_position( data,flag )
		flag = close_position( data,last_data,flag )
		flag = add_position( data,flag )
	
	# ポジションがない場合
	else:
		flag = find_unexpected_pos( flag )
		flag = entry_signal( data,last_data,flag )
	
	# 確定足が更新された場合
	if data["settled"]["close_time"] > last_data[-1]["close_time"]:
		last_data.append( data["settled"] )
		if len(last_data) > need_term:
			del last_data[0]
	
	time.sleep(wait)