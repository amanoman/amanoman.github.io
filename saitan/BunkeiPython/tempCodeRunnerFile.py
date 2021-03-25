n = int(input())
lists = []
count = 1
while count <= n:
    marks,nums = map(str,input().split())
    if marks =="S":
        int(nums)
        lists.append(nums)
    elif marks == "H":
        nums = int(nums) + 13
        lists.append(nums)
    elif marks == "C":
        nums = int(nums) + 26
        lists.append(nums)
    elif marks == "D":
        nums = int(nums) + 39
        lists.append(nums)

    count +=1
for i in range(1,53):
    if not i in lists:
        if i <= 13:
            print(f"S{i} ")
        if 13 < i <= 26:
            print(f"H{i-13} ")
        if 27 < i <= 39:
            print(f"C{i-26} ")
        if 40 < i <= 53:
            print(f"D{i-39} ")