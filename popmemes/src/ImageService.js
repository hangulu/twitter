import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class ImageService {
  // Get all popmemes
  getPopmemes() {
      const url = `${API_URL}/api/popmemes/`;
      return axios.get(url).then(response => response.data);
  }

  // Get a single popmeme, by its username
  getPopmeme(user) {
      const url = `${API_URL}/api/popmemes/${user}`;
      return axios.get(url).then(response => response.data);
  }

  // Delete a single popmeme, by its username
  deletePopmeme(user) {
      const url = `${API_URL}/api/popmemes/${user}`;
      return axios.delete(url);
  }

  // Add a new popmeme
  createPopmeme(user) {
      const url = `${API_URL}/api/popmemes/`;
      return axios.post(url, user);
  }

  // Update a meme
  updatePopmeme(user){
      const url = `${API_URL}/api/user/${user}`;
      return axios.put(url, user);
  }
}
