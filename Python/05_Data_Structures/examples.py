# ============================================================================
#                   PYTHON DATA STRUCTURES - CODE EXAMPLES
# ============================================================================

# ============================================================================
#                              1. LISTS
# ============================================================================

print("=" * 60)
print("                         LISTS")
print("=" * 60)

# ----------------------------------------------------------------------------
# Creation
# ----------------------------------------------------------------------------
print("\n=== List Creation ===")

numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2]]
empty = []
from_range = list(range(5))

print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"From range: {from_range}")


# ----------------------------------------------------------------------------
# Accessing Elements
# ----------------------------------------------------------------------------
print("\n=== Accessing Elements ===")

lst = [10, 20, 30, 40, 50]
print(f"List: {lst}")
print(f"lst[0]: {lst[0]}")         # 10
print(f"lst[-1]: {lst[-1]}")       # 50
print(f"lst[1:4]: {lst[1:4]}")     # [20, 30, 40]
print(f"lst[::2]: {lst[::2]}")     # [10, 30, 50]
print(f"lst[::-1]: {lst[::-1]}")   # [50, 40, 30, 20, 10]


# ----------------------------------------------------------------------------
# List Methods - Adding
# ----------------------------------------------------------------------------
print("\n=== Adding Elements ===")

lst = [1, 2, 3]
print(f"Original: {lst}")

lst.append(4)
print(f"After append(4): {lst}")

lst.insert(0, 0)
print(f"After insert(0, 0): {lst}")

lst.extend([5, 6])
print(f"After extend([5, 6]): {lst}")

# Using + operator (creates new list)
new_lst = lst + [7, 8]
print(f"Using + [7, 8]: {new_lst}")


# ----------------------------------------------------------------------------
# List Methods - Removing
# ----------------------------------------------------------------------------
print("\n=== Removing Elements ===")

lst = [1, 2, 3, 2, 4, 5]
print(f"Original: {lst}")

lst.remove(2)  # Removes first occurrence
print(f"After remove(2): {lst}")

popped = lst.pop()  # Removes and returns last
print(f"After pop(): {lst}, popped: {popped}")

popped = lst.pop(0)  # Removes and returns at index
print(f"After pop(0): {lst}, popped: {popped}")

del lst[0]  # Delete at index
print(f"After del lst[0]: {lst}")


# ----------------------------------------------------------------------------
# List Methods - Searching and Sorting
# ----------------------------------------------------------------------------
print("\n=== Searching and Sorting ===")

lst = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {lst}")

print(f"index(4): {lst.index(4)}")   # 2
print(f"count(1): {lst.count(1)}")   # 2

lst.sort()
print(f"After sort(): {lst}")

lst.sort(reverse=True)
print(f"After sort(reverse=True): {lst}")

lst.reverse()
print(f"After reverse(): {lst}")

# sorted() returns new list
original = [3, 1, 4, 1, 5]
sorted_lst = sorted(original)
print(f"sorted({original}): {sorted_lst}")


# ----------------------------------------------------------------------------
# List Comprehension
# ----------------------------------------------------------------------------
print("\n=== List Comprehension ===")

# Squares
squares = [x**2 for x in range(6)]
print(f"Squares: {squares}")

# Even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: {evens}")

# Conditional expression
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(f"Labels: {labels}")

# Nested list comprehension (matrix)
matrix = [[i*3 + j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Flatten matrix
flat = [num for row in matrix for num in row]
print(f"Flattened: {flat}")


# ============================================================================
#                              2. TUPLES
# ============================================================================

print("\n" + "=" * 60)
print("                         TUPLES")
print("=" * 60)

# ----------------------------------------------------------------------------
# Creation and Basics
# ----------------------------------------------------------------------------
print("\n=== Tuple Creation ===")

my_tuple = (1, 2, 3, 4, 5)
single = (5,)  # Single element - comma required!
no_parens = 1, 2, 3
from_list = tuple([1, 2, 3])

print(f"Tuple: {my_tuple}")
print(f"Single element: {single}, type: {type(single)}")
print(f"Without parens: {no_parens}")

# Accessing (same as list)
print(f"my_tuple[0]: {my_tuple[0]}")
print(f"my_tuple[-1]: {my_tuple[-1]}")
print(f"my_tuple[1:4]: {my_tuple[1:4]}")


# ----------------------------------------------------------------------------
# Tuple Unpacking
# ----------------------------------------------------------------------------
print("\n=== Tuple Unpacking ===")

# Basic unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")

# Swap values
a, b = 5, 10
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Extended unpacking
first, *rest = (1, 2, 3, 4, 5)
print(f"first={first}, rest={rest}")

first, *middle, last = (1, 2, 3, 4, 5)
print(f"first={first}, middle={middle}, last={last}")

# Unpacking in function return
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

low, high, total = get_stats([1, 2, 3, 4, 5])
print(f"Stats: min={low}, max={high}, sum={total}")


# ============================================================================
#                              3. SETS
# ============================================================================

print("\n" + "=" * 60)
print("                          SETS")
print("=" * 60)

# ----------------------------------------------------------------------------
# Creation and Basics
# ----------------------------------------------------------------------------
print("\n=== Set Creation ===")

my_set = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])  # Duplicates removed
empty = set()  # NOT {}

print(f"Set: {my_set}")
print(f"From list with duplicates: {from_list}")
print(f"Empty set: {empty}")


# ----------------------------------------------------------------------------
# Set Methods
# ----------------------------------------------------------------------------
print("\n=== Set Methods ===")

s = {1, 2, 3}
print(f"Original: {s}")

s.add(4)
print(f"After add(4): {s}")

s.update([5, 6, 7])
print(f"After update([5,6,7]): {s}")

s.remove(7)
print(f"After remove(7): {s}")

s.discard(100)  # No error if not found
print(f"After discard(100): {s}")


# ----------------------------------------------------------------------------
# Set Operations
# ----------------------------------------------------------------------------
print("\n=== Set Operations ===")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(f"A = {A}")
print(f"B = {B}")

print(f"Union (A | B): {A | B}")
print(f"Intersection (A & B): {A & B}")
print(f"Difference (A - B): {A - B}")
print(f"Symmetric Difference (A ^ B): {A ^ B}")

print(f"\n{{1,2}}.issubset({{1,2,3}}): {{1,2}}.issubset({{1,2,3}})")
print(f"Result: {({1,2}.issubset({1,2,3}))}")


# ----------------------------------------------------------------------------
# Practical Set Uses
# ----------------------------------------------------------------------------
print("\n=== Practical Uses ===")

# Remove duplicates from list
lst = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(lst))
print(f"Remove duplicates: {lst} -> {unique}")

# Find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"Common elements: {common}")


# ============================================================================
#                           4. DICTIONARIES
# ============================================================================

print("\n" + "=" * 60)
print("                      DICTIONARIES")
print("=" * 60)

# ----------------------------------------------------------------------------
# Creation and Basics
# ----------------------------------------------------------------------------
print("\n=== Dictionary Creation ===")

person = {"name": "John", "age": 25, "city": "Delhi"}
empty = {}
from_keys = dict.fromkeys(['a', 'b', 'c'], 0)
from_tuples = dict([('x', 1), ('y', 2)])

print(f"Person: {person}")
print(f"From keys: {from_keys}")
print(f"From tuples: {from_tuples}")


# ----------------------------------------------------------------------------
# Accessing Values
# ----------------------------------------------------------------------------
print("\n=== Accessing Values ===")

person = {"name": "John", "age": 25, "city": "Delhi"}

print(f"person['name']: {person['name']}")
print(f"person.get('age'): {person.get('age')}")
print(f"person.get('email', 'N/A'): {person.get('email', 'N/A')}")


# ----------------------------------------------------------------------------
# Dictionary Methods
# ----------------------------------------------------------------------------
print("\n=== Dictionary Methods ===")

person = {"name": "John", "age": 25}
print(f"Original: {person}")

# Adding/Updating
person["email"] = "john@mail.com"
print(f"After adding email: {person}")

person.update({"age": 26, "job": "Developer"})
print(f"After update: {person}")

# Removing
age = person.pop("age")
print(f"After pop('age'): {person}, removed: {age}")

# Keys, Values, Items
print(f"\nKeys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")


# ----------------------------------------------------------------------------
# Iterating Dictionary
# ----------------------------------------------------------------------------
print("\n=== Iterating Dictionary ===")

person = {"name": "John", "age": 25, "city": "Delhi"}

print("Iterating keys:")
for key in person:
    print(f"  {key}")

print("\nIterating values:")
for value in person.values():
    print(f"  {value}")

print("\nIterating key-value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")


# ----------------------------------------------------------------------------
# Dictionary Comprehension
# ----------------------------------------------------------------------------
print("\n=== Dictionary Comprehension ===")

# Squares dictionary
squares = {x: x**2 for x in range(6)}
print(f"Squares: {squares}")

# Filter dictionary
original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {k: v for k, v in original.items() if v > 2}
print(f"Filtered (v > 2): {filtered}")

# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(f"Swapped: {swapped}")


# ============================================================================
#                        PRACTICE PROBLEMS
# ============================================================================

print("\n" + "=" * 60)
print("                   PRACTICE PROBLEMS")
print("=" * 60)

# Problem 1: Merge two lists alternately
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged = [val for pair in zip(list1, list2) for val in pair]
print(f"\n1. Merge alternately: {merged}")

# Problem 2: Find second largest in list
numbers = [10, 20, 4, 45, 99]
unique = list(set(numbers))
unique.sort()
print(f"2. Second largest in {numbers}: {unique[-2]}")

# Problem 3: Count frequency of elements
items = ['a', 'b', 'a', 'c', 'b', 'a']
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1
print(f"3. Frequency count: {freq}")

# Problem 4: Remove duplicates preserving order
lst = [1, 2, 2, 3, 1, 4, 3, 5]
unique = list(dict.fromkeys(lst))
print(f"4. Remove duplicates: {unique}")

# Problem 5: Group items by property
students = [
    {'name': 'Alice', 'grade': 'A'},
    {'name': 'Bob', 'grade': 'B'},
    {'name': 'Charlie', 'grade': 'A'},
    {'name': 'David', 'grade': 'B'},
]
by_grade = {}
for student in students:
    grade = student['grade']
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student['name'])
print(f"5. Group by grade: {by_grade}")

# Problem 6: Find intersection of multiple lists
lists = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
result = set(lists[0])
for lst in lists[1:]:
    result &= set(lst)
print(f"6. Intersection of lists: {list(result)}")

# Problem 7: Sort dictionary by value
d = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_by_value = dict(sorted(d.items(), key=lambda x: x[1]))
print(f"7. Sort by value: {sorted_by_value}")

# Problem 8: Flatten nested list
nested = [[1, 2], [3, 4], [5, [6, 7]]]
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
print(f"8. Flatten nested: {flatten(nested)}")

# Problem 9: Find most common element
lst = [1, 2, 3, 2, 2, 4, 3, 2]
from collections import Counter
most_common = Counter(lst).most_common(1)[0]
print(f"9. Most common in {lst}: {most_common[0]} ({most_common[1]} times)")

# Problem 10: Two sum problem
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9
print(f"10. Two sum {nums}, target={target}: {two_sum(nums, target)}")
