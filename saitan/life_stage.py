age = 65
type = ['赤ちゃん','幼児','子ども','ティーンエイジャー','大人','高齢者']

if age < 2:
    age_range = 0
    print(f"あなたは{type[age_range]}です！")
elif age >= 2 and age < 4:
    age_range = 1
    print(f"あなたは{type[age_range]}です！")
elif age >= 4 and age < 13:
    age_range = 2
    print(f"あなたは{type[age_range]}です！")
elif age >= 13 and age < 20:
    age_range = 3
    print(f"あなたは{type[age_range]}です！")
elif age >= 20 and age < 65:
    age_range = 4
    print(f"あなたは{type[age_range]}です！")
else:
    age_range = 5
    print(f"あなたは{type[age_range]}です！")