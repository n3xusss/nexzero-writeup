# Use the official Python image
FROM python:3.9

RUN apt-get update && apt-get install curl socat

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN adduser none-root
RUN chown -R none-root:none-root /app
USER none-root
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
