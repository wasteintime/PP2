fruits = ["apple", "banana", "cherry"]
for f in fruits:
    if f == "banana":
        break
    print(f)


nums = [1, 3, 6, 2]
for n in nums:
    if n > 5:
        break
    print(n)


for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(i, j)


words = ["go", "wait", "stop", "run"]
for w in words:
    if w == "stop":
        break
    print(w)


nums = [2, 4, -1, 5]
for n in nums:
    if n < 0:
        break
    print(n)
