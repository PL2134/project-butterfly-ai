# send_question.py

import os
import requests

# Load environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Load questions
def load_questions(filename="questions.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        questions = [line.strip() for line in file if line.strip()]
    return questions

# Load last sent index
def load_last_index(filename="index.txt"):
    if not os.path.exists(filename):
        return 0
    with open(filename, "r") as file:
        index = int(file.read().strip())
    return index

# Save new index
def save_last_index(index, filename="index.txt"):
    with open(filename, "w") as file:
        file.write(str(index))

# Send message
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

if __name__ == "__main__":
    if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
        questions = load_questions()
        index = load_last_index()
        question = questions[index % len(questions)]  # wrap around if needed

        result = send_telegram_message(question)
        print(result)

        # Save the next index
        save_last_index((index + 1) % len(questions))
    else:
        print("Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID environment variables.")
        