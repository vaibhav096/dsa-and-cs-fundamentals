# ============================================================================
#                         PYTHON BASICS - CODE EXAMPLES
# ============================================================================

# ----------------------------------------------------------------------------
# 1. PRINT STATEMENT
# ----------------------------------------------------------------------------

print("Hello World")                        # Basic print
print("Hello", "World")                     # Multiple values (space separated)
print("Hello", "World", sep="-")            # Custom separator
print("Hello", end=" ")                     # Custom end character
print("World")                              # Continues on same line

# Print with different data types
print(100)                                  # Integer
print(3.14)                                 # Float
print(True)                                 # Boolean

# Formatted print
name = "John"
age = 25
print(f"Name: {name}, Age: {age}")          # f-string (recommended)
print("Name: {}, Age: {}".format(name, age)) # format method
print("Name: %s, Age: %d" % (name, age))    # % formatting (old style)


# ----------------------------------------------------------------------------
# 2. VARIABLES
# ----------------------------------------------------------------------------

# Creating variables
x = 10                  # integer
name = "Alice"          # string
price = 99.99           # float
is_valid = True         # boolean

# Multiple assignment
a, b, c = 1, 2, 3       # Different values
x = y = z = 0           # Same value

# Swapping variables (Pythonic way)
a, b = 5, 10
a, b = b, a             # Now a=10, b=5
print(f"After swap: a={a}, b={b}")

# Variable reassignment
x = 5
print(type(x))          # <class 'int'>
x = "Hello"
print(type(x))          # <class 'str'> - Dynamic typing!


# ----------------------------------------------------------------------------
# 3. DATA TYPES
# ----------------------------------------------------------------------------

# Integer
num1 = 100
num2 = -50
num3 = 0

# Float
pi = 3.14159
temperature = -10.5

# Complex
complex_num = 3 + 4j
print(f"Real part: {complex_num.real}, Imaginary part: {complex_num.imag}")

# String
str1 = "Hello"
str2 = 'World'
str3 = """This is
a multi-line
string"""

# Boolean
is_active = True
is_deleted = False
result = 10 > 5         # True

# List (mutable, ordered)
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

# Tuple (immutable, ordered)
coordinates = (10, 20)
rgb = (255, 128, 0)

# Dictionary (key-value pairs)
person = {
    "name": "John",
    "age": 25,
    "city": "Delhi"
}

# Set (unique elements, unordered)
unique_numbers = {1, 2, 3, 2, 1}  # Stores {1, 2, 3}

# None
result = None


# ----------------------------------------------------------------------------
# 4. TYPE CHECKING
# ----------------------------------------------------------------------------

x = 100
print(type(x))                      # <class 'int'>
print(isinstance(x, int))           # True
print(isinstance(x, (int, float)))  # True (checks multiple types)

# Check if variable is None
value = None
if value is None:
    print("Value is None")


# ----------------------------------------------------------------------------
# 5. TYPE CONVERSION
# ----------------------------------------------------------------------------

# String to Integer
num_str = "100"
num = int(num_str)
print(num + 50)                     # 150

# String to Float
price_str = "99.99"
price = float(price_str)
print(price)                        # 99.99

# Number to String
age = 25
age_str = str(age)
print("Age is " + age_str)          # Age is 25

# To Boolean
print(bool(0))                      # False
print(bool(1))                      # True
print(bool(""))                     # False
print(bool("hello"))                # True
print(bool([]))                     # False (empty list)
print(bool([1, 2]))                 # True

# List and Tuple conversion
my_list = [1, 2, 3]
my_tuple = tuple(my_list)           # (1, 2, 3)
back_to_list = list(my_tuple)       # [1, 2, 3]


# ----------------------------------------------------------------------------
# 6. INPUT FROM USER
# ----------------------------------------------------------------------------

# Basic string input
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# Integer input
# age = int(input("Enter your age: "))
# print(f"You will be {age + 1} next year")

# Float input
# height = float(input("Enter your height in meters: "))
# print(f"Your height is {height} meters")

# Taking multiple inputs in one line
# a, b = input("Enter two numbers: ").split()
# a, b = int(a), int(b)
# print(f"Sum: {a + b}")

# Taking multiple integers using map
# a, b, c = map(int, input("Enter three numbers: ").split())
# print(f"Sum: {a + b + c}")


# ----------------------------------------------------------------------------
# 7. COMMON OPERATIONS
# ----------------------------------------------------------------------------

# String concatenation
first = "Hello"
second = "World"
result = first + " " + second       # Hello World

# String repetition
stars = "*" * 10                    # **********

# Length of string/list
text = "Python"
print(len(text))                    # 6

# Membership check
print("P" in "Python")              # True
print(5 in [1, 2, 3, 4, 5])        # True


# ----------------------------------------------------------------------------
# 8. PRACTICE PROBLEMS
# ----------------------------------------------------------------------------

# Problem 1: Calculate area of rectangle
length = 10
width = 5
area = length * width
print(f"Area of rectangle: {area}")

# Problem 2: Convert Celsius to Fahrenheit
celsius = 37
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Problem 3: Calculate simple interest
principal = 10000
rate = 5
time = 2
interest = (principal * rate * time) / 100
print(f"Simple Interest: {interest}")

# Problem 4: Swap two numbers without temp variable
x, y = 10, 20
x, y = y, x
print(f"After swap: x={x}, y={y}")

# Problem 5: Check if number is even or odd
num = 7
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
