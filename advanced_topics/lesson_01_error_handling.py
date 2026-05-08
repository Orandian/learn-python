# ============================================
# ADVANCED LESSON 01 — Error Handling 🛡️
# Difficulty: Intermediate
# ============================================
# Python uses try/except/else/finally to handle errors gracefully.
#
# Structure:
#   try:
#       → code that might fail
#   except SomeError:
#       → runs if that specific error occurs
#   except (TypeError, ValueError):
#       → catch multiple errors at once
#   else:
#       → runs only if NO error occurred
#   finally:
#       → ALWAYS runs, error or not (great for cleanup)
#
# Common built-in exceptions:
#   ValueError      → wrong value type (e.g. int("abc"))
#   TypeError       → wrong type used (e.g. "a" + 1)
#   ZeroDivisionError → divide by zero
#   FileNotFoundError → file doesn't exist
#   KeyError        → dict key doesn't exist
#   IndexError      → list index out of range
# ============================================

# --- TASK 1 ---
# Write a function called safe_divide(a, b) that:
#   - Returns a / b
#   - Catches ZeroDivisionError and returns "Cannot divide by zero"
#   - Catches TypeError and returns "Both arguments must be numbers"
# Test it with: safe_divide(10, 2), safe_divide(10, 0), safe_divide("a", 2)

# YOUR CODE HERE:


# --- TASK 2 ---
# Write a function called read_file(filename) that:
#   - Tries to open and return the contents of the file
#   - Catches FileNotFoundError and returns "File not found"
#   - Uses a finally block to print "Attempted to read: <filename>"
# Test it with a file that exists and one that doesn't.

# YOUR CODE HERE:


# --- TASK 3 — Custom Exceptions ---
# You can create your own exception classes by inheriting from Exception.
#
#   class NegativeAgeError(Exception):
#       pass
#
# Create a custom exception called InvalidScoreError.
# Write a function called set_score(score) that:
#   - Raises InvalidScoreError if score is below 0 or above 100
#   - Returns the score if valid
# Wrap the call in a try/except to catch your custom exception.

# YOUR CODE HERE:


# --- TASK 4 ---
# The else block in try/except runs ONLY when no error occurs.
# Write a function called parse_number(value) that:
#   - Tries to convert value to a float
#   - In the else block, prints "Successfully parsed: <value>"
#   - In the except block, prints "Could not parse: <value>"
# Test with "3.14", "hello", "99"

# YOUR CODE HERE:
