# ============================================
# ADVANCED LESSON 02 — Decorators 🎨
# Difficulty: Intermediate / Hard
# ============================================
# A decorator is a function that wraps another function to add
# extra behaviour — without modifying the original function.
#
# Basic structure:
#   def my_decorator(func):
#       def wrapper(*args, **kwargs):
#           print("Before the function")
#           result = func(*args, **kwargs)   # call the original
#           print("After the function")
#           return result
#       return wrapper
#
#   @my_decorator          ← syntactic sugar for: greet = my_decorator(greet)
#   def greet(name):
#       print(f"Hello, {name}!")
#
# Coming from JS? Decorators are similar to higher-order functions
# or middleware — wrapping a function to add behaviour.
# ============================================

# --- TASK 1 ---
# Create a decorator called logger that:
#   - Prints "Calling: <function name>" before the function runs
#   - Prints "Finished: <function name>" after it runs
# Apply it to a simple function called add(a, b) that returns a + b.
# Hint: use func.__name__ to get the function's name.

# YOUR CODE HERE:


# --- TASK 2 ---
# Create a decorator called timer that:
#   - Records the time before and after the function runs (use time module)
#   - Prints "Execution time: <X> seconds"
# Apply it to a function called slow_task() that uses time.sleep(1).

# YOUR CODE HERE:


# --- TASK 3 ---
# Create a decorator called repeat(n) that runs the decorated function n times.
# This is a decorator with an argument — it needs an extra outer function:
#
#   def repeat(n):
#       def decorator(func):
#           def wrapper(*args, **kwargs):
#               for _ in range(n):
#                   func(*args, **kwargs)
#           return wrapper
#       return decorator
#
#   @repeat(3)
#   def say_hello():
#       print("Hello!")
#
# Create your own function and apply @repeat(4) to it.

# YOUR CODE HERE:


# --- TASK 4 ---
# Create a decorator called require_positive that:
#   - Checks if ALL arguments passed to the function are positive numbers
#   - If not, prints "Error: all arguments must be positive" and returns None
#   - Otherwise calls the function normally
# Apply it to a function called multiply(a, b) that returns a * b.

# YOUR CODE HERE:
