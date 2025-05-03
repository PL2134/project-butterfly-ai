# send_question.py

# 27/04/2024 v1.0 This script sends a daily reflective question to a Telegram bot.
# 03/05/2025 v2.0 LLM added.

import os
import requests
from datetime import datetime

from generate_question import generate_question
from memory_store import load_yesterday_answer

# Environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    if not response.ok:
        print("Failed to send message:", response.text)

if __name__ == "__main__":
    # Dynamically calculate the day
    START_DATE = datetime(2024, 12, 1)  # Change to your real Day 1
    day_count = (datetime.today() - START_DATE).days + 1

    # Load memory + generate a question
    yesterday_answer = load_yesterday_answer()
    question = generate_question(yesterday_answer, day_count)

    # Send to Telegram
    message = f"🦋 Day {day_count} — Your Reflective Question:\n\n{question}"
    send_telegram_message(message)