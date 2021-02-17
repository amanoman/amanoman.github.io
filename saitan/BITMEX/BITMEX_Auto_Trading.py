from bitmex import bitmex
from PASSWORDS.password import *

USE_TESTNET = True

api_key = bitmex_apikey
api_secret = bitmex_secret

if USE_TESTNET:
    api_key = bitmex_test_apikey
    api_secret = bitmex_test_secret
    
bitmex_client = bitmex(test=False,api_key=api_key,api_secret=api_secret)

#orderbook, res = bitmex_client.OrderBook.OrderBook_getL2(symbol='XBTUSD',depth=20).result()
#print(orderbook)

#margin, res = bitmex_client.User.User_getMargin().result()
#print(margin)
def order_market(symbol,size,**options):
    try:
        order, res = bitmex_client.Order.Order_new(symbol=symbol,orderQty=size,ordType='Market',**options).result()
        return order
    except Exception as e:
        print(e)
        return None

order = order_market('XBTUSD', 20)
