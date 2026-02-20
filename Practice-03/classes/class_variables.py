# Example 1
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person1("Emil", 36)
print(p1.name)
print(p1.age)

# Example 2
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person2("Tobias", 25)
print(p2.name)
print(p2.age)

# Example 3
class Car1:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car1("Toyota", "Corolla")
print(car1.brand)
print(car1.model)

# Example 4
class Book1:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book1("1984", "Orwell")
print(book1.title)
print(book1.author)

# Example 5
class City1:
    def __init__(self, name, population):
        self.name = name
        self.population = population

city1 = City1("Oslo", 634000)
print(city1.name)
print(city1.population)

# Example 1
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person1("Tobias", 25)
print(p1.age)
p1.age = 26
print(p1.age)

# Example 2
class Car1:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car1("Toyota", "Corolla")
print(car1.model)
car1.model = "Camry"
print(car1.model)

# Example 3
class Book1:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book1("1984", "Orwell")
book1.title = "Animal Farm"
print(book1.title)

# Example 4
class City1:
    def __init__(self, name, population):
        self.name = name
        self.population = population

city1 = City1("Oslo", 634000)
city1.population = 650000
print(city1.population)

# Example 5
class Laptop1:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

laptop1 = Laptop1("Dell", 8)
laptop1.ram = 16
print(laptop1.ram)

# Example 1
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person1("Linus", 30)
del p1.age
print(p1.name)
# print(p1.age)  # would cause an error

# Example 2
class Car1:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car1("Toyota", "Corolla")
del car1.model
print(car1.brand)

# Example 3
class Book1:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book1("1984", "Orwell")
del book1.author
print(book1.title)

# Example 4
class City1:
    def __init__(self, name, population):
        self.name = name
        self.population = population

city1 = City1("Oslo", 634000)
del city1.population
print(city1.name)

# Example 5
class Laptop1:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

laptop1 = Laptop1("Dell", 8)
del laptop1.ram
print(laptop1.brand)

# Example 1
class Person1:
    species = "Human"  # Class property

    def __init__(self, name):
        self.name = name  # Instance property

p1 = Person1("Emil")
p2 = Person1("Tobias")
print(p1.name, p2.name)
print(p1.species, p2.species)

# Example 2
class Car1:
    wheels = 4  # Class property

    def __init__(self, brand):
        self.brand = brand  # Instance property

car1 = Car1("Toyota")
car2 = Car1("Honda")
print(car1.brand, car2.brand)
print(car1.wheels, car2.wheels)

# Example 3
class Book1:
    category = "Fiction"  # Class property

    def __init__(self, title):
        self.title = title  # Instance property

book1 = Book1("1984")
book2 = Book1("Animal Farm")
print(book1.title, book2.title)
print(book1.category, book2.category)

# Example 4
class City1:
    continent = "Europe"  # Class property

    def __init__(self, name):
        self.name = name  # Instance property

city1 = City1("Oslo")
city2 = City1("Bergen")
print(city1.name, city2.name)
print(city1.continent, city2.continent)

# Example 5
class Laptop1:
    brand_type = "PC"  # Class property

    def __init__(self, model):
        self.model = model  # Instance property

laptop1 = Laptop1("XPS")
laptop2 = Laptop1("Inspiron")
print(laptop1.model, laptop2.model)
print(laptop1.brand_type, laptop2.brand_type)

# Example 1
class Person1:
    def __init__(self, name):
        self.name = name

p1 = Person1("Tobias")
p1.age = 25
p1.city = "Oslo"
print(p1.name, p1.age, p1.city)

# Example 2
class Car1:
    def __init__(self, brand):
        self.brand = brand

car1 = Car1("Toyota")
car1.color = "Red"
car1.year = 2020
print(car1.brand, car1.color, car1.year)

# Example 3
class Book1:
    def __init__(self, title):
        self.title = title

book1 = Book1("1984")
book1.pages = 328
book1.publisher = "Secker & Warburg"
print(book1.title, book1.pages, book1.publisher)

# Example 4
class City1:
    def __init__(self, name):
        self.name = name

city1 = City1("Oslo")
city1.population = 634000
city1.country = "Norway"
print(city1.name, city1.population, city1.country)

# Example 5
class Laptop1:
    def __init__(self, model):
        self.model = model

laptop1 = Laptop1("XPS")
laptop1.ram = 16
laptop1.cpu = "Intel i7"
print(laptop1.model, laptop1.ram, laptop1.cpu)

