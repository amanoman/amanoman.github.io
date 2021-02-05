
import ccxt
from pprint import pprint

bitflyer = ccxt.bitflyer()
bitflyer.apiKey = '' #apiKeyのKのみ大文字注意
bitflyer.secret = ''


orders = bitflyer.fetch_open_orders(
#orders = bitflyer.fetchOrders(
	symbol = "BTC/JPY",
	params = {"product_code" : "FX_BTC_JPY"})
pprint( orders )