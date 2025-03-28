import { jest } from '@jest/globals';
import initCommand from '../../commands/init.js';

// Mock dependencies
const mockPrompt = jest.fn();
const mockCreateHabit = jest.fn();

jest.mock('inquirer', () => ({
  prompt: mockPrompt,
}));

jest.mock('../../services/api.js', () => ({
  default: {
    createHabit: mockCreateHabit,
  },
}));

jest.mock('chalk', () => ({
  blue: (text) => text,
  green: (text) => text,
  red: (text) => text,
}));

describe('initCommand', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('should create a habit successfully', async () => {
    // Mock inquirer response
    const mockAnswers = {
      name: 'Morning Exercise',
      type: 'Exercise',
      description: '30 minutes of cardio',
      frequency: 3,
    };
    mockPrompt.mockResolvedValue(mockAnswers);

    // Mock API response
    mockCreateHabit.mockResolvedValue({ id: '123', ...mockAnswers });

    // Execute command
    await initCommand();

    // Verify inquirer was called with correct questions
    expect(mockPrompt).toHaveBeenCalledWith([
      expect.objectContaining({
        name: 'name',
        message: 'What would you like to name this habit?',
      }),
      expect.objectContaining({
        name: 'type',
        message: 'What type of habit is this?',
        choices: expect.any(Array),
      }),
      expect.objectContaining({
        name: 'description',
        message: 'Describe your habit goal:',
      }),
      expect.objectContaining({
        name: 'frequency',
        message: 'How many times per week do you want to do this?',
        min: 1,
        max: 7,
        default: 3,
      }),
    ]);

    // Verify API was called with correct data
    expect(mockCreateHabit).toHaveBeenCalledWith(mockAnswers);
  });

  it('should handle API errors gracefully', async () => {
    // Mock inquirer response
    const mockAnswers = {
      name: 'Morning Exercise',
      type: 'Exercise',
      description: '30 minutes of cardio',
      frequency: 3,
    };
    mockPrompt.mockResolvedValue(mockAnswers);

    // Mock API error
    const mockError = new Error('API Error');
    mockCreateHabit.mockRejectedValue(mockError);

    // Mock console.error and process.exit
    const consoleSpy = jest.spyOn(console, 'error').mockImplementation();
    const exitSpy = jest.spyOn(process, 'exit').mockImplementation();

    // Execute command
    await initCommand();

    // Verify error handling
    expect(consoleSpy).toHaveBeenCalledWith(
      expect.stringContaining('Error creating habit:'),
      mockError.message,
    );
    expect(exitSpy).toHaveBeenCalledWith(1);

    // Clean up
    consoleSpy.mockRestore();
    exitSpy.mockRestore();
  });
});
