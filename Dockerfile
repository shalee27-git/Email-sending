# Use an official Python runtime
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
