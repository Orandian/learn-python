# ============================================
# PROJECT 01 — Command-Line Calculator 🧮
# Difficulty: Intermediate
# ============================================
# Build a calculator that keeps running until the user types "quit".
#
# Requirements:
#   1. Show a menu: add, subtract, multiply, divide, quit
#   2. Ask the user to pick an operation
#   3. Ask for two numbers
#   4. Show the result
#   5. Keep looping — ask if they want another calculation
#   6. Handle invalid inputs (letters instead of numbers, divide by zero)
#
# Skills used: functions, loops, conditionals, error handling (try/except)
#
# BONUS:
#   - Add a "history" feature that stores all past calculations in a list
#   - Print the history when the user types "history"
#
# Example run:
#   === Calculator ===
#   Operations: add | subtract | multiply | divide | history | quit
#   Choose operation: add
#   Enter first number: 10
#   Enter second number: 5
#   Result: 10 + 5 = 15
# ============================================

# YOUR CODE HERE:
operation_list = ["add", "subtract", "multiply", "divide", "history", "quit"]
history = []


def calculate(a, b, operator="add"):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Cannot divide by zero."


def show_history():
    for i, h in enumerate(history):
        print(f"{i + 1}: {h}\n")


def show_operation_sign(operator):
    if operator == "add":
        return "+"
    elif operator == "subtract":
        return "-"
    elif operator == "multiply":
        return "*"
    else:
        return "/"


while True:
    operation = input(
        "Operations: add | subtract | multiply | divide | history | quit: "
    )
    if operation == "quit":
        break
    elif operation == "history":
        show_history()
    elif operation not in operation_list:
        print("Invalid operation. Please choose from the list.")
    else:
        try:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))
            result = calculate(first_number, second_number, operation)
            result_string = f"{first_number} {show_operation_sign(operation)} {second_number} = {result}"
            print(f"Result: {result_string}")
            history.append(result_string)
        except ValueError:
            print("Something went wrong in your operation")
