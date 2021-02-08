import requests
from datetime import datetime
import time

#Cryptwatchから○分足のデータを取得する関数を作成
def get_price(min):

    #APIで価格を取得する
    response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc",params = { "periods" : min })
    response = response.json()
    data = response["result"][str(min)][-2]#最新がリストの最後のデータなので、最後から２番目＝[-2]している。最新データには終値がないから。高値、安値を取得する場合でも確定していないので注意。

    close_time = data[0] #１個前のリストデータの先頭のタイムスタンプを取得
    open_price = data[1] #１個前のリストデータの２番めのOHLCVデータのO始値を取得
    close_price = data[4]#１個前のリストデータの２番めのOHLCVデータのC終値を取得

    #日時・終値・始値の３つを返す
    return close_time, open_price, close_price

#日時・終値・始値を表示する関数を作成
def print_price(close_time, open_price, close_price):
    print(f"時間:{datetime.fromtimestamp(close_time).strftime('%Y年%m月%d日 %H:%M')} 始値:{str(open_price)} 終値:{str(close_price)}")

#ここからがメイン処理
last_time = 0
while True:
    #get_price()関数を使って最新のローソク足の日時・始値・終値を取得する
    close_time, open_price, close_price = get_price(60)

    if close_time != last_time:  #close_time == last_timeである間は実行されない
        last_time = close_time

        # print_price()関数を使って価格データを表示する
        print_price(close_time, open_price, close_price)

    time.sleep(10)