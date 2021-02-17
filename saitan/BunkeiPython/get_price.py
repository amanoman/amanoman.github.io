import requests
from datetime import datetime
import time
import json

def get_price(min, before=0,after=0):
    price = []
    params = {"periods" :min}
    if before != 0:
        params["before"] = before
    if after != 0:
        params["after"] = after

    response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc", params)
    data = response.json()

    if data["result"][str(min)]is not None:
        for i in data["result"][str(min)]:
            price.append({"close_time" : i[0],
                "close_time_dt" : datetime.fromtimestamp(i[0]).strftime('%Y/%m/%d/%H:%M'),
                "open_price" : i[1],
                "high_price" : i[2],
                "low_price" : i[3],
                "close_price" : i[4]})
        return price

    else:
        print("データが存在しません")
        return None


#ここからメイン
price = get_price(300, after=1611757669)

if price is not None:
    print(f'先頭データ{price[0]["close_time_dt"]}UNIX時間{str(price[0]["close_time"])}')
    print(f'先頭データ{price[-1]["close_time_dt"]}UNIX時間{str(price[-1]["close_time"])}')
    print(f'合計{str(len(price))}件のローソク足データを取得')
    print("-"*20)
    print("-"*20)

file = open("./{0}-{1}-price.json".format(price[0]["close_time"],price[-1]["close_time"]),"w",encoding="utf-8")
json.dump(price,file,indent=4)
