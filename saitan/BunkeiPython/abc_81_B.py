N = int(input())
lists = list(map(int,input().split()))
count = 0
while True:
    for num in lists:
        if num % 2 == 0:
            lists = [x/2 for x in lists]
        else:
            break
    count += 1
        

        
print(lists)
print(count)
    
            

    
