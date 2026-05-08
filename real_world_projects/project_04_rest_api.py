# ============================================
# REAL-WORLD PROJECT 04 — REST API with Flask 🚀
# Difficulty: Hard
# ============================================
# Build a fully working REST API for a simple task manager
# using Flask — Python's most popular web framework.
#
# This is your first backend API in Python — very similar to
# building APIs in Express.js (Node) or Laravel (PHP).
#
# Requirements — build these endpoints:
#   GET    /tasks          → return all tasks
#   GET    /tasks/<id>     → return a single task by ID
#   POST   /tasks          → create a new task (JSON body)
#   PUT    /tasks/<id>     → update a task by ID
#   DELETE /tasks/<id>     → delete a task by ID
#
# Each task has: id, title, description, status, created_at
# Store tasks in a JSON file (tasks.json) — no database needed.
#
# Skills used: Flask, REST principles, JSON, error handling, routes
#
# Setup:
#   pip install flask
#
# Test your API with:
#   - curl commands in terminal
#   - Postman (you already have it installed!)
#   - The requests library in another Python script
#
# BONUS:
#   - Add input validation (title required, status must be valid)
#   - Add a search endpoint: GET /tasks?status=pending
#   - Add pagination: GET /tasks?page=1&limit=10
#   - Return proper HTTP status codes (200, 201, 404, 400)
#
# Hint — basic Flask structure:
#   from flask import Flask, jsonify, request
#   app = Flask(__name__)
#
#   @app.route("/tasks", methods=["GET"])
#   def get_tasks():
#       return jsonify({"tasks": []})
#
#   if __name__ == "__main__":
#       app.run(debug=True)
#
# Example responses:
#   GET /tasks
#   → {"tasks": [{"id": 1, "title": "Learn Flask", "status": "pending"}]}
#
#   POST /tasks  (body: {"title": "New task", "description": "Details"})
#   → {"message": "Task created", "task": {...}}
#
#   DELETE /tasks/1
#   → {"message": "Task deleted"}
# ============================================

from flask import Flask, jsonify, request
import json
import os
from datetime import datetime

app = Flask(__name__)
TASKS_FILE = "tasks.json"
VALID_STATUSES = ["pending", "in_progress", "completed"]


# YOUR CODE HERE:


if __name__ == "__main__":
    app.run(debug=True)
