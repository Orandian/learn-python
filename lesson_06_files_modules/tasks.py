# ============================================
# LESSON 06 — Files & Modules
# ============================================
# Reading/writing files in Python is simple.
# Always use "with open(...)" — it auto-closes the file.
#
#   with open("file.txt", "r") as f:   # r=read, w=write, a=append
#       content = f.read()
#
# Importing modules:
#   import math
#   from datetime import datetime
# ============================================

# --- TASK 1: Write to a file ---
# Write a program that creates a file called "my_notes.txt"
# and writes 3 lines of text into it (anything you like).

# YOUR CODE HERE:
with open("my_notes.txt", "w") as f:
    f.write("Line 1: This is my first note.\n")
    f.write("Line 2: Python is great for file handling.\n")
    f.write("Line 3: I am learning a lot!\n")

# --- TASK 2: Read from a file ---
# Read the "my_notes.txt" file you just created and print each line.
# Hint: use f.readlines() to get a list of lines.

# YOUR CODE HERE:
with open("my_notes.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())  # Print each line without extra newlines

# --- TASK 3: Append to a file ---
# Open "my_notes.txt" in append mode and add one more line.
# Then read and print the full file to confirm.

# YOUR CODE HERE:
with open("my_notes.txt", "a") as f:
    f.write("Line 4: This is my fourth note.\n")

with open("my_notes.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())  # Print each line without extra newlines

# --- TASK 4: Use the math module ---
# Import the math module and use it to:
# - Print the square root of 144
# - Print the value of pi
# - Round 4.7 up using math.ceil()

# YOUR CODE HERE:
import math

print(math.sqrt(144))  # Square root of 144
print(math.pi)  # Value of pi
print(math.ceil(4.7))  # Round 4.7 up

# --- TASK 5: Use the datetime module ---
# from datetime import datetime
# Print today's date and time using datetime.now()

# YOUR CODE HERE:
import datetime

print(datetime.datetime.now())  # Print today's date and time
