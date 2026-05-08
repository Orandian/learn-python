# ============================================
# REAL-WORLD PROJECT 03 — Web Scraper 🕷️
# Difficulty: Hard
# ============================================
# Build a web scraper that extracts data from a public website
# and saves it to a JSON file for analysis.
#
# Target: https://books.toscrape.com (a safe, legal scraping practice site)
#
# Requirements:
#   1. Scrape the homepage and extract for each book:
#        - Title
#        - Price
#        - Star rating (One/Two/Three/Four/Five → convert to 1-5)
#        - Availability (In stock / Out of stock)
#   2. Save all books to "books.json"
#   3. After scraping, show a summary:
#        - Total books found
#        - Average price
#        - Most expensive book
#        - Cheapest book
#        - Books with 5-star rating
#   4. Handle pagination — scrape ALL pages (not just page 1)
#   5. Add error handling for network issues
#
# Skills used: requests, BeautifulSoup, JSON, loops, error handling
#
# Setup:
#   pip install requests beautifulsoup4
#
# BONUS:
#   - Filter and display books by minimum star rating
#   - Sort books by price (low to high)
#   - Scrape a specific genre/category page
#
# Hint — basic scraping structure:
#   import requests
#   from bs4 import BeautifulSoup
#
#   response = requests.get("https://books.toscrape.com")
#   soup = BeautifulSoup(response.text, "html.parser")
#   books = soup.find_all("article", class_="product_pod")
#   for book in books:
#       title = book.h3.a["title"]
#       price = book.find("p", class_="price_color").text
#
# Example output:
#   Scraping page 1... ✅
#   Scraping page 2... ✅
#   ...
#   === Scrape Complete ===
#   Total books    : 1000
#   Average price  : £35.07
#   Most expensive : £59.99 — "Shakespeare's Sonnets"
#   Cheapest       : £10.00 — "A Light in the Attic"
#   5-star books   : 68
# ============================================

import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://books.toscrape.com/catalogue/"
START_URL = "https://books.toscrape.com"

# Map word ratings to numbers
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


# YOUR CODE HERE:
