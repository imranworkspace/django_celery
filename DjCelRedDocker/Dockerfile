# Use official Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirnments.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirnments.txt

# Copy project files
COPY . .

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Expose Django port
EXPOSE 8006

# Default command (overridden in docker-compose.yml for Celery/Flower)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8006"]
