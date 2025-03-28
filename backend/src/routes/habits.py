from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from src.models.habit import Habit, HabitCreate, HabitUpdate
from src.controllers.habit_controller import HabitController

router = APIRouter()
habit_controller = HabitController()


@router.get("/", response_model=List[Habit])
async def get_habits():
    """Get all habits for the current user"""
    return await habit_controller.get_all_habits()


@router.get("/{habit_id}", response_model=Habit)
async def get_habit(habit_id: str):
    """Get a specific habit by ID"""
    try:
        uuid = UUID(habit_id)
        habit = await habit_controller.get_habit(uuid)
        if not habit:
            raise HTTPException(status_code=404, detail="Habit not found")
        return habit
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid habit ID format")


@router.post("/", response_model=Habit)
async def create_habit(habit: HabitCreate):
    """Create a new habit"""
    return await habit_controller.create_habit(habit)


@router.put("/{habit_id}", response_model=Habit)
async def update_habit(habit_id: str, habit: HabitUpdate):
    """Update an existing habit"""
    try:
        uuid = UUID(habit_id)
        updated_habit = await habit_controller.update_habit(uuid, habit)
        if not updated_habit:
            raise HTTPException(status_code=404, detail="Habit not found")
        return updated_habit
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid habit ID format")


@router.delete("/{habit_id}")
async def delete_habit(habit_id: str):
    """Delete a habit"""
    try:
        uuid = UUID(habit_id)
        success = await habit_controller.delete_habit(uuid)
        if not success:
            raise HTTPException(status_code=404, detail="Habit not found")
        return {"message": "Habit deleted successfully"}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid habit ID format")
