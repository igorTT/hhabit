"""
Test suite for the MotivatorAgent class.

This module contains tests for the MotivatorAgent, which is responsible for:
- Providing daily motivation based on user progress
- Suggesting personalized challenges
- Generating celebration messages for achievements
- Handling various types of user data and goals
- Managing motivation strategies and feedback

The tests cover motivation generation, challenge suggestions, and error handling scenarios.
"""

import pytest
from src.agents.motivator_agent import MotivatorAgent
from unittest.mock import MagicMock


@pytest.fixture
def motivator_agent(mock_agent):
    """
    Creates a test instance of MotivatorAgent.

    Returns:
        MotivatorAgent: A configured instance for testing

    Note:
        Uses a mock agent to avoid actual API calls during testing
    """
    return MotivatorAgent(mock_agent)


@pytest.fixture
def sample_daily_data():
    """
    Provides sample daily health tracking data.

    Returns:
        dict: A dictionary containing mock daily health data including:
            - exercise completion and duration
            - meditation completion and duration
            - nutrition completion and meal count
            - sleep duration

    Note:
        This data represents a "perfect day" scenario for testing
        motivation generation
    """
    return {
        "exercise": {"completed": True, "duration": 30},
        "meditation": {"completed": True, "duration": 15},
        "nutrition": {"completed": True, "meals": 3},
        "sleep": {"duration": 8}
    }


@pytest.fixture
def sample_weekly_data():
    """
    Provides sample weekly health tracking data.

    Returns:
        list: A list of dictionaries containing mock weekly health data
            Each dictionary represents one day with the same structure as
            sample_daily_data, plus a date field.

    Note:
        This data includes both successful and missed activities to test
        challenge suggestion functionality
    """
    return [
        {
            "date": "2024-03-20",
            "exercise": {"completed": True, "duration": 30},
            "meditation": {"completed": True, "duration": 15},
            "nutrition": {"completed": True, "meals": 3},
            "sleep": {"duration": 8}
        },
        {
            "date": "2024-03-21",
            "exercise": {"completed": False, "duration": 0},
            "meditation": {"completed": True, "duration": 15},
            "nutrition": {"completed": True, "meals": 3},
            "sleep": {"duration": 7}
        }
    ]


@pytest.fixture
def sample_achievements():
    """
    Provides sample user achievements.

    Returns:
        list: A list of strings containing mock achievements including:
            - Exercise completion milestones
            - Sleep schedule consistency
            - Meditation practice streaks

    Note:
        This data represents typical user achievements for testing
        celebration message generation
    """
    return [
        "Completed 30 minutes of exercise",
        "Maintained consistent sleep schedule",
        "Practiced meditation daily"
    ]


@pytest.fixture
def sample_goals():
    """
    Provides sample health and fitness goals.

    Returns:
        dict: A dictionary containing mock goals including:
            - exercise target duration and frequency
            - meditation target duration and frequency
            - nutrition target meals and type
            - sleep target duration and type

    Note:
        This data represents typical user goals for testing
        challenge suggestion functionality
    """
    return {
        "exercise": {"target_duration": 30, "frequency": "daily"},
        "meditation": {"target_duration": 15, "frequency": "daily"},
        "nutrition": {"target_meals": 3, "type": "balanced"},
        "sleep": {"target_duration": 8, "type": "consistent"}
    }


def test_provide_daily_motivation(motivator_agent, sample_daily_data, sample_achievements):
    """
    Test providing daily motivation based on progress.

    Expected behavior:
    - Generates personalized motivation message
    - Returns a non-empty string response
    - Response contains expected mock content

    Preconditions:
    - Valid motivator_agent instance
    - Valid daily data structure
    - Valid achievements list

    Postconditions:
    - Motivation message is generated without errors
    - Response is properly formatted
    """
    result = motivator_agent.provide_daily_motivation(
        sample_daily_data, sample_achievements)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Mocked agent response" in result


def test_suggest_challenges(motivator_agent, sample_weekly_data, sample_goals):
    """
    Test suggesting personalized challenges.

    Expected behavior:
    - Generates challenge suggestions based on progress
    - Returns a non-empty string response
    - Response contains expected mock content

    Preconditions:
    - Valid motivator_agent instance
    - Valid weekly data structure
    - Valid goals structure

    Postconditions:
    - Challenge suggestions are generated without errors
    - Response is properly formatted
    """
    result = motivator_agent.suggest_challenges(
        sample_weekly_data, sample_goals)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Mocked agent response" in result


def test_generate_celebration_message(motivator_agent, sample_achievements):
    """
    Test generating celebration messages for achievements.

    Expected behavior:
    - Creates celebratory message for specific achievement
    - Returns a non-empty string response
    - Response contains expected mock content

    Preconditions:
    - Valid motivator_agent instance
    - Valid achievement string
    - Valid achievements list

    Postconditions:
    - Celebration message is generated without errors
    - Response is properly formatted
    """
    result = motivator_agent.generate_celebration_message(
        sample_achievements[0], [sample_achievements[0]])
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Mocked agent response" in result


def test_empty_daily_data(motivator_agent):
    """
    Test handling of empty daily data input.

    Expected behavior:
    - Raises ValueError when empty data is provided
    - Prevents motivation generation with invalid data

    Preconditions:
    - Valid motivator_agent instance
    - Empty dictionary as input
    - Empty achievements list

    Postconditions:
    - Exception is raised with appropriate message
    - No motivation message is generated
    """
    with pytest.raises(ValueError):
        motivator_agent.provide_daily_motivation({}, [])


def test_invalid_weekly_data(motivator_agent):
    """
    Test handling of invalid weekly data input.

    Expected behavior:
    - Raises ValueError when invalid data is provided
    - Prevents challenge suggestion with invalid data

    Preconditions:
    - Valid motivator_agent instance
    - Empty list as input
    - Empty goals dictionary

    Postconditions:
    - Exception is raised with appropriate message
    - No challenges are suggested
    """
    with pytest.raises(ValueError):
        motivator_agent.suggest_challenges([], {})
