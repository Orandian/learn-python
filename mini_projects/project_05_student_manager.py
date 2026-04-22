# ============================================
# PROJECT 05 — Student Grade Manager 🎓
# Difficulty: Hard
# ============================================
# Build an OOP-based student grade management system.
#
# Requirements:
#   1. Create a Student class with:
#        - name, student_id, grades (dict of subject: score)
#        - add_grade(subject, score) method
#        - get_average() method — returns average of all grades
#        - get_letter_grade() method:
#            90-100 → "A", 80-89 → "B", 70-79 → "C",
#            60-69 → "D", below 60 → "F"
#        - report() method — prints a full summary
#
#   2. Create a Classroom class with:
#        - a list of Student objects
#        - add_student(student) method
#        - find_student(name) method — search by name
#        - top_student() method — returns student with highest average
#        - class_average() method — returns average of all students
#        - save_to_file() / load_from_file() — save/load using JSON
#
#   3. Build a menu-driven interface:
#        Options: add student | add grade | view student | 
#                 class report | top student | save | load | quit
#
# Skills used: OOP, classes, inheritance, JSON, file I/O, lists, dicts
#
# BONUS:
#   - Add input validation (scores must be 0-100)
#   - Sort students by average when showing class report
#   - Add a Subject class with a max_score attribute
#
# Example run:
#   === Student Manager ===
#   Options: add student | add grade | view student | report | quit
#   Choose: add student
#   Name: Alice
#   Student ID: S001
#   Student Alice added!
#
#   Choose: add grade
#   Student name: Alice
#   Subject: Math
#   Score: 92
#   Grade added!
#
#   Choose: view student
#   Student name: Alice
#   --- Alice (S001) ---
#   Math: 92
#   Average: 92.0 | Grade: A
# ============================================

# YOUR CODE HERE:
