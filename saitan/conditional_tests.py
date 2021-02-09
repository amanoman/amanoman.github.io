name_1 = 'david'
print("文字の一致と不一致のテスト")
print(name_1 == 'david')
print(name_1 == 'caroline')

name_2 = 'Bob'
print('lower()メソッド使用')
print(name_2.lower()=='bob')

num_1 = 20
num_2 = 11
print('数値の一致不一致とandとor')
print(num_1 >= 20 and num_2 < 20)
print(num_1 < 20 or num_2 <= 10)

lists = ['david','caroline','tom']
print('要素がリストに存在するかしないか')
print('Tom'.lower() in lists)
print('James'.lower() in lists)
print('James'.lower() not in lists)

