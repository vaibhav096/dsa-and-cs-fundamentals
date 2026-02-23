# ============================================================================
#                    ADVANCED PYTHON - CODE EXAMPLES
# ============================================================================

# ----------------------------------------------------------------------------
# 1. ITERATORS
# ----------------------------------------------------------------------------

print("=== Iterators ===")

# Basic iteration
lst = [1, 2, 3]
itr = iter(lst)  # Get iterator
print(f"next(itr): {next(itr)}")  # 1
print(f"next(itr): {next(itr)}")  # 2
print(f"next(itr): {next(itr)}")  # 3

# Custom Iterator
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.n = self.start
        return self

    def __next__(self):
        if self.n > 0:
            result = self.n
            self.n -= 1
            return result
        raise StopIteration

print("\nCustom CountDown iterator:")
for num in CountDown(5):
    print(num, end=" ")
print()


# ----------------------------------------------------------------------------
# 2. GENERATORS
# ----------------------------------------------------------------------------

print("\n=== Generators ===")

# Basic Generator
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1

print("count_up(5):", end=" ")
for num in count_up(5):
    print(num, end=" ")
print()

# Generator for Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Fibonacci(10):", list(fibonacci(10)))

# Generator Expression
squares_gen = (x**2 for x in range(5))
print(f"Generator expression type: {type(squares_gen)}")
print(f"List from generator: {list(squares_gen)}")

# Infinite Generator
def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1

counter = infinite_counter()
print(f"Infinite counter: {next(counter)}, {next(counter)}, {next(counter)}")

# Generator with send()
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

acc = accumulator()
next(acc)  # Initialize
print(f"\nAccumulator with send(): {acc.send(10)}, {acc.send(5)}, {acc.send(3)}")


# ----------------------------------------------------------------------------
# 3. DECORATORS
# ----------------------------------------------------------------------------

print("\n=== Decorators ===")

# Basic Decorator
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print("Using @logger decorator:")
result = add(5, 3)

# Timer Decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "Done"

print("\nUsing @timer decorator:")
slow_function()

# Decorator with Parameters
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

print("\nUsing @repeat(3) decorator:")
greet("World")

# Using functools.wraps
from functools import wraps

def better_logger(func):
    @wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@better_logger
def my_function():
    """This is my function's docstring"""
    pass

print(f"\nWith @wraps - function name: {my_function.__name__}")
print(f"With @wraps - docstring: {my_function.__doc__}")


# ----------------------------------------------------------------------------
# 4. COMPREHENSIONS
# ----------------------------------------------------------------------------

print("\n=== Comprehensions ===")

# List Comprehension
squares = [x**2 for x in range(6)]
print(f"Squares: {squares}")

evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: {evens}")

labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(f"Labels: {labels}")

# Nested List Comprehension
matrix = [[i*3 + j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Flatten matrix
flat = [num for row in matrix for num in row]
print(f"Flattened: {flat}")

# Dictionary Comprehension
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dict: {squares_dict}")

# Set Comprehension
unique_squares = {x**2 for x in [-2, -1, 0, 1, 2]}
print(f"Unique squares: {unique_squares}")

# Generator Expression (lazy)
sum_of_squares = sum(x**2 for x in range(1000))
print(f"Sum of squares (0-999): {sum_of_squares}")


# ----------------------------------------------------------------------------
# 5. LAMBDA FUNCTIONS
# ----------------------------------------------------------------------------

print("\n=== Lambda Functions ===")

# Basic lambda
add = lambda a, b: a + b
print(f"lambda add(5, 3): {add(5, 3)}")

# Lambda with conditional
max_val = lambda a, b: a if a > b else b
print(f"lambda max(10, 5): {max_val(10, 5)}")

# Lambda with multiple operations
process = lambda x: x.strip().lower().replace(" ", "_")
print(f"lambda process('  Hello World  '): '{process('  Hello World  ')}'")


# ----------------------------------------------------------------------------
# 6. MAP, FILTER, REDUCE
# ----------------------------------------------------------------------------

print("\n=== Map, Filter, Reduce ===")

numbers = [1, 2, 3, 4, 5]

# Map
doubled = list(map(lambda x: x * 2, numbers))
print(f"Map (double): {doubled}")

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filter (evens): {evens}")

# Reduce
from functools import reduce
product = reduce(lambda a, b: a * b, numbers)
print(f"Reduce (product): {product}")

# Combining map and filter
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(10))))
print(f"Combined (squares of evens): {result}")

# Same with comprehension (more Pythonic)
result = [x**2 for x in range(10) if x % 2 == 0]
print(f"Using comprehension: {result}")


# ----------------------------------------------------------------------------
# 7. ARGS AND KWARGS
# ----------------------------------------------------------------------------

print("\n=== Args and Kwargs ===")

def show_args(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

show_args(1, 2, 3, name="John", age=25)

# Unpacking
def add_three(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(f"Unpacking list: {add_three(*nums)}")

d = {'a': 1, 'b': 2, 'c': 3}
print(f"Unpacking dict: {add_three(**d)}")


# ----------------------------------------------------------------------------
# 8. CONTEXT MANAGERS
# ----------------------------------------------------------------------------

print("\n=== Context Managers ===")

# Custom context manager using class
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self.start
        print(f"Elapsed time: {self.elapsed:.4f} seconds")
        return False

with Timer():
    total = sum(range(100000))
    print(f"Sum: {total}")

# Context manager using decorator
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Acquiring {name}")
    try:
        yield name
    finally:
        print(f"Releasing {name}")

print("\nUsing @contextmanager:")
with managed_resource("Database Connection") as resource:
    print(f"Using {resource}")


# ----------------------------------------------------------------------------
# 9. WALRUS OPERATOR (:=)
# ----------------------------------------------------------------------------

print("\n=== Walrus Operator ===")

# In if statement
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if (n := len(data)) > 5:
    print(f"Data has {n} elements, which is > 5")

# In list comprehension
numbers = [1, 2, 3, 4, 5]
results = [y for x in numbers if (y := x**2) > 10]
print(f"Squares > 10: {results}")

# In while loop (conceptual)
# while (line := input()) != "quit":
#     print(f"You entered: {line}")


# ----------------------------------------------------------------------------
# 10. PRACTICAL EXAMPLES
# ----------------------------------------------------------------------------

print("\n=== Practical Examples ===")

# Memoization decorator
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(30) with memoization: {fibonacci(30)}")

# Validation decorator
def validate_positive(func):
    @wraps(func)
    def wrapper(*args):
        if any(arg < 0 for arg in args if isinstance(arg, (int, float))):
            raise ValueError("All arguments must be positive")
        return func(*args)
    return wrapper

@validate_positive
def calculate_area(length, width):
    return length * width

print(f"Area(5, 3): {calculate_area(5, 3)}")

# Pipeline using reduce
def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)

# Create pipeline: double -> add_one -> square
double = lambda x: x * 2
add_one = lambda x: x + 1
square = lambda x: x ** 2

pipeline = compose(square, add_one, double)  # Applied right to left
print(f"Pipeline(5): double->add_one->square = {pipeline(5)}")  # ((5*2)+1)^2 = 121


print("\n=== Advanced Examples Complete ===")
