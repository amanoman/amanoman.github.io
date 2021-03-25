BIG_NUM = 20000000000

table=[[[0]*10 for i in range(0,3)]for k in range(0,4)]

N =int(input())

for loop in range(N):
    house_id,floor,room,add = map(int,input().split())
    table[house_id-1][floor-1][room-1]+=add

x =0

for i in range(4):
    if x !=0:
        print("#"*20)
    x += 1

    for a in range(3):
        for b in range(10):
            print(f" {table[i][a][b]}",end="")
        print()