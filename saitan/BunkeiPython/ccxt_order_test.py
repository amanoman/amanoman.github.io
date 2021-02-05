import ccxt
from pprint import pprint
from PASSWORDS.password import *

bitflyer = ccxt.bitflyer()
bitflyer.apiKey = bitFlyer_apiKey
bitflyer.secret = bitFlyer_secret

orders = bitflyer.create_order(
    symbol = "BTC/JPY",
    type='limit',
    side='buy',
    price='3050000',
    amount='0.01',
    params = {"product_code" : "FX_BTC_JPY"})

#print(orders)

orders = bitflyer.fetch_open_orders(
    symbol="FX_BTC_JPY",
    params={"product_code" : "FX_BTC_JPY"})

for order in orders:
    print(order['id'])
