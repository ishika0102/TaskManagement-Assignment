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
   CREATE DATABASE TaskManagement_1;

   USE TaskManagement;

   CREATE TABLE tasks (
    id VARCHAR(50) PRIMARY KEY,  -- Use VARCHAR for string-based IDs, with a reasonable length like 50
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('pending', 'completed') DEFAULT 'pending',
    deadline DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_by VARCHAR(255),
    updated_by VARCHAR(255),
    UNIQUE (id)  );

   ```

## Features

1. Create/Add a new task
2. Retrieve a task by its ID
3. Retrieve a list of all tasks
4. Update an existing task
5. Delete a task by its ID

## Technologies Used

- **Backend**: FastAPI, Pydantic, MySQL
- **Frontend**: React, Axios, HTML , CSS

## Backend

### Prerequisites

1. Python installed.
2. Install required packages:

   ```sql
   pip install fastapi pydantic mysql-connector-python
   ```

Create a `.env` file in the root directory of your project with the following MySQL database configuration:

```sql
DB_URL=localhost
DB_NAME=TaskManagement_1
DB_USER=your_user
DB_PASSWORD=your_password
```

### To run the backend :

```python
uvicorn backend.app.main:app --reload --port 8000
```

To run test :

```python
 PYTHONPATH=. pytest
```

## Frontend:

### Prerequisites:

1. node installed
2. cd frontend/task-management

```sql
 npm install
```

### To run the frontend :

(make sure to cd frontend/task-management)

```sql
npm start
```

### Below is screenshot of the frontend

![alt text](<Screenshot from 2024-10-20 11-19-38.png>)

### Note:

- Includes API documentation (Swagger documentation) at /docs
