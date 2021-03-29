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

    def bitbank_market(side,lot)
        o_pair = "xrp_jpy"
        o_price =""
        o_amount =lot
        o_side =side
        o_type = "marker"
        while True:
            try:
                order = prv.order(o_pair,o_price,o_amount,o_side,o_type)

def main():
    pub_set = BitBankPubAPI()
    prv_set = BitBankPrvAPI()
    #dt_jst_aware = datetime.datetime.fromtimestamp(0,datetime.timezone(datetime.timedelta(hours=9)))
#------------------------------------------------------#
last_time = 0
pub_set = BitBankPubAPI()
prv_set = BitBankPrvAPI()   
while True:
    ticker = pub_set.get_ticker('xrp_jpy')
    assets = prv_set.get_asset()
    asset_jpy = assets['assets'][0]
    asset_btc = assets['assets'][1]
    asset_ltc = assets['assets'][2]
    asset_xrp = assets['assets'][3]
    asset_eth = assets['assets'][4]
    asset_mona = assets['assets'][5]
    
    now = time.time()

    if now > last_time: 
        print("#"*30)
        print(f"現在時刻:{datetime.fromtimestamp(now).strftime('%Y/%m/%d %H:%M')}")
        print(f"B i d :{ticker['sell']}")
        print(f"A s k :{ticker['buy']}")
        print(f"最高値:{ticker['high']}")
        print(f"最安値:{ticker['low']}")
        print(f"現在値:{ticker['last']}")
        print(f"Volume:{ticker['vol']}")
        print("-"*30)
        print('通貨: ' + asset_jpy['asset'])
        print('利用可能な数量: ' + asset_jpy['free_amount'])
        print('保有量: ' + asset_jpy['onhand_amount'])
        print('ロックされている数量: ' + asset_jpy['locked_amount'])
        #print('手数料: ' + asset_jpy['withdrawal_fee'])
        print("-"*30)
        print('通貨: ' + asset_xrp['asset'])
        print('利用可能な数量: ' + asset_xrp['free_amount'])
        print('保有量: ' + asset_xrp['onhand_amount'])
        print('ロックされている数量: ' + asset_xrp['locked_amount'])
        print('手数料: ' + asset_xrp['withdrawal_fee'])
        print("-"*30)
        
        o_pair = "xrp_jpy"
        o_price =""
        o_amount =lot
        o_side =side
        o_type = "marker"
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
