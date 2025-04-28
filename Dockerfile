# Use official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Install system dependencies (optional: libpq-dev for Postgres, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies first
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all project files into container
COPY ./new_user .

# Expose the port gunicorn will run on
EXPOSE 8000
RUN python3 manage.py migrate

# Command to run gunicorn
CMD ["gunicorn", "new_user.wsgi:application", "--workers", "3", "--bind", "0.0.0.0:8000"]
