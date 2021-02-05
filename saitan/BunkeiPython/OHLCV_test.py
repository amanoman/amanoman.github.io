import requests
from datetime import datetime
import time

    #CryptowatchのAPIで１分足を取得
response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc?periods=60")
response = response.json()

#前回の時間をlast_timeに入れる
last_data = response["result"]["60"][-2]
last_time = datetime.fromtimestamp(last_data[0]).strftime('%d/%m/%d %H:%M')
time.sleep(10)

while True:

    response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc?periods=60")
    response = response.json()

    #最後から２番目のローソク足を取り出す
    data = response["result"]["60"][-2]

    #今回の時間をclose_timeに入れる
    #ローソク足から日時・始値・終値を取り出す
    close_time = datetime.fromtimestamp(data[0]).strftime('%Y/%m/%d %H:%M')
    open_price = data[1]
    close_price = data[4]

    #前回の時間(last_time)と今回の時間(close_time)が違う場合のみprintする。
    if close_time != last_time:
        print(f"時間：{close_time}\n始値：{str(open_price)}\n終値：{str(close_price)}")
        # 前回の時間(last_time)を今回の時間(close_time)で上書きする。
        last_time = close_time

    time.sleep(10)
