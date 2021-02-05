import ccxt
from pprint import pprint
from PASSWORDS.password import *

bitflyer = ccxt.bitflyer()
bitflyer.apiKey = bitFlyer_apiKey
bitflyer.secret = bitFlyer_secret

orders = bitflyer.fetch_orders(
    symbol="FX_BTC_JPY",
    params= {"product_code" : "FX_BTC_JPY",
        "count": 10})

#pprint(orders)
#for order in orders:
     #print(f'{order["id"]} : 注文状況{order["status"]} : サイズ{order["remaining"]}')

bitflyer.cancel_order(
    symbol = "FX_BTC_JPY",
    id= orders[-1]["id"],
    params = { "product_code" : "FX_BTC_JPY"}
)


for order in orders:
    print(f'{order["id"]} : 注文状況{order["status"]} : サイズ{order["remaining"]}')

    

