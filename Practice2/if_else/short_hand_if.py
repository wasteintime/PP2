# Пример 1
a = 5
b = 2
if a > b: print("a is greater than b")

# Пример 2
x = 10
y = 15
if x < y: print("x is less than y")

# Пример 3
num = 7
if num % 2 == 0: print("Even number")

# Пример 4
score = 90
if score >= 50: print("Passed")

# Пример 5
temperature = 30
if temperature > 25: print("It's hot today")


# Пример 1
a = 2
b = 330
print("A") if a > b else print("B")

# Пример 2
x = 10
y = 5
print("x is bigger") if x > y else print("y is bigger")

# Пример 3
num = 8
print("Even") if num % 2 == 0 else print("Odd")

# Пример 4
score = 45
print("Passed") if score >= 50 else print("Failed")

# Пример 5
temperature = 18
print("Warm") if temperature > 20 else print("Cool")


# Пример 1
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

# Пример 2
x = 15
y = 7
max_value = x if x > y else y
print("Maximum value:", max_value)

# Пример 3
score = 85
result = "Pass" if score >= 50 else "Fail"
print(result)

# Пример 4
num = 9
parity = "Even" if num % 2 == 0 else "Odd"
print(parity)

# Пример 5
temperature = 22
weather = "Hot" if temperature > 30 else "Warm"
print(weather)


# Пример 1
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Пример 2
x = 5
y = 10
print("x > y") if x > y else print("=") if x == y else print("y > x")

# Пример 3
score = 75
print("Excellent") if score >= 90 else print("Good") if score >= 50 else print("Fail")

# Пример 4
temperature = 15
print("Hot") if temperature > 30 else print("Warm") if temperature > 20 else print("Cold")

# Пример 5
num = -5
print("Positive") if num > 0 else print("Zero") if num == 0 else print("Negative")


# Пример 1 — Finding max
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

# Пример 2 — Default username
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

# Пример 3 — Pass or fail
score = 40
result = "Pass" if score >= 50 else "Fail"
print(result)

# Пример 4 — Even or odd
num = 11
parity = "Even" if num % 2 == 0 else "Odd"
print(parity)

# Пример 5 — Temperature category
temperature = 28
category = "Hot" if temperature > 30 else "Warm"
print(category)


