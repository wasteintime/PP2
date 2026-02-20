# Example 1
class Person1:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person1("Emil")
p1.greet()

# Example 2
class Person2:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi, I'm " + self.name)

p2 = Person2("Anna")
p2.greet()

# Example 3
class Person3:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hey! My name is {self.name}")

p3 = Person3("John")
p3.greet()

# Example 4
class Person4:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Greetings from {self.name}")

p4 = Person4("Maria")
p4.greet()

# Example 5
class Person5:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello there, I am " + self.name)

p5 = Person5("Ali")
p5.greet()

# Example 1
class Calculator1:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc1 = Calculator1()
print(calc1.add(5, 3))
print(calc1.multiply(4, 7))

# Example 2
class Calculator2:
    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        return a / b

calc2 = Calculator2()
print(calc2.subtract(10, 4))
print(calc2.divide(20, 5))

# Example 3
class Calculator3:
    def power(self, a, b):
        return a ** b

    def modulo(self, a, b):
        return a % b

calc3 = Calculator3()
print(calc3.power(2, 3))
print(calc3.modulo(10, 3))

# Example 4
class Calculator4:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc4 = Calculator4()
print(calc4.add(7, 8))
print(calc4.multiply(6, 9))

# Example 5
class Calculator5:
    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        return a / b

calc5 = Calculator5()
print(calc5.subtract(15, 7))
print(calc5.divide(50, 10))

# Accessing properties
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"

p1 = Person1("Tobias", 28)
print(p1.get_info())

# Modifying properties
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")

p2 = Person2("Linus", 25)
p2.celebrate_birthday()
p2.celebrate_birthday()

# Without __str__
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person1("Emil", 36)
print(p1)  # Will print object reference

# With __str__
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p2 = Person2("Tobias", 36)
print(p2)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")

    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f"- {song}")

# 5 examples
my_playlist1 = Playlist("Favorites")
my_playlist1.add_song("Bohemian Rhapsody")
my_playlist1.add_song("Stairway to Heaven")
my_playlist1.show_songs()

my_playlist2 = Playlist("Chill")
my_playlist2.add_song("Imagine")
my_playlist2.add_song("Let it be")
my_playlist2.show_songs()

my_playlist3 = Playlist("Rock")
my_playlist3.add_song("Hotel California")
my_playlist3.add_song("Sweet Child O' Mine")
my_playlist3.show_songs()

my_playlist4 = Playlist("Pop")
my_playlist4.add_song("Thriller")
my_playlist4.add_song("Like a Prayer")
my_playlist4.show_songs()

my_playlist5 = Playlist("Jazz")
my_playlist5.add_song("So What")
my_playlist5.add_song("Take Five")
my_playlist5.show_songs()


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello!")

p1 = Person("Emil")

# Deleting method
del Person.greet

# This will raise an error:
# p1.greet()



