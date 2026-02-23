# ============================================================================
#                  EXCEPTION HANDLING - CODE EXAMPLES
# ============================================================================

# ----------------------------------------------------------------------------
# 1. BASIC TRY-EXCEPT
# ----------------------------------------------------------------------------

print("=== Basic Try-Except ===")

# Division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Invalid conversion
try:
    number = int("hello")
except ValueError:
    print("Error: Cannot convert 'hello' to integer!")

# Index out of range
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError:
    print("Error: Index out of range!")


# ----------------------------------------------------------------------------
# 2. MULTIPLE EXCEPT BLOCKS
# ----------------------------------------------------------------------------

print("\n=== Multiple Except Blocks ===")

def safe_divide(a, b):
    try:
        a = float(a)
        b = float(b)
        result = a / b
        return result
    except ValueError:
        return "Error: Invalid number format"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid type"

print(safe_divide(10, 2))       # 5.0
print(safe_divide("10", "2"))   # 5.0
print(safe_divide(10, 0))       # Error: Cannot divide by zero
print(safe_divide("abc", 2))    # Error: Invalid number format


# ----------------------------------------------------------------------------
# 3. CATCHING MULTIPLE EXCEPTIONS IN ONE BLOCK
# ----------------------------------------------------------------------------

print("\n=== Catching Multiple Exceptions ===")

try:
    # This could raise ValueError or TypeError
    value = int(input if False else "10")  # Simulated input
except (ValueError, TypeError) as e:
    print(f"Error: {e}")


# ----------------------------------------------------------------------------
# 4. GENERIC EXCEPTION HANDLING
# ----------------------------------------------------------------------------

print("\n=== Generic Exception ===")

def risky_operation(data):
    try:
        result = data[0] / data[1]
        return result
    except Exception as e:
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {e}")
        return None

print(risky_operation([10, 2]))    # 5.0
print(risky_operation([10, 0]))    # ZeroDivisionError
print(risky_operation("ab"))       # TypeError


# ----------------------------------------------------------------------------
# 5. ELSE CLAUSE
# ----------------------------------------------------------------------------

print("\n=== Else Clause ===")

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    else:
        print("Division successful!")
        return result
    finally:
        print("Operation complete.\n")

print(f"Result: {divide_numbers(10, 2)}")
print(f"Result: {divide_numbers(10, 0)}")


# ----------------------------------------------------------------------------
# 6. FINALLY CLAUSE
# ----------------------------------------------------------------------------

print("\n=== Finally Clause ===")

def read_file_safely(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
        return None
    finally:
        if file:
            file.close()
            print("File closed.")
        print("Cleanup complete.")

read_file_safely("nonexistent.txt")


# ----------------------------------------------------------------------------
# 7. RAISE STATEMENT
# ----------------------------------------------------------------------------

print("\n=== Raise Statement ===")

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

# Test validation
test_ages = [25, -5, 200, "twenty"]
for age in test_ages:
    try:
        result = validate_age(age)
        print(f"Valid age: {result}")
    except (ValueError, TypeError) as e:
        print(f"Invalid age '{age}': {e}")


# ----------------------------------------------------------------------------
# 8. RE-RAISING EXCEPTIONS
# ----------------------------------------------------------------------------

print("\n=== Re-raising Exceptions ===")

def process_data(data):
    try:
        result = 100 / data
        return result
    except ZeroDivisionError:
        print("Logging: Division by zero attempted")
        raise  # Re-raise the same exception

try:
    process_data(0)
except ZeroDivisionError:
    print("Caught re-raised exception in main code")


# ----------------------------------------------------------------------------
# 9. ASSERT STATEMENT
# ----------------------------------------------------------------------------

print("\n=== Assert Statement ===")

def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), "All elements must be numbers"
    return sum(numbers) / len(numbers)

# Valid case
try:
    print(f"Average: {calculate_average([1, 2, 3, 4, 5])}")
except AssertionError as e:
    print(f"Assertion failed: {e}")

# Invalid case - empty list
try:
    print(f"Average: {calculate_average([])}")
except AssertionError as e:
    print(f"Assertion failed: {e}")


# ----------------------------------------------------------------------------
# 10. CUSTOM EXCEPTIONS
# ----------------------------------------------------------------------------

print("\n=== Custom Exceptions ===")

class ValidationError(Exception):
    """Base class for validation errors"""
    pass

class InvalidEmailError(ValidationError):
    """Raised when email is invalid"""
    def __init__(self, email, message="Invalid email format"):
        self.email = email
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: '{self.email}'"

class InvalidAgeError(ValidationError):
    """Raised when age is invalid"""
    def __init__(self, age, message="Invalid age"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.age}"

def validate_email(email):
    if "@" not in email or "." not in email:
        raise InvalidEmailError(email)
    return True

def validate_user_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    return True

# Test custom exceptions
test_data = [
    ("email", "john@example.com"),
    ("email", "invalid-email"),
    ("age", 25),
    ("age", -5),
]

for field_type, value in test_data:
    try:
        if field_type == "email":
            validate_email(value)
            print(f"Valid email: {value}")
        else:
            validate_user_age(value)
            print(f"Valid age: {value}")
    except ValidationError as e:
        print(f"Validation error: {e}")


# ----------------------------------------------------------------------------
# 11. EXCEPTION CHAINING
# ----------------------------------------------------------------------------

print("\n=== Exception Chaining ===")

def fetch_data():
    raise ConnectionError("Failed to connect to server")

def process_request():
    try:
        fetch_data()
    except ConnectionError as e:
        raise RuntimeError("Request processing failed") from e

try:
    process_request()
except RuntimeError as e:
    print(f"Error: {e}")
    print(f"Caused by: {e.__cause__}")


# ----------------------------------------------------------------------------
# 12. CONTEXT MANAGERS
# ----------------------------------------------------------------------------

print("\n=== Context Managers ===")

# Using with statement for file handling
# with open("test.txt", "w") as f:
#     f.write("Hello, World!")

# Custom context manager
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"Connecting to {self.db_name}...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}...")
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
        return False  # Don't suppress exceptions

    def query(self, sql):
        print(f"Executing: {sql}")
        return "Query results"

# Using custom context manager
with DatabaseConnection("mydb") as db:
    result = db.query("SELECT * FROM users")
    print(f"Result: {result}")


# Context manager with decorator
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"Time elapsed: {elapsed:.4f} seconds")

with timer():
    # Simulate some work
    total = sum(range(100000))
    print(f"Sum: {total}")


# ----------------------------------------------------------------------------
# 13. PRACTICAL EXAMPLES
# ----------------------------------------------------------------------------

print("\n=== Practical Examples ===")

# Example 1: Safe dictionary access
def safe_get(dictionary, key, default=None):
    try:
        return dictionary[key]
    except KeyError:
        return default

data = {"name": "John", "age": 25}
print(f"Name: {safe_get(data, 'name')}")
print(f"Email: {safe_get(data, 'email', 'Not provided')}")


# Example 2: Safe type conversion
def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(f"safe_int('42'): {safe_int('42')}")
print(f"safe_int('abc'): {safe_int('abc')}")
print(f"safe_int(None): {safe_int(None)}")


# Example 3: Retry mechanism
import time

def retry(func, max_attempts=3, delay=1):
    """Retry a function up to max_attempts times"""
    for attempt in range(1, max_attempts + 1):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_attempts:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                raise

# Simulating a flaky function
attempt_count = 0
def flaky_function():
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ConnectionError("Connection failed")
    return "Success!"

try:
    result = retry(flaky_function, max_attempts=3, delay=0.1)
    print(f"Final result: {result}")
except ConnectionError:
    print("All attempts failed")


# Example 4: Input validation with exceptions
def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt) if False else "5")  # Simulated
            if value <= 0:
                raise ValueError("Number must be positive")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")
            break  # For demo purposes

print(f"Positive number: {get_positive_number('Enter positive number: ')}")


print("\n=== Exception Handling Complete ===")
