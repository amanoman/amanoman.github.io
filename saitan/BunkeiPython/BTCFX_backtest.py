import requests
from datetime import datetime
import time


# 最初に１度だけCryptowatchから価格データ取得
response = requests.get(
	"https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc", params={"periods": 60})

# 指定されたローソク足の価格データ（OHLC）を返す関数


def get_price(min, i):
	data = response.json()
	return {"close_time": data["result"][str(min)][i][0],
         "open_price": data["result"][str(min)][i][1],
         "high_price": data["result"][str(min)][i][2],
         "low_price": data["result"][str(min)][i][3],
         "close_price": data["result"][str(min)][i][4]}


# 時間と始値・終値を表示する関数
def print_price(data):
	print("時間： " + datetime.fromtimestamp(data["close_time"]).strftime(
		'%Y/%m/%d %H:%M') + " 始値： " + str(data["open_price"]) + " 終値： " + str(data["close_price"]))


# 各ローソク足が陽線・陰線の基準を満たしているか確認する関数
def check_candle(data, side):
	realbody_rate = abs(data["close_price"] - data["open_price"]
	                    ) / (data["high_price"]-data["low_price"])
	increase_rate = data["close_price"] / data["open_price"] - 1

	if side == "buy":
		if data["close_price"] < data["open_price"]:
			return False
		elif increase_rate < 0.0003:
			return False
		elif realbody_rate < 0.5:
			return False
		else:
			return True

	if side == "sell":
		if data["close_price"] > data["open_price"]:
			return False
		elif increase_rate > -0.0003:
			return False
		elif realbody_rate < 0.5:
			return False
		else:
			return True


# ローソク足が連続で上昇しているか確認する関数
def check_ascend(data, last_data):
	if data["open_price"] > last_data["open_price"] and data["close_price"] > last_data["close_price"]:
		return True
	else:
		return False

# ローソク足が連続で下落しているか確認する関数


def check_descend(data, last_data):
	if data["open_price"] < last_data["open_price"] and data["close_price"] < last_data["close_price"]:
		return True
	else:
		return False


# 買いシグナルが出たら指値で買い注文を出す関数
def buy_signal(data, last_data, flag):
	if flag["buy_signal"] == 0 and check_candle(data, "buy"):
		flag["buy_signal"] = 1

	elif flag["buy_signal"] == 1 and check_candle(data, "buy") and check_ascend(data, last_data):
		flag["buy_signal"] = 2

	elif flag["buy_signal"] == 2 and check_candle(data, "buy") and check_ascend(data, last_data):
		print("３本連続で陽線 なので" + str(data["close_price"]) + "で買い指値を入れます")
		flag["buy_signal"] = 3

		# ここに買い指値注文のコードを入れる
		flag["order"]["exist"] = True
		flag["order"]["side"] = "BUY"

	else:
		flag["buy_signal"] = 0
	return flag


# 売りシグナルが出たら指値で売り注文を出す関数
def sell_signal(data, last_data, flag):
	if flag["sell_signal"] == 0 and check_candle(data, "sell"):
		flag["sell_signal"] = 1

	elif flag["sell_signal"] == 1 and check_candle(data, "sell") and check_descend(data, last_data):
		flag["sell_signal"] = 2

	elif flag["sell_signal"] == 2 and check_candle(data, "sell") and check_descend(data, last_data):
		print("３本連続で陰線 なので" + str(data["close_price"]) + "で売り指値を入れます")
		flag["sell_signal"] = 3

		# ここに売り指値注文のコードを入れる
		flag["order"]["exist"] = True
		flag["order"]["side"] = "SELL"

	else:
		flag["sell_signal"] = 0
	return flag


# 手仕舞いのシグナルが出たら決済の成行注文を出す関数
def close_position(data, last_data, flag):
	if flag["position"]["side"] == "BUY":
		if data["close_price"] < last_data["close_price"]:
			print("前回の終値を下回ったので" + str(data["close_price"]) + "あたりで成行で決済します")
			# 決済の成行注文のコードを入れる
			flag["position"]["exist"] = False

	if flag["position"]["side"] == "SELL":
		if data["close_price"] > last_data["close_price"]:
			print("前回の終値を上回ったので" + str(data["close_price"]) + "あたりで成行で決済します")
			# 決済の成行注文のコードを入れる
			flag["position"]["exist"] = False
	return flag


# サーバーに出した注文が約定したかどうかチェックする関数
def check_order(flag):

	# 注文状況を確認して通っていたら以下を実行
	# 一定時間で注文が通っていなければキャンセルする

	flag["order"]["exist"] = False
	flag["order"]["count"] = 0
	flag["position"]["exist"] = True
	flag["position"]["side"] = flag["order"]["side"]
	return flag


# ここからメイン処理の部分
# まず初期値の取得
last_data = get_price(60, 0)
print_price(last_data)


# 注文管理用のフラッグを準備
flag = {
	"buy_signal": 0,
	"sell_signal": 0,
	"order": {
		"exist": False,
		"side": "",
		"count": 0
	},
	"position": {
		"exist": False,
		"side": ""
	}
}

# 500回ループ処理
i = 1
while i < 500:
	if flag["order"]["exist"]:
		flag = check_order(flag)

	data = get_price(60, i)
	print_price(data)

	if flag["position"]["exist"]:
		flag = close_position(data, last_data, flag)
	else:
		flag = buy_signal(data, last_data, flag)
		flag = sell_signal(data, last_data, flag)
	last_data["close_time"] = data["close_time"]
	last_data["open_price"] = data["open_price"]
	last_data["close_price"] = data["close_price"]
	i += 1
