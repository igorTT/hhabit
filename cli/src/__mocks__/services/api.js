const mockCreateHabit = jest.fn();
const mockGetHabits = jest.fn();
const mockGetHabit = jest.fn();
const mockUpdateHabit = jest.fn();
const mockDeleteHabit = jest.fn();

export default {
  createHabit: mockCreateHabit,
  getHabits: mockGetHabits,
  getHabit: mockGetHabit,
  updateHabit: mockUpdateHabit,
  deleteHabit: mockDeleteHabit,
};
