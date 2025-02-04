# Use an official Python image as the base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose necessary ports (modify if needed)
EXPOSE 8080

# Run the application (modify based on your main entry point)
CMD ["python3", "main.py"]
