"""
Base agent implementation using TogetherAI.
"""

from crewai import Task, Agent, Crew
from typing import Optional, Dict, Any
from src.config.ai_config import MODEL_CONFIG, SYSTEM_PROMPTS


class BaseAgent:
    def __init__(self, agent_type: str, agent: Agent):
        """
        Initialize a base agent with TogetherAI configuration.

        Args:
            agent_type (str): Type of agent (planner, tracker, analyzer, motivator)
            agent (Agent): CrewAI agent instance
        """
        self.agent_type = agent_type
        self.agent = agent
        self.system_prompt = SYSTEM_PROMPTS.get(agent_type, "")

        # Configure agent with TogetherAI settings
        self.agent.llm_config = {
            "config_list": [{
                "model": MODEL_CONFIG["model"],
                "api_key": MODEL_CONFIG.get("api_key"),
                "base_url": "https://api.together.xyz/v1",
                "api_type": "together",
                "max_tokens": MODEL_CONFIG["max_tokens"],
                "temperature": MODEL_CONFIG["temperature"],
                "top_p": MODEL_CONFIG["top_p"],
                "top_k": MODEL_CONFIG["top_k"],
                "repetition_penalty": MODEL_CONFIG["repetition_penalty"],
                "stop": MODEL_CONFIG["stop"]
            }]
        }

    def execute(self, task: str) -> str:
        """
        Execute a task using the agent with TogetherAI.

        Args:
            task (str): Task description

        Returns:
            str: Agent's response
        """
        crewai_task = Task(
            description=f"{self.system_prompt}\n\nTask: {task}",
            expected_output="A detailed response based on the task description",
            agent=self.agent
        )
        return self.agent.execute_task(crewai_task)
