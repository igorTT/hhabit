# HealthHabit CLI - AI-Powered Health Habit Tracker

## Overview
HealthHabit CLI is a terminal-based application that leverages AI agents using CrewAI to help users build, maintain, and optimize healthy habits. The system is built using a Node.js-based CLI interface that communicates with a backend CrewAI service implemented in Python. The assistant agents collaboratively help users set goals, track progress, analyze behavior, and stay motivated.

---

## Goals
- Provide an AI-driven experience for setting and managing health-related habits.
- Use CrewAI multi-agent collaboration to automate planning, tracking, analysis, and motivation.
- Offer an intuitive CLI interface for interaction.
- Enable personalization and adaptability based on user behavior over time.

---

## Core Features

### 1. Goal Setting (PlannerAgent)
- Gathers user preferences and lifestyle information.
- Sets weekly/daily habit goals (e.g., hydration, sleep, exercise).
- Adapts goals based on feedback and performance.

### 2. Daily Tracking (TrackerAgent)
- Prompts user to log daily habit data via CLI.
- Stores and organizes data locally or via API.
- Optionally fetches from third-party health APIs (future).

### 3. Behavior Analysis (AnalyzerAgent)
- Reviews logged data.
- Detects patterns, highlights missed goals, and suggests improvements.
- Offers weekly or monthly summaries.

### 4. Motivation (MotivatorAgent)
- Sends encouraging messages.
- Recommends fun challenges or adjustments to boost engagement.
- Provides educational or inspirational health content.

---

## Technical Stack

### Node.js CLI
- Uses packages like `commander`, `inquirer`, and `chalk`.
- Handles user input/output and session flow.
- Sends data to Python CrewAI service via HTTP requests (or other IPC).

### Python Backend (CrewAI)
- Implements AI agents using CrewAI framework.
- Each agent performs a specific task in the workflow.
- Exposes endpoints for Node.js CLI to interact with.

### Optional Storage
- Local JSON/SQLite for initial version.
- Future option: cloud storage for multi-device sync.

---

## CLI Commands (Proposed)
```bash
$ healthhabit init       # Setup goals
$ healthhabit track      # Log daily data
$ healthhabit analyze    # Get insights
$ healthhabit motivate   # Receive encouragement
$ healthhabit plan       # View/edit current goals
```

---

## Future Enhancements
- Integration with wearable APIs (Fitbit, Apple Health)
- Voice-based input/output
- Social/leaderboard features
- Cross-platform desktop version (Electron or Tauri)

---

## Development Plan (High-Level)
1. Define CrewAI agents and implement minimal versions in Python.
2. Build Node.js CLI interface with mock agent responses.
3. Connect CLI to real CrewAI backend.
4. Add data persistence.
5. Iterate with more features and API integrations.

