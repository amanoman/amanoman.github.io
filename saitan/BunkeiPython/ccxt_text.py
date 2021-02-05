import ccxt
from pprint import pprint
from PASSWORDS.password import *


bitflyer = ccxt.bitflyer()
bitflyer.apiKey = bitFlyer_apiKey  # apiKeyのKのみ大文字注意
bitflyer.secret = bitFlyer_secret


order = bitflyer.create_order(
    symbol = 'BTC/JPY',
    type='limit',
    side='buy',
    price='3100000',
    amount='0.01',
    params = {"product_code" : "FX_BTC_JPY"})

pprint(order)
