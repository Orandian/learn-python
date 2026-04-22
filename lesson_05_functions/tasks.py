# ============================================
# LESSON 05 — Functions
# ============================================
# Python uses "def" to define functions (no function keyword like JS/PHP)
#
#   JS:     function greet(name) { return "Hello " + name; }
#   PHP:    function greet($name) { return "Hello " . $name; }
#   Python: def greet(name):
#               return "Hello " + name
#
# Default parameters (like JS):
#   def greet(name="World"):
#       return f"Hello, {name}!"
# ============================================

# --- TASK 1 ---
# Write a function called greet(name) that returns "Hello, <name>!"
# Call it with your own name and print the result.

# YOUR CODE HERE:
def greet(name):
    return f"Hello, {name}!"


print(greet("Yan Naing Htwe"))  # Example call with the name "Alice"

# --- TASK 2 ---
# Write a function called calculate(a, b, operation="add") that:
#   - Adds a + b if operation is "add"
#   - Subtracts a - b if operation is "subtract"
#   - Multiplies a * b if operation is "multiply"
#   - Divides a / b if operation is "divide" (handle divide by zero!)
# Test it with a few different calls.


# YOUR CODE HERE:
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Cannot divide by zero."
    else:
        return "Error: Invalid operation."


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

while operation not in ["add", "subtract", "multiply", "divide"]:
    print("Invalid operation. Please enter add, subtract, multiply, or divide.")
    operation = input("Enter operation (add, subtract, multiply, divide): ")
print(calculate(number1, number2, operation))  # Use the specified operation


# --- TASK 3 ---
# *args — accepts any number of arguments (like JS rest params ...args)
# Write a function called total(*numbers) that returns the sum of all numbers passed.
# e.g. total(1, 2, 3, 4) → 10


# YOUR CODE HERE:
def total(*numbers):
    return sum(numbers)


print(total(1, 2, 3, 4))  # Example call that should return 10

# --- TASK 4 ---
# Lambda functions — like JS arrow functions, for short one-liners
#   JS:     const double = (x) => x * 2
#   Python: double = lambda x: x * 2
#
# Create a lambda that squares a number, and use it with the map() function
# to square every number in a list: [1, 2, 3, 4, 5]

# YOUR CODE HERE:
square = lambda x: x * x  # Lambda function to square a number
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Should print [1, 4, 9, 16, 25]
