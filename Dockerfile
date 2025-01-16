# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install netcat (choose netcat-openbsd for compatibility)
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 8000

# Start the application (handled by docker-compose)
