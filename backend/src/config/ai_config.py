"""
Configuration settings for AI model integration.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# TogetherAI Configuration
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
MODEL_NAME = os.getenv(
    "MODEL_NAME", "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "4096"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

# Model Configuration
MODEL_CONFIG = {
    "model": MODEL_NAME,
    "max_tokens": MAX_TOKENS,
    "temperature": TEMPERATURE,
    "top_p": 0.95,
    "top_k": 40,
    "repetition_penalty": 1.1,
    "stop": ["</s>", "Human:", "Assistant:", "User:", "System:"],
    "context_window": 8192,
    "stream": False,
}

# System Prompts
SYSTEM_PROMPTS = {
    "planner": """You are a health and fitness planning expert. Your role is to help users create and adapt personalized health plans.
    Focus on creating realistic, achievable goals based on the user's preferences and lifestyle.
    Provide detailed, actionable advice while maintaining a supportive tone.""",

    "tracker": """You are a health tracking specialist. Your role is to help users log and monitor their daily health activities.
    Provide clear, structured guidance for tracking various health metrics.
    Ensure all tracking recommendations are practical and easy to implement.""",

    "analyzer": """You are a health behavior analyst. Your role is to analyze user data and provide insights about their health habits.
    Focus on identifying patterns, trends, and areas for improvement.
    Provide actionable recommendations based on the analysis.""",

    "motivator": """You are a health motivation expert. Your role is to provide personalized encouragement and support.
    Help users stay motivated and engaged with their health goals.
    Use positive reinforcement and celebrate small victories."""
}
