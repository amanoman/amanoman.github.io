import ccxt
from pprint import pprint

bitflyer = ccxt.bitflyer()
bitflyer.apiKey = '' #apiKeyのKのみ大文字注意
bitflyer.secret = ''

order = bitflyer.create_order(
    symbol = 'BTC/JPY',
    type='limit',
    side='buy',
    price='3100000',
    amount='0.01',
    params = {"product_code" : "FX_BTC_JPY"})

pprint(order)