import ccxt
from pprint import pprint
from PASSWORDS.password import *

bitflyer = ccxt.bitflyer()
bitflyer.apiKey = bitFlyer_apiKey
bitflyer.secret = bitFlyer_secret

orders = bitflyer.fetch_open_orders(
    symbol = "FX_BTC_JPY",
    params = {"product_code" : "FX_BTC_JPY"})

for order in orders:
    print(order["id"])
    bitflyer.cancel_order(
        symbol="FX_BTC_JPY",
        id = order["id"],
        params = {"product_code" : "FX_BTC_JPY"})

orders = bitflyer.fetch_open_orders(
    symbol="FX_BTC_JPY",
    params={"product_code": "FX_BTC_JPY"})

for order in orders:
    print(order['id'])