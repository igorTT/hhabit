from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from uuid import UUID, uuid4


class HabitBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    frequency: str = Field(..., pattern="^(daily|weekly|monthly)$")
    target_value: Optional[float] = None
    unit: Optional[str] = None
    reminder_time: Optional[str] = None  # Format: "HH:MM"


class HabitCreate(HabitBase):
    pass


class HabitUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    frequency: Optional[str] = Field(None, pattern="^(daily|weekly|monthly)$")
    target_value: Optional[float] = None
    unit: Optional[str] = None
    reminder_time: Optional[str] = None
    is_active: Optional[bool] = None


class Habit(HabitBase):
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID = Field(default_factory=uuid4)  # Default UUID for testing
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True
    streak: int = 0
    last_completed: Optional[datetime] = None

    class Config:
        from_attributes = True
