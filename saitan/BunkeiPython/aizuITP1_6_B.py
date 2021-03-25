n = int(input())
lists = []
count = 1
while count <= n:
    marks,nums = map(str,input().split())
    if marks =="S":
        nums = int(nums)
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
    count += 1

for i in range(1,53):
    if not i in lists:
        if i <= 13:
            print(f"S {i}")
        if 13 < i <= 26:
            print(f"H {i-13}")
        if 26 < i <= 39:
            print(f"C {i-26}")
        if 39 < i <= 53:
            print(f"D {i-39}")


# rank   1  2  3  4  5  6  7  8  9 10 11 12 13̃̃̃̃̃
#---------------------------------------------
# S:     1  2  3  4  5  6  7  8  9 10 11 12 13
# H:    14 15 16 17 18 19 20 21 22 23 24 25 26
# C:    27 28 29 30 31 32 33 34 35 36 37 38 39
# D:    40 41 42 43 44 45 46 47 48 49 50 51 52

#for i in range(1,53):
#   if not (i in cards):
#        # cards にiが存在しない場合の処理
