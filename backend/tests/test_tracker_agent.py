"""
Test suite for the TrackerAgent class.

This module contains tests for the TrackerAgent, which is responsible for:
- Logging daily health and fitness data
- Generating daily progress reports
- Checking data consistency across time periods
- Handling edge cases and invalid inputs

The tests cover both successful operations and error handling scenarios.
"""

import pytest
from src.agents.tracker_agent import TrackerAgent
from unittest.mock import MagicMock


@pytest.fixture
def tracker_agent(mock_agent):
    """
    Creates a test instance of TrackerAgent.

    Returns:
        TrackerAgent: A configured instance for testing

    Note:
        Uses a mock agent to avoid actual API calls during testing
    """
    return TrackerAgent(mock_agent)


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
        This data includes both successful and missed goals to test
        consistency checking functionality
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


def test_log_daily_data(tracker_agent, sample_daily_data):
    """
    Test logging daily health tracking data.

    Expected behavior:
    - Successfully logs the provided daily data
    - Returns a non-empty string response
    - Response contains expected mock content

    Preconditions:
    - Valid tracker_agent instance
    - Valid daily data structure

    Postconditions:
    - Data is processed without errors
    - Response is properly formatted
    """
    result = tracker_agent.log_daily_data(sample_daily_data)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Mocked agent response" in result


def test_generate_daily_report(tracker_agent, sample_daily_data):
    """
    Test generating a daily progress report.

    Expected behavior:
    - Creates a formatted report from daily data
    - Returns a non-empty string response
    - Response contains expected mock content

    Preconditions:
    - Valid tracker_agent instance
    - Valid daily data structure

    Postconditions:
    - Report is generated without errors
    - Response is properly formatted
    """
    result = tracker_agent.generate_daily_report(sample_daily_data)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Mocked agent response" in result


def test_check_consistency(tracker_agent, sample_weekly_data):
    """
    Test checking data consistency across time periods.

    Expected behavior:
    - Analyzes weekly data for patterns and inconsistencies
    - Returns a non-empty string response
    - Response contains expected mock content

    Preconditions:
    - Valid tracker_agent instance
    - Valid weekly data structure with multiple days

    Postconditions:
    - Consistency check completes without errors
    - Response is properly formatted
    """
    result = tracker_agent.check_consistency(sample_weekly_data)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Mocked agent response" in result


def test_empty_daily_data(tracker_agent):
    """
    Test handling of empty daily data input.

    Expected behavior:
    - Raises ValueError when empty data is provided
    - Prevents logging of invalid data

    Preconditions:
    - Valid tracker_agent instance
    - Empty dictionary as input

    Postconditions:
    - Exception is raised with appropriate message
    - No data is logged
    """
    with pytest.raises(ValueError):
        tracker_agent.log_daily_data({})


def test_invalid_weekly_data(tracker_agent):
    """
    Test handling of invalid weekly data input.

    Expected behavior:
    - Raises ValueError when empty list is provided
    - Prevents consistency check on invalid data

    Preconditions:
    - Valid tracker_agent instance
    - Empty list as input

    Postconditions:
    - Exception is raised with appropriate message
    - No consistency check is performed
    """
    with pytest.raises(ValueError):
        tracker_agent.check_consistency([])
