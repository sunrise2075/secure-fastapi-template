# Use an official Python runtime as a parent image
FROM python:3.10-slim

LABEL authors="sunrise2075"

# Set the working directory in the container
WORKDIR /app

RUN apt-get update -y
RUN apt-get install pkg-config -y
RUN apt-get install -y python3-dev build-essential
RUN apt-get install -y default-libmysqlclient-dev

RUN pip install --upgrade pip

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

