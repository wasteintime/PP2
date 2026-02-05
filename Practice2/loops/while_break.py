i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1


nums = [2, 5, 11, 7]
i = 0
while i < len(nums):
    if nums[i] > 10:
        print("Found:", nums[i])
        break
    i += 1


while True:
    text = input("Type something: ")
    if text == "stop":
        break
    print("You typed:", text)


i = 1
while i <= 5:
    if i == 4:
        break
    print(i)
    i += 1


i = 1
while i <= 10:
    if i % 7 == 0:
        print("Divisible by 7:", i)
        break
    i += 1


