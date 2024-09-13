# Use the official Node.js image as the parent image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the current directory contents into the working directory in the container
COPY . .

# Expose port 3000 for the React app
EXPOSE 3000

# Command to run the app
CMD ["npm", "start"]
