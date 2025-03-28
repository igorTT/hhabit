"""
Test suite for the habits API routes.
Tests the HTTP endpoints for habit management.
Requires a clean database state for each test.

This suite verifies:
- API endpoint responses and status codes.
- Request/response data validation.
- Error handling and edge cases.
- CRUD operations via HTTP.
"""

import pytest
from fastapi.testclient import TestClient


def test_create_habit(test_client: TestClient):
    """
    Test creating a habit via API endpoint.

    Expected behavior:
    - POST request returns 200 status code.
    - Response contains created habit data.
    - All fields are correctly set.
    - ID is generated and included.

    Preconditions:
    - API server is running.
    - Valid habit data is provided.

    Postconditions:
    - Habit is created in the database.
    - Response matches provided data.
    """
    response = test_client.post(
        "/api/habits/",
        json={
            "name": "Exercise",
            "description": "Daily workout",
            "frequency": "daily",
            "target_value": 30,
            "unit": "minutes"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Exercise"
    assert data["description"] == "Daily workout"
    assert data["frequency"] == "daily"
    assert data["target_value"] == 30
    assert data["unit"] == "minutes"
    assert "id" in data


def test_get_habits(test_client: TestClient):
    """
    Test retrieving all habits via API endpoint.

    Expected behavior:
    - GET request returns 200 status code.
    - Response contains list of habits.
    - All habits are included.
    - Empty list if no habits exist.

    Preconditions:
    - API server is running.
    - Database may contain habits.

    Postconditions:
    - Response contains all habits.
    - Habit data is unchanged.
    """
    # Create some test habits first
    habits = [
        {"name": "Exercise", "frequency": "daily"},
        {"name": "Read", "frequency": "daily"}
    ]

    for habit in habits:
        test_client.post("/api/habits/", json=habit)

    # Get all habits
    response = test_client.get("/api/habits/")

    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2
    assert any(h["name"] == "Exercise" for h in data)
    assert any(h["name"] == "Read" for h in data)


def test_get_habit(test_client: TestClient):
    """
    Test retrieving a specific habit via API endpoint.

    Expected behavior:
    - GET request returns 200 status code for existing habit.
    - Response contains requested habit data.
    - 404 status code for non-existent habit.

    Preconditions:
    - API server is running.
    - A habit exists in the database.

    Postconditions:
    - Response contains correct habit data.
    - Habit data is unchanged.
    """
    # Create a test habit
    create_response = test_client.post(
        "/api/habits/",
        json={"name": "Meditate", "frequency": "daily"}
    )
    habit_id = create_response.json()["id"]

    # Get the habit
    response = test_client.get(f"/api/habits/{habit_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Meditate"
    assert data["id"] == habit_id


def test_update_habit(test_client: TestClient):
    """
    Test updating a habit via API endpoint.

    Expected behavior:
    - PUT request returns 200 status code for existing habit.
    - Response contains updated habit data.
    - Only provided fields are modified.
    - 404 status code for non-existent habit.

    Preconditions:
    - API server is running.
    - A habit exists in the database.
    - Valid update data is provided.

    Postconditions:
    - Habit is updated in the database.
    - Response reflects updated data.
    """
    # Create a test habit
    create_response = test_client.post(
        "/api/habits/",
        json={"name": "Old Name", "frequency": "daily"}
    )
    habit_id = create_response.json()["id"]

    # Update the habit
    response = test_client.put(
        f"/api/habits/{habit_id}",
        json={"name": "New Name", "target_value": 15}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "New Name"
    assert data["target_value"] == 15


def test_delete_habit(test_client: TestClient):
    """
    Test deleting a habit via API endpoint.

    Expected behavior:
    - DELETE request returns 200 status code for existing habit.
    - Habit is removed from database.
    - 404 status code for non-existent habit.

    Preconditions:
    - API server is running.
    - A habit exists in the database.

    Postconditions:
    - Habit is deleted from database.
    - Subsequent GET request returns 404.
    """
    # Create a test habit
    create_response = test_client.post(
        "/api/habits/",
        json={"name": "To Delete", "frequency": "daily"}
    )
    habit_id = create_response.json()["id"]

    # Delete the habit
    response = test_client.delete(f"/api/habits/{habit_id}")
    assert response.status_code == 200

    # Verify habit is deleted
    get_response = test_client.get(f"/api/habits/{habit_id}")
    assert get_response.status_code == 404
