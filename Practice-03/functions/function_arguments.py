def my_function(fname):
    print(fname + " Smith")

my_function("John")
my_function("Anna")
my_function("Mike")

def greet(name):
    print("Hello, " + name)

greet("Ali")
greet("Dana")
greet("Arman")

def student(name):
    print(name + " is a student")

student("Aruzhan")
student("Nurlan")
student("Dias")

def age_info(name):
    print(name + " is 18 years old")

age_info("Zhanibek")
age_info("Aigerim")
age_info("Ruslan")

def city(name):
    print(name + " lives in Almaty")

city("Asel")
city("Timur")
city("Madina")

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("John", "Smith")
my_function("Anna", "Brown")

def greet(fname, lname):
    print("Hello, " + fname + " " + lname)

greet("Ali", "Khan")
greet("Dana", "Sadykova")

def student(fname, lname):
    print(fname + " " + lname + " is a student")

student("Aruzhan", "Nurmukhambet")
student("Dias", "Kenzhebek")

def age_info(fname, lname):
    print(fname + " " + lname + " is 18 years old")

age_info("Zhanibek", "Zhuma")
age_info("Aigerim", "Tursyn")

def city(fname, lname):
    print(fname + " " + lname + " lives in Almaty")

city("Asel", "Karimova")
city("Timur", "Bekov")

def greet(name="guest"):
    print("Hi", name)

greet("Ali")
greet("Dana")
greet()
greet("Arman")

def goodbye(name="everyone"):
    print("Goodbye", name)

goodbye("Aruzhan")
goodbye("Dias")
goodbye()
goodbye("Nurlan")

def city(name="visitor"):
    print(name, "welcome to Almaty")

city("Timur")
city("Asel")
city()
city("Madina")

def age(name="student"):
    print(name, "is 18 years old")

age("Zhanibek")
age("Aigerim")
age()
age("Ruslan")

def study(name="learner"):
    print(name, "is studying Python")

study("Ali")
study("Dana")
study()
study("Arman")

# 1
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function(animal="cat", name="Milo")
my_function("cat", "Milo")



# 2
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function(animal="parrot", name="Rio")
my_function("parrot", "Rio")



# 3
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function(animal="hamster", name="Nibbles")
my_function("hamster", "Nibbles")



# 4
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function(animal="rabbit", name="Snowy")
my_function("rabbit", "Snowy")



# 5
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function(animal="turtle", name="Shelly")
my_function("turtle", "Shelly")

def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

# 5 examples
my_function("dog", name="Buddy", age=5)
my_function("cat", name="Milo", age=3)
my_function("parrot", name="Rio", age=2)
my_function("hamster", name="Nibbles", age=1)
my_function("rabbit", name="Snowy", age=4)


def my_function(fruits):
    for fruit in fruits:
        print(fruit)

# 5 examples
my_fruits1 = ["apple", "banana", "cherry"]
my_fruits2 = ["orange", "kiwi", "melon"]
my_fruits3 = ["grape", "pear", "plum"]
my_fruits4 = ["mango", "pineapple", "papaya"]
my_fruits5 = ["strawberry", "blueberry", "raspberry"]

my_function(my_fruits1)
my_function(my_fruits2)
my_function(my_fruits3)
my_function(my_fruits4)
my_function(my_fruits5)


def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

# 5 examples
person1 = {"name": "Emil", "age": 25}
person2 = {"name": "Anna", "age": 30}
person3 = {"name": "John", "age": 22}
person4 = {"name": "Maria", "age": 28}
person5 = {"name": "Ali", "age": 35}

my_function(person1)
my_function(person2)
my_function(person3)
my_function(person4)
my_function(person5)

def my_function(x, y):
    return x + y

# 5 examples
print(my_function(5, 3))
print(my_function(10, 7))
print(my_function(2, 8))
print(my_function(15, 5))
print(my_function(1, 9))

def my_function():
    return ["apple", "banana", "cherry"]

# 5 examples
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])
# Repeat with other calls for practice
fruits2 = my_function()
print(fruits2)
fruits3 = my_function()
print(fruits3)

def my_function():
    return (10, 20)


x, y = my_function()
print("x:", x, "y:", y)


def my_function(name, /):
    print("Hello", name)


my_function("Emil")
my_function("Anna")
my_function("John")
my_function("Maria")
my_function("Ali")

def my_function(*, name):
    print("Hello", name)


my_function(name="Emil")
my_function(name="Anna")
my_function(name="John")
my_function(name="Maria")
my_function(name="Ali")


def my_function(a, b, /, *, c, d):
    return a + b + c + d

print(my_function(5, 10, c=15, d=20))
print(my_function(1, 2, c=3, d=4))
print(my_function(7, 8, c=9, d=10))
print(my_function(0, 5, c=10, d=15))
print(my_function(2, 3, c=4, d=5))

