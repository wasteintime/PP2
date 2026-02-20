# Add 10 to argument a
x = lambda a: a + 10

# 5 examples
print(x(5))
print(x(10))
print(x(0))
print(x(-5))
print(x(100))

# Multiply a and b
x = lambda a, b: a * b

# 5 examples
print(x(5, 6))
print(x(2, 3))
print(x(10, 10))
print(x(-2, 4))
print(x(0, 100))

# Sum a, b, c
x = lambda a, b, c: a + b + c

# 5 examples
print(x(5, 6, 2))
print(x(1, 2, 3))
print(x(10, 20, 30))
print(x(0, 0, 0))
print(x(-1, 5, 2))

# Function that returns a lambda
def myfunc(n):
    return lambda a: a * n

# 5 examples
mydoubler = myfunc(2)
mytripler = myfunc(3)
myquadrupler = myfunc(4)

print(mydoubler(11))
print(mytripler(11))
print(myquadrupler(5))
print(mydoubler(7))
print(mytripler(2))

words = ["apple", "pie", "banana", "cherry"]

# 5 examples
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

# Reverse length
sorted_words_rev = sorted(words, key=lambda x: len(x), reverse=True)
print(sorted_words_rev)

# Alphabetical
sorted_alpha = sorted(words, key=lambda x: x)
print(sorted_alpha)

# Last letter
sorted_last = sorted(words, key=lambda x: x[-1])
print(sorted_last)

# Uppercase first
sorted_upper = sorted(words, key=lambda x: x.upper())
print(sorted_upper)