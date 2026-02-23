# ============================================================================
#                    PYTHON CONTROL FLOW - CODE EXAMPLES
# ============================================================================

# ----------------------------------------------------------------------------
# 1. IF-ELIF-ELSE STATEMENTS
# ----------------------------------------------------------------------------

print("=== If-Elif-Else ===")

age = 20

# Simple if
if age >= 18:
    print("You are an adult")

# if-else
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")  # This prints

# if-elif-else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")


# ----------------------------------------------------------------------------
# 2. NESTED IF STATEMENTS
# ----------------------------------------------------------------------------

print("\n=== Nested If ===")

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")

# Better way - combine conditions
if age >= 18 and has_license:
    print("You can drive")


# ----------------------------------------------------------------------------
# 3. TERNARY OPERATOR
# ----------------------------------------------------------------------------

print("\n=== Ternary Operator ===")

age = 20

# Traditional way
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Ternary way (one line)
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Practical examples
number = 7
result = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {result}")

# Ternary with function calls
x = 10
y = 20
max_val = x if x > y else y
print(f"Max of {x} and {y}: {max_val}")


# ----------------------------------------------------------------------------
# 4. TRUTHY AND FALSY VALUES
# ----------------------------------------------------------------------------

print("\n=== Truthy and Falsy ===")

# Falsy values
falsy_values = [False, None, 0, 0.0, "", [], {}, set()]

for val in falsy_values:
    if not val:
        print(f"{repr(val)} is Falsy")

# Practical use
name = ""
display_name = name if name else "Anonymous"
print(f"Display name: {display_name}")

# Check if list has elements
my_list = [1, 2, 3]
if my_list:  # Better than if len(my_list) > 0
    print("List is not empty")


# ----------------------------------------------------------------------------
# 5. FOR LOOP
# ----------------------------------------------------------------------------

print("\n=== For Loop ===")

# Iterate over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate over string
print("\nCharacters in 'Python':")
for char in "Python":
    print(char, end=" ")
print()

# Iterate over range
print("\nNumbers 0-4:")
for i in range(5):
    print(i, end=" ")
print()

# Range with start and stop
print("\nNumbers 1-5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# Range with step
print("\nEven numbers 0-10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# Reverse iteration
print("\nCountdown 5-1:")
for i in range(5, 0, -1):
    print(i, end=" ")
print()


# ----------------------------------------------------------------------------
# 6. WHILE LOOP
# ----------------------------------------------------------------------------

print("\n=== While Loop ===")

# Count from 1 to 5
count = 1
while count <= 5:
    print(count, end=" ")
    count += 1
print()

# Sum until condition
total = 0
num = 1
while total < 100:
    total += num
    num += 1
print(f"Sum exceeded 100 at: {total}, last number added: {num-1}")

# While with user input (commented to avoid blocking)
# while True:
#     user_input = input("Enter 'quit' to exit: ")
#     if user_input.lower() == 'quit':
#         break
#     print(f"You entered: {user_input}")


# ----------------------------------------------------------------------------
# 7. BREAK STATEMENT
# ----------------------------------------------------------------------------

print("\n=== Break Statement ===")

# Find first even number
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break

# Search for element
target = 5
found = False
for i, num in enumerate([1, 3, 5, 7, 9]):
    if num == target:
        print(f"Found {target} at index {i}")
        found = True
        break
if not found:
    print(f"{target} not found")


# ----------------------------------------------------------------------------
# 8. CONTINUE STATEMENT
# ----------------------------------------------------------------------------

print("\n=== Continue Statement ===")

# Print only odd numbers
print("Odd numbers from 0-9:")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i, end=" ")
print()

# Skip negative numbers
numbers = [1, -2, 3, -4, 5]
positive_sum = 0
for num in numbers:
    if num < 0:
        continue
    positive_sum += num
print(f"Sum of positive numbers: {positive_sum}")


# ----------------------------------------------------------------------------
# 9. PASS STATEMENT
# ----------------------------------------------------------------------------

print("\n=== Pass Statement ===")

# Empty function placeholder
def future_function():
    pass  # TODO: Implement later

# Empty class placeholder
class FutureClass:
    pass

# In conditional
x = 10
if x > 5:
    pass  # Placeholder for future code
else:
    print("x is small")

print("Pass allows empty code blocks")


# ----------------------------------------------------------------------------
# 10. ELSE WITH LOOPS
# ----------------------------------------------------------------------------

print("\n=== Else with Loops ===")

# For-else (else runs if no break)
print("Searching for 10 in [1,2,3,4,5]:")
for num in [1, 2, 3, 4, 5]:
    if num == 10:
        print("Found!")
        break
else:
    print("Not found (else executed)")

# For-else with break
print("\nSearching for 3 in [1,2,3,4,5]:")
for num in [1, 2, 3, 4, 5]:
    if num == 3:
        print("Found!")
        break
else:
    print("Not found")  # This won't print

# Practical use: Check if number is prime
num = 17
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print(f"{num} is not prime")
        break
else:
    print(f"{num} is prime")


# ----------------------------------------------------------------------------
# 11. ENUMERATE()
# ----------------------------------------------------------------------------

print("\n=== Enumerate ===")

fruits = ["apple", "banana", "cherry"]

# Without enumerate (not Pythonic)
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (Pythonic)
print("\nWith enumerate:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Start from 1
print("\nStart from 1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")


# ----------------------------------------------------------------------------
# 12. ZIP()
# ----------------------------------------------------------------------------

print("\n=== Zip ===")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Iterate over two lists together
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Zip with three lists
cities = ["NYC", "LA", "Chicago"]
print("\nWith three lists:")
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")

# Unequal length lists (stops at shortest)
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
print("\nUnequal lists:")
for a, b in zip(list1, list2):
    print(a, b)  # Only prints 3 pairs


# ----------------------------------------------------------------------------
# 13. NESTED LOOPS
# ----------------------------------------------------------------------------

print("\n=== Nested Loops ===")

# Multiplication table
print("Multiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="\t")
    print()

# Print pattern - right triangle
print("\nRight triangle pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Print pattern - pyramid
print("\nPyramid pattern:")
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# ----------------------------------------------------------------------------
# 14. PRACTICE PROBLEMS
# ----------------------------------------------------------------------------

print("\n=== Practice Problems ===")

# Problem 1: Sum of digits
num = 12345
digit_sum = 0
while num > 0:
    digit_sum += num % 10
    num //= 10
print(f"Sum of digits of 12345: {digit_sum}")

# Problem 2: Reverse a number
num = 12345
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(f"Reverse of 12345: {reversed_num}")

# Problem 3: Factorial using loop
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n}: {factorial}")

# Problem 4: Fibonacci series
n = 10
a, b = 0, 1
print(f"First {n} Fibonacci numbers:", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# Problem 5: Check if palindrome
string = "radar"
is_palindrome = True
for i in range(len(string) // 2):
    if string[i] != string[-(i + 1)]:
        is_palindrome = False
        break
print(f"Is '{string}' palindrome? {is_palindrome}")

# Problem 6: Find GCD using loop
a, b = 48, 18
while b:
    a, b = b, a % b
print(f"GCD of 48 and 18: {a}")

# Problem 7: Print prime numbers up to n
n = 30
print(f"Prime numbers up to {n}:", end=" ")
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()
