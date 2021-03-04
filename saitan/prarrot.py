prompt = "あなたが誰か教えてくれたら、あなた向けのあいさつをします"
prompt += "\nあなたのお名前は？"

name = input(prompt)
print(f"\nこんにちは、{name}!")

prompt ="\n何歳ですか？"
age = input(prompt)
age = int(age)
print(f"\n{age}歳なんですね！")

prompt = "身長は何センチ？"
height = input(prompt)
height = int(height)
if height >= 170:
    print(f"おっきいですね！")
else:
    print("なるほどですね！")


