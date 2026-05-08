# ============================================
# ADVANCED LESSON 04 — Comprehensions ⚡
# Difficulty: Intermediate
# ============================================
# Comprehensions are a Pythonic way to build collections
# in a single, readable line. Much cleaner than a for loop
# when the logic is simple.
#
# Types:
#   List:   [expression for item in iterable if condition]
#   Dict:   {key: value for item in iterable if condition}
#   Set:    {expression for item in iterable if condition}
#
# Compared to JS:
#   JS:     array.filter(x => x > 0).map(x => x * 2)
#   Python: [x * 2 for x in array if x > 0]
# ============================================

# --- TASK 1 — List Comprehensions ---
# Using list comprehensions (no for loops), create:
#   a) A list of squares for numbers 1-20
#   b) A list of only the odd numbers from 1-50
#   c) A list of words longer than 4 characters from this list:
words = ["cat", "elephant", "dog", "python", "ant", "javascript", "pig"]

# YOUR CODE HERE:


# --- TASK 2 — Dict Comprehensions ---
# Using dict comprehensions, create:
#   a) A dict mapping each number 1-10 to its cube  {1: 1, 2: 8, 3: 27 ...}
#   b) A dict mapping each word in `words` above to its length
#   c) Invert this dict (swap keys and values):
original = {"a": 1, "b": 2, "c": 3}

# YOUR CODE HERE:


# --- TASK 3 — Set Comprehensions ---
# Sets only store unique values — useful for deduplication.
# Using set comprehensions:
#   a) Create a set of the first letters of each word in `words`
#   b) Create a set of even numbers from 1-30

# YOUR CODE HERE:


# --- TASK 4 — Nested Comprehensions ---
# You can nest comprehensions to flatten or transform 2D data.
#
# Example — flatten a 2D list:
#   matrix = [[1,2,3],[4,5,6],[7,8,9]]
#   flat = [num for row in matrix for num in row]
#   → [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Tasks:
#   a) Flatten this matrix into a single list:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   b) Create a 3x3 multiplication table as a 2D list using a nested comprehension
#      Result: [[1,2,3],[2,4,6],[3,6,9]]

# YOUR CODE HERE:


# --- TASK 5 — Refactor Challenge ---
# Rewrite the following for loop as a single list comprehension:
result = []
for x in range(1, 21):
    if x % 2 == 0:
        result.append(x ** 3)

# YOUR ONE-LINER HERE:
