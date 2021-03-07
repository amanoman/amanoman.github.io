sandwich_orders = ['トマトサンド','チキンサンド','パストラミサンド','たまごサンド','チーズサンド','パストラミサンド','ツナサンド','パストラミサンド','カルビサンド','ポークサンド']
finished_sandwiches = []

print('パストラミサンドは品切れです')
remove_sandwich = 'パストラミサンド'
while remove_sandwich in sandwich_orders:
    sandwich_orders.remove(remove_sandwich)
while sandwich_orders:
    
    current_order = sandwich_orders.pop()
    print(f"{current_order}ができました")
    finished_sandwiches.append(current_order)

print(f"できあがったサンドイッチ一覧です")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

finished_sandwiches.append(remove_sandwich)
print(finished_sandwiches)
if remove_sandwich in finished_sandwiches:
    print('パストラミサンドが残っています')

