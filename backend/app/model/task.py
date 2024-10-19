from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, constr, Field, validator


class TaskBase(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., max_length=255)
    description: Optional[str] = None
    status: Optional[str] = Field(default="pending",
                                  pattern="^(pending|completed)$")
    deadline: Optional[datetime] = None
    created_by: Optional[str] = Field(None, max_length=255)
    updated_by: Optional[str] = Field(None, max_length=255)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class TaskCreate(TaskBase):
    title: str = Field(..., description="The title of the task")
    description: str = Field(...,
                             description="A brief description of the task")
    deadline: datetime = Field(..., description="The deadline for the task")
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    status: str = Field(default="pending",
                        description="The status of the task")

    @validator('status')
    def status_not_empty(cls, value):
        if value is None or value.strip() == "":
            raise ValueError('status cannot be empty or None')
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Task 1",
                "description": "This is task 1",
                "deadline": "2022-01-01T00:00:00Z",
                "created_by": "user1",
                "updated_by": "user1",
                "status": "pending"
            }
        }


class TaskUpdate(TaskBase):
    title: str = Field(..., description="The title of the task")
    description: str = Field(...,
                             description="A brief description of the task")
    deadline: datetime = Field(..., description="The deadline for the task")
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    status: str = Field(default="pending",
                        description="The status of the task")

    @validator('status')
    def status_not_empty(cls, value):
        if value is None or value.strip() == "":
            raise ValueError('status cannot be empty or None')
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Task 1",
                "description": "This is task 1",
                "deadline": "2022-01-01T00:00:00Z",
                "created_by": "user1",
                "updated_by": "user1",
                "status": "pending"
            }
        }
