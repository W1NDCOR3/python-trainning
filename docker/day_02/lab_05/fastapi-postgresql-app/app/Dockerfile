# Use the official Python image as the base image
FROM diogoromero/app:latest

# Install Poetry
RUN pip install poetry

# Set working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install project dependencies
RUN poetry install --only main

# Expose the port the app runs on
EXPOSE 8000

