# ============================================
# REAL-WORLD PROJECT 01 — Weather App 🌤️
# Difficulty: Intermediate
# ============================================
# Build a command-line weather app that fetches real live
# weather data from a public API.
#
# API: OpenWeatherMap (free tier)
# Sign up at: https://openweathermap.org/api
# Get your free API key → copy it into API_KEY below
#
# Requirements:
#   1. Ask the user for a city name
#   2. Fetch current weather using the OpenWeatherMap API
#   3. Display:
#        - City name and country
#        - Temperature (°C)
#        - Feels like temperature
#        - Weather description (e.g. "light rain")
#        - Humidity %
#        - Wind speed
#   4. Handle errors:
#        - City not found (API returns 404)
#        - No internet connection
#        - Invalid API key
#   5. Ask if the user wants to check another city (loop)
#
# Skills used: requests library, JSON, error handling, loops, f-strings
#
# Setup:
#   pip install requests
#
# BONUS:
#   - Save search history to a JSON file
#   - Add a 5-day forecast option
#   - Convert between °C and °F based on user preference
#
# API Endpoint:
#   https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric
#
# Example output:
#   === Weather for London, GB ===
#   🌡️  Temperature : 14.2°C (Feels like 12.8°C)
#   🌥️  Description : overcast clouds
#   💧 Humidity    : 78%
#   💨 Wind Speed  : 5.3 m/s
# ============================================

import requests
import json
import os

API_KEY = "YOUR_API_KEY_HERE"  # ← Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
HISTORY_FILE = "weather_history.json"


# YOUR CODE HERE:
