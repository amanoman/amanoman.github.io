guests = ["じいちゃん","薗じい","薗ばあ"]

message1 = f"{guests[0]}お久しぶり！夕食を一緒に食べに来てください！"
message2 = f"{guests[1]}お久しぶり！夕食を一緒に食べに来てください！"
message3 = f"{guests[2]}お久しぶり！夕食を一緒に食べに来てください！"

get_table ="大きなテーブルを見つけたので、もっとたくさんゲストを招待しましょう！"


print(message1)
print(message2)
print(message3)


print(get_table)

guests.insert(0,"ベル")
guests.insert(2,"ミー")
guests.append("ベリー")

print(guests)

message1 = f"{guests[0]}お久しぶり！夕食を一緒に食べに来てください！"
message2 = f"{guests[1]}お久しぶり！夕食を一緒に食べに来てください！"
message3 = f"{guests[2]}お久しぶり！夕食を一緒に食べに来てください！"
message4 = f"{guests[3]}お久しぶり！夕食を一緒に食べに来てください！"
message5 = f"{guests[4]}お久しぶり！夕食を一緒に食べに来てください！"
message6 = f"{guests[5]}お久しぶり！夕食を一緒に食べに来てください！"

print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)

print("残念ながら大きなテーブルが夕食に間に合いませんでした・・・")

sorry_message =f"{guests.pop()}ごめんなさい、また今度夕食にきてください！" 
print(sorry_message)
sorry_message =f"{guests.pop()}ごめんなさい、また今度夕食にきてください！" 
print(sorry_message)
sorry_message =f"{guests.pop()}ごめんなさい、また今度夕食にきてください！" 
print(sorry_message)
sorry_message =f"{guests.pop()}ごめんなさい、また今度夕食にきてください！" 
print(sorry_message)

print(f"{guests[0]}予定どおり夕食に来てください！")
print(f"{guests[1]}予定どおり夕食に来てください！")

del guests[1]
del guests[0]

print(guests)