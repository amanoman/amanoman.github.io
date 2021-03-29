import python_bitbankcc
from PASSWORDS.password import *
from datetime import datetime
import time

class BitBankPubAPI:

    def __init__(self):
        self.pub = python_bitbankcc.public()

    def get_ticker(self, pair):
        try:
            value = self.pub.get_ticker(pair)
            #data = value.json()
            return value
        except Exception as e:
            print(e)
            return None

class BitBankPrvAPI:

    def __init__(self):
        API_KEY = BITBANK_API_KEY
        API_SECRET = BITBANK_API_SECRET
        self.prv = python_bitbankcc.private(API_KEY, API_SECRET)

    def get_asset(self):
        try:
            value = self.prv.get_asset()
            return value
        except Exception as e:
            print(e)
            return None

   
    
    def main():
        pub_set = BitBankPubAPI()
        prv_set = BitBankPrvAPI()
        #dt_jst_aware = datetime.datetime.fromtimestamp(0,datetime.timezone(datetime.timedelta(hours=9)))
# #------------------------------------------------------#
pub_set = BitBankPubAPI()
prv_set = BitBankPrvAPI()
API_KEY = BITBANK_API_KEY
API_SECRET = BITBANK_API_SECRET
pub = python_bitbankcc.public()
prv = python_bitbankcc.private(API_KEY,API_SECRET)

tickers = pub.get_ticker('xrp_jpy')
for ticker,value in tickers.items():
    print(f"【{ticker}】:{value}")
assets = prv_set.get_asset()
asset_xrp = assets['assets'][3]
for asset,value in asset_xrp.items():
    print(f"【{asset}】:{value}")