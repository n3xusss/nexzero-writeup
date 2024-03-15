# Use the official Node.js image as a base image
FROM node:14

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the SQLite database file
COPY mydatabase.db .

# Copy the rest of the application code
COPY . .

# Expose the port your app will run on
EXPOSE 3000

# Command to run your application
CMD ["node", "auth.js"]

