from datetime import datetime, timedelta
from typing import Dict, Any, List
from src.agents import PlannerAgent, TrackerAgent, AnalyzerAgent, MotivatorAgent


def example_workflow():
    # Initialize agents
    planner = PlannerAgent()
    tracker = TrackerAgent()
    analyzer = AnalyzerAgent()
    motivator = MotivatorAgent()

    # Example user preferences
    user_preferences = {
        "exercise_goals": "30 minutes daily",
        "sleep_goals": "8 hours per night",
        "nutrition_goals": "balanced diet with 5 servings of vegetables",
        "stress_management": "10 minutes meditation daily",
        "current_fitness_level": "intermediate",
        "preferred_exercise_time": "morning"
    }

    # 1. Create weekly plan
    print("\n=== Creating Weekly Plan ===")
    weekly_plan = planner.create_weekly_plan(user_preferences)
    print(weekly_plan)

    # 2. Log daily data
    print("\n=== Logging Daily Data ===")
    daily_data = {
        "exercise": {"completed": True, "duration": "35 minutes", "type": "running"},
        "sleep": {"hours": 7.5, "quality": "good"},
        "nutrition": {"vegetables": 4, "water_intake": "2L"},
        "meditation": {"completed": True, "duration": "10 minutes"}
    }
    daily_log = tracker.log_daily_data(daily_data)
    print(daily_log)

    # 3. Generate daily report
    print("\n=== Generating Daily Report ===")
    daily_report = tracker.generate_daily_report(datetime.now(), daily_data)
    print(daily_report)

    # 4. Analyze weekly progress
    print("\n=== Analyzing Weekly Progress ===")
    weekly_data = [
        daily_data,
        # Add more daily data entries here
    ]
    weekly_analysis = analyzer.analyze_weekly_progress(weekly_data)
    print(weekly_analysis)

    # 5. Provide daily motivation
    print("\n=== Providing Daily Motivation ===")
    recent_achievements = [
        "Completed 5 days of consistent exercise", "Improved sleep quality"]
    motivation = motivator.provide_daily_motivation(
        daily_data, recent_achievements)
    print(motivation)

    # 6. Suggest challenges
    print("\n=== Suggesting Challenges ===")
    current_goals = {
        "exercise": "30 minutes daily",
        "sleep": "8 hours per night",
        "nutrition": "5 servings of vegetables"
    }
    challenges = motivator.suggest_challenges(user_preferences, current_goals)
    print(challenges)

    # 7. Generate insights report
    print("\n=== Generating Monthly Insights Report ===")
    monthly_data = weekly_data * 4  # Example monthly data
    insights = analyzer.generate_insights_report(
        "month", monthly_data, current_goals)
    print(insights)

    # 8. Celebrate achievement
    print("\n=== Celebrating Achievement ===")
    achievement = "Completed 30 days of consistent meditation"
    celebration = motivator.generate_celebration_message(
        achievement, daily_data)
    print(celebration)


if __name__ == "__main__":
    example_workflow()
