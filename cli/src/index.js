#!/usr/bin/env node

import { program } from 'commander';
import chalk from 'chalk';
import initCommand from './commands/init.js';
import trackCommand from './commands/track.js';
import analyzeCommand from './commands/analyze.js';
import motivateCommand from './commands/motivate.js';

program
  .name('healthhabit')
  .description('AI-Powered Health Habit Tracker')
  .version('1.0.0');

program
  .command('init')
  .description('Initialize your health habits')
  .action(initCommand);

program
  .command('track')
  .description('Track your daily habits')
  .action(trackCommand);

program
  .command('analyze')
  .description('Analyze your habit progress')
  .action(analyzeCommand);

program
  .command('motivate')
  .description('Get motivation for your habits')
  .action(motivateCommand);

program.parse();
