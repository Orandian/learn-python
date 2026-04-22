# ============================================
# PROJECT 03 — Contact Book 📒
# Difficulty: Intermediate / Hard
# ============================================
# Build a contact book that stores contacts as JSON and supports
# full CRUD operations (Create, Read, Update, Delete).
#
# Requirements:
#   1. Store contacts in a "contacts.json" file
#   2. Each contact has: name, phone, email
#   3. Menu options: add, search, update, delete, list all, quit
#   4. "add"     → collect name, phone, email and save
#   5. "search"  → search by name (partial match OK) and display result
#   6. "update"  → find a contact by name, allow editing phone or email
#   7. "delete"  → find by name and remove
#   8. "list"    → display all contacts in a neat format
#
# Skills used: dicts, lists, file I/O, JSON, functions, loops
#
# Hint — working with JSON:
#   import json
#   # Save:  json.dump(data, f, indent=2)
#   # Load:  data = json.load(f)
#
# BONUS:
#   - Sort contacts alphabetically when listing
#   - Validate phone number (must be digits only, 7-15 chars)
#   - Validate email format (must contain @ and .)
#
# Example run:
#   === Contact Book ===
#   Options: add | search | update | delete | list | quit
#   Choose: search
#   Search name: yan
#   Found: Yan Naing Htwe | 09123456789 | yan@email.com
# ============================================

# YOUR CODE HERE:
