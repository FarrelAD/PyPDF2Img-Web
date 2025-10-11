# Dockerfile

# 1. Use an official, slim Python runtime as the base image
FROM python:3.11-slim

# 2. Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Install necessary system dependencies
# poppler-utils is for your PDF processing
# build-essential & libpq-dev are common for Django projects (e.g., for psycopg2)
RUN apt-get update && apt-get install -y \
    poppler-utils \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Set the working directory inside the container
WORKDIR /app

# 5. Copy and install Python dependencies
# This is done in a separate step to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of your application's source code
COPY . .

# 7. Make the startup script executable
RUN chmod +x start.sh

# 8. Define the command to run your application
CMD ["./start.sh"]
