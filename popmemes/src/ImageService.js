import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class ImageService {
  // Get all popmemes
  getPopimages() {
      const url = `${API_URL}/api/popimg/`;
      return axios.get(url).then(response => response.data);
  }

  // Get a single popmeme, by its username
  getPopimage(user) {
      const url = `${API_URL}/api/popimg/${user}`;
      return axios.get(url).then(response => response.data);
  }

  // Delete a single popmeme, by its username
  deletePopimage(user) {
      const url = `${API_URL}/api/popimg/${user}`;
      return axios.delete(url);
  }

  // Add a new popmeme
  createPopimage(user) {
      const url = `${API_URL}/api/popimg/`;
      return axios.post(url, user);
  }

  // Update a meme
  updatePopimage(user){
      const url = `${API_URL}/api/popimg/${user}`;
      return axios.put(url, user);
  }
}
