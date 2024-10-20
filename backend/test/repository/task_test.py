import pytest
from unittest.mock import MagicMock, patch
from pytest_mock import mocker

from fastapi import HTTPException
from backend.app.model.task import TaskBase
from backend.app.repository.task import (
    create_task,
    get_tasks,
    get_task,
    update_task,
    delete_task,
)

# Sample task data
sample_task = TaskBase(id=1,
                       title="test-1",
                       description="This is a test task.",
                       deadline="2022-01-01T00:00:00Z",
                       createdBy="user1",
                       updatedBy="user1",
                       status="pending")


# Mock database connection and cursor
@pytest.fixture
def mock_db_connection(mocker):
    mock_connection = mocker.patch("backend.app.core.db.create_connection",
                                   return_value=MagicMock())
    return mock_connection


@pytest.fixture
def mock_cursor(mock_db_connection):
    cursor = MagicMock()
    mock_db_connection.return_value.cursor.return_value = cursor
    return cursor


def test_create_task(mock_cursor):
    # Arrange
    mock_cursor.execute.return_value = None
    mock_cursor.fetchall.return_value = []

    # Act
    task = create_task(sample_task)

    # Assert
    assert task.id == sample_task.id
    mock_cursor.execute.assert_called_once()


def test_get_tasks(mock_cursor):
    # Arrange
    mock_cursor.fetchall.return_value = [
        (1, "test-1", "This is a test task.", "2022-01-01T00:00:00Z",
         "user@example.com", "user@example.com", "pending")
    ]
    mock_cursor.description = [("id", ), ("title", ), ("description", ),
                               ("deadline", ), ("created_by", ),
                               ("updated_by", ), ("status", )]

    # Act
    tasks = get_tasks()

    # Assert
    assert len(tasks) == 1
    assert tasks[0].title == "task-1"


def test_get_task_found(mock_cursor):
    # Arrange
    mock_cursor.fetchone.return_value = (1, "test-1", "This is a test task.",
                                         "2022-01-01T00:00:00Z",
                                         "user@example.com",
                                         "user@example.com", "pending")
    mock_cursor.description = [("id", ), ("title", ), ("description", ),
                               ("deadline", ), ("created_by", ),
                               ("updated_by", ), ("status", )]

    # Act
    task = get_task(1)

    # Assert
    assert task.id == 1
    assert task.title == "task-1"


def test_get_task_not_found(mock_cursor):
    # Arrange
    mock_cursor.fetchone.return_value = None

    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        get_task(999)

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "An unexpected error occurred."


def test_update_task(mock_cursor):
    # Arrange
    mock_cursor.execute.return_value = None
    mock_cursor.fetchall.return_value = []

    # Act
    updated_task = update_task(1, sample_task)

    # Assert
    assert updated_task.id == sample_task.id
    mock_cursor.execute.assert_called_once()


def test_delete_task(mock_cursor):
    # Arrange
    mock_cursor.fetchone.return_value = (1, "test-1", "This is a test task.",
                                         "2022-01-01T00:00:00Z",
                                         "user@example.com",
                                         "user@example.com", "pending")
    mock_cursor.description = [("id", ), ("title", ), ("description", ),
                               ("deadline", ), ("created_by", ),
                               ("updated_by", ), ("status", )]

    # Act
    deleted_task = delete_task(1)

    # Assert
    assert deleted_task.id == 1
    mock_cursor.execute.assert_called_once()


def test_create_task_database_error(mock_cursor):
    # Arrange
    mock_cursor.execute.side_effect = Exception("Database error")

    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        create_task(sample_task)

    assert exc_info.value.status_code == 500
    assert "An unexpected error occurred." in exc_info.value.detail


# Additional tests can be added for other exceptions
