import axios from 'axios';

class ApiService {
  constructor() {
    this.baseURL = process.env.API_URL || 'http://localhost:8000';
    this.client = axios.create({
      baseURL: this.baseURL,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }

  async getHabits() {
    try {
      const response = await this.client.get('/api/habits');
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async getHabit(habitId) {
    try {
      const response = await this.client.get(`/api/habits/${habitId}`);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async createHabit(habitData) {
    try {
      const response = await this.client.post('/api/habits', habitData);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async updateHabit(habitId, habitData) {
    try {
      const response = await this.client.put(
        `/api/habits/${habitId}`,
        habitData,
      );
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  async deleteHabit(habitId) {
    try {
      const response = await this.client.delete(`/api/habits/${habitId}`);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  handleError(error) {
    if (error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      return new Error(error.response.data.detail || 'An error occurred');
    } else if (error.request) {
      // The request was made but no response was received
      return new Error('No response received from server');
    } else {
      // Something happened in setting up the request that triggered an Error
      return new Error('Error setting up the request');
    }
  }
}

export default new ApiService();
