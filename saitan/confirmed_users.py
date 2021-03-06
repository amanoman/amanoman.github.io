unconfirmed_users = ['alice','brian','candace']
confirmed_users=[]

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"確認中のユーザー：{current_user}")
    confirmed_users.append(current_user)

print("\n以下のユーザーは確認済みです。")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())