import requests
from datetime import datetime
import time

response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc",params = { "periods" : 60 })

def get_price(min,i):
    data = response.json()
    return {"close_time" : data["result"][str(min)][i][0],
            "open_price" : data["result"][str(min)][i][1],
            "high_price" : data["result"][str(min)][i][2],
            "low_price" : data["result"][str(min)][i][3],
            "close_price" : data["result"][str(min)][i][4]}

def print_price(data):
    print(f'時間{datetime.fromtimestamp(data["close_time"]).strftime("%Y/%m/%d/%H:%M/")}始値:{data["open_price"]}/終値:{data["close_price"]}')

#各ローソク足がエントリーの条件（陽線）を満たしているか確認する関数
def check_candle(data):
    realbody_rate = abs(data["close_price"] - data["open_price"]/(data["high_price"]-data["low_price"]))
    increase_rate = data["close_price"] / data["open_price"] - 1

    if data["close_price"] < data["open_price"] : return False
    elif increase_rate < 0.0005 : return False
    elif realbody_rate <0.5 : return False
    else: return True

#ローソク足の始値・終値が連続で切り上がっているか確認する関数
def check_ascend(data,last_data):
    if data["open_price"] > last_data["open_price"] and data["close_price"] > last_data["close_price"]:
        return True
    else:
        return False

#買いシグナルが店頭したら指値で買い注文する関数
def buy_signal(data,last_data,flag):
    if flag["buy_signal"] == 0 and check_candle(data):
        flag["buy_signal"] = 1
    elif flag["buy_signal"] == 1 and check_candle(data) and check_ascend(data,last_data):
        flag["buy_signal"] = 2
    elif flag["buy_signal"] == 2 and check_candle(data) and check_ascend(data,last_data):
        print(f"3本連続で陽線なので{str(data['close_price'])}で買い指値")
        #ここに買い注文のコードを入れる

        flag["buy_signal"] = 3
        flag["order"] = True
    else:
        flag["buy_signal"] = 0
    return flag

#手仕舞いのシグナルが出たら決済の成り行き注文を出す関数
def close_position(data,last_data,flag):
    if data["close_price"] < last_data["close_price"]:
        print(f"前回の終値を下回ったので{str(data['close_price'])}で決済")
        flag["position"] = False
    return flag

def check_order(flag):

    #注文状況を確認して通っていたら以下を実行
    #一定時間で注文が通っていなければキャンセルする

    flag["order"] = False
    flag["position"] = True
    return flag

#ここからメイン処理
last_data = get_price(60,0)
print_price(last_data)

flag = {
        "buy_signal" :0,
        "sell_signal" :0,
        "order" :False,
        "position":False
}
i=1

while i<500:
    if flag["order"]:
        flag = check_order(flag)
    
    data = get_price(60,i)
    if data["close_time"] != last_data["close_time"]:
        print_price(data)

        if flag["position"]:
            flag = close_position(data,last_data,flag)
        else:
            flag = buy_signal(data,last_data,flag)
        
        last_data["close_time"] = data["close_time"]
        last_data["open_price"] = data["open_price"]
        last_data["close_price"] = data["close_price"]
        i +=1
    time.sleep(0)