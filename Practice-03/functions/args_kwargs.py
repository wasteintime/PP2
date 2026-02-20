def my_function(*kids):
    print("The youngest child is", kids[2])

# 5 examples
my_function("Emil", "Tobias", "Linus")
my_function("Alice", "Bob", "Charlie")
my_function("Anna", "Elsa", "Olaf")
my_function("John", "Paul", "George")
my_function("Tom", "Jerry", "Spike")

def my_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

# 5 examples
my_function("Emil", "Tobias", "Linus")
my_function(1, 2, 3)
my_function("Apple", "Banana", "Cherry")
my_function("Dog", "Cat", "Mouse")
my_function(10, 20, 30)


def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

# 5 examples
my_function("Hello", "Emil", "Tobias", "Linus")
my_function("Hi", "Alice", "Bob")
my_function("Welcome", "Anna", "Elsa")
my_function("Hey", "John", "Paul")
my_function("Greetings", "Tom", "Jerry")

def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# 5 examples
print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))
print(my_function(2, 4, 6, 8, 10))
print(my_function(7, 3, 5))

def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# 5 examples
print(my_function(3, 7, 2, 9, 1))
print(my_function(10, 5, 8))
print(my_function(100, 200, 50))
print(my_function(1, 1, 1, 1))
print(my_function(0, -5, -2))


def my_function(**kid):
    print("His last name is", kid["lname"])

# 5 examples
my_function(fname="Tobias", lname="Refsnes")
my_function(fname="Alice", lname="Smith")
my_function(fname="John", lname="Doe")
my_function(fname="Anna", lname="Brown")
my_function(fname="Tom", lname="Jones")

def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

# 5 examples
my_function(name="Tobias", age=30, city="Bergen")
my_function(name="Alice", age=25, city="Oslo")
my_function(name="John", age=40, city="New York")
my_function(name="Anna", age=28, city="London")
my_function(name="Tom", age=35, city="Paris")

def my_function(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

# 5 examples
my_function("emil123", age=25, city="Oslo", hobby="coding")
my_function("alice456", age=22, city="Berlin", hobby="painting")
my_function("john789", age=30, city="London", hobby="reading")
my_function("anna321", age=28, city="Paris", hobby="traveling")
my_function("tom654", age=35, city="Rome", hobby="swimming")

def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# 5 examples
my_function("User Info", "Emil", "Tobias", age=25, city="Oslo")
my_function("Team Members", "Alice", "Bob", role="Leader", city="Berlin")
my_function("Students", "John", "Anna", grade=10, school="High School")
my_function("Pets", "Tom", "Jerry", type="Cat", color="White")
my_function("Players", "Messi", "Ronaldo", team="PSG", age=36)

# Using * to unpack a list
def my_function(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(my_function(*numbers))

# Using ** to unpack a dictionary
def my_function(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)

