# ============================================================================
#                       PYTHON STRINGS - CODE EXAMPLES
# ============================================================================

# ----------------------------------------------------------------------------
# 1. STRING CREATION
# ----------------------------------------------------------------------------

print("=== String Creation ===")

# Different ways to create strings
str1 = 'Hello'
str2 = "World"
str3 = '''Multi
line
string'''
str4 = """Another
multi-line"""

print(str1)
print(str3)

# String with quotes inside
quote1 = "It's Python"
quote2 = 'He said "Hello"'
quote3 = "He said \"Hello\""  # Using escape

print(quote1)
print(quote2)


# ----------------------------------------------------------------------------
# 2. STRING INDEXING
# ----------------------------------------------------------------------------

print("\n=== String Indexing ===")

s = "Python"
print(f"String: {s}")
print(f"s[0] = '{s[0]}'")       # P
print(f"s[5] = '{s[5]}'")       # n
print(f"s[-1] = '{s[-1]}'")     # n (last char)
print(f"s[-6] = '{s[-6]}'")     # P (first char)

# Cannot modify (strings are immutable)
# s[0] = 'J'  # This would cause an error!


# ----------------------------------------------------------------------------
# 3. STRING SLICING
# ----------------------------------------------------------------------------

print("\n=== String Slicing ===")

s = "Python Programming"
print(f"String: '{s}'")

print(f"s[0:6] = '{s[0:6]}'")       # Python
print(f"s[7:] = '{s[7:]}'")         # Programming
print(f"s[:6] = '{s[:6]}'")         # Python
print(f"s[-11:] = '{s[-11:]}'")     # Programming
print(f"s[::2] = '{s[::2]}'")       # Pto rgamn
print(f"s[::-1] = '{s[::-1]}'")     # gnimmargorP nohtyP (reverse)

# Copy string
s_copy = s[:]
print(f"Copy: '{s_copy}'")


# ----------------------------------------------------------------------------
# 4. STRING OPERATORS
# ----------------------------------------------------------------------------

print("\n=== String Operators ===")

# Concatenation
first = "Hello"
second = "World"
result = first + " " + second
print(f"Concatenation: {result}")

# Repetition
stars = "*" * 10
print(f"Repetition: {stars}")

# Membership
print(f"'Py' in 'Python': {'Py' in 'Python'}")
print(f"'java' not in 'Python': {'java' not in 'Python'}")

# Comparison
print(f"'apple' < 'banana': {'apple' < 'banana'}")
print(f"'Apple' < 'apple': {'Apple' < 'apple'}")


# ----------------------------------------------------------------------------
# 5. STRING METHODS - CASE
# ----------------------------------------------------------------------------

print("\n=== Case Methods ===")

s = "hello WORLD"
print(f"Original: '{s}'")
print(f"upper(): '{s.upper()}'")
print(f"lower(): '{s.lower()}'")
print(f"capitalize(): '{s.capitalize()}'")
print(f"title(): '{s.title()}'")
print(f"swapcase(): '{s.swapcase()}'")


# ----------------------------------------------------------------------------
# 6. STRING METHODS - SEARCH
# ----------------------------------------------------------------------------

print("\n=== Search Methods ===")

s = "Hello World, Hello Python"
print(f"String: '{s}'")

print(f"find('Hello'): {s.find('Hello')}")       # 0
print(f"find('Java'): {s.find('Java')}")         # -1
print(f"rfind('Hello'): {s.rfind('Hello')}")     # 13
print(f"count('Hello'): {s.count('Hello')}")     # 2
print(f"count('l'): {s.count('l')}")             # 4

print(f"startswith('Hello'): {s.startswith('Hello')}")
print(f"endswith('Python'): {s.endswith('Python')}")


# ----------------------------------------------------------------------------
# 7. STRING METHODS - CHECK
# ----------------------------------------------------------------------------

print("\n=== Check Methods ===")

print(f"'Hello'.isalpha(): {'Hello'.isalpha()}")       # True
print(f"'Hello123'.isalpha(): {'Hello123'.isalpha()}") # False
print(f"'123'.isdigit(): {'123'.isdigit()}")           # True
print(f"'Hello123'.isalnum(): {'Hello123'.isalnum()}") # True
print(f"'   '.isspace(): {'   '.isspace()}")           # True
print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")       # True
print(f"'hello'.islower(): {'hello'.islower()}")       # True


# ----------------------------------------------------------------------------
# 8. STRING METHODS - MODIFICATION
# ----------------------------------------------------------------------------

print("\n=== Modification Methods ===")

s = "Hello World"
print(f"Original: '{s}'")
print(f"replace('World', 'Python'): '{s.replace('World', 'Python')}'")

s = "  Hello World  "
print(f"\nOriginal: '{s}'")
print(f"strip(): '{s.strip()}'")
print(f"lstrip(): '{s.lstrip()}'")
print(f"rstrip(): '{s.rstrip()}'")

print(f"\n'Hi'.center(10, '-'): '{'Hi'.center(10, '-')}'")
print(f"'Hi'.ljust(10, '-'): '{'Hi'.ljust(10, '-')}'")
print(f"'Hi'.rjust(10, '-'): '{'Hi'.rjust(10, '-')}'")
print(f"'42'.zfill(5): '{'42'.zfill(5)}'")


# ----------------------------------------------------------------------------
# 9. SPLIT AND JOIN
# ----------------------------------------------------------------------------

print("\n=== Split and Join ===")

# Split
s = "apple,banana,cherry"
fruits = s.split(",")
print(f"Split '{s}': {fruits}")

s = "Hello World Python"
words = s.split()
print(f"Split on space: {words}")

s = "apple,banana,cherry,date"
parts = s.split(",", 2)  # Max 2 splits
print(f"Split with maxsplit=2: {parts}")

# Join
fruits = ['apple', 'banana', 'cherry']
result = ",".join(fruits)
print(f"Join with ',': '{result}'")

result = " ".join(fruits)
print(f"Join with ' ': '{result}'")

# Splitlines
s = "Line1\nLine2\nLine3"
lines = s.splitlines()
print(f"Splitlines: {lines}")


# ----------------------------------------------------------------------------
# 10. STRING FORMATTING
# ----------------------------------------------------------------------------

print("\n=== String Formatting ===")

name = "Alice"
age = 25
height = 5.6

# f-strings (recommended)
print(f"Name: {name}, Age: {age}")
print(f"Sum: {5 + 3}")
print(f"Upper: {name.upper()}")

# Format specifiers
pi = 3.14159
print(f"Pi: {pi:.2f}")           # 2 decimal places
print(f"Padded: {42:05d}")       # Zero-padded
print(f"Percent: {0.25:.0%}")    # As percentage
print(f"Comma: {1000000:,}")     # Thousand separator

# Alignment
print(f"Left: |{name:<10}|")
print(f"Right: |{name:>10}|")
print(f"Center: |{name:^10}|")

# format() method
print("\nUsing format():")
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# Old style (%)
print("\nUsing % operator:")
print("Name: %s, Age: %d" % (name, age))
print("Float: %.2f" % pi)


# ----------------------------------------------------------------------------
# 11. ESCAPE CHARACTERS
# ----------------------------------------------------------------------------

print("\n=== Escape Characters ===")

print("Hello\nWorld")        # Newline
print("Hello\tWorld")        # Tab
print("Path: C:\\Users\\")   # Backslash
print("He said \"Hi\"")      # Double quote
print('It\'s Python')        # Single quote

# Raw string (ignores escape characters)
print(r"C:\new\folder")      # Prints as-is


# ----------------------------------------------------------------------------
# 12. PRACTICE PROBLEMS
# ----------------------------------------------------------------------------

print("\n=== Practice Problems ===")

# Problem 1: Reverse a string
s = "Python"
reversed_s = s[::-1]
print(f"Reverse of '{s}': '{reversed_s}'")

# Problem 2: Check palindrome
s = "radar"
is_palindrome = s == s[::-1]
print(f"Is '{s}' palindrome? {is_palindrome}")

# Problem 3: Count vowels
s = "Hello World"
vowels = sum(1 for c in s.lower() if c in 'aeiou')
print(f"Vowels in '{s}': {vowels}")

# Problem 4: Remove duplicates (preserve order)
s = "programming"
unique = ''.join(dict.fromkeys(s))
print(f"Remove duplicates from '{s}': '{unique}'")

# Problem 5: Check anagram
s1, s2 = "listen", "silent"
is_anagram = sorted(s1) == sorted(s2)
print(f"Are '{s1}' and '{s2}' anagrams? {is_anagram}")

# Problem 6: Count words
sentence = "Python is a great language"
word_count = len(sentence.split())
print(f"Word count in '{sentence}': {word_count}")

# Problem 7: Find most frequent character
s = "programming"
from collections import Counter
most_common = Counter(s).most_common(1)[0]
print(f"Most frequent char in '{s}': '{most_common[0]}' ({most_common[1]} times)")

# Problem 8: Capitalize first letter of each word (manual)
s = "hello world python"
result = ' '.join(word.capitalize() for word in s.split())
print(f"Capitalize words: '{result}'")

# Problem 9: Check if string contains only digits
s = "12345"
print(f"Is '{s}' all digits? {s.isdigit()}")

# Problem 10: Replace spaces with hyphens
s = "Hello World Python"
result = s.replace(" ", "-")
print(f"Replace spaces: '{result}'")

# Problem 11: Extract numbers from string
s = "abc123def456"
numbers = ''.join(c for c in s if c.isdigit())
print(f"Extract numbers from '{s}': '{numbers}'")

# Problem 12: Check if string is rotation of another
s1, s2 = "abcd", "cdab"
is_rotation = len(s1) == len(s2) and s2 in s1 + s1
print(f"Is '{s2}' rotation of '{s1}'? {is_rotation}")
