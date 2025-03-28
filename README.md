# HealthHabit

An AI-powered health habit tracking application that uses CrewAI to help users build and maintain healthy habits through an intuitive CLI interface. The system leverages multiple AI agents working together to provide personalized health guidance and support.

## Features

### AI-Powered Health Management
- **Smart Goal Setting**: Personalized health and fitness goals based on your preferences and lifestyle
- **Daily Tracking**: Easy logging of exercise, meditation, nutrition, and sleep data
- **Behavior Analysis**: AI-driven insights and pattern recognition for your health habits
- **Motivational Support**: Personalized encouragement and challenge suggestions

### CrewAI Agents
The system uses four specialized AI agents working together:
1. **PlannerAgent**: Creates and adapts personalized health plans
2. **TrackerAgent**: Manages daily habit tracking and data collection
3. **AnalyzerAgent**: Provides insights and identifies behavior patterns
4. **MotivatorAgent**: Delivers personalized motivation and challenges

## Project Structure

```
hhabit/
├── cli/                 # Node.js CLI application
│   ├── src/
│   │   ├── commands/   # CLI commands
│   │   ├── services/   # API communication
│   │   └── utils/      # Helper functions
│   └── data/          # Local JSON storage
├── backend/           # Python CrewAI backend
│   ├── src/
│   │   ├── agents/    # CrewAI agents
│   │   ├── api/       # FastAPI endpoints
│   │   └── utils/     # Helper functions
│   ├── tests/         # Test suite
│   │   ├── unit/      # Unit tests
│   │   └── utils/     # Test utilities
│   └── data/         # Shared data storage
└── docs/             # Documentation
    ├── ai-instrutions.md  # AI system design
    └── test_documentation_guidelines.md  # Test standards
```

## Prerequisites

- Node.js (v20.17.0 or higher)
  - We recommend using nvm (Node Version Manager) to manage Node.js versions
  - The project includes a `.nvmrc` file for automatic version switching
- Python (3.10 or higher)
- Yarn package manager
- TogetherAI API key

## Setup

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   # or
   source venv/bin/activate     # On Unix/MacOS
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your TogetherAI API key:
   ```
   TOGETHER_API_KEY=your_api_key_here
   API_HOST=0.0.0.0
   API_PORT=8000
   ```

5. Start the backend server:
   ```bash
   uvicorn src.api.main:app --reload
   ```

### CLI Setup

1. Navigate to the CLI directory:
   ```bash
   cd cli
   ```

2. If using nvm, install and use the correct Node.js version:
   ```bash
   nvm install
   nvm use
   ```

3. Install dependencies:
   ```bash
   yarn install
   ```

4. Link the CLI globally:
   ```bash
   yarn link
   ```

## Usage

Once set up, you can use the following commands:

```bash
healthhabit init       # Setup goals and preferences
healthhabit track      # Log daily health data
healthhabit analyze    # Get AI-powered insights
healthhabit motivate   # Receive personalized encouragement
healthhabit plan       # View and adjust your health plan
```

## Development

### Running Tests
The project includes comprehensive test suites for both backend and CLI components:

```bash
# Run backend tests
cd backend
pytest

# Run CLI tests
cd cli
yarn test
```

### Documentation
- Test documentation follows strict guidelines for clarity and maintainability
- AI system design and architecture are documented in `docs/ai-instrutions.md`
- Test documentation standards are defined in `docs/test_documentation_guidelines.md`

## Future Enhancements

- Integration with wearable APIs (Fitbit, Apple Health)
- Voice-based input/output
- Social/leaderboard features
- Cross-platform desktop version (Electron or Tauri)
- Enhanced AI capabilities for more personalized recommendations
- Multi-device sync support

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 