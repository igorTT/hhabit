from typing import Dict, Any, List
from .base_agent import BaseAgent
from crewai import Agent


class TrackerAgent(BaseAgent):
    def __init__(self, agent: Agent = None):
        if agent is None:
            agent = Agent(
                name="Tracker",
                role="Health Habit Tracker",
                goal="Track and analyze daily health habits and progress",
                backstory="An experienced health habit tracker with expertise in monitoring and analyzing health-related activities.",
                verbose=True
            )
        super().__init__(agent)

    def log_daily_data(self, data: Dict[str, Any]) -> str:
        """Log daily health and wellness data."""
        if not data:
            raise ValueError("Daily data cannot be empty")

        task = f"""Log and analyze this daily health data: {data}
        Provide a summary of the logged activities and their completion status."""
        return self.execute(task)

    def generate_daily_report(self, data: Dict[str, Any]) -> str:
        """Generate a daily report based on logged data."""
        if not data:
            raise ValueError("Daily data cannot be empty")

        task = f"""Generate a detailed daily report for this data: {data}
        Include insights about exercise, meditation, nutrition, and sleep patterns."""
        return self.execute(task)

    def check_consistency(self, weekly_data: List[Dict[str, Any]]) -> str:
        """Check consistency of weekly health data."""
        if not weekly_data:
            raise ValueError("Weekly data cannot be empty")

        task = f"""Analyze the consistency of this weekly health data: {weekly_data}
        Identify patterns, trends, and areas for improvement."""
        return self.execute(task)
