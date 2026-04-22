# ============================================
# LESSON 02 — Conditionals (if / elif / else)
# ============================================
# Key difference from JS/PHP/Java:
#   - No parentheses required around condition
#   - No curly braces — use a colon + indentation
#   - "elif" instead of "else if"
#
# Python:          JS/Java equivalent:
#   if x > 10:       if (x > 10) {
#       print("big")     console.log("big")
#   elif x > 5:      } else if (x > 5) {
#       print("mid")     console.log("mid")
#   else:            } else {
#       print("small")   console.log("small")
#                    }
# ============================================

# --- TASK 1 ---
# Write a program that asks the user for their age using input()
# Then print:
#   - "Child" if age < 13
#   - "Teenager" if 13 <= age < 18
#   - "Adult" if age >= 18
# Note: input() returns a string, convert it with int()  e.g. int(input("Age: "))

# YOUR CODE HERE:
age = int(input("Age: "))
if age < 13:
    print("Child")
elif age < 18 and age >= 13:
    print("Teenager")
else:
    print("Adult")

# --- TASK 2 ---
# FizzBuzz (classic!) — for a number entered by the user:
#   - Print "Fizz" if divisible by 3
#   - Print "Buzz" if divisible by 5
#   - Print "FizzBuzz" if divisible by both
#   - Otherwise print the number itself
# Hint: use the modulo operator %

# YOUR CODE HERE:
num = int(input("Number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

# --- TASK 3 ---
# Python has a shorthand one-liner conditional (like JS ternary operator):
#   JS:     let label = x > 0 ? "positive" : "negative"
#   Python: label = "positive" if x > 0 else "negative"
#
# Use this to assign "Pass" or "Fail" based on a score variable, then print it.

# YOUR CODE HERE:
score = int(input("Score: "))
result = "Pass" if score >= 50 else "Fail"
print(result)
