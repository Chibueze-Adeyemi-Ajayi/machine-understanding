# Base image
FROM python:3.10.12-slim

# Create the app-build directory
WORKDIR /app-build

# Copy requirements.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy application code to the app-build directory
COPY . .

# Expose the port the Flask app will run on
EXPOSE 3000

# Set environment variable for Flask app (assuming app.py is in app-build)
ENV FLASK_APP=/app-build/api.py

# Set working directory to app-build before running the app
WORKDIR /app-build

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]