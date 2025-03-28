const inquirer = require('inquirer');
const chalk = require('chalk');
const api = require('../services/api');

async function trackCommand() {
  console.log(chalk.blue('Starting habit tracking...'));

  try {
    // Get all habits
    const habits = await api.getHabits();

    if (habits.length === 0) {
      console.log(
        chalk.yellow(
          'No habits found. Please create a habit first using: healthhabit init',
        ),
      );
      return;
    }

    // Let user select which habit to track
    const { habitId } = await inquirer.prompt([
      {
        type: 'list',
        name: 'habitId',
        message: 'Which habit would you like to track?',
        choices: habits.map((habit) => ({
          name: `${habit.name} (${habit.type})`,
          value: habit.id,
        })),
      },
    ]);

    // Get completion status
    const { completed } = await inquirer.prompt([
      {
        type: 'confirm',
        name: 'completed',
        message: 'Did you complete this habit today?',
      },
    ]);

    // Update the habit
    await api.updateHabit(habitId, { completed });

    console.log(chalk.green('Successfully updated your habit tracking!'));
  } catch (error) {
    console.error(chalk.red('Error tracking habit:'), error.message);
    process.exit(1);
  }
}

module.exports = trackCommand;
