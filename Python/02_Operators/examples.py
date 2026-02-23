# ============================================================================
#                      PYTHON OPERATORS - CODE EXAMPLES
# ============================================================================

# ----------------------------------------------------------------------------
# 1. ARITHMETIC OPERATORS
# ----------------------------------------------------------------------------

a, b = 10, 3

print("=== Arithmetic Operators ===")
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")       # Addition: 13
print(f"a - b = {a - b}")       # Subtraction: 7
print(f"a * b = {a * b}")       # Multiplication: 30
print(f"a / b = {a / b}")       # Division: 3.333... (always float)
print(f"a // b = {a // b}")     # Floor Division: 3
print(f"a % b = {a % b}")       # Modulus: 1
print(f"a ** b = {a ** b}")     # Exponentiation: 1000

# Floor division with negative numbers
print(f"-10 // 3 = {-10 // 3}") # -4 (floors towards negative infinity)
print(f"10 // -3 = {10 // -3}") # -4

# Modulus with negative numbers
print(f"-10 % 3 = {-10 % 3}")   # 2 (result has same sign as divisor)


# ----------------------------------------------------------------------------
# 2. COMPARISON OPERATORS
# ----------------------------------------------------------------------------

x, y = 5, 10

print("\n=== Comparison Operators ===")
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")      # False
print(f"x != y: {x != y}")      # True
print(f"x > y: {x > y}")        # False
print(f"x < y: {x < y}")        # True
print(f"x >= y: {x >= y}")      # False
print(f"x <= y: {x <= y}")      # True

# Chained comparisons (Pythonic!)
age = 25
print(f"\n18 <= {age} <= 65: {18 <= age <= 65}")  # True

# String comparison (lexicographic)
print(f"\n'apple' < 'banana': {'apple' < 'banana'}")  # True
print(f"'Apple' < 'apple': {'Apple' < 'apple'}")      # True (uppercase < lowercase)


# ----------------------------------------------------------------------------
# 3. ASSIGNMENT OPERATORS
# ----------------------------------------------------------------------------

print("\n=== Assignment Operators ===")

x = 10
print(f"x = {x}")

x += 5      # x = x + 5
print(f"x += 5: {x}")   # 15

x -= 3      # x = x - 3
print(f"x -= 3: {x}")   # 12

x *= 2      # x = x * 2
print(f"x *= 2: {x}")   # 24

x /= 4      # x = x / 4
print(f"x /= 4: {x}")   # 6.0

x = 10
x //= 3     # x = x // 3
print(f"x //= 3: {x}")  # 3

x = 10
x %= 3      # x = x % 3
print(f"x %= 3: {x}")   # 1

x = 2
x **= 3     # x = x ** 3
print(f"x **= 3: {x}")  # 8


# ----------------------------------------------------------------------------
# 4. LOGICAL OPERATORS
# ----------------------------------------------------------------------------

print("\n=== Logical Operators ===")

a, b = True, False

print(f"a = {a}, b = {b}")
print(f"a and b: {a and b}")    # False
print(f"a or b: {a or b}")      # True
print(f"not a: {not a}")        # False
print(f"not b: {not b}")        # True

# Practical example
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"\nCan drive: {can_drive}")  # True

# Short-circuit evaluation demo
def check():
    print("Function called!")
    return True

print("\nShort-circuit with and:")
result = False and check()  # Function NOT called
print(f"Result: {result}")

print("\nShort-circuit with or:")
result = True or check()    # Function NOT called
print(f"Result: {result}")

# Using logical operators with non-boolean values
# and returns first falsy value or last value
print(f"\n0 and 5: {0 and 5}")           # 0
print(f"3 and 5: {3 and 5}")             # 5
print(f"'' and 'hello': {'' and 'hello'}")  # ''

# or returns first truthy value or last value
print(f"\n0 or 5: {0 or 5}")             # 5
print(f"3 or 5: {3 or 5}")               # 3
print(f"'' or 'default': {'' or 'default'}")  # default


# ----------------------------------------------------------------------------
# 5. BITWISE OPERATORS
# ----------------------------------------------------------------------------

print("\n=== Bitwise Operators ===")

a, b = 5, 3  # 5 = 101, 3 = 011

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")

print(f"a & b = {a & b} (binary: {bin(a & b)})")   # 1 (001)
print(f"a | b = {a | b} (binary: {bin(a | b)})")   # 7 (111)
print(f"a ^ b = {a ^ b} (binary: {bin(a ^ b)})")   # 6 (110)
print(f"~a = {~a}")                                 # -6 (two's complement)
print(f"a << 1 = {a << 1}")                        # 10 (1010) - multiply by 2
print(f"a >> 1 = {a >> 1}")                        # 2 (10) - divide by 2

# Practical bitwise tricks
print("\n=== Bitwise Tricks ===")

# Check if number is even or odd
num = 7
print(f"Is {num} odd? {bool(num & 1)}")  # True (last bit is 1)

num = 8
print(f"Is {num} odd? {bool(num & 1)}")  # False (last bit is 0)

# Multiply and divide by powers of 2
x = 5
print(f"{x} * 4 = {x << 2}")    # 20 (shift left by 2 = multiply by 4)
print(f"{x} * 8 = {x << 3}")    # 40 (shift left by 3 = multiply by 8)

x = 20
print(f"{x} / 4 = {x >> 2}")    # 5 (shift right by 2 = divide by 4)

# Swap using XOR
a, b = 10, 20
print(f"\nBefore swap: a={a}, b={b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"After XOR swap: a={a}, b={b}")

# Find unique element (all others appear twice)
arr = [2, 3, 5, 3, 2]
result = 0
for num in arr:
    result ^= num
print(f"\nUnique element in {arr}: {result}")  # 5


# ----------------------------------------------------------------------------
# 6. MEMBERSHIP OPERATORS
# ----------------------------------------------------------------------------

print("\n=== Membership Operators ===")

# In string
text = "Hello World"
print(f"'World' in '{text}': {'World' in text}")        # True
print(f"'world' in '{text}': {'world' in text}")        # False (case-sensitive)

# In list
numbers = [1, 2, 3, 4, 5]
print(f"\n3 in {numbers}: {3 in numbers}")              # True
print(f"10 not in {numbers}: {10 not in numbers}")      # True

# In dictionary (checks keys)
person = {"name": "John", "age": 25}
print(f"\n'name' in person: {'name' in person}")        # True
print(f"'John' in person: {'John' in person}")          # False (checks keys, not values)
print(f"'John' in person.values(): {'John' in person.values()}")  # True


# ----------------------------------------------------------------------------
# 7. IDENTITY OPERATORS
# ----------------------------------------------------------------------------

print("\n=== Identity Operators ===")

# Lists
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a")
print(f"\na == b: {a == b}")        # True (same values)
print(f"a is b: {a is b}")          # False (different objects)
print(f"a is c: {a is c}")          # True (same object)

# Memory address
print(f"\nid(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")            # Same as id(a)

# None check (always use 'is' for None)
x = None
print(f"\nx is None: {x is None}")  # True (correct way)
print(f"x == None: {x == None}")    # True (works but not recommended)

# Integer caching
x = 256
y = 256
print(f"\nx = y = 256")
print(f"x is y: {x is y}")          # True (cached)

x = 257
y = 257
print(f"\nx = y = 257")
print(f"x is y: {x is y}")          # May be False (not cached)


# ----------------------------------------------------------------------------
# 8. OPERATOR PRECEDENCE
# ----------------------------------------------------------------------------

print("\n=== Operator Precedence ===")

# Without parentheses
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")      # 14 (not 20)

# With parentheses
result = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result}")    # 20

# Exponentiation is right-associative
result = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {result}")    # 512 (2^9, not 8^2)

result = (2 ** 3) ** 2
print(f"(2 ** 3) ** 2 = {result}")  # 64 (8^2)

# Complex expression
result = 5 + 2 * 3 ** 2 - 8 / 4
print(f"5 + 2 * 3 ** 2 - 8 / 4 = {result}")  # 5 + 18 - 2 = 21.0


# ----------------------------------------------------------------------------
# 9. WALRUS OPERATOR (Python 3.8+)
# ----------------------------------------------------------------------------

print("\n=== Walrus Operator ===")

# Traditional way
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = len(numbers)
if length > 5:
    print(f"List has {length} elements, which is > 5")

# With walrus operator
if (n := len(numbers)) > 5:
    print(f"List has {n} elements, which is > 5 (walrus)")

# In list comprehension
# Get squares of positive numbers, but also use the squares
data = [1, -2, 3, -4, 5]
squares = [sq for x in data if x > 0 and (sq := x ** 2) > 0]
print(f"Squares of positive numbers: {squares}")


# ----------------------------------------------------------------------------
# 10. PRACTICE PROBLEMS
# ----------------------------------------------------------------------------

print("\n=== Practice Problems ===")

# Problem 1: Check if a number is between 10 and 100 (inclusive)
num = 50
is_between = 10 <= num <= 100
print(f"Is {num} between 10 and 100? {is_between}")

# Problem 2: Check if a year is a leap year
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(f"Is {year} a leap year? {is_leap}")

# Problem 3: Get last digit of a number
num = 12345
last_digit = num % 10
print(f"Last digit of {num}: {last_digit}")

# Problem 4: Check if a number is divisible by both 3 and 5
num = 15
divisible = num % 3 == 0 and num % 5 == 0
print(f"Is {num} divisible by 3 and 5? {divisible}")

# Problem 5: Toggle a boolean
flag = True
flag = not flag
print(f"Toggled flag: {flag}")  # False
