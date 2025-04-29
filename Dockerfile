# Use a slim official Python image
FROM python:3.11-slim

# Avoid interactive prompts during installs
ENV DEBIAN_FRONTEND=noninteractive

# Set a working directory inside the container
WORKDIR /app

# Copy dependency list first, install, then copy the rest
# This optimizes Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project files
COPY . .

# Create a non-root user and switch to it
RUN adduser --disabled-login --gecos "" appuser
USER appuser

# Metadata for Docker Hub best practices
LABEL org.opencontainers.image.source="https://github.com/PL2134/project-butterfly-ai"
LABEL org.opencontainers.image.description="Project Butterfly AI personal growth assistant container"
LABEL org.opencontainers.image.licenses="MIT"

# By default, run the script
CMD ["python", "send_question.py"]