# Use a slim official Python image
FROM python:3.11-slim

# Avoid interactive prompts during installs
ENV DEBIAN_FRONTEND=noninteractive

# Create a non-root user (optional but good practice)
RUN adduser --disabled-login --gecos "" appuser
USER appuser

# Set a working directory inside the container
WORKDIR /app

# Copy dependency list first, install, then copy the rest.
# This keeps rebuilds fast when only your code changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project files
COPY . .

# By default, run the script
CMD ["python", "send_question.py"]