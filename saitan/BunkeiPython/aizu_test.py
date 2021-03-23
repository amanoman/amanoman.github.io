n = int(input())
for i in range(3,n+1):
    j = i
    count=0
    if i % 3 == 0:
        print(" ",i,end="")
    elif i % 10 == 3:
        print(" ",i,end="")
    else:    
        while j > 0 and count <1: #331
            j //= 10
            if j % 10 == 3:
                print(" ",i,end="")
                count +=1