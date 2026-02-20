# 5 examples of simple classes and objects

# Example 1
class MyClass1:
    x = 5
p1 = MyClass1()
print(p1.x)

# Example 2
class MyClass2:
    x = 10
p2 = MyClass2()
print(p2.x)

# Example 3
class MyClass3:
    x = "Hello"
p3 = MyClass3()
print(p3.x)

# Example 4
class MyClass4:
    x = [1, 2, 3]
p4 = MyClass4()
print(p4.x)

# Example 5
class MyClass5:
    x = True
p5 = MyClass5()
print(p5.x)

# 5 examples of deleting objects

# Example 1
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)
del p1

# Example 2
p2 = MyClass()
print(p2.x)
del p2

# Example 3
p3 = MyClass()
print(p3.x)
del p3

# Example 4
p4 = MyClass()
print(p4.x)
del p4

# Example 5
p5 = MyClass()
print(p5.x)
del p5

# 5 examples of creating multiple objects

# Example 1
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
print(p1.x, p2.x, p3.x)

# Example 2
class Car:
    wheels = 4
car1 = Car()
car2 = Car()
car3 = Car()
print(car1.wheels, car2.wheels, car3.wheels)

# Example 3
class Person:
    name = "Unknown"
person1 = Person()
person2 = Person()
person3 = Person()
print(person1.name, person2.name, person3.name)

# Example 4
class Animal:
    species = "Cat"
a1 = Animal()
a2 = Animal()
a3 = Animal()
print(a1.species, a2.species, a3.species)

# Example 5
class Phone:
    brand = "Apple"
ph1 = Phone()
ph2 = Phone()
ph3 = Phone()
print(ph1.brand, ph2.brand, ph3.brand)

# 5 examples of empty classes using pass

# Example 1
class Person1:
    pass

# Example 2
class Person2:
    pass

# Example 3
class Person3:
    pass

# Example 4
class Vehicle1:
    pass

# Example 5
class Vehicle2:
    pass

