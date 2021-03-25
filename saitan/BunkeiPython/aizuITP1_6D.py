n,m = map(int,input().split())
A_lists=[[]for i in range(n)]
for i in range(n):
    A_lists[i]=list(map(int,input().split()))

b_lists=[[0]*1 for i in range(m)]
for i in range(m):
    b_lists[i] = int(input())
print(A_lists)
print(b_lists)
for row in range(n):
    tmp = 0
    for col in range(m):
        tmp += A_lists[row][col]*b_lists[col]
    print("%D"%(tmp))