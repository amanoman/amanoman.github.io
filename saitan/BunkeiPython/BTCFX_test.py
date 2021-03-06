import requests
from datetime import datetime
import time
import ccxt
from PASSWORDS.password import *

bitflyer = ccxt.bitflyer()
bitflyer.apiKey = bitFlyer_apiKey
bitflyer.secret = bitFlyer_secret

#Cryptowatchから価格を取得する関数
def get_price(min,i):
    response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc", params={"periods": 60})
    data = response.json()
    return { "close_time" : data["result"][str(min)][i][0],
            "open_price" : data["result"][str(min)][i][1],
            "high_price" : data["result"][str(min)][i][2],
            "low_price" : data["result"][str(min)][i][3],
            "close_price" : data["result"][str(min)][i][4]}

#時間と始値・終値を表示する関数
def print_price(data):
    print(f'時間：{datetime.fromtimestamp(data["close_time"]).strftime("%Y/%m/%d/%H:%M")}/始値：{str(data["open_price"])}/終値：{str(data["close_price"])}')

#各ローソク足が陽線・陰線の基準を満たしているか確認する関数
def check_candle(data,side):
    realbody_rate = abs(data["close_price"] - data["open_price"] / (data["high_price"]-data["low_price"]))
    increase_rate = data["close_price"] / data["open_price"] - 1

    if side == "buy":
        if data["close_price"] < data["open_price"] : return False
        elif increase_rate < 0.0003 : return False
        elif realbody_rate < 0.5 : return False
        else : return True

    if side == "sell":
        if data["close_price"] > data["open_price"]: return False
        elif increase_rate > -0.0003 : return False
        elif realbody_rate < 0.5 : return False
        else : return True
    
#ローソク足が連続で上昇しているか確認する関数
def check_ascend(data,last_data):
    if data["open_price"] > last_data["open_price"] and data["close_price"] > last_data["close_price"]:
        return True
    else:
        return False

#ローソク足がr年族で下落しているか確認する関数
def check_descend(data,last_data):
    if data["open_price"] < last_data["open_price"] and data["close_price"] < last_data["close_price"]:
        return True
    else:
        return False
#買いシグナルが出たら指値で買い注文を出す関数
def buy_signal(data,last_data,flag):
    if flag["buy_signal"] == 0 and check_candle(data,"buy"):
        flag["buy_signal"] = 1

    elif flag["buy_signal"] == 1 and check_candle(data,"buy") and check_ascend(data,last_data):
        flag["buy_signal"] = 2
    
    elif flag["buy_signal"] == 2 and check_candle(data,"buy") and check_ascend(data,last_data):
        print(f'３本連続で陽線なので{str(data["close_price"])}で買い指値を入れます')
        flag["buy_signal"] = 3

        order = bitFlyer.create_order(
            symbol = 'FX_BTC_JPY',
            type = 'limit',
            side ='buy',
            price = data["close_price"],
            amount = 'o.01',
            params = {"product_code" : "FX_BTC_JPY"})
        flag["order"]["exist"] = True
        flag["order"]["side"] = "BUY"

    else:
            flag["buy_signal"] = 0

    return flag

#売りシグナルがでたら指値で売り注文を出す関数
def sell_signal(data,last_data,flag):
    if flag["sell_signal"] == 0 and check_candle(data,"sell"):
        flag["sell_signal"] = 1

    elif flag["sell_signal"] == 1 and check_candle(data,"sell") and check_descend(data,last_data):
        flag["sell_signal"] = 2

    elif flag["sell_signal"] == 2 and check_candle(data,"sell") and check_descend(data,last_data):
        print(f'３本連続で陰線なので{str(data["close_price"])}で売り指値を入れます')
        flag["sell_signal"] = 3
        
        order = bitflyer.create_order(
            symbol = 'FX_BTC_JPY',
            type = 'limit',
            side = 'side',
            price=data["close_price"],
            amount='0.01',
            params = { "product_code" : "FX_BTC_JPY"})
        flag["order"]["exist"] = True
        flag["order"]["side"] = "SELL"
    
    else:
        flag["sell_signal"] = 0
    return flag

#手仕舞いのシグナルが出たら決済の成行注文を出す関数
def close_position(data,last_data,flag):
    if flag["position"]["side"] == 'BUY':
        if data["close_price"] < last_data["close_price"]:
            print(f'前回の終値を下回ったので{str(data["close_price"])}あたりで成行で決済します')
            order = bitflyer.create_order(
                symbol = 'FX_BTC_JPY',
                type = 'market',
                side = 'sell',
                amount = '0.01',
                params = {"product_code" : "FX_BTC_JPY"})
            flag["position"]["exist"] = False

    if flag["position"]["side"] == 'SELL':
        if data["close_price"] < last_data["close_price"]:
            print(f'前回の終値を上回ったので{str(data["close_price"])}あたりで成行で決済します')
            order=bitflyer.create_order(
                symbol = 'FX_BTC_JPY',
                type = 'market',
                side = 'buy',
                amount = '0.01',
                params = {"product_code": "FX_BTC_JPY"})
            flag["position"]["exist"]=False

#サーバーに出した注文が約定したかどうかチェックする関数
def check_order(flag):
    position = bitflyer.private_get_getpositions(params= {"product_code" : "FX_BTC_JPY"})
    orders = bitflyer.getch_open_orders(
            symbol = "FX_BTC_JPY",
            params = {"product_code" : "FX_BTC_JPY"})

    if position:
        print("注文が約定しました！")
        flag["order"]["exitst"] = False
        flag["order"]["count"] = 0
        flag["position"]["exitst"] = True
        flag["position"]["side"] = flag["order"]["side"]
    else:
        if orders:
            print("まだ未約定の注文があります")
            for o in orders:
                print(o["id"])
            flag["order"]["count"] += 1
            if flag["order"]["count"] > 6:
                flag = cancel_order(orders,flag)
        else:
            print("注文が遅延しているようです")
    return flag


#注文をキャンセルする関数
def cancel_order(orders,flag):
    for o in orders:
        bitflyer.cancel_order(
            symbol = "FX_BTC_JPY",
            id = o["id"],
            params = {"product_code" : "FX_BTC_JPY"})
    print("約定していない注文をキャンセルしました")
    flag["order"]["count"] = 0
    flag["order"]["exist"]  = False

    time.sleep(20)
    position = bitflyer.private_get_getpositions(params = {"product_code" : "FX_BTC_JPY"})
    if not position:
        print("現在、未決済の建玉はありません")
    else:
        print("現在、まだ未決済の建玉があります")
        flag["position"]["exitst"] = True
        flag["position"]["side"] = position[0]["side"]
    return flag

#ここからがメイン
last_data = get_price(60,-2)
print_price(last_data)
time.sleep(10)

flag = {
    "buy_signal": 0,
    "sell_signal" : 0,
    "order" : {
        "exist" : False,
        "side" : "",
        "count" : 0
    },
    "position" : {
        "exist" : False,
        "side" : ""
    }
    
}

while True:
    if flag["order"]["exist"]:
        flag = check_order(flag)

    data = get_price(60,-2)
    if data["close_time"] != last_data["close_time"]:
        print_price(data)
        if flag["position"]["exist"]:
            flag = close_position(data,lasta_data,flag)
        else:
            flag = buy_signal(data,last_data,flag)
            flag = sell_signal(data,last_data,flag)
        last_data["close_time"] = data["close_time"]
        last_data["open_price"] = data["open_price"]
        last_data["close_price"] = data["close_price"]

    time.sleep(10)
