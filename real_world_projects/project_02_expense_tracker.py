# ============================================
# REAL-WORLD PROJECT 02 — Expense Tracker 💰
# Difficulty: Intermediate
# ============================================
# Build a personal expense tracker that logs, categorises,
# and summarises your spending — saved to a CSV file.
#
# Requirements:
#   1. Menu options: add, view, summary, delete, quit
#   2. "add"     → ask for: amount, category, description, date (default today)
#   3. "view"    → display all expenses in a table format
#   4. "summary" → show:
#                   - Total spent
#                   - Total per category
#                   - Most expensive single expense
#                   - Average expense
#   5. "delete"  → remove an expense by its ID
#   6. Save/load all data to "expenses.csv" using the csv module
#
# Categories: food, transport, entertainment, health, shopping, other
#
# Skills used: csv module, datetime, dicts, lists, functions, loops
#
# Setup: no extra libraries needed — csv and datetime are built-in
#
# BONUS:
#   - Filter view by category or date range
#   - Set a monthly budget and warn when exceeded
#   - Export a summary report to a .txt file
#
# Hint — working with CSV:
#   import csv
#   # Write:
#   with open("expenses.csv", "a", newline="") as f:
#       writer = csv.DictWriter(f, fieldnames=["id","amount","category","description","date"])
#       writer.writerow({"id": 1, "amount": 9.99, ...})
#   # Read:
#   with open("expenses.csv", "r") as f:
#       reader = csv.DictReader(f)
#       for row in reader:
#           print(row)
#
# Example output:
#   === Expense Summary ===
#   Total spent     : $245.30
#   Food            : $89.50
#   Transport       : $45.00
#   Entertainment   : $110.80
#   Most expensive  : $75.00 — Concert tickets (entertainment)
#   Average expense : $35.04
# ============================================

import csv
import os
from datetime import date

CATEGORIES = ["food", "transport", "entertainment", "health", "shopping", "other"]
CSV_FILE = "expenses.csv"
FIELDNAMES = ["id", "amount", "category", "description", "date"]


# YOUR CODE HERE:
