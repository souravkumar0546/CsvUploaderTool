# CSV Uploader Tool

## Overview
The CSV Uploader Tool is a web application that allows users to upload CSV files and map the data to a structured format. The tool is built using Django for the backend and React for the frontend.

## Features
- **Drag and Drop File Upload**: Users can drag and drop CSV files or choose files manually for upload.
- **Data Mapping**: The backend processes the CSV file and maps the data to a predefined structure.
- **Error Handling**: Displays appropriate messages for errors and validation issues.
- **Responsive Design**: Layout is designed to be user-friendly and responsive.

## Technologies Used
- **Frontend**: React
- **Backend**: Django
- **Docker**: Used to containerize both the frontend and backend, making it easier to run the application consistently across different environments

## Getting Started

### Prerequisites
- Docker and Docker Compose (for setting up the application using containers)
- Node.js and npm (for frontend development)
- Python 3.x (for backend development)


### Setup

#### Clone the Repository
```bash
git clone https://github.com/souravkumar0546/CsvUploaderTool.git
```
#### Using Docker (Recommended)
1. **Navigate to the Main Directory**
   ```bash
    cd backend
    ```
2. **Create an .env file in the backend directory by copying the .env.example file**
   ```bash
   cp backend/.env.example backend/.env
   ```
3. **Configure the Environment Variables: Edit the .env file in the backend directory to include your Gemini API key**
   ```bash
   API_KEY=your-api-key-here
   ```
4. **Run the Application using Docker Compose:**
   ```bash
   docker-compose up --build
   ```
**Access the Application:**
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
   
#### Without Docker (Manual Setup)
#### Backend

1. **Navigate to the Backend Directory**
    ```bash
    cd backend
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup Environment Variables**:
    Copy the `.env.example` file to `.env` and configure your  Gemini API key.

    Example:
    ```env
    API_KEY=your-api-key-here
    ```

5. **Start the Development Server**:
    ```bash
    python manage.py runserver
    ```

#### Frontend
1. **Navigate to the Frontend Directory**:
    ```bash
    cd frontend
    ```

2. **Install Dependencies**:
    ```bash
    npm install
    ```

3. **Start the Development Server**:
    ```bash
    npm start
    ```


**Access the Application**:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000

## Future Improvements and Features
If more time were available, the following improvements and features would have been considered:

- **Enhanced Error Handling**: Improve error handling on both the frontend and backend to provide more detailed error messages and recovery options for users.
- **CSV File Validation**: Implement additional validation for CSV files to ensure data integrity before processing. This includes checking for correct file format and content.
- **Data Export Feature**: Add functionality for users to export the mapped data to various formats (e.g., CSV, Excel) for further analysis or reporting.
- **Performance Optimization**: Optimize both frontend and backend performance to handle larger files.
- **Adding Mapped Data to Database**: Ensure that the mapped data is correctly added to the database for persistent storage and further processing.
