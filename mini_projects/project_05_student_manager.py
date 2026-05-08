# ============================================
# PROJECT 05 — Student Grade Manager 🎓
# Difficulty: Hard
# ============================================
# OOP-based student grade management system.
# Key concepts: classes, methods, JSON, file I/O, DRY code
# ============================================

import json
import os

FILE_PATH = "students.json"  # Single source of truth for the file name


# ============================================
# STUDENT CLASS
# Represents a single student and their grades
# ============================================

class Student:
    def __init__(self, name, student_id):
        """Initialise a student with a name, ID, and empty grades dict."""
        self.name = name
        self.student_id = student_id
        self.grades = {}  # { "Math": 90, "English": 85 }

    def add_grade(self, subject, score):
        """Add or update a grade for a subject. Score must be between 0 and 100."""
        if not (0 <= score <= 100):
            print("Score must be between 0 and 100.")
            return
        self.grades[subject] = score
        print(f"Grade added: {subject} → {score}")

    def get_average(self):
        """Return the average score across all subjects. Returns 0 if no grades."""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def get_letter_grade(self):
        """Convert the average score to a letter grade (A-F)."""
        average = self.get_average()
        # Using a list of tuples keeps the thresholds in one place (DRY)
        thresholds = [(90, "A"), (80, "B"), (70, "C"), (60, "D")]
        for minimum, letter in thresholds:
            if average >= minimum:
                return letter
        return "F"

    def report(self):
        """Print a full summary of the student's grades and performance."""
        print(f"\n--- {self.name} ({self.student_id}) ---")
        if not self.grades:
            print("No grades recorded yet.")
        else:
            for subject, score in self.grades.items():
                print(f"  {subject}: {score}")
            print(f"  Average: {self.get_average():.1f} | Grade: {self.get_letter_grade()}")

    # ---- Serialisation helpers (for saving/loading JSON) ----

    def to_dict(self):
        """Convert the Student object to a plain dict for JSON storage."""
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grades": self.grades,
        }

    @classmethod
    def from_dict(cls, data):
        """Rebuild a Student object from a dict loaded from JSON."""
        student = cls(data["name"], data["student_id"])
        student.grades = data.get("grades", {})
        return student


# ============================================
# CLASSROOM CLASS
# Manages a collection of Student objects
# ============================================

class Classroom:
    def __init__(self):
        """Initialise with an empty list of students."""
        self.students = []

    def add_student(self, student):
        """Add a Student object to the classroom."""
        self.students.append(student)
        print(f"Student {student.name} ({student.student_id}) added!")

    def find_student(self, name):
        """Find and return a student by partial name match (case-insensitive). Returns None if not found."""
        name = name.lower()
        for student in self.students:
            if name in student.name.lower():
                return student
        return None

    def top_student(self):
        """Return the student with the highest average. Returns None if no students."""
        if not self.students:
            return None
        # key= tells max() what to compare by — keeps logic in one line (DRY)
        return max(self.students, key=lambda s: s.get_average())

    def class_average(self):
        """Return the average score across all students. Returns 0 if no students."""
        if not self.students:
            return 0
        return sum(s.get_average() for s in self.students) / len(self.students)

    def class_report(self):
        """Print a full report for every student, sorted by average (highest first)."""
        if not self.students:
            print("No students in the classroom.")
            return
        print("\n=== Class Report ===")
        # Sort students by average descending — DRY: reuses get_average()
        sorted_students = sorted(self.students, key=lambda s: s.get_average(), reverse=True)
        for student in sorted_students:
            student.report()
        print(f"\nClass Average: {self.class_average():.1f}")

    # ---- File I/O ----

    def save_to_file(self):
        """Save all students to a JSON file using each student's to_dict() method."""
        data = [student.to_dict() for student in self.students]
        with open(FILE_PATH, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to {FILE_PATH}.")

    def load_from_file(self):
        """Load students from JSON and rebuild Student objects using from_dict()."""
        if not os.path.exists(FILE_PATH):
            return  # No file yet — start fresh
        try:
            with open(FILE_PATH, "r") as f:
                data = json.load(f)
            # Rebuild each Student object from its dict representation
            self.students = [Student.from_dict(d) for d in data]
            print(f"Loaded {len(self.students)} student(s) from {FILE_PATH}.")
        except (json.JSONDecodeError, KeyError):
            print("Could not load data. Starting fresh.")


# ============================================
# HELPER FUNCTIONS
# Keeps the menu loop clean and readable
# ============================================

def prompt_score():
    """Ask the user for a score and validate it's a number. Returns float or None."""
    try:
        return float(input("Score (0-100): "))
    except ValueError:
        print("Invalid score. Please enter a number.")
        return None


def handle_add_student(classroom):
    """Collect name and ID, then add a new student to the classroom."""
    name = input("Student name: ").strip()
    student_id = input("Student ID: ").strip()
    if not name or not student_id:
        print("Name and ID cannot be empty.")
        return
    classroom.add_student(Student(name, student_id))


def handle_add_grade(classroom):
    """Find a student by name and add a grade for a subject."""
    name = input("Student name: ").strip()
    student = classroom.find_student(name)
    if not student:
        print("Student not found.")
        return
    subject = input("Subject: ").strip()
    score = prompt_score()
    if score is not None:
        student.add_grade(subject, score)


def handle_view_student(classroom):
    """Find a student by name and print their report."""
    name = input("Student name: ").strip()
    student = classroom.find_student(name)
    if student:
        student.report()
    else:
        print("Student not found.")


def handle_top_student(classroom):
    """Find and display the top-performing student."""
    student = classroom.top_student()
    if student:
        print(f"\nTop Student: {student.name} | Average: {student.get_average():.1f} | Grade: {student.get_letter_grade()}")
    else:
        print("No students yet.")


# Maps menu commands to their handler functions (DRY — no long if/elif chain)
MENU_OPTIONS = {
    "add student":   handle_add_student,
    "add grade":     handle_add_grade,
    "view student":  handle_view_student,
    "report":        Classroom.class_report,
    "top student":   handle_top_student,
    "save":          Classroom.save_to_file,
    "load":          Classroom.load_from_file,
}

MENU_DISPLAY = " | ".join(MENU_OPTIONS.keys()) + " | quit"


# ============================================
# MAIN PROGRAM
# ============================================

classroom = Classroom()
classroom.load_from_file()  # Load existing data on startup

while True:
    print(f"\nOptions: {MENU_DISPLAY}")
    choice = input("Choose: ").strip().lower()

    if choice == "quit":
        classroom.save_to_file()  # Auto-save on exit
        print("Goodbye! 👋")
        break
    elif choice in MENU_OPTIONS:
        # Call the matching handler function, passing classroom as argument
        MENU_OPTIONS[choice](classroom)
    else:
        print("Invalid option. Please choose from the menu.")
