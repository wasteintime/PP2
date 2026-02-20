# Double all numbers in a list
numbers = [1, 2, 3, 4, 5]

# 5 examples
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

tripled = list(map(lambda x: x * 3, numbers))
print(tripled)

squared = list(map(lambda x: x ** 2, numbers))
print(squared)

halved = list(map(lambda x: x / 2, numbers))
print(halved)

negated = list(map(lambda x: -x, numbers))
print(negated)


