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

# List of valid operations the user can choose from
operation_list = ["add", "subtract", "multiply", "divide", "history", "quit"]

# Stores all past calculations as formatted strings
history = []


def calculate(a, b, operator="add"):
    """Perform arithmetic based on the given operator. Returns the result or an error message."""
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        # Guard against division by zero
        if b != 0:
            return a / b
        else:
            return "Error: Cannot divide by zero."


def show_history():
    """Print all past calculations with their index numbers."""
    for i, h in enumerate(history):
        print(f"{i + 1}: {h}\n")


def show_operation_sign(operator):
    """Return the symbol for a given operation name (e.g. 'add' → '+')."""
    if operator == "add":
        return "+"
    elif operator == "subtract":
        return "-"
    elif operator == "multiply":
        return "*"
    else:
        return "/"


# Main loop — keeps the calculator running until the user types "quit"
while True:
    operation = input(
        "Operations: add | subtract | multiply | divide | history | quit: "
    )

    if operation == "quit":
        # Exit the program
        break
    elif operation == "history":
        # Show all previous calculations
        show_history()
    elif operation not in operation_list:
        # Handle unrecognised operation
        print("Invalid operation. Please choose from the list.")
    else:
        try:
            # Get two numbers from the user (float supports decimals)
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))

            # Calculate the result and format it for display
            result = calculate(first_number, second_number, operation)
            result_string = f"{first_number} {show_operation_sign(operation)} {second_number} = {result}"

            print(f"Result: {result_string}")

            # Save this calculation to history
            history.append(result_string)
        except ValueError:
            # Triggered when user types letters instead of numbers
            print("Something went wrong in your operation")
