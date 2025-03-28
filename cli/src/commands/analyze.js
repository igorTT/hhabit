const chalk = require('chalk');
const api = require('../services/api');

async function analyzeCommand() {
  console.log(chalk.blue('Analyzing your habits...'));

  try {
    const habits = await api.getHabits();

    if (habits.length === 0) {
      console.log(
        chalk.yellow(
          'No habits found. Please create a habit first using: healthhabit init',
        ),
      );
      return;
    }

    console.log('\n' + chalk.cyan('Your Habit Analysis:'));
    console.log('==================\n');

    habits.forEach((habit) => {
      console.log(chalk.blue(`${habit.name} (${habit.type})`));
      console.log(`Description: ${habit.description}`);
      console.log(`Weekly Goal: ${habit.frequency} times`);
      console.log(
        `Completion Rate: ${
          habit.completed ? 'Completed today' : 'Not completed today'
        }`,
      );
      console.log('------------------\n');
    });
  } catch (error) {
    console.error(chalk.red('Error analyzing habits:'), error.message);
    process.exit(1);
  }
}

module.exports = analyzeCommand;
