
FROM python:3.10-slim


# Install Poetry
RUN pip install poetry

# Set working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install project dependencies
RUN poetry install 

# Expose the port the app runs on
EXPOSE 8000

