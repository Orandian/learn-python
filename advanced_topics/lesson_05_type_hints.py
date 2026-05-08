# ============================================
# ADVANCED LESSON 05 — Type Hints & Typing 📝
# Difficulty: Intermediate
# ============================================
# Python is dynamically typed, but you can add optional type hints
# to make your code more readable and catch bugs early (like TypeScript).
#
# Basic syntax:
#   def greet(name: str) -> str:
#       return f"Hello, {name}!"
#
#   age: int = 25
#   prices: list[float] = [1.99, 3.50]
#   person: dict[str, str] = {"name": "Yan"}
#
# From the typing module (for older Python / complex types):
#   from typing import Optional, Union, List, Dict, Tuple, Any
#
#   Optional[str]        → str or None
#   Union[int, float]    → either int or float
#   list[int | None]     → list of int or None (Python 3.10+)
#
# Type hints don't enforce types at runtime — they are hints
# for developers and tools like mypy or VS Code IntelliSense.
# ============================================

from typing import Optional, Union

# --- TASK 1 ---
# Add proper type hints to these functions:
# a) A function that takes a name (str) and age (int) and returns a greeting (str)
# b) A function that takes a list of numbers and returns their average (float)
# c) A function that takes a score (int) and returns a letter grade (str)

# YOUR CODE HERE:


# --- TASK 2 — Optional types ---
# Optional[X] means the value can be X or None.
# Write a function called find_user(users, name) where:
#   - users is a list of dicts
#   - name is a str
#   - Returns the matching dict or None if not found
# Add full type hints including Optional return type.

# YOUR CODE HERE:


# --- TASK 3 — Union types ---
# Union[X, Y] means the value can be X or Y.
# Write a function called parse_input(value: Union[str, int]) -> float that:
#   - If value is a string, tries to convert it to float
#   - If value is already an int, converts it to float
#   - Returns the float result

# YOUR CODE HERE:


# --- TASK 4 — Type hint a class ---
# Add type hints to this class. Fill in all the missing hints:

class BankAccount:
    owner: str
    balance: float

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance

# Rewrite the class above with full type hints on all methods.

# YOUR CODE HERE:
