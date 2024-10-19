# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.route import task
from backend.app.core.db import create_default_user, create_connection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task.router, prefix="/api")


@app.on_event("startup")
def on_startup():
    """Event handler for app startup"""
    print("App Startup Logic Goes Here")
    create_default_user()


@app.get("/test-db")
def test_db():
    connection = create_connection()
    if connection and connection.is_connected():
        return {"message": "Database connection is successful!"}
    else:
        return {"message": "Failed to connect to the database."}
