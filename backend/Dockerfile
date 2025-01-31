FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg xvfb wget unzip libglib2.0-0 libnss3 libgconf-2-4 libxss1 libasound2 && \
    rm -rf /var/lib/apt/lists/*

# Install Chrome + ChromeDriver
# Use slim base image to keep the size minimal
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget curl gnupg2 ca-certificates ffmpeg xvfb tor \
    && mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | tee /etc/apt/keyrings/google-chrome-keyring.gpg > /dev/null \
    && chmod a+r /etc/apt/keyrings/google-chrome-keyring.gpg \
    && echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list > /dev/null \
    && apt-get update && apt-get install -y google-chrome-stable \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the bot files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt




# Expose if you run a Flask/FastAPI service
EXPOSE 8000

CMD ["celery", "-A", "celery_app", "worker", "--loglevel=info", "--concurrency=4"]
