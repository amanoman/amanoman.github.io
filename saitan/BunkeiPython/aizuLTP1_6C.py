n = int(input())
count =1
rooms = [[[0 for bil in range(10)] for floor in range(3)]for room in range(4)]
for items in rooms:
    for item in items:
        for i in item:
            count=1
            if count != 10:
                print(i,end="")
            elif count == 10:
                print("####")
        count+=1
            
        
for i in range(n):
    b, f, r, v = map(int, input().split())
    rooms =[[[v for room in range(r)] for floor in range(f)]for bil in range(b)]
    #for r in rooms:
        #if count == 3:
           # print(####)


"""
dict_A ={}

billdings =[floor]
floors = [rooms]
rooms =[]
volumes =[]
"""


#4 * 10 * 3
#1 1 3 10
#int(b,f,r,v)

#year = [[[0 for i in range(7)] for j in range(5)] for k in range(12)]   
# 3次元配列の初期化