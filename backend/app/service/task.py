from backend.app.model.task import TaskCreate
from backend.app.repository import task as repository


def create_task(task_create: TaskCreate) -> dict:
    """Create a new task"""
    #     TODO: Generate the task ID and add to the task_create and change in table that id is unique and not auto_increment
    repository.create_task(task_create)


def get_tasks() -> dict:
    """Get all tasks"""
    return repository.get_tasks()


def get_task(task_id: int) -> dict:
    """Get a task by ID"""
    #     TODO: If task not found return 404
    return repository.get_task(task_id)


def update_task(task_id: int, task_update) -> dict:
    """Update a task by ID"""
    return repository.update_task(task_id, task_update)


def delete_task(task_id: int) -> dict:
    """Delete a task by ID"""
    #     TODO: IF task not found return 404
    return repository.delete_task(task_id)
