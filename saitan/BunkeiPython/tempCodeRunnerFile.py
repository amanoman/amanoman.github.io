lists = list(map(int,input().split()))

for list in reversed(lists):
    print(list,end="")
    count+=1
    if count != n:
        print(" ",end="")