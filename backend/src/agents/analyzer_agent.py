from typing import Dict, Any, List
from .base_agent import BaseAgent
from crewai import Agent


class AnalyzerAgent(BaseAgent):
    def __init__(self, agent: Agent = None):
        if agent is None:
            agent = Agent(
                name="Analyzer",
                role="Health Data Analyzer",
                goal="Analyze health data to identify patterns and provide insights",
                backstory="An experienced health data analyst with expertise in identifying patterns and trends in health-related activities.",
                verbose=True
            )
        super().__init__(agent)

    def analyze_weekly_progress(self, weekly_data: List[Dict[str, Any]]) -> str:
        """Analyze weekly progress and provide insights."""
        if not weekly_data:
            raise ValueError("Weekly data cannot be empty")

        task = f"""Analyze this weekly health data: {weekly_data}
        Provide insights about progress, achievements, and areas for improvement."""
        return self.execute(task)

    def identify_behavior_patterns(self, monthly_data: List[Dict[str, Any]]) -> str:
        """Identify patterns in monthly health behavior data."""
        if not monthly_data:
            raise ValueError("Monthly data cannot be empty")

        task = f"""Analyze these monthly health patterns: {monthly_data}
        Identify trends, correlations, and behavioral patterns."""
        return self.execute(task)

    def generate_insights_report(self, data: List[Dict[str, Any]], goals: Dict[str, Any]) -> str:
        """Generate a comprehensive insights report."""
        if not data:
            raise ValueError("Data cannot be empty")
        if not goals:
            raise ValueError("Goals cannot be empty")

        task = f"""Generate an insights report based on this data and goals:
        Data: {data}
        Goals: {goals}
        
        Provide detailed analysis and recommendations."""
        return self.execute(task)
