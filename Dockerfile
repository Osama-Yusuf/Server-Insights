# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

RUN apt update && apt install -y curl

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose port 5000 for the Flask app
EXPOSE 8080

# Run the Flask app in the background
CMD ["python", "app.py"]
