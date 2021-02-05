import ccxt
from pprint import pprint
from PASSWORDS.password import *

bitflyer = ccxt.bitflyer()
bitflyer.apiKey = bitFlyer_apiKey
bitflyer.secret = bitFlyer_secret

collateral = bitflyer.private_get_getcollateral()
pprint(collateral)