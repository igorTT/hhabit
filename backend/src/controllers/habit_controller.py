from typing import List, Optional
from uuid import UUID
from src.models.habit import Habit, HabitCreate, HabitUpdate
from src.services.habit_service import HabitService


class HabitController:
    def __init__(self):
        self.habit_service = HabitService()

    async def get_all_habits(self) -> List[Habit]:
        """Get all habits for the current user"""
        return await self.habit_service.get_all_habits()

    async def get_habit(self, habit_id: UUID) -> Optional[Habit]:
        """Get a specific habit by ID"""
        return await self.habit_service.get_habit(habit_id)

    async def create_habit(self, habit: HabitCreate) -> Habit:
        """Create a new habit"""
        return await self.habit_service.create_habit(habit)

    async def update_habit(self, habit_id: UUID, habit: HabitUpdate) -> Optional[Habit]:
        """Update an existing habit"""
        return await self.habit_service.update_habit(habit_id, habit)

    async def delete_habit(self, habit_id: UUID) -> bool:
        """Delete a habit"""
        return await self.habit_service.delete_habit(habit_id)

    async def complete_habit(self, habit_id: UUID) -> Optional[Habit]:
        """Mark a habit as completed"""
        return await self.habit_service.complete_habit(habit_id)

    async def get_habit_stats(self, habit_id: UUID) -> dict:
        """Get statistics for a specific habit"""
        return await self.habit_service.get_habit_stats(habit_id)
