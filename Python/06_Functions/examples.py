# ============================================================================
#                      PYTHON FUNCTIONS - CODE EXAMPLES
# ============================================================================

# ----------------------------------------------------------------------------
# 1. BASIC FUNCTION DEFINITION
# ----------------------------------------------------------------------------

print("=== Basic Functions ===")

# Simple function
def greet():
    print("Hello, World!")

greet()

# Function with parameter
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Alice")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")


# ----------------------------------------------------------------------------
# 2. DEFAULT PARAMETERS
# ----------------------------------------------------------------------------

print("\n=== Default Parameters ===")

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))              # Hello, Alice!
print(greet("Bob", "Hi"))          # Hi, Bob!
print(greet("Charlie", greeting="Good morning"))

# CAUTION: Mutable default argument trap
def append_to(element, lst=[]):  # DON'T DO THIS!
    lst.append(element)
    return lst

# print(append_to(1))  # [1]
# print(append_to(2))  # [1, 2] - NOT [2]!

# Correct way
def append_to_correct(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst


# ----------------------------------------------------------------------------
# 3. KEYWORD ARGUMENTS
# ----------------------------------------------------------------------------

print("\n=== Keyword Arguments ===")

def create_user(name, age, city):
    return {"name": name, "age": age, "city": city}

# Positional
user1 = create_user("John", 25, "Delhi")
print(f"Positional: {user1}")

# Keyword (any order)
user2 = create_user(city="Mumbai", age=30, name="Alice")
print(f"Keyword: {user2}")


# ----------------------------------------------------------------------------
# 4. *args (Variable Positional Arguments)
# ----------------------------------------------------------------------------

print("\n=== *args ===")

def add_all(*args):
    print(f"args = {args}, type = {type(args)}")
    return sum(args)

print(f"add_all(1, 2): {add_all(1, 2)}")
print(f"add_all(1, 2, 3, 4, 5): {add_all(1, 2, 3, 4, 5)}")

# Unpacking a list with *
numbers = [1, 2, 3, 4, 5]
print(f"add_all(*numbers): {add_all(*numbers)}")


# ----------------------------------------------------------------------------
# 5. **kwargs (Variable Keyword Arguments)
# ----------------------------------------------------------------------------

print("\n=== **kwargs ===")

def show_info(**kwargs):
    print(f"kwargs = {kwargs}, type = {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

show_info(name="John", age=25, city="Delhi")

# Unpacking a dict with **
data = {"name": "Alice", "age": 30}
show_info(**data)


# ----------------------------------------------------------------------------
# 6. COMBINED PARAMETERS
# ----------------------------------------------------------------------------

print("\n=== Combined Parameters ===")

def func(a, b, *args, c=10, d=20, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"c={c}, d={d}")
    print(f"kwargs={kwargs}")

func(1, 2, 3, 4, 5, c=100, x=200, y=300)


# ----------------------------------------------------------------------------
# 7. RETURN VALUES
# ----------------------------------------------------------------------------

print("\n=== Return Values ===")

# Multiple return values (returns tuple)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers), sum(numbers)/len(numbers)

stats = get_stats([1, 2, 3, 4, 5])
print(f"Stats tuple: {stats}")

# Unpacking return values
minimum, maximum, total, average = get_stats([1, 2, 3, 4, 5])
print(f"Min: {minimum}, Max: {maximum}, Total: {total}, Avg: {average}")


# ----------------------------------------------------------------------------
# 8. SCOPE
# ----------------------------------------------------------------------------

print("\n=== Variable Scope ===")

global_var = "I am global"

def show_scope():
    local_var = "I am local"
    print(f"Inside function - global_var: {global_var}")
    print(f"Inside function - local_var: {local_var}")

show_scope()
print(f"Outside function - global_var: {global_var}")
# print(local_var)  # ERROR - local_var not accessible

# Using global keyword
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(f"Counter after 2 increments: {counter}")

# Using nonlocal keyword
def outer():
    x = 10
    print(f"outer before inner: x = {x}")

    def inner():
        nonlocal x
        x = 20
        print(f"inner: x = {x}")

    inner()
    print(f"outer after inner: x = {x}")

outer()


# ----------------------------------------------------------------------------
# 9. LAMBDA FUNCTIONS
# ----------------------------------------------------------------------------

print("\n=== Lambda Functions ===")

# Basic lambda
add = lambda a, b: a + b
print(f"Lambda add(5, 3): {add(5, 3)}")

# Lambda with one argument
square = lambda x: x ** 2
print(f"Lambda square(5): {square(5)}")

# Lambda with no arguments
greet = lambda: "Hello!"
print(f"Lambda greet(): {greet()}")

# Lambda with conditional
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(f"Lambda is_even(7): {is_even(7)}")


# ----------------------------------------------------------------------------
# 10. HIGHER-ORDER FUNCTIONS
# ----------------------------------------------------------------------------

print("\n=== map() ===")

numbers = [1, 2, 3, 4, 5]

# Square each number
squares = list(map(lambda x: x**2, numbers))
print(f"Squares: {squares}")

# Convert to strings
strings = list(map(str, numbers))
print(f"As strings: {strings}")

# Multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
sums = list(map(lambda x, y: x + y, a, b))
print(f"Sum of two lists: {sums}")


print("\n=== filter() ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Filter strings longer than 3 chars
words = ["hi", "hello", "hey", "world", "bye"]
long_words = list(filter(lambda x: len(x) > 3, words))
print(f"Long words: {long_words}")


print("\n=== reduce() ===")

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(f"Sum: {total}")

# Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum: {maximum}")


# ----------------------------------------------------------------------------
# 11. SORTING WITH KEY FUNCTION
# ----------------------------------------------------------------------------

print("\n=== Sorting with key ===")

# Sort strings by length
words = ["python", "is", "awesome", "and", "fun"]
sorted_by_length = sorted(words, key=len)
print(f"By length: {sorted_by_length}")

# Sort tuples by second element
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"By score (descending): {sorted_by_score}")

# Sort dictionaries
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
sorted_by_age = sorted(people, key=lambda x: x["age"])
print(f"By age: {sorted_by_age}")


# ----------------------------------------------------------------------------
# 12. RECURSION
# ----------------------------------------------------------------------------

print("\n=== Recursion ===")

# Factorial
def factorial(n):
    if n <= 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(f"factorial(5): {factorial(5)}")

# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"First 10 Fibonacci: {[fibonacci(i) for i in range(10)]}")

# Sum of list using recursion
def sum_recursive(lst):
    if not lst:  # Base case: empty list
        return 0
    return lst[0] + sum_recursive(lst[1:])

print(f"sum_recursive([1,2,3,4,5]): {sum_recursive([1,2,3,4,5])}")


# ----------------------------------------------------------------------------
# 13. CLOSURES
# ----------------------------------------------------------------------------

print("\n=== Closures ===")

def outer(x):
    def inner(y):
        return x + y  # inner "closes over" x
    return inner

add_10 = outer(10)
add_20 = outer(20)

print(f"add_10(5): {add_10(5)}")    # 15
print(f"add_20(5): {add_20(5)}")    # 25

# Counter using closure
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter = make_counter()
print(f"counter(): {counter()}")  # 1
print(f"counter(): {counter()}")  # 2
print(f"counter(): {counter()}")  # 3


# ----------------------------------------------------------------------------
# 14. FIRST-CLASS FUNCTIONS
# ----------------------------------------------------------------------------

print("\n=== First-Class Functions ===")

# Assign to variable
def greet(name):
    return f"Hello, {name}"

say_hello = greet
print(say_hello("Alice"))

# Pass as argument
def apply_twice(func, value):
    return func(func(value))

def double(x):
    return x * 2

result = apply_twice(double, 5)  # double(double(5)) = double(10) = 20
print(f"apply_twice(double, 5): {result}")

# Return from function
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

triple = multiplier(3)
print(f"triple(5): {triple(5)}")


# ----------------------------------------------------------------------------
# 15. FUNCTION ANNOTATIONS
# ----------------------------------------------------------------------------

print("\n=== Function Annotations ===")

def greet(name: str, age: int = 0) -> str:
    return f"Hello {name}, you are {age}"

print(greet("Alice", 25))
print(f"Annotations: {greet.__annotations__}")


# ----------------------------------------------------------------------------
# 16. PRACTICE PROBLEMS
# ----------------------------------------------------------------------------

print("\n=== Practice Problems ===")

# Problem 1: Check if prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"is_prime(17): {is_prime(17)}")
print(f"is_prime(20): {is_prime(20)}")

# Problem 2: Palindrome check
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(f"is_palindrome('radar'): {is_palindrome('radar')}")
print(f"is_palindrome('A man a plan a canal Panama'): {is_palindrome('A man a plan a canal Panama')}")

# Problem 3: GCD using recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(f"gcd(48, 18): {gcd(48, 18)}")

# Problem 4: Power function using recursion
def power(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)

print(f"power(2, 10): {power(2, 10)}")

# Problem 5: Count occurrences using recursion
def count_occurrence(lst, target):
    if not lst:
        return 0
    return (1 if lst[0] == target else 0) + count_occurrence(lst[1:], target)

print(f"count_occurrence([1,2,1,3,1], 1): {count_occurrence([1,2,1,3,1], 1)}")
