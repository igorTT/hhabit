from typing import Dict, Any, List
from .base_agent import BaseAgent
from crewai import Agent


class MotivatorAgent(BaseAgent):
    def __init__(self, agent: Agent = None):
        if agent is None:
            agent = Agent(
                name="Motivator",
                role="Health Motivation Specialist",
                goal="Provide motivation and encouragement for health goals",
                backstory="An experienced health coach with expertise in motivating individuals to achieve their health and wellness goals.",
                verbose=True
            )
        super().__init__(agent)

    def provide_daily_motivation(self, daily_data: Dict[str, Any], achievements: List[str]) -> str:
        """Provide daily motivation based on progress and achievements."""
        if not daily_data:
            raise ValueError("Daily data cannot be empty")

        task = f"""Provide motivation based on this daily progress and achievements:
        Daily Data: {daily_data}
        Recent Achievements: {achievements}
        
        Offer encouragement and celebrate progress."""
        return self.execute(task)

    def suggest_challenges(self, weekly_data: List[Dict[str, Any]], goals: Dict[str, Any]) -> str:
        """Suggest new challenges based on progress and goals."""
        if not weekly_data:
            raise ValueError("Weekly data cannot be empty")
        if not goals:
            raise ValueError("Goals cannot be empty")

        task = f"""Suggest new challenges based on this progress and goals:
        Weekly Data: {weekly_data}
        Current Goals: {goals}
        
        Propose engaging challenges that align with current progress."""
        return self.execute(task)

    def generate_celebration_message(self, achievement: str, context: List[Dict[str, Any]]) -> str:
        """Generate a celebration message for a specific achievement."""
        if not achievement:
            raise ValueError("Achievement cannot be empty")

        task = f"""Generate a celebration message for this achievement:
        Achievement: {achievement}
        Context: {context}
        
        Create an inspiring and personalized celebration message."""
        return self.execute(task)
