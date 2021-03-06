responses = {}

polling_active = True

while polling_active:
    name = input("\nあなたのお名前は？")
    response = input("いつか登りたい山は何ですか")

    responses[name] = response

    repeat = input("誰か他に回答してくれる人はいますか？(yes/no)")
    if repeat == 'no':
        polling_active = False
        print("\n---投票結果--")
        for name,response in responses.items():
            print(f"{name}さんが登りたいのは{response}です。")
