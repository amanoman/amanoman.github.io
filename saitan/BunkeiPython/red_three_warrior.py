import requests
from datetime import datetime
import time


def get_price(min):
    response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc",params = { "periods" : min })
    data = response.json() 
    last_data = data["result"][str(min)][-2] 

    return {"close_time" : last_data[0],
            "open_price" : last_data[1],
            "high_price" : last_data[2],
            "low_price" : last_data[3],
            "close_price" : last_data[4]}
    #この関数を使って取得したデータはdata["open_price"]などで取り出せる

def print_price(data):
    print(f"時間:{datetime.fromtimestamp(data['close_time']).strftime('%Y/%m/%d/%H:%M')} 始値:{data['open_price']}/終値:{data['close_price']}")

def check_candle(data):
    realbody_rate = abs(data["close_price"] - data["open_price"] / (data["high_price"] - data["low_price"])) #ローソク足の実体の割合
    increase_rate = data["close_price"] / data["open_price"] -1 #価格の上昇率

    if data["close_price"] < data["open_price"] : return False #終値が始値より小さかったらFalse
    elif increase_rate < 0.005 : return False #価格の上昇率が0.005より小さかったらFalse
    elif realbody_rate < 0.5 : return False #ローソク足の実体の割合が50%未満ならFalse
    else : return True #上記以外の場合はTrueなのでlongCondition

def check_ascend(data,last_data):
    if data["open_price"] > last_data["open_price"] and data["close_price"] > last_data["close_price"]: #始値と終値が両方前日を上回る場合True
        return True
    else: #そうじゃない場合はFalse
        return False

last_data = get_price(60)
print_price(last_data)
flag = 0

while True:
    data = get_price(60)

    if data["close_time"] != last_data["close_time"]: #今のclose時間が更新されたかどうかの判定。更新されていたら価格をプリントしてフラグチェック。
        print_price(data)

        if flag == 0 and check_candle(data):
            flag = 1
        elif flag == 1 and check_candle(data) and check_ascend(data,last_data):
            print("２本連続で陽線")
            flag = 2
        elif flag == 2 and check_candle(date) and check_ascend(data,last_data):
            print("３本連続で陽線なので買い！")
            flag = 3
        else:
            flag = 0
        #close_timeたちを今の時間のものに更新する。次の更新があるまでこのまま。
        last_data["close_time"] = data["close_time"]
        last_data["open_price"] = data["open_price"]
        last_data["close_price"] = data["close_price"]

    time.sleep(10) #10秒に１回この処理を実施。1分間に回更新をかけている。