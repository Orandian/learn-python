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

import json
import os


def load_contacts():
    """Load and return all contacts from contacts.json. Returns empty list if file is missing or corrupt."""
    try:
        with open("contacts.json", "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_contacts(data):
    """Save the full contacts list to contacts.json."""
    with open("contacts.json", "w") as f:
        json.dump(data, f, indent=2)


def add_new_contact():
    """Collect name, phone, and email from user and add a new contact after validation."""
    data = load_contacts()

    contact_name = input("Contact Name: ")
    contact_phone = input("Contact Phone Number: ")

    # Phone must be digits only and between 7-15 characters
    if not (contact_phone.isdigit() and 7 <= len(contact_phone) <= 15):
        print("Invalid phone number.")
        return

    contact_mail = input("Contact Mail: ")

    # Basic email validation — must contain @ and .
    if "@" not in contact_mail or "." not in contact_mail:
        print("Invalid email.")
        return

    # Build the contact object
    new_contact_json = {
        "name": contact_name,
        "phone": contact_phone,
        "mail": contact_mail,
    }

    # Append and save
    data.append(new_contact_json)
    with open("contacts.json", "w") as f:
        json.dump(data, f, indent=2)


def search_contact():
    """Search contacts by partial name match (case-insensitive) and display results."""
    data = load_contacts()

    search_name = input("Search name: ").lower()

    # List comprehension — keep contacts where search term appears in the name
    filtered_contact = [
        contact for contact in data if search_name in contact.get("name", "").lower()
    ]

    if filtered_contact:
        for contact in filtered_contact:
            found_contact = (
                f"{contact['name']} | {contact['phone']} | {contact['mail']}"
            )
            print(f"Found: {found_contact}")
    else:
        print("No matching contacts found.")


def update_contact():
    """Find a contact by name and update their phone or email after validation."""
    print("Updating contact")
    data = load_contacts()
    name = input("Enter name to update: ").lower()

    for contact in data:
        if name in contact["name"].lower():
            print(f"Found: {contact['name']} | {contact['phone']} | {contact['mail']}")

            new_phone = input("New phone (leave blank to keep current): ")

            if new_phone:
                # Validate new phone before updating
                if not (new_phone.isdigit() and 7 <= len(new_phone) <= 15):
                    print("Invalid phone number.")
                    return
                contact["phone"] = new_phone

            new_email = input("New email (leave blank to keep current): ")

            if new_email:
                # Validate new email before updating
                if "@" not in new_email or "." not in new_email:
                    print("Invalid email.")
                    return
                contact["mail"] = new_email

            # Save updated data back to file
            save_contacts(data)
            print("Contact updated.")
            return

    print("Contact not found.")


def delete_contact():
    """Find a contact by partial name match and remove them from the list."""
    data = load_contacts()
    name = input("Enter name to delete: ").lower()

    for contact in data:
        if name in contact["name"].lower():
            # Remove the matched contact and save
            data.remove(contact)
            save_contacts(data)
            print("Contact deleted.")
            return

    print("No matching contact found.")


def show_contact_list():
    """Display all contacts sorted alphabetically by name."""
    print("=== Contact List ===")
    data = load_contacts()

    # Sort contacts by name (case-insensitive) using a lambda
    data.sort(key=lambda x: x["name"].lower())

    for index, item in enumerate(data):
        contact_text = f"{index + 1}. {item['name']} | {item['phone']} | {item['mail']}"
        print(contact_text)


# Create contacts.json with an empty list if it doesn't exist yet
if not os.path.exists("contacts.json"):
    with open("contacts.json", "w") as f:
        json.dump([], f)


# Main loop — keeps the app running until the user types "quit"
while True:
    operator = input("Options: add | search | update | delete | list | quit: ")

    if operator == "quit":
        break
    elif operator == "add":
        add_new_contact()
    elif operator == "search":
        search_contact()
    elif operator == "update":
        update_contact()
    elif operator == "delete":
        delete_contact()
    elif operator == "list":
        show_contact_list()
    else:
        # Handle any unrecognised input
        print("Invalid option. Choose: add, search, update, delete, list, quit")
