### generate_question.py

# 03/05/2025 v1.0 This script generates a reflective question using an LLM.

import os
from huggingface_hub import InferenceClient

MODEL_NAME = "mistralai/Mixtral-8x7B-Instruct-v0.1"  # Change as needed
HF_TOKEN = os.getenv("HF_TOKEN")  # Optional: for authenticated access

client = InferenceClient(model=MODEL_NAME, token=HF_TOKEN)

def generate_question(yesterday_answer: str, day_count: int) -> str:
    prompt = f"""
    You are an AI career coach helping a user transition from Site Reliability Engineer to AI Engineer in 5 months.
    Today is Day {day_count}. Yesterday the user reflected:
    "{yesterday_answer}"

    Based on that, generate a short, thoughtful, reflective question to help them grow today.
    Respond only with the question.
    """

    response = client.text_generation(prompt, max_new_tokens=100, temperature=0.7)
    return response.strip()