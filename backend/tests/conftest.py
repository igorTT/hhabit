"""
Test configuration and fixtures for the HealthHabit test suite.

This module provides comprehensive test setup and teardown functionality for the
HealthHabit application. It includes:

1. Core Test Infrastructure:
   - FastAPI test client configuration
   - HabitService test instance management
   - Database cleanup utilities

2. Mock Objects:
   - OpenAI API response mocks
   - CrewAI agent, task, and crew mocks
   - Message and choice simulation classes

3. Environment Setup:
   - Test environment variable configuration
   - API key and endpoint management
   - Automatic cleanup procedures

The fixtures are designed to provide a consistent, isolated testing environment
for all test modules in the suite.
"""

import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.services.habit_service import HabitService
import os
from unittest.mock import patch, MagicMock
from crewai import Agent, Task, Crew


@pytest.fixture
def test_client():
    """
    Creates a test client for the FastAPI application.

    Returns:
        TestClient: A configured test client instance

    Note:
        Uses the main FastAPI app instance.
        Automatically handles request/response cycle.
        Provides a clean environment for each test.
    """
    return TestClient(app)


@pytest.fixture
def habit_service():
    """
    Creates a test instance of HabitService.

    Returns:
        HabitService: A clean instance for testing

    Note:
        Clears any existing data before each test.
        Ensures tests start with a clean state.
        Provides isolation between test cases.
    """
    service = HabitService()
    # Clear any existing data
    service.habits = {}
    return service


@pytest.fixture(autouse=True)
def setup_test_environment():
    """
    Sets up test environment variables.

    Expected behavior:
    - Configures required environment variables
    - Provides test API keys and endpoints
    - Automatically cleans up after tests

    Preconditions:
    - None (autouse fixture)

    Postconditions:
    - Environment variables are restored
    - Test environment is properly configured
    """
    with patch.dict(os.environ, {
        'OPENAI_API_KEY': 'test-api-key',
        'OPENAI_API_BASE': 'https://api.openai.com/v1',
    }):
        yield


class MockMessage:
    """
    Simulates an OpenAI API message response.

    Attributes:
        content (str): The message content

    Note:
        Used for mocking OpenAI API responses
        in test scenarios
    """

    def __init__(self, content):
        self.content = content


class MockChoice:
    """
    Simulates an OpenAI API choice response.

    Attributes:
        message (MockMessage): The associated message

    Note:
        Used for mocking OpenAI API responses
        in test scenarios
    """

    def __init__(self, content):
        self.message = MockMessage(content)


@pytest.fixture(autouse=True)
def mock_openai_completion():
    """
    Mocks OpenAI API completion calls.

    Expected behavior:
    - Intercepts OpenAI API calls
    - Returns mock response data
    - Simulates successful completion

    Preconditions:
    - None (autouse fixture)

    Postconditions:
    - Mock is properly cleaned up
    - API calls are intercepted
    """
    mock_response = MagicMock()
    mock_response.choices = [MockChoice("Mocked response for testing")]
    mock_response.model_dump = MagicMock(return_value={
        "id": "test-id",
        "object": "chat.completion",
        "created": 1234567890,
        "model": "gpt-4",
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "Mocked response for testing"
                },
                "finish_reason": "stop",
                "index": 0
            }
        ]
    })

    with patch('litellm.completion', return_value=mock_response) as mock:
        yield mock


@pytest.fixture(autouse=True)
def mock_crewai_agent():
    """
    Mocks CrewAI agent execution.

    Expected behavior:
    - Intercepts CrewAI agent task execution
    - Returns mock response data
    - Simulates successful task completion

    Preconditions:
    - None (autouse fixture)

    Postconditions:
    - Mock is properly cleaned up
    - Agent execution is intercepted
    """
    with patch('crewai.agent.Agent.execute_task', return_value="Mocked agent response") as mock:
        yield mock


@pytest.fixture
def mock_agent():
    """
    Creates a mock CrewAI agent for testing.

    Returns:
        MagicMock: A configured mock agent with:
            - Basic attributes (name, role, goal, etc.)
            - Mocked execution method
            - Empty tools list

    Note:
        Provides a consistent mock agent for
        testing agent interactions
    """
    agent = MagicMock(spec=Agent)
    agent.name = "Test Agent"
    agent.role = "Test Role"
    agent.goal = "Test Goal"
    agent.backstory = "Test Backstory"
    agent.verbose = False
    agent.max_rpm = None
    agent._rpm_controller = None
    agent._token_process = None
    agent.security_config = None
    agent.tools = []
    agent.execute_task = MagicMock(return_value="Mocked agent response")
    return agent


@pytest.fixture
def mock_task():
    """
    Creates a mock CrewAI task for testing.

    Returns:
        MagicMock: A configured mock task with:
            - Mocked execution method
            - Standard task attributes

    Note:
        Provides a consistent mock task for
        testing task execution
    """
    task = MagicMock(spec=Task)
    task.execute = MagicMock(return_value="Mocked task response")
    return task


@pytest.fixture
def mock_crew():
    """
    Creates a mock CrewAI crew for testing.

    Returns:
        MagicMock: A configured mock crew with:
            - Mocked kickoff method
            - Standard crew attributes

    Note:
        Provides a consistent mock crew for
        testing crew operations
    """
    crew = MagicMock(spec=Crew)
    crew.kickoff = MagicMock(return_value="Mocked crew response")
    return crew
