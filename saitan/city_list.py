lists = {
    'first_name':'amano',
    'last_name':'takayuki',
    'age':39,
    'city':'hisai',
}

print(lists.get('name','登録されていません'))

favalite_numbers = {
    'ukita':3,
    'amano':8,
    'taniguchi':1,
    'miura':3,
    'ono':10,
}

print(favalite_numbers['amano'])

for key,value in favalite_numbers.items():
    print(key)
    print(value)

print('-' *10)

for name in favalite_numbers.keys():
    print(name.title())

for num in favalite_numbers.values():
    print(num)

print("*"*100)
livers={'amazon':'south_america','nile':'africa','micicipi':'north_america'}
for key,value in livers.items():
    print(f"{key.title()}川は{value.title()}を流れている")

for liver in livers.keys():
    print(liver.title())

for place in livers.values():
    print(place.title())
