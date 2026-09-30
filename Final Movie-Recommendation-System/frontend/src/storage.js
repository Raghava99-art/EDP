const WATCHLIST_KEY = "movie_match_watchlist";
const RATINGS_KEY = "movie_match_ratings";

export function getWatchlist() {
  return JSON.parse(localStorage.getItem(WATCHLIST_KEY) || "[]");
}

export function isInWatchlist(id) {
  return getWatchlist().some(movie => movie.id === id);
}

export function toggleWatchlist(movie) {
  const list = getWatchlist();
  const exists = list.some(item => item.id === movie.id);

  const updated = exists
    ? list.filter(item => item.id !== movie.id)
    : [...list, movie];

  localStorage.setItem(WATCHLIST_KEY, JSON.stringify(updated));
  return updated;
}

export function getRatings() {
  return JSON.parse(localStorage.getItem(RATINGS_KEY) || "{}");
}

export function saveRating(movieId, rating) {
  const ratings = getRatings();
  ratings[movieId] = rating;
  localStorage.setItem(RATINGS_KEY, JSON.stringify(ratings));
}
