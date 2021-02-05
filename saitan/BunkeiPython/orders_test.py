
import ccxt
from pprint import pprint
from PASSWORDS.password import *

bitflyer = ccxt.bitflyer()
bitflyer.apiKey = bitFlyer_apiKey  # apiKeyのKのみ大文字注意
bitflyer.secret = bitFlyer_secret


#orders = bitflyer.fetch_open_orders(
#	symbol = "BTC/JPY",
#	params = {"product_code" : "FX_BTC_JPY"})
orders = bitflyer.fetch_open_orders(
	symbol= "FX_BTC_JPY", #シンボル表示がBTC/JPYではうまくいかない
	params= {"product_code" : "FX_BTC_JPY"})

pprint(orders)
