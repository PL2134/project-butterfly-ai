### daily_agent.py

# 03/05/2025 v1.0 This script is for the dry run of the Daily Agent project.

from generate_question import generate_question
from memory_store import load_yesterday_answer, store_today_answer

import sys

def run_daily_agent():
    day_count = 21  # You can calculate this from a start date
    yesterday = load_yesterday_answer()
    question = generate_question(yesterday, day_count)

    print("Today's Question:", question)

    # (Optional) Store dummy response for testing
    user_answer = input("\nYour Answer: ")
    store_today_answer(user_answer)

if __name__ == "__main__":
    run_daily_agent()
