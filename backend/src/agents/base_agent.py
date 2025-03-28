from crewai import Task, Agent, Crew
from typing import Optional, Dict, Any


class BaseAgent:
    def __init__(self, agent: Agent):
        self.agent = agent

    def execute(self, task: str) -> str:
        """Execute a task using the agent."""
        crewai_task = Task(
            description=task,
            expected_output="A detailed response based on the task description",
            agent=self.agent
        )
        return self.agent.execute_task(crewai_task)
