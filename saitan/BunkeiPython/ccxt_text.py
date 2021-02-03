import ccxt
from pprint import pprint

bitflyer = ccxt.bitflyer()
ticker = bitflyer.fetch_ticker('BTC/JPY', params = {"product_code" : "FX_BTC_JPY"})
pprint(ticker)


pprint("-" *100)

bitflyer.apikey = 'QaQKsPrCRd2PQUnSkMeSeg'
bitflyer.secret = 'TtDihu2tSEfvf5o9SJ12k/CIliylx7+vTmaqS2Ec7rI='

collateral = bitflyer.private_get_getcollateral()
pprint(collateral)
