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
#------------------------------------------------------#
last_time = 0
pub_set = BitBankPubAPI()
prv_set = BitBankPrvAPI()
API_KEY = BITBANK_API_KEY
API_SECRET = BITBANK_API_SECRET
prv = python_bitbankcc.private(API_KEY,API_SECRET)

ticker = pub_set.get_ticker('xrp_jpy')
assets = prv_set.get_asset()
asset_jpy = assets['assets'][0]
asset_btc = assets['assets'][1]
asset_ltc = assets['assets'][2]
asset_xrp = assets['assets'][3]
asset_eth = assets['assets'][4]
asset_mona = assets['assets'][5]

now = time.time()

lot = 100/float(ticker['buy'])
print(f"-----約定履歴-----")


trades = prv.get_trade_history('xrp_jpy',"30")
last_price = 200
for trade in trades['trades'] :
   print('取引ID: ' + str(trade['trade_id']))
   print('通貨ペア: ' + trade['pair'])
   print('注文ID: ' + str(trade['order_id']))
   print('売買: ' + trade['side'])
   print('注文タイプ: ' + trade['type']) # 指値 or 成行
   print('注文量: ' + trade['amount'])
   amount = trade['amount']
   print('価格: ' + trade['price'])
   price = trade['price']
   print('Maker/Taker: ' + trade['maker_taker'])
   print('ベース手数料: ' + trade['fee_amount_base'])
   print('クォート手数料: ' + trade['fee_amount_quote'])
   print('約定日時: ' + str(datetime.fromtimestamp(trade['executed_at']/1000.0)))
   print(f"前回価格:{float(amount) * float(price)}")
   print(f"現在価格:{float(amount) * float(last_price)}")
   print('---------------------------------')


if ticker["last"] > last_price * 1.20:
    print(f"-----{lot}XRP分売り注文-----")
    o_pair = "xrp_jpy"
    o_price ="ticker['sell']"
    o_amount =lot
    o_side ='sell'
    o_type = "market"
    order = prv.order(o_pair,o_price,o_amount,o_side,o_type)
    #注文情報の表示
    print('注文ID: ' + str(order['order_id']))
    print('通貨ペア: ' + order['pair'])
    print('売買: ' + order['side'])
    print('注文タイプ: ' + order['type'])
    print('注文数量: ' + order['start_amount'])
    print('未約定数量: ' + order['remaining_amount'])
    print('約定数量: ' + order['executed_amount'])

    if order['type'] == 'limit' :
        print('注文価格: ' + order['price'])
    if order['type'] == 'market' :
        print('平均約定価格: ' + order['average_price'])

    print('注文日時: ' + str(datetime.fromtimestamp(order['ordered_at']/1000.0)))
    print('ステータス: ' + order['status'])
    print("#"*30)

last_time = now

#asset_dict = prv_set.get_asset()
##print(asset_dict['assets'])

time.sleep(30)
if __name__ == '__main__':
    main()
