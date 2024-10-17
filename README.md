# Task Management Project

## Project Structure

This project is a Task Management application that includes a backend service. Before running the project, ensure you have configured your database correctly.

### Prerequisites

1. Make sure you have a MySQL server running.
2. Update your database configuration in the `.env` file as needed.

### Database Setup

Follow the steps below to create the necessary database and tables:

1. **Create the Database**:
   Execute the following SQL command to create a database called `TaskManagement`:

   ```sql
   CREATE DATABASE TaskManagement;
   USE TaskManagement;
   CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL );
    CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('pending', 'completed') DEFAULT 'pending',
    deadline DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_by VARCHAR(255),
    updated_by VARCHAR(255));
   ```

### Notes:

- Make sure to add any additional instructions relevant to your project, such as how to run the backend or any other configurations needed.
- You can modify the sections as per your project needs, like adding sections for installation, usage, and any other relevant information.
