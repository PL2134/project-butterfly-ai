### memory_store.py

# 03/05/2025 v1.0 This script is part of a simple memory management system. it allows storing and retrieving user answers from a JSON file.

import json
from datetime import date

MEMORY_FILE = "user_memory.json"

def load_yesterday_answer() -> str:
    try:
        with open(MEMORY_FILE, 'r') as f:
            data = json.load(f)
            yesterday = str(date.today().fromordinal(date.today().toordinal() - 1))
            return data.get(yesterday, "No entry from yesterday.")
    except FileNotFoundError:
        return "No memory file found."

def store_today_answer(answer: str):
    today = str(date.today())
    try:
        with open(MEMORY_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data[today] = answer

    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=2)
