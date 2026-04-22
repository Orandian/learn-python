# ============================================
# LESSON 04 — Data Structures
# ============================================
# Python has 4 key built-in collections:
#   list    → ordered, mutable       [1, 2, 3]
#   tuple   → ordered, immutable     (1, 2, 3)
#   dict    → key-value pairs        {"name": "Yan"}  (like JS objects / PHP arrays)
#   set     → unique values only     {1, 2, 3}
# ============================================

# --- TASK 1: Lists ---
# Create a list of 5 fruits.
# - Print the first and last item
# - Add a new fruit using .append()
# - Remove one using .remove()
# - Sort the list using .sort()

# YOUR CODE HERE:
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0])  # First item
print(fruits[-1])  # Last item
fruits.append("fig")  # Add a new fruit
fruits.remove("banana")  # Remove one fruit
print(fruits)  # Print the list after modifications``
fruits.sort()  # Sort the list
print(fruits)  # Print the sorted list

# --- TASK 2: Dictionary ---
# Create a dict representing a person with keys: name, age, language, is_learning
# - Print each key-value pair using a for loop
# - Add a new key "country" to the dict
# - Check if "email" key exists using the `in` keyword

# YOUR CODE HERE:
person = {"name": "Alice", "age": 30, "language": "Python", "is_learning": True}

for key, value in person.items():
    print(f"{key}: {value}")

person["country"] = "USA"  # Add a new key
print(f"Country: {person['country']}")

if "email" in person:
    print(f"Email: {person['email']}")
else:
    print("Email not found.")

# --- TASK 3: Tuple ---
# Tuples are like lists but cannot be changed after creation (immutable).
# Create a tuple of 3 coordinates (x, y, z).
# Unpack them into separate variables and print each.
# e.g. x, y, z = my_tuple

# YOUR CODE HERE:
coordinates = (10, 20, 30)
x, y, z = coordinates  # Unpack the tuple
print(f"x: {x}, y: {y}, z: {z}")

# --- TASK 4: Set ---
# Sets automatically remove duplicates.
# Create a list with some duplicate numbers, convert it to a set, and print it.
# e.g. numbers = [1, 2, 2, 3, 3, 3, 4]  → set: {1, 2, 3, 4}

# YOUR CODE HERE:
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers)  # Convert list to set to remove duplicates
print(unique_numbers)  # Print the set of unique numbers
