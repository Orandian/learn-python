# ============================================
# PROJECT 04 — Quiz Game 🎯
# Difficulty: Intermediate / Hard
# ============================================
# Build a multiple-choice quiz game with scoring and a timer.
#
# Requirements:
#   1. Define at least 5 questions as a list of dicts, each with:
#        - "question": the question text
#        - "options": list of 4 choices ["A. ...", "B. ...", "C. ...", "D. ..."]
#        - "answer": the correct option letter e.g. "A"
#   2. Shuffle the questions each game (use: import random; random.shuffle())
#   3. Show each question with options and ask for input (A/B/C/D)
#   4. Track score — +1 for correct, show correct answer if wrong
#   5. At the end show: score, percentage, and a rating message:
#        - 100%      → "Perfect! 🏆"
#        - 80-99%    → "Great job! 🌟"
#        - 60-79%    → "Good effort! 👍"
#        - below 60% → "Keep practising! 💪"
#
# Skills used: lists, dicts, loops, functions, randomisation
#
# BONUS:
#   - Add a countdown timer per question using the `time` module
#   - Save the high score to a file and display it at the start
#   - Add a "hint" option that eliminates one wrong answer
#
# Example run:
#   === Python Quiz ===
#   Q1: What is the output of print(type(42))?
#   A. <class 'str'>   B. <class 'int'>   C. <class 'float'>   D. <class 'bool'>
#   Your answer: B
#   ✅ Correct!
# ============================================

# YOUR CODE HERE:
import random
import time

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B",
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C",
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": [
            "A. Charles Dickens",
            "B. William Shakespeare",
            "C. Mark Twain",
            "D. Jane Austen",
        ],
        "answer": "B",
    },
    {
        "question": "Which language is primarily used for web development?",
        "options": ["A. Python", "B. C++", "C. Java", "D. JavaScript"],
        "answer": "D",
    },
]

point = 0

random.shuffle(questions)


def get_hint(q):
    # remove one wrong option
    wrong_options = [opt for opt in q["options"] if not opt.startswith(q["answer"])]
    removed = random.choice(wrong_options)
    return [opt for opt in q["options"] if opt != removed]


def load_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0


high_score = load_high_score()


def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))


def ask_question(q, index):
    global point

    print(" === Python Quiz ===")
    print(f"High Score: {high_score} out of {len(questions)}")

    options_line = " ".join(q["options"])
    print(f"Q{index + 1}: {q['question']}")
    print(options_line)

    start_time = time.time()

    real_answer = q["answer"].lower()
    user_input = input("Your answer: ").lower()

    if user_input == "h":
        start_time = time.time()
        hinted_options = get_hint(q)
        print("Hint used! Options reduced:")
        print(" ".join(hinted_options))

        user_input = input("Your answer: ").strip().lower()

    end_time = time.time()

    # ⏱️ Timer check
    if end_time - start_time > 10:
        print("⏰ Time's up!")
    elif real_answer == user_input:
        point += 1
        print("✅ Correct!")
    else:
        print(f"❌ Wrong! Correct answer is {real_answer}")

    print()  # spacing after each question


def show_question():
    for index, q in enumerate(questions):
        ask_question(q, index)


show_question()

total = len(questions)
percentage = round((point / total) * 100)

print(f"Score: {point}/{total}")
print(f"Percentage: {percentage:.0f}%")

if point >= high_score:
    save_high_score(point)

if percentage == 100:
    print("Perfect! 🏆")
elif 80 <= percentage < 100:
    print("Great job! 🌟")
elif 60 <= percentage < 80:
    print("Good effort! 👍")
else:
    print("Keep practising! 💪")
