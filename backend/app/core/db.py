# app/db.py

import mysql.connector
from mysql.connector import Error
from backend.app.core.config import config

# Configuration parameters
DATABASE_URL = config.db_url
DATABASE_NAME = config.db_name
DATABASE_USER = config.db_user
DATABASE_PASSWORD = config.db_password


def create_connection():
    """Create a database connection to a MySQL database."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=DATABASE_URL,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            database=DATABASE_NAME,
            auth_plugin='mysql_native_password')
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    """Execute a single query."""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def create_default_user():
    connection = create_connection()
    if connection:
        create_user_query = """
        INSERT INTO user (username, email, password) 
        VALUES ('user', 'user@example.com', 'user@123')
        """
        execute_query(connection, create_user_query)
        connection.close()
