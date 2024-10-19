from fastapi import HTTPException
from backend.app.core.db import create_connection, execute_query
from backend.app.model.task import TaskBase
from typing import List

from mysql.connector import Error, InterfaceError, ProgrammingError, IntegrityError

db_connection = create_connection()
print(db_connection)


def create_task(task) -> dict:
    """Create a new task."""
    try:
        create_task_query = f"""
        INSERT INTO tasks (title, description, deadline, created_by, updated_by, status)
        VALUES ('{task.title}', '{task.description}', '{task.deadline}', '{task.created_by}', '{task.updated_by}', '{task.status}')"""

        execute_query(db_connection, create_task_query)

    except InterfaceError as e:
        print(e)
        # Connection error (e.g., unable to connect to the database)
        raise HTTPException(
            status_code=500,
            detail="Database connection error. Please try again.") from e

    except ProgrammingError as e:
        print(e)
        # Table not found or SQL syntax error
        raise HTTPException(
            status_code=400,
            detail="Invalid database table or SQL syntax error.") from e

    except IntegrityError as e:
        print(e)
        # Duplicate entry error or other integrity constraint violations
        raise HTTPException(
            status_code=400,
            detail="Duplicate entry error. The task already exists.") from e

    except Error as e:
        print(e)
        # General MySQL error
        raise HTTPException(
            status_code=500,
            detail="Error executing the query in the database.") from e

    except Exception as e:
        print(e)
        # Catching any other unexpected errors
        raise HTTPException(status_code=500,
                            detail="An unexpected error occurred.") from e


def get_tasks() -> List[TaskBase]:
    """Get all tasks."""
    try:
        get_tasks_query = "SELECT * FROM tasks"
        cursor = db_connection.cursor()
        cursor.execute(get_tasks_query)
        tasks = cursor.fetchall()

        # Get column names to create a mapping
        column_names = [column[0] for column in cursor.description]

        # Map each task tuple to TaskBase using a dictionary comprehension
        task_list = [
            TaskBase(**dict(zip(column_names, task))) for task in tasks
        ]

        return task_list

    except Error as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="Error executing the query in the database.") from e

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,
                            detail="An unexpected error occurred.") from e


# def get_task(task_id) -> dict:
#     """Get a task by ID."""
#     try:
#         get_task_query = f"SELECT * FROM tasks WHERE id = {task_id}"
#         cursor = db_connection.cursor()
#         cursor.execute(get_task_query)
#         task = cursor.fetchone()
#         return task
#     except Error as e:
#         print(e)
#         raise HTTPException(
#             status_code=500,
#             detail="Error executing the query in the database.") from e

#     except Exception as e:
#         print(e)
#         raise HTTPException(status_code=500,
#                             detail="An unexpected error occurred.") from e

# def update_task(task_id, task_update) -> dict:
#     """Update a task by ID."""

#     print("this is task id:" + str(task_id))
#     print("this is task update:" + task_update.title)
#     try:
#         update_task_query = f"""
#         UPDATE tasks
#         SET title = '{task_update.title}', description = '{task_update.description}', deadline = '{task_update.deadline}', updated_by = '{task_update.updated_by}'
#         WHERE id = {task_id}"""
#         execute_query(db_connection, update_task_query)
#     except Error as e:
#         print(e)
#         raise HTTPException(
#             status_code=500,
#             detail="Error executing the query in the database.") from e

#     except Exception as e:
#         print("in update repository")
#         print(e)
#         raise HTTPException(status_code=500,
#                             detail="An unexpected error occurred.") from e

# def delete_task(task_id) -> dict:
#     """Delete a task by ID."""
#     try:
#         delete_task_query = f"DELETE FROM tasks WHERE id = {task_id}"
#         execute_query(db_connection, delete_task_query)
#     except Error as e:
#         print(e)
#         raise HTTPException(
#             status_code=500,
#             detail="Error executing the query in the database.") from e

#     except Exception as e:
#         print("in delete repository")
#         print(e)
#         raise HTTPException(status_code=500,
#                             detail="An unexpected error occurred.") from e


def get_task(task_id: int) -> TaskBase:
    """Get a task by ID."""
    try:
        get_task_query = f"SELECT * FROM tasks WHERE id = {task_id}"
        cursor = db_connection.cursor()
        cursor.execute(get_task_query)
        task = cursor.fetchone()

        if task:
            column_names = [column[0] for column in cursor.description]
            task_dict = dict(zip(column_names, task))
            return TaskBase(**task_dict)
        else:
            raise HTTPException(status_code=404, detail="Task not found")

    except Error as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="Error executing the query in the database.") from e

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,
                            detail="An unexpected error occurred.") from e


def update_task(task_id: int, task_update: TaskBase) -> TaskBase:
    """Update a task by ID."""
    try:
        update_task_query = f"""
        UPDATE tasks
        SET title = '{task_update.title}', description = '{task_update.description}', 
            deadline = '{task_update.deadline}', updated_by = '{task_update.updated_by}',
            status = '{task_update.status}'
        WHERE id = {task_id}"""

        cursor = db_connection.cursor()
        cursor.execute(update_task_query)
        db_connection.commit()

        # After updating, fetch the updated task and return it
        return get_task(task_id)

    except Error as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="Error executing the query in the database.") from e

    except Exception as e:
        print("in update repository")
        print(e)
        raise HTTPException(status_code=500,
                            detail="An unexpected error occurred.") from e


def delete_task(task_id: int) -> TaskBase:
    """Delete a task by ID."""
    try:
        # First, get the task to return it after deletion
        task_to_delete = get_task(task_id)

        delete_task_query = f"DELETE FROM tasks WHERE id = {task_id}"
        cursor = db_connection.cursor()
        cursor.execute(delete_task_query)
        db_connection.commit()

        return task_to_delete  # Returning the deleted task details

    except Error as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="Error executing the query in the database.") from e

    except Exception as e:
        print("in delete repository")
        print(e)
        raise HTTPException(status_code=500,
                            detail="An unexpected error occurred.") from e
