import json
from typing import List, Optional
from uuid import UUID
from datetime import datetime
from pathlib import Path
from src.models.habit import Habit, HabitCreate, HabitUpdate


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


class HabitService:
    def __init__(self):
        self.data_file = Path("data/habits.json")
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        self._load_data()

    def _load_data(self):
        """Load habits data from JSON file"""
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                self.habits = {UUID(k): Habit(**v)
                               for k, v in json.load(f).items()}
        else:
            self.habits = {}

    def _save_data(self):
        """Save habits data to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump({str(k): v.model_dump()
                      for k, v in self.habits.items()}, f, cls=UUIDEncoder)

    async def get_all_habits(self) -> List[Habit]:
        """Get all habits"""
        return list(self.habits.values())

    async def get_habit(self, habit_id: UUID) -> Optional[Habit]:
        """Get a specific habit by ID"""
        return self.habits.get(habit_id)

    async def create_habit(self, habit: HabitCreate) -> Habit:
        """Create a new habit"""
        new_habit = Habit(**habit.model_dump())
        self.habits[new_habit.id] = new_habit
        self._save_data()
        return new_habit

    async def update_habit(self, habit_id: UUID, habit: HabitUpdate) -> Optional[Habit]:
        """Update an existing habit"""
        if habit_id not in self.habits:
            return None

        existing_habit = self.habits[habit_id]
        update_data = habit.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(existing_habit, field, value)

        existing_habit.updated_at = datetime.utcnow()
        self._save_data()
        return existing_habit

    async def delete_habit(self, habit_id: UUID) -> bool:
        """Delete a habit"""
        if habit_id in self.habits:
            del self.habits[habit_id]
            self._save_data()
            return True
        return False

    async def complete_habit(self, habit_id: UUID) -> Optional[Habit]:
        """Mark a habit as completed"""
        if habit_id not in self.habits:
            return None

        habit = self.habits[habit_id]
        habit.last_completed = datetime.utcnow()
        habit.streak += 1
        self._save_data()
        return habit

    async def get_habit_stats(self, habit_id: UUID) -> dict:
        """Get statistics for a specific habit"""
        if habit_id not in self.habits:
            return {}

        habit = self.habits[habit_id]
        return {
            "streak": habit.streak,
            "last_completed": habit.last_completed,
            "created_at": habit.created_at,
            "completion_rate": self._calculate_completion_rate(habit)
        }

    def _calculate_completion_rate(self, habit: Habit) -> float:
        """Calculate the completion rate for a habit"""
        # This is a simplified version. In a real application,
        # you would want to track actual completions over time
        if not habit.last_completed:
            return 0.0
        return 1.0  # Placeholder
