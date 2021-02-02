print("元のリストを表示")
worlds = ["nazca","MachuPicchu","pyramid","GrandCanyon","Mt.Fuji"]
print(worlds)
print("\n")

print("sorted関数で昇順")
print(sorted(worlds))
print(worlds)
print("\n")

print("sorted関数で降順")
print(sorted(worlds,reverse=True))
print(worlds)
print("\n")

print("reverseメソッドで逆順")
worlds.reverse()
print(worlds)
print("\n")

print("reverseメソッドで正順")
worlds.reverse()
print(worlds)
print("\n")

print("sortメソッドで昇順")
worlds.sort()
print(worlds)
print("\n")

print("sortメソッドで降順")
worlds.sort(reverse=True)
print(worlds)
print("\n")

length = len(worlds)

print(f"リストの長さは{length}です")

