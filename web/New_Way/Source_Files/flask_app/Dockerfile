# Use the official Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app
RUN apt-get update && apt-get install socat -y
# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
