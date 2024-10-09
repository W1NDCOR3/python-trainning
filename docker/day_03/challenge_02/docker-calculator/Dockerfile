# Use Python image as base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc && \
    pip install psycopg2-binary

# Copy the Python script into the container
COPY calculator.py .

# Start the container with a shell to keep it alive
CMD ["tail", "-f", "/dev/null"]
