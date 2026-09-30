import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000/api";

const api = axios.create({
  baseURL: API_URL,
  timeout: 10000
});

export async function getMovies() {
  const response = await api.get("/movies?limit=100");
  return response.data.data;
}

export async function searchMovies(query) {
  const response = await api.get("/movies/search", {
    params: { q: query }
  });
  return response.data.data;
}

export async function getMovie(id) {
  const response = await api.get(`/movies/${id}`);
  return response.data.data;
}

export async function getRecommendations(id, limit = 6) {
  const response = await api.get(`/recommendations/${id}`, {
    params: { limit }
  });
  return response.data;
}
