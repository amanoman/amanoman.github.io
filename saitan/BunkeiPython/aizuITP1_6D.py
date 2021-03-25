n,m = map(int,input().split())
A_lists=[]
b_lists=[]
for i in range(n):
    A_lists[i-1] = list(map(int,input().split())
    #A_lists.append(A)
#print(A_lists)
for j in range(m):
    b = int(input())
    b_lists.append(b)
print(b_lists)
c = 0
for k in range(m):
    C += A_lists[k] * b_lists[k]
    print(C)
#table [[for i in range()]]
