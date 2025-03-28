const chalk = require('chalk');
const api = require('../services/api');

const motivationalQuotes = [
  'Every small step counts towards your bigger goal!',
  "You're making progress, keep going!",
  'Your future self will thank you for your efforts today.',
  "Consistency is key - you've got this!",
  'Small habits, big changes. Keep pushing forward!',
  "You're stronger than you think. Keep going!",
  'Every day is a new opportunity to improve.',
  'Your dedication is inspiring!',
  "Remember why you started. You've got this!",
  'Progress is progress, no matter how small.',
];

async function motivateCommand() {
  console.log(chalk.blue('Generating motivation...'));

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

    // Get a random motivational quote
    const quote =
      motivationalQuotes[Math.floor(Math.random() * motivationalQuotes.length)];

    console.log('\n' + chalk.cyan('Your Daily Motivation:'));
    console.log('==================\n');
    console.log(chalk.green(`"${quote}"`));

    console.log('\n' + chalk.cyan('Your Habits Status:'));
    console.log('==================\n');

    habits.forEach((habit) => {
      const status = habit.completed
        ? chalk.green('✓ Completed')
        : chalk.yellow('○ Pending');
      console.log(`${status} - ${habit.name}`);
    });
  } catch (error) {
    console.error(chalk.red('Error generating motivation:'), error.message);
    process.exit(1);
  }
}

module.exports = motivateCommand;
