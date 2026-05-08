# ============================================
# ADVANCED LESSON 03 — Generators & Iterators 🔄
# Difficulty: Intermediate / Hard
# ============================================
# A generator is a function that yields values one at a time
# instead of returning all at once. It's memory-efficient for
# large sequences because it only computes values when needed.
#
#   def count_up(n):
#       for i in range(n):
#           yield i        # pauses here, resumes on next()
#
#   gen = count_up(3)
#   print(next(gen))  → 0
#   print(next(gen))  → 1
#   print(next(gen))  → 2
#
# You can also loop over a generator with for:
#   for num in count_up(5):
#       print(num)
#
# Generator expressions (like list comprehensions but lazy):
#   squares = (x**2 for x in range(10))  ← uses () not []
# ============================================

# --- TASK 1 ---
# Write a generator function called fibonacci() that yields
# Fibonacci numbers indefinitely (no limit).
# Use it to print the first 10 Fibonacci numbers.
# Hint: keep track of two previous values and yield the next.

# YOUR CODE HERE:


# --- TASK 2 ---
# Write a generator function called read_in_chunks(filename, chunk_size)
# that reads a text file and yields it line by line in groups of chunk_size.
# Example: chunk_size=2 → yields 2 lines at a time as a list.
# Test it by creating a sample text file first.

# YOUR CODE HERE:


# --- TASK 3 ---
# Generator expressions vs list comprehensions:
#   List:      [x**2 for x in range(1000000)]  → creates all in memory
#   Generator: (x**2 for x in range(1000000))  → lazy, one at a time
#
# Use the time module to compare how long it takes to:
#   a) Create a list of squares for numbers 1 to 1,000,000
#   b) Create a generator of squares for numbers 1 to 1,000,000
# Print the time difference and the memory benefit.

# YOUR CODE HERE:


# --- TASK 4 — Custom Iterator ---
# You can make any class iterable by implementing __iter__ and __next__.
#
# Create a class called Countdown that:
#   - Takes a start number in __init__
#   - __iter__ returns self
#   - __next__ decrements and returns the current number
#   - Raises StopIteration when it reaches 0
#
# Use it in a for loop: for n in Countdown(5): print(n)

# YOUR CODE HERE:
