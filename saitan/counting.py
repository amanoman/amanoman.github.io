current_number = 0
while current_number < 10:
    #print(current_number)
    current_number +=1
    if current_number % 2 == 0:
        continue
    print(current_number)

prompt = "\n何か書いてください。繰り返してお返事します"
prompt += "\nプログラムを止めるには’終了’と入力してください"
message = ""
active = True
while active:
    message = input(prompt)

    if message == '終了':
        active = False
    else:
        print(message)

#while message != '終了':
#    message=input(prompt)
#    if message != '終了':
#       print(message)

prompt = "\n行ったことのある街を教えて下さい"
prompt += "\nプログラムを止めるには’終了’と入力してください"
while True:
    city = input(prompt)

    if city =='終了':
        break
    else:
        print(f"{city.title()}に行くのって最高です！")