# ============================================
# PROJECT 02 — To-Do List App 📝
# Difficulty: Intermediate
# ============================================
# Build a to-do list that saves tasks to a file so they persist
# between runs of the program.
#
# Requirements:
#   1. On startup, load existing tasks from "todos.txt" (if it exists)
#   2. Show a menu: add, view, complete, delete, quit
#   3. "add"      → ask for a task name, add it with status "pending"
#   4. "view"     → show all tasks with their number and status
#   5. "complete" → ask for task number, mark it as "done ✓"
#   6. "delete"   → ask for task number, remove it from the list
#   7. "quit"     → save all tasks to "todos.txt" and exit
#
# Skills used: lists, dicts, loops, file I/O, functions
#
# BONUS:
#   - Save/load tasks using JSON instead of plain text (import json)
#   - Add a "priority" field (high / medium / low) when adding a task
#   - Filter view by status: show only pending or only done tasks
#
# Example run:
#   === To-Do List ===
#   1. [ ] Buy groceries
#   2. [✓] Learn Python
#   Choose: complete
#   Task number: 1
#   "Buy groceries" marked as done!
# ============================================

import json
import os

# Valid menu operations
operation_list = ["add", "view", "complete", "delete", "quit", "view by filter"]

# Valid priority levels for tasks
priority_list = ["high", "medium", "low"]


def show_todos():
    """Display all tasks with their index, completion status, and priority."""
    print("=== To-Do List ===")
    with open("todos.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    for index, item in enumerate(data):
        # Show ✓ if complete, otherwise show empty space
        mark = "✓" if item["status"] == "complete" else " "
        print(f"{index + 1}. [{mark}] {item['task']} ({item['priority']})")


def show_todos_by_filter():
    """Display tasks filtered by status or priority."""
    with open("todos.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    choice = input("Filter by (status/priority): ").lower()

    if choice == "status":
        status = input("Enter status (complete/incomplete): ").lower()
        # Keep only tasks matching the chosen status
        filtered = [item for item in data if item["status"] == status]

    elif choice == "priority":
        priority = input("Enter priority (high/medium/low): ").lower()
        # Keep only tasks matching the chosen priority
        filtered = [item for item in data if item["priority"] == priority]

    else:
        print("Invalid filter type")
        return

    print("=== Filtered To-Do List ===")
    for index, item in enumerate(filtered):
        mark = "✓" if item["status"] == "complete" else " "
        print(f"{index + 1}. [{mark}] {item['task']} ({item['priority']})")


def add_new_todo():
    """Ask the user for a task and priority, then save it to todos.json."""
    new_note = input("What's your task: ")
    priority = input("Choose priority (high / medium / low): ")

    # Validate priority before saving
    if priority not in priority_list:
        print("Choose from the priority list (high / medium / low)")
        return

    # Build the task object
    new_note_json = {"task": new_note, "status": "incomplete", "priority": priority}

    with open("todos.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    # Append new task and save back to file
    data.append(new_note_json)
    with open("todos.json", "w") as f:
        json.dump(data, f, indent=4)


def complete_task():
    """Mark a task as complete by its displayed number."""
    try:
        # Subtract 1 to convert from display number (1-based) to list index (0-based)
        task_number = int(input("Task number: ")) - 1

        with open("todos.json", "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

        if 0 <= task_number < len(data):
            data[task_number]["status"] = "complete"
        else:
            print("Invalid task number")
            return

        with open("todos.json", "w") as f:
            json.dump(data, f, indent=4)

        print(f'"{data[task_number]["task"]}" marked as done!')
    except ValueError:
        # Triggered when user types letters instead of a number
        print("Something went wrong in your operation")


def delete_task():
    """Remove a task permanently by its displayed number."""
    try:
        # Subtract 1 to convert from display number (1-based) to list index (0-based)
        task_number = int(input("Task number you want to delete: ")) - 1

        with open("todos.json", "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

        if 0 <= task_number < len(data):
            # pop() removes and returns the item at the given index
            removed_task = data.pop(task_number)
        else:
            print("Invalid task number")
            return

        with open("todos.json", "w") as f:
            json.dump(data, f, indent=4)

        print(f'"{removed_task["task"]}" deleted!')
    except ValueError:
        # Triggered when user types letters instead of a number
        print("Something went wrong in your operation")


# Create todos.json with an empty list if it doesn't exist yet
if not os.path.exists("todos.json"):
    with open("todos.json", "w") as f:
        json.dump([], f)


# Main loop — keeps the app running until the user types "quit"
while True:
    operator = input("Choose: (quit, add, view, complete, delete, view by filter)")

    if operator == "quit":
        break
    elif operator == "add":
        add_new_todo()
    elif operator == "view":
        show_todos()
    elif operator == "complete":
        complete_task()
    elif operator == "delete":
        delete_task()
    elif operator == "view by filter":
        show_todos_by_filter()
    else:
        # Handle any unrecognised input
        print(
            "Invalid option. Choose: quit, add, view, complete, delete, view by filter"
        )
