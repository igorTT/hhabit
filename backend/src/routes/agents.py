from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List
from datetime import datetime
from src.agents import PlannerAgent, TrackerAgent, AnalyzerAgent, MotivatorAgent

router = APIRouter()

# Initialize agents
planner_agent = PlannerAgent()
tracker_agent = TrackerAgent()
analyzer_agent = AnalyzerAgent()
motivator_agent = MotivatorAgent()

# Planner Agent Routes


@router.post("/planner/weekly-plan")
async def create_weekly_plan(user_preferences: Dict[str, Any]):
    """Create a personalized weekly health plan"""
    try:
        return planner_agent.create_weekly_plan(user_preferences)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/planner/adjust-goals")
async def adjust_goals(current_goals: Dict[str, Any], performance_data: Dict[str, Any]):
    """Adjust goals based on performance"""
    try:
        return planner_agent.adjust_goals(current_goals, performance_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Tracker Agent Routes


@router.post("/tracker/log-daily")
async def log_daily_data(habit_data: Dict[str, Any]):
    """Log daily habit data"""
    try:
        return tracker_agent.log_daily_data(habit_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/tracker/daily-report")
async def generate_daily_report(date: datetime, habit_data: Dict[str, Any]):
    """Generate daily report"""
    try:
        return tracker_agent.generate_daily_report(date, habit_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/tracker/check-consistency")
async def check_consistency(weekly_data: List[Dict[str, Any]]):
    """Check habit consistency"""
    try:
        return tracker_agent.check_consistency(weekly_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Analyzer Agent Routes


@router.post("/analyzer/weekly-progress")
async def analyze_weekly_progress(weekly_data: List[Dict[str, Any]]):
    """Analyze weekly progress"""
    try:
        return analyzer_agent.analyze_weekly_progress(weekly_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyzer/behavior-patterns")
async def identify_behavior_patterns(historical_data: List[Dict[str, Any]]):
    """Identify behavior patterns"""
    try:
        return analyzer_agent.identify_behavior_patterns(historical_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyzer/insights-report")
async def generate_insights_report(
    time_period: str,
    data: List[Dict[str, Any]],
    goals: Dict[str, Any]
):
    """Generate insights report"""
    try:
        return analyzer_agent.generate_insights_report(time_period, data, goals)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Motivator Agent Routes


@router.post("/motivator/daily-motivation")
async def provide_daily_motivation(
    user_data: Dict[str, Any],
    recent_achievements: List[str]
):
    """Provide daily motivation"""
    try:
        return motivator_agent.provide_daily_motivation(user_data, recent_achievements)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/motivator/suggest-challenges")
async def suggest_challenges(
    user_preferences: Dict[str, Any],
    current_goals: Dict[str, Any]
):
    """Suggest health challenges"""
    try:
        return motivator_agent.suggest_challenges(user_preferences, current_goals)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/motivator/celebration")
async def generate_celebration_message(
    achievement: str,
    user_data: Dict[str, Any]
):
    """Generate celebration message"""
    try:
        return motivator_agent.generate_celebration_message(achievement, user_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
