# Sort list of tuples by second element
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]

# 5 examples
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

# Sort by name
sorted_by_name = sorted(students, key=lambda x: x[0])
print(sorted_by_name)

# Sort descending by age
sorted_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_desc)

# Sort by length of name
sorted_by_len = sorted(students, key=lambda x: len(x[0]))
print(sorted_by_len)

# Sort by modulo age 5
sorted_mod5 = sorted(students, key=lambda x: x[1] % 5)
print(sorted_mod5)