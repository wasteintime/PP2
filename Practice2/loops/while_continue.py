i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1


i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1


nums = [2, -3, 5, -1, 4]
i = 0
while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i])
    i += 1


while True:
    text = input("Enter text: ")
    if text == "":
        continue
    print("You entered:", text)
    if text == "stop":
        break


i = 1
while i <= 20:
    if i % 5 == 0:
        i += 1
        continue
    print(i)
    i += 1


