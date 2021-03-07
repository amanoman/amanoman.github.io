favalite_places = {}

polling_active = True
while polling_active:
    print("世界中どこでも好きなところに行けるとしたらどこに行きたいですか？")
    name = input("\n名前を教えてください：")
    answer = input(f"{name}さんの行きたいところを教えてください：")
    favalite_places[name]=answer

    end_switch = input("質問を繰り返しますか？(yes/no)")
    if end_switch == 'no':
        polling_active = False
print(f"======投票の結果======")
for key,value in favalite_places.items():
    print(f"{key}さんは{value}に行きたいそうです。")
    