import inquirer from 'inquirer';
import chalk from 'chalk';
import api from '../services/api.js';

async function initCommand() {
  console.log(chalk.blue('Initializing HealthHabit...'));

  try {
    const answers = await inquirer.prompt([
      {
        type: 'input',
        name: 'name',
        message: 'What would you like to name this habit?',
        validate: (input) => input.length > 0 || 'Name is required',
      },
      {
        type: 'list',
        name: 'type',
        message: 'What type of habit is this?',
        choices: [
          'Exercise',
          'Sleep',
          'Nutrition',
          'Hydration',
          'Meditation',
          'Other',
        ],
      },
      {
        type: 'input',
        name: 'description',
        message: 'Describe your habit goal:',
        validate: (input) => input.length > 0 || 'Description is required',
      },
      {
        type: 'number',
        name: 'frequency',
        message: 'How many times per week do you want to do this?',
        min: 1,
        max: 7,
        default: 3,
      },
    ]);

    const habit = await api.default.createHabit(answers);
    console.log(chalk.green('Successfully created your habit!'));
    console.log(chalk.blue('Habit ID:'), habit.id);
  } catch (error) {
    console.error(chalk.red('Error creating habit:'), error.message);
    process.exit(1);
  }
}

export default initCommand;
