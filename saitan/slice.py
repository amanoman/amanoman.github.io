pizzas = ["チーズピザ","グリルチキンピザ","ペパロニピザ","トマトピザ","カルビピザ"]
for pizza in pizzas:
    print(f"私は{pizza}が好きです！")
print("昔からピザが大好き！")
print("嫌いなピザはありません！")
print("私はピザが大好きです！")

my_pizzas = pizzas[:] #[:]を使わずにmy_pizzas=pizzasとしてしまうとmy_pizzasとpizzasが同じリストとして扱われる。片方にappendしたつもりが両方にappendされる。
friend_pizzas = pizzas[:]


print("-"*50)
print("リストの最初の３つの要素です")
print(my_pizzas[:3])

print("リストの中央の３つの要素を出力します")
print(my_pizzas[1:4])

print("リストの最後の３つの要素です")
print(my_pizzas[-3:])
print("-"*50)

my_pizzas.append("ハバネロピザ")
friend_pizzas.append("ポテトピザ")

print(f"私の好きなピザ")
for my_pizza in my_pizzas:
    print(my_pizza)

print(f"友達が好きなピザ")
for friend_pizza in friend_pizzas:
    print(friend_pizza)