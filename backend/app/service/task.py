from fastapi import HTTPException, status
from backend.app.model.task import TaskCreate
from backend.app.repository import task as repository
from backend.app.core.generate_id import generate_task_id

from backend.app.core.constants import TASK_NOT_FOUND, TASK_UPDATE_FAILED


def create_task(task_create: TaskCreate) -> dict:
    """Create a new task"""
    # Generate a unique 6-character task ID
    task_id = generate_task_id()

    # Assign the generated task ID to the task_create object
    task_create.id = task_id

    # Call the repository to save the task with the unique ID
    new_task = repository.create_task(task_create)

    # Return the task details as a dictionary
    return new_task


def get_tasks() -> dict:
    """Get all tasks"""
    return repository.get_tasks()


def get_task(task_id: int) -> dict:
    """Get a task by ID"""

    task = repository.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=TASK_NOT_FOUND)
    return task


def update_task(task_id: int, task_update) -> dict:
    """Update a task by ID"""

    # Assuming repository is a database handler and returns None if the task is not found
    task = repository.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=TASK_NOT_FOUND)

        # Proceed with the update
    updated_task = repository.update_task(task_id, task_update)

    # In case the update fails due to some internal reason
    if updated_task is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=TASK_UPDATE_FAILED)

    return updated_task


def delete_task(task_id: int):
    """Delete a task by ID"""
    task = repository.delete_task(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=TASK_NOT_FOUND)
