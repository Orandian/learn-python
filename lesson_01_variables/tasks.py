# ============================================
# LESSON 01 — Variables & Data Types
# ============================================
# Coming from JS/PHP/Java? Here are the key differences:
#   - No var/let/const or $  → just write: name = "value"
#   - No semicolons needed
#   - True/False (capital T/F), None (instead of null)
# ============================================

# --- TASK 1 ---
# Create variables for: your name, age, favourite language, and is_learning (True/False)
# Then print them all using an f-string.
# Example output: "Hi, I'm Yan, I'm 25 years old, I love Java, and learning Python: True"

# YOUR CODE HERE:
name = "Yan"
age = 25
favourite_language = "Java"
is_learning = True

print(
    f"Hi, I'm {name}, I'm {age} years old, I love {favourite_language}, and learning Python: {is_learning}"
)

# --- TASK 2 ---
# Python has these built-in types: str, int, float, bool, None
# Use the type() function to print the type of each variable you created above.
# Example: print(type(name))  → <class 'str'>

# YOUR CODE HERE:
print(type(name))

# --- TASK 3 ---
# String operations — try these:
# 1. Convert your name to uppercase using .upper()
# 2. Get the length of your name using len()
# 3. Repeat your name 3 times using *  e.g. "Yan" * 3

# YOUR CODE HERE:
print(name.upper())
print(len(name))
print(name * 3)

# --- BONUS ---
# In Python, you can swap two variables in one line (no temp variable needed!)
# a = 5
# b = 10
# a, b = b, a   ← try this and print a and b after the swap

# YOUR CODE HERE:
a = 5
b = 10
a, b = b, a
print(a)  # Should print 10
print(b)  # Should print 5
