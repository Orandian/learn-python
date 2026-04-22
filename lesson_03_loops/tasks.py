# ============================================
# LESSON 03 — Loops (for / while)
# ============================================
# Python's for loop is like JS "for...of" — it iterates over items directly.
#   JS:     for (let i of [1,2,3]) { ... }
#   Python: for i in [1, 2, 3]:  ...
#
# To loop with an index, use range():
#   for i in range(5):       → 0, 1, 2, 3, 4
#   for i in range(1, 6):    → 1, 2, 3, 4, 5
#   for i in range(0, 10, 2):→ 0, 2, 4, 6, 8
# ============================================

# --- TASK 1 ---
# Use a for loop with range() to print numbers 1 to 10.
# Then modify it to print only even numbers between 1 and 20.

# YOUR CODE HERE:
for i in range(1, 11):
    print(i)

for i in range(2, 21, 2):
    print(i)

# --- TASK 2 ---
# Loop over this list of languages and print each one:
languages = ["Python", "JavaScript", "PHP", "Java"]
# Bonus: also print the index using enumerate()
# e.g. "0: Python", "1: JavaScript" ...

# YOUR CODE HERE:
for index, lang in enumerate(languages):
    print(f"{index}: {lang}")

# --- TASK 3 ---
# While loop — guess the number game:
# Set a secret number (e.g. secret = 7)
# Use a while loop to keep asking the user to guess until they get it right.
# Print "Too high!", "Too low!", or "Correct!" accordingly.

# YOUR CODE HERE:
secret = 7
while True:
    guess = int(input("Guess the number: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")
        break

# --- TASK 4 ---
# List comprehension — Python's superpower!
# It's like a one-line for loop that builds a list.
#   squares = [x**2 for x in range(1, 6)]  → [1, 4, 9, 16, 25]
#
# Create a list of all even numbers from 1 to 20 using a list comprehension.

# YOUR CODE HERE:
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)
