n = int(input())
lists = list(map(int,input().split()))

for i in range(1,n+1):
    print(lists[n-i],end="")
    if i != n:
        print(" ",end ="")
    else:
        print()

"""
for list in reversed(lists):
    print(list,end="")
    count+=1
    if count != n:
        print(" ",end="")
"""

