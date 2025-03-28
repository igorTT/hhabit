"""
Test suite for the PlannerAgent class.

This module contains tests for the PlannerAgent, which is responsible for:
- Creating personalized daily health and fitness plans
- Adjusting plans based on user performance
- Handling user preferences and constraints
- Managing plan modifications and updates

The tests cover plan creation, adjustment, and error handling scenarios.
"""

import pytest
from src.agents.planner_agent import PlannerAgent
from unittest.mock import MagicMock


@pytest.fixture
def planner_agent(mock_agent):
    """
    Creates a test instance of PlannerAgent.

    Returns:
        PlannerAgent: A configured instance for testing

    Note:
        Uses a mock agent to avoid actual API calls during testing
    """
    return PlannerAgent(mock_agent)


@pytest.fixture
def sample_preferences():
    """
    Provides sample user preferences for health planning.

    Returns:
        dict: A dictionary containing mock user preferences including:
            - exercise type and duration
            - meditation type and duration
            - nutrition type and meal count
            - sleep duration

    Note:
        This data represents typical user preferences for testing
    """
    return {
        "exercise": {"type": "running", "duration": 30},
        "meditation": {"type": "mindfulness", "duration": 15},
        "nutrition": {"type": "balanced", "meals": 3},
        "sleep": {"duration": 8}
    }


@pytest.fixture
def sample_performance():
    """
    Provides sample user performance data.

    Returns:
        dict: A dictionary containing mock performance data including:
            - exercise completion and duration
            - meditation completion and duration
            - nutrition completion and meal count
            - sleep duration

    Note:
        This data includes both completed and missed activities to test
        plan adjustment functionality
    """
    return {
        "exercise": {"completed": True, "duration": 25},
        "meditation": {"completed": False, "duration": 0},
        "nutrition": {"completed": True, "meals": 3},
        "sleep": {"duration": 7}
    }


def test_create_daily_plan(planner_agent, sample_preferences):
    """
    Test creating a personalized daily health plan.

    Expected behavior:
    - Generates a plan based on user preferences
    - Returns a non-empty string response
    - Response contains expected mock content

    Preconditions:
    - Valid planner_agent instance
    - Valid preferences structure

    Postconditions:
    - Plan is generated without errors
    - Response is properly formatted
    """
    result = planner_agent.create_daily_plan(sample_preferences)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Mocked agent response" in result


def test_adjust_plan(planner_agent, sample_performance):
    """
    Test adjusting a plan based on performance data.

    Expected behavior:
    - Modifies plan based on performance feedback
    - Returns a non-empty string response
    - Response contains expected mock content

    Preconditions:
    - Valid planner_agent instance
    - Valid performance data structure

    Postconditions:
    - Plan is adjusted without errors
    - Response is properly formatted
    """
    result = planner_agent.adjust_plan(sample_performance)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Mocked agent response" in result


def test_empty_preferences(planner_agent):
    """
    Test handling of empty preferences input.

    Expected behavior:
    - Raises ValueError when empty preferences are provided
    - Prevents creation of invalid plan

    Preconditions:
    - Valid planner_agent instance
    - Empty dictionary as input

    Postconditions:
    - Exception is raised with appropriate message
    - No plan is created
    """
    with pytest.raises(ValueError):
        planner_agent.create_daily_plan({})


def test_invalid_performance(planner_agent):
    """
    Test handling of invalid performance data input.

    Expected behavior:
    - Raises ValueError when invalid performance data is provided
    - Prevents plan adjustment with invalid data

    Preconditions:
    - Valid planner_agent instance
    - Invalid data structure as input

    Postconditions:
    - Exception is raised with appropriate message
    - No plan adjustment is performed
    """
    with pytest.raises(ValueError):
        planner_agent.adjust_plan({"invalid": "data"})
