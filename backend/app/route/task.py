from fastapi import APIRouter

from backend.app.model.task import TaskCreate, TaskUpdate
from backend.app.service import task as service
# from app.repository import task as repository

router = APIRouter()


@router.post("/tasks", tags=["Tasks"])
def create_task(task_create: TaskCreate):
    try:
        service.create_task(task_create)
        return {"message": "Task created successfully"}
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())


@router.get("/tasks", tags=["Tasks"])
def get_tasks():
    return service.get_tasks()


@router.get("/tasks/{task_id}", tags=["Tasks"])
def get_task(task_id: int):
    return service.get_task(task_id)


@router.put("/tasks/{task_id}", tags=["Tasks"])
def update_task(task_id: int, task_update: TaskUpdate):
    service.update_task(task_id, task_update)
    return {"message": "Task updated successfully"}


@router.delete("/tasks/{task_id}", tags=["Tasks"])
def delete_task(task_id: int):
    return service.delete_task(task_id)
