import ccxt
from PASSWORDS.password import *

bitflyer = ccxt.bitflyer()
bitflyer.apiKey = bitFlyer_apiKey
bitflyer.secret = bitFlyer_secret

def check_bf_positions():
    while True:
        try:
            size=[]
            price=[]
            positions = bitflyer.private_get_getpositions(params = {"product_code" : "FX_BTC_JPY"})
            if not positions:
                print("現在ポジションは存在しません")
                return 0,0,None
            for pos in position:
                size.append(pos["size"])
                price.apped(pos["price"])
                side = pos["side"]

            #平均建値を計算する。
            average_price = round(sum(price[i] * size[i] for i in range(len(price)))/sum(size))
            sum_size = round(sum(size),2)
            print(f"保有中の建玉：合計{len(price)}つ\n平均建値:{average_price}円\n合計サイズ:{sum_size}BTC\n方向:{side}")

            #価格・サイズ・方向を返す
            return average_price,sum_size,side
        
        except ccxt.BaseError as e:
            print("BitFlyerのAPIで問題発生:",e)
            print("20秒待機してやり直します")
            time.sleep(20)

#実行処理
price,size,side = check_bf_positions()