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