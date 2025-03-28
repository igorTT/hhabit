from typing import Dict, Any
from .base_agent import BaseAgent
from crewai import Agent


class PlannerAgent(BaseAgent):
    def __init__(self, agent: Agent = None):
        if agent is None:
            agent = Agent(
                name="Planner",
                role="Health and Wellness Planner",
                goal="Create and adjust personalized health and wellness plans",
                backstory="An experienced health and wellness planner with expertise in creating balanced, achievable plans.",
                verbose=True
            )
        super().__init__(agent)

    def create_daily_plan(self, preferences: Dict[str, Any]) -> str:
        """Create a daily plan based on user preferences."""
        if not preferences:
            raise ValueError("Preferences cannot be empty")

        task = f"""Create a daily plan based on these preferences: {preferences}
        The plan should include specific times and activities for exercise, meditation, nutrition, and sleep."""
        return self.execute(task)

    def adjust_plan(self, performance: Dict[str, Any]) -> str:
        """Adjust the plan based on performance data."""
        if not isinstance(performance, dict) or not all(key in performance for key in ["exercise", "meditation", "nutrition", "sleep"]):
            raise ValueError("Invalid performance data format")

        task = f"""Analyze this performance data and suggest plan adjustments: {performance}
        Consider completion rates and durations to optimize the plan."""
        return self.execute(task)
