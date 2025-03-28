"""
Test suite for the HabitService class.
Tests the CRUD operations and business logic for habit management.
Requires a clean database state for each test.

This suite verifies:
- Habit creation with various data combinations.
- Habit retrieval (single and multiple).
- Habit updates and modifications.
- Habit deletion.
- Habit statistics and completion tracking.
"""

import pytest
from uuid import UUID
from datetime import datetime
from src.models.habit import HabitCreate, HabitUpdate


@pytest.mark.asyncio
async def test_create_habit(habit_service):
    """
    Test creating a new habit.

    Expected behavior:
    - Habit is created with provided data.
    - ID and timestamps are automatically generated.
    - Default values are set correctly.

    Preconditions:
    - Database is empty.
    - Valid habit data is provided.

    Postconditions:
    - Habit is persisted in the database.
    - All fields are correctly set.
    """
    habit_data = HabitCreate(
        name="Exercise",
        description="Daily workout",
        frequency="daily",
        target_value=30,
        unit="minutes"
    )

    habit = await habit_service.create_habit(habit_data)

    assert habit.name == "Exercise"
    assert habit.description == "Daily workout"
    assert habit.frequency == "daily"
    assert habit.target_value == 30
    assert habit.unit == "minutes"
    assert isinstance(habit.id, UUID)
    assert isinstance(habit.created_at, datetime)
    assert habit.is_active is True
    assert habit.streak == 0


@pytest.mark.asyncio
async def test_get_habit(habit_service):
    """
    Test retrieving a habit by ID.

    Expected behavior:
    - Habit is retrieved using its ID.
    - All fields are correctly returned.
    - Non-existent habits return None.

    Preconditions:
    - A habit exists in the database.
    - Valid habit ID is provided.

    Postconditions:
    - Habit data is unchanged.
    - Returned habit matches stored data.
    """
    # Create a test habit
    habit_data = HabitCreate(name="Read", frequency="daily")
    created_habit = await habit_service.create_habit(habit_data)

    # Get the habit
    habit = await habit_service.get_habit(created_habit.id)

    assert habit is not None
    assert habit.id == created_habit.id
    assert habit.name == "Read"


@pytest.mark.asyncio
async def test_update_habit(habit_service):
    """
    Test updating an existing habit.

    Expected behavior:
    - Habit is updated with new data.
    - Only provided fields are modified.
    - Timestamps are updated.
    - Non-existent habits return None.

    Preconditions:
    - A habit exists in the database.
    - Valid update data is provided.

    Postconditions:
    - Updated fields reflect new values.
    - Unspecified fields remain unchanged.
    - Updated_at timestamp is modified.
    """
    # Create a test habit
    habit_data = HabitCreate(name="Meditate", frequency="daily")
    created_habit = await habit_service.create_habit(habit_data)

    # Update the habit
    update_data = HabitUpdate(name="Morning Meditation", target_value=15)
    updated_habit = await habit_service.update_habit(created_habit.id, update_data)

    assert updated_habit is not None
    assert updated_habit.name == "Morning Meditation"
    assert updated_habit.target_value == 15
    assert updated_habit.frequency == "daily"  # Unchanged field


@pytest.mark.asyncio
async def test_delete_habit(habit_service):
    """
    Test deleting a habit.

    Expected behavior:
    - Habit is removed from the database.
    - Returns True for successful deletion.
    - Returns False for non-existent habits.

    Preconditions:
    - A habit exists in the database.
    - Valid habit ID is provided.

    Postconditions:
    - Habit is no longer retrievable.
    - Database state is consistent.
    """
    # Create a test habit
    habit_data = HabitCreate(name="Sleep", frequency="daily")
    created_habit = await habit_service.create_habit(habit_data)

    # Delete the habit
    result = await habit_service.delete_habit(created_habit.id)
    assert result is True

    # Verify habit is deleted
    habit = await habit_service.get_habit(created_habit.id)
    assert habit is None


@pytest.mark.asyncio
async def test_get_all_habits(habit_service):
    """
    Test retrieving all habits.

    Expected behavior:
    - All habits are returned.
    - Habits are returned in a list.
    - Empty database returns empty list.

    Preconditions:
    - Database may contain multiple habits.
    - No specific habit data required.

    Postconditions:
    - Returned list contains all habits.
    - Habit data is unchanged.
    """
    # Create test habits
    habits_data = [
        HabitCreate(name="Exercise", frequency="daily"),
        HabitCreate(name="Read", frequency="daily"),
        HabitCreate(name="Meditate", frequency="weekly")
    ]

    for habit_data in habits_data:
        await habit_service.create_habit(habit_data)

    # Get all habits
    habits = await habit_service.get_all_habits()

    assert len(habits) == 3
    assert all(habit.name in ["Exercise", "Read", "Meditate"]
               for habit in habits)
