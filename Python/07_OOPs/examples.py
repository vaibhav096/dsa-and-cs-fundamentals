# ============================================================================
#                          OOP - CODE EXAMPLES
# ============================================================================

# ----------------------------------------------------------------------------
# 1. BASIC CLASS AND OBJECT
# ----------------------------------------------------------------------------

print("=== Basic Class and Object ===")

class Dog:
    # Class attribute
    species = "Canine"

    # Constructor
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    def description(self):
        return f"{self.name} is {self.age} years old"


# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"dog1.name: {dog1.name}")
print(f"dog1.bark(): {dog1.bark()}")
print(f"dog1.description(): {dog1.description()}")
print(f"Dog.species: {Dog.species}")
print(f"dog1.species: {dog1.species}")


# ----------------------------------------------------------------------------
# 2. INSTANCE vs CLASS ATTRIBUTES
# ----------------------------------------------------------------------------

print("\n=== Instance vs Class Attributes ===")

class Employee:
    # Class attributes
    company = "TechCorp"
    employee_count = 0

    def __init__(self, name, salary):
        # Instance attributes
        self.name = name
        self.salary = salary
        Employee.employee_count += 1


e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

print(f"e1.name: {e1.name}")
print(f"e2.name: {e2.name}")
print(f"Employee.company: {Employee.company}")
print(f"Employee.employee_count: {Employee.employee_count}")

# Modifying class attribute affects all instances
Employee.company = "NewCorp"
print(f"After change - e1.company: {e1.company}")
print(f"After change - e2.company: {e2.company}")


# ----------------------------------------------------------------------------
# 3. CLASS METHODS AND STATIC METHODS
# ----------------------------------------------------------------------------

print("\n=== Class Methods and Static Methods ===")

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # Instance method
    def display(self):
        return f"{self.day}/{self.month}/{self.year}"

    # Class method - alternative constructor
    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        return cls(day, month, year)

    # Class method - another alternative constructor
    @classmethod
    def today(cls):
        import datetime
        t = datetime.date.today()
        return cls(t.day, t.month, t.year)

    # Static method - utility function
    @staticmethod
    def is_valid_date(day, month, year):
        return 1 <= day <= 31 and 1 <= month <= 12 and year > 0


# Using different constructors
d1 = Date(25, 12, 2023)
d2 = Date.from_string("15-08-2023")
d3 = Date.today()

print(f"d1: {d1.display()}")
print(f"d2: {d2.display()}")
print(f"d3: {d3.display()}")
print(f"Is 31/12/2023 valid? {Date.is_valid_date(31, 12, 2023)}")


# ----------------------------------------------------------------------------
# 4. ENCAPSULATION
# ----------------------------------------------------------------------------

print("\n=== Encapsulation ===")

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public
        self._holder = "Unknown"              # Protected (convention)
        self.__balance = balance              # Private (name mangling)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        return "Invalid amount"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New balance: {self.__balance}"
        return "Invalid amount or insufficient funds"

    def get_balance(self):
        return self.__balance


acc = BankAccount("123456", 1000)
print(f"Account: {acc.account_number}")
print(acc.deposit(500))
print(acc.withdraw(200))
print(f"Balance: {acc.get_balance()}")

# Private attribute is name-mangled
# print(acc.__balance)  # AttributeError
print(f"Accessing via name mangling: {acc._BankAccount__balance}")


# ----------------------------------------------------------------------------
# 5. PROPERTY DECORATOR
# ----------------------------------------------------------------------------

print("\n=== Property Decorator ===")

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter for radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter for radius"""
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Read-only property"""
        return 3.14159 * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2


c = Circle(5)
print(f"Radius: {c.radius}")
print(f"Area: {c.area}")
print(f"Diameter: {c.diameter}")

c.radius = 10
print(f"New radius: {c.radius}")
print(f"New area: {c.area}")


# ----------------------------------------------------------------------------
# 6. INHERITANCE
# ----------------------------------------------------------------------------

print("\n=== Inheritance ===")

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

    def info(self):
        return f"I am {self.name}"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed

    def speak(self):  # Override parent method
        return "Woof!"

    def info(self):
        return f"{super().info()} and I am a {self.breed}"


class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers")

print(f"dog.speak(): {dog.speak()}")
print(f"cat.speak(): {cat.speak()}")
print(f"dog.info(): {dog.info()}")
print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")


# ----------------------------------------------------------------------------
# 7. MULTIPLE INHERITANCE
# ----------------------------------------------------------------------------

print("\n=== Multiple Inheritance ===")

class Flyable:
    def fly(self):
        return "Flying high!"


class Swimmable:
    def swim(self):
        return "Swimming fast!"


class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack!"


duck = Duck()
print(f"duck.fly(): {duck.fly()}")
print(f"duck.swim(): {duck.swim()}")
print(f"duck.quack(): {duck.quack()}")
print(f"MRO: {Duck.__mro__}")


# Diamond problem
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(f"\nDiamond problem - d.method(): {d.method()}")  # B (MRO: D -> B -> C -> A)
print(f"D.__mro__: {D.__mro__}")


# ----------------------------------------------------------------------------
# 8. POLYMORPHISM
# ----------------------------------------------------------------------------

print("\n=== Polymorphism ===")

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Polymorphic behavior
shapes = [Rectangle(4, 5), Circle(3), Triangle(6, 4)]
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")


# ----------------------------------------------------------------------------
# 9. ABSTRACTION
# ----------------------------------------------------------------------------

print("\n=== Abstraction ===")

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def info(self):  # Concrete method
        return f"This is a {self.brand}"


class Car(Vehicle):
    def start(self):
        return "Car engine starting..."

    def stop(self):
        return "Car engine stopping..."


class Bike(Vehicle):
    def start(self):
        return "Bike engine starting..."

    def stop(self):
        return "Bike engine stopping..."


# vehicle = Vehicle("Generic")  # TypeError - can't instantiate abstract class
car = Car("Toyota")
bike = Bike("Honda")

print(f"car.start(): {car.start()}")
print(f"bike.start(): {bike.start()}")
print(f"car.info(): {car.info()}")


# ----------------------------------------------------------------------------
# 10. DUNDER METHODS
# ----------------------------------------------------------------------------

print("\n=== Dunder Methods ===")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)

    def __bool__(self):
        return self.x != 0 or self.y != 0


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"v1 == v2: {v1 == v2}")
print(f"len(v1): {len(v1)}")
print(f"bool(Vector(0, 0)): {bool(Vector(0, 0))}")


# ----------------------------------------------------------------------------
# 11. CALLABLE OBJECTS
# ----------------------------------------------------------------------------

print("\n=== Callable Objects (__call__) ===")

class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count


counter = Counter()
print(f"counter(): {counter()}")  # 1
print(f"counter(): {counter()}")  # 2
print(f"counter(): {counter()}")  # 3


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor


double = Multiplier(2)
triple = Multiplier(3)
print(f"double(5): {double(5)}")
print(f"triple(5): {triple(5)}")


# ----------------------------------------------------------------------------
# 12. COMPOSITION vs INHERITANCE
# ----------------------------------------------------------------------------

print("\n=== Composition vs Inheritance ===")

# Composition - "has a" relationship
class Engine:
    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()  # Composition

    def start(self):
        return f"{self.brand}: {self.engine.start()}"


car = Car("Toyota")
print(f"car.start(): {car.start()}")


# ----------------------------------------------------------------------------
# 13. PRACTICE: COMPLETE CLASS EXAMPLE
# ----------------------------------------------------------------------------

print("\n=== Complete Example: Library System ===")

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} [{status}]"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}')"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Added: {book.title}"

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                return f"Borrowed: {book.title}"
        return "Book not available"

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed = False
                return f"Returned: {book.title}"
        return "Book not found"

    def __len__(self):
        return len(self.books)

    def __iter__(self):
        return iter(self.books)


# Using the library system
lib = Library("City Library")
lib.add_book(Book("Python Guide", "Guido", "001"))
lib.add_book(Book("Data Science", "Jake", "002"))

print(f"Library: {lib.name}")
print(f"Total books: {len(lib)}")

print("\nAll books:")
for book in lib:
    print(f"  {book}")

print(f"\n{lib.borrow_book('001')}")

print("\nAfter borrowing:")
for book in lib:
    print(f"  {book}")
