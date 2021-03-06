<<<<<<< HEAD
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

language = favorite_languages.get('bob','データがありません')
print(f"Sarahが好きなプログラミング言語は{language}です")


vote_list = ['jen','sarah','edward']

for name in favorirte_languages.keys():
    print(name)
    if name in vote_list:
      print(f"{name.title()}さん投票ありがとう！")
    #else:
        #print("投票しろ！")
=======
    city = input(prompt)

    if city =='終了':
        break
    else:
        print(f"{city.title()}に行くのって最高です！")
>>>>>>> 26089ea2cd58cbb66f71b6e60f445223aff1726f
