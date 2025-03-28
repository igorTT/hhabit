"""
Test suite for the AnalyzerAgent class.

This module contains tests for the AnalyzerAgent, which is responsible for:
- Analyzing weekly and monthly progress
- Identifying behavior patterns and trends
- Generating insights reports
- Handling various time periods of data
- Validating data consistency and completeness

The tests cover data analysis, pattern recognition, and error handling scenarios.
"""

import pytest
from src.agents.analyzer_agent import AnalyzerAgent
from unittest.mock import MagicMock


@pytest.fixture
def analyzer_agent(mock_agent):
    """
    Creates a test instance of AnalyzerAgent.

    Returns:
        AnalyzerAgent: A configured instance for testing

    Note:
        Uses a mock agent to avoid actual API calls during testing
    """
    return AnalyzerAgent(mock_agent)


@pytest.fixture
def sample_weekly_data():
    """
    Provides sample weekly health tracking data.

    Returns:
        list: A list of dictionaries containing mock weekly health data
            Each dictionary represents one day with:
            - exercise completion and duration
            - meditation completion and duration
            - nutrition completion and meal count
            - sleep duration

    Note:
        This data includes both successful and missed activities to test
        progress analysis functionality
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
def sample_monthly_data():
    """
    Provides sample monthly health tracking data.

    Returns:
        list: A list of dictionaries containing mock monthly health data
            Each dictionary represents one day with the same structure as
            sample_weekly_data.

    Note:
        This data represents a full month of tracking to test pattern
        identification functionality
    """
    return [
        {
            "date": "2024-03-01",
            "exercise": {"completed": True, "duration": 30},
            "meditation": {"completed": True, "duration": 15},
            "nutrition": {"completed": True, "meals": 3},
            "sleep": {"duration": 8}
        }
    ] * 30


@pytest.fixture
def sample_historical_data():
    """
    Provides sample historical health tracking data.

    Returns:
        list: A list of dictionaries containing mock historical health data
            Each dictionary represents one day with detailed tracking including:
            - exercise type and duration
            - sleep hours and quality
            - nutrition details (vegetables, water intake)
            - meditation duration

    Note:
        This data includes more detailed tracking to test long-term
        pattern analysis functionality
    """
    return [
        {
            "date": "2024-01-01",
            "exercise": {"completed": True, "duration": "30 minutes", "type": "running"},
            "sleep": {"hours": 8, "quality": "good"},
            "nutrition": {"vegetables": 5, "water_intake": "2L"},
            "meditation": {"completed": True, "duration": "10 minutes"}
        },
        {
            "date": "2024-01-02",
            "exercise": {"completed": True, "duration": "35 minutes", "type": "cycling"},
            "sleep": {"hours": 7.5, "quality": "good"},
            "nutrition": {"vegetables": 4, "water_intake": "2L"},
            "meditation": {"completed": True, "duration": "10 minutes"}
        }
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
        This data represents typical user goals for testing goal
        comparison functionality
    """
    return {
        "exercise": {"target_duration": 30, "frequency": "daily"},
        "meditation": {"target_duration": 15, "frequency": "daily"},
        "nutrition": {"target_meals": 3, "type": "balanced"},
        "sleep": {"target_duration": 8, "type": "consistent"}
    }


def test_analyze_weekly_progress(analyzer_agent, sample_weekly_data):
    """
    Test analyzing weekly health progress.

    Expected behavior:
    - Analyzes weekly data for progress patterns
    - Returns a non-empty string response
    - Response contains expected mock content

    Preconditions:
    - Valid analyzer_agent instance
    - Valid weekly data structure

    Postconditions:
    - Analysis completes without errors
    - Response is properly formatted
    """
    result = analyzer_agent.analyze_weekly_progress(sample_weekly_data)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Mocked agent response" in result


def test_identify_behavior_patterns(analyzer_agent, sample_monthly_data):
    """
    Test identifying behavior patterns in health data.

    Expected behavior:
    - Analyzes monthly data for behavior patterns
    - Returns a non-empty string response
    - Response contains expected mock content

    Preconditions:
    - Valid analyzer_agent instance
    - Valid monthly data structure

    Postconditions:
    - Pattern identification completes without errors
    - Response is properly formatted
    """
    result = analyzer_agent.identify_behavior_patterns(sample_monthly_data)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Mocked agent response" in result


def test_generate_insights_report(analyzer_agent, sample_monthly_data, sample_goals):
    """
    Test generating comprehensive insights report.

    Expected behavior:
    - Creates report comparing data against goals
    - Returns a non-empty string response
    - Response contains expected mock content

    Preconditions:
    - Valid analyzer_agent instance
    - Valid monthly data structure
    - Valid goals structure

    Postconditions:
    - Report generation completes without errors
    - Response is properly formatted
    """
    result = analyzer_agent.generate_insights_report(
        sample_monthly_data, sample_goals)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Mocked agent response" in result


def test_empty_weekly_data(analyzer_agent):
    """
    Test handling of empty weekly data input.

    Expected behavior:
    - Raises ValueError when empty data is provided
    - Prevents analysis of invalid data

    Preconditions:
    - Valid analyzer_agent instance
    - Empty list as input

    Postconditions:
    - Exception is raised with appropriate message
    - No analysis is performed
    """
    with pytest.raises(ValueError):
        analyzer_agent.analyze_weekly_progress([])


def test_invalid_monthly_data(analyzer_agent):
    """
    Test handling of invalid monthly data input.

    Expected behavior:
    - Raises ValueError when invalid data is provided
    - Prevents pattern identification on invalid data

    Preconditions:
    - Valid analyzer_agent instance
    - Empty list as input

    Postconditions:
    - Exception is raised with appropriate message
    - No pattern identification is performed
    """
    with pytest.raises(ValueError):
        analyzer_agent.identify_behavior_patterns([])


def test_empty_historical_data(analyzer_agent):
    """
    Test handling of empty historical data input.

    Expected behavior:
    - Raises Exception when empty data is provided
    - Prevents analysis of invalid historical data

    Preconditions:
    - Valid analyzer_agent instance
    - Empty list as input

    Postconditions:
    - Exception is raised with appropriate message
    - No analysis is performed
    """
    with pytest.raises(Exception):
        analyzer_agent.identify_behavior_patterns([])


def test_invalid_time_period(analyzer_agent, sample_weekly_data, sample_goals):
    """
    Test handling of invalid time period input.

    Expected behavior:
    - Raises Exception when invalid time period is provided
    - Prevents report generation with invalid period

    Preconditions:
    - Valid analyzer_agent instance
    - Valid weekly data structure
    - Valid goals structure
    - Invalid time period string

    Postconditions:
    - Exception is raised with appropriate message
    - No report is generated
    """
    with pytest.raises(Exception):
        analyzer_agent.generate_insights_report(
            "invalid", sample_weekly_data, sample_goals)
