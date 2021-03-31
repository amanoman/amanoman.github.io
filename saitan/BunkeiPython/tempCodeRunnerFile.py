for num in lists:
    if num % 2 == 0:
        lists = [x//2 for x in lists]
        count += 1
        
    else:
        
print(lists)
print(count)
    