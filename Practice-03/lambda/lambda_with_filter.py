numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# 5 examples
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

greater_than_4 = list(filter(lambda x: x > 4, numbers))
print(greater_than_4)

less_than_5 = list(filter(lambda x: x < 5, numbers))
print(less_than_5)

divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(divisible_by_3)