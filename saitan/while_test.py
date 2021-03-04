active = True
while active:
    prompt = "年齢によりチケットの料金が違います"
    prompt += "年齢を教えて下さい"
    age = input(prompt)
    age = int(age)
    if age < 3:
        print(f"{age}歳は３歳未満なので無料です")
    elif age >=3 and age <= 12:
        print(f"{age}歳なので1000円です")
    elif age >= 100:
        break
    else:
        print(f"{age}歳は1500円です")