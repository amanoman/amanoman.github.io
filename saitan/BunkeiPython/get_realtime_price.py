import requests
from datetime import datetime
import time
import json
import ccxt
from PASSWORDS.password import *


#-------------設定項目------------------------

wait = 60                    # ループの待機時間（30秒推奨）
buy_term = 30                # 最高値（上値）ブレイクアウト期間
sell_term = 30               # 最安値（下値）ブレイクアウト期間
chart_sec = 300             # 使用する時間軸（秒換算）
chart_API = "cryptowatch"    # 価格の取得元を（cryptowatch/cryptocompare）から選択

judge_price={
  "BUY" : "close_price",     # ブレイク判断　高値（high_price)か終値（close_price）を使用
  "SELL": "close_price"      # ブレイク判断　安値 (low_price)か終値（close_price）を使用
}

volatility_term = 5          # 平均ボラティリティの計算に使う期間
stop_range = 2               # 何レンジ幅にストップを入れるか
trade_risk = 0.01            # 1トレードあたり口座の何％まで損失を許容するか
levarage = 1                 # レバレッジ倍率の設定

entry_times = 2              # 何回に分けて追加ポジションを取るか
entry_range = 0.5              # 何レンジごとに追加ポジションを取るか

trailing_config = "ON"       # ONで有効 OFFで無効
stop_AF = 0.02               # 加速係数
stop_AF_add = 0.02           # 加速係数を増やす度合
stop_AF_max = 0.2            # 加速係数の上限

filter_VER = "A"           # フィルター設定／OFFで無効
MA_term = 200                # トレンドフィルターに使う移動平均線の期間

bitflyer = ccxt.bitflyer()
bitflyer.apiKey = bitFlyer_apiKey         # APIキーを設定
bitflyer.secret = bitFlyer_secret         # APIシークレットを設定
bitflyer.timeout = 30000     # 通信のタイムアウト時間の設定

line_config = "ON"          # LINE通知をするかどうかの設定
log_config = "OFF"          # ログファイルを出力するかの設定
log_file_path = ""          # ログを記録するファイル名と出力パス
line_token = LINE_token     # LINE通知を使用する場合はAPIキーを入力


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

# json形式のファイルから価格データを読み込む関数
def get_price_from_file(path):
	file = open(path,"r",encoding="utf-8")
	price = json.load(file)
	return price


# ここからメイン
price = get_realtime_price(60)
print(price)
#ファイルから読みこむ場合
#price = get_price_from_file("./ファイル名.json")