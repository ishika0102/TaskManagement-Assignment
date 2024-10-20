from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from pydantic import ValidationError

from backend.app.model.task import TaskCreate, TaskUpdate
from backend.app.service import task as service
from backend.app.core.constants import TASK_DELETED_SUCCESSFULLY
# from app.repository import task as repository

router = APIRouter()


@router.post("/tasks", tags=["Tasks"])
def create_task(task_create: TaskCreate):
    try:
        result = service.create_task(task_create)
        return result
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=e.errors())


@router.get("/tasks", tags=["Tasks"])
def get_tasks():
    return service.get_tasks()


@router.get("/tasks/{task_id}", tags=["Tasks"])
def get_task(task_id: int):
    return service.get_task(task_id)


@router.put("/tasks/{task_id}", tags=["Tasks"])
def update_task(task_id: int, task_update: TaskUpdate):
    updated_task = service.update_task(task_id, task_update)
    return updated_task


@router.delete("/tasks/{task_id}", tags=["Tasks"])
def delete_task(task_id: int):
    service.delete_task(task_id)
    return {"message": TASK_DELETED_SUCCESSFULLY}
