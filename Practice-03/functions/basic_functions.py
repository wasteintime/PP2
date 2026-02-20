def greet():
    print("Hi there!")

def say_name():
    print("My name is Python")

def welcome():
    print("Welcome to programming")

def info():
    print("This is a function")
    print("It can run multiple commands")

def goodbye():
    print("Goodbye!")

greet()
say_name()
welcome()
info()
goodbye()

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(68))
print(fahrenheit_to_celsius(86))
print(fahrenheit_to_celsius(104))

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

t1 = 32
t2 = 212
t3 = 59

print(fahrenheit_to_celsius(t1))
print(fahrenheit_to_celsius(t2))
print(fahrenheit_to_celsius(t3))

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(round(fahrenheit_to_celsius(77), 2))
print(round(fahrenheit_to_celsius(91), 2))
print(round(fahrenheit_to_celsius(45), 2))


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temps = [50, 68, 77, 86]

for t in temps:
    print(fahrenheit_to_celsius(t))

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print("77F =", fahrenheit_to_celsius(77), "C")
print("100F =", fahrenheit_to_celsius(100), "C")
print("41F =", fahrenheit_to_celsius(41), "C")