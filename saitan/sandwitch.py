sandwich_orders = ['トマトサンド','チキンサンド','たまごサンド','チーズサンド','ツナサンド','カルビサンド','`ポークサンド']
finished_sandwiches = []
polling_active = True

message = "\n メニューからサンドウィッチを注文してください："
print(sandwich_orders)
order = input(message)
while poling_active:
    while order in sandwich_orders:
    sandwich_orders.remove(order)
    print(f"ご注文は{order}ですね！")
    finished_sandwiches.append(order)
    print(f"おまたせしました{order}です！")
repeat = input("他に注文はございますか？(yes/no)")
if repeat == no:
    polling_active = False
    

