import MovieCard from "./MovieCard";

export default function MovieGrid({ movies, onWatchlist, watchlist }) {
  if (!movies.length) {
    return <div className="empty">No movies found.</div>;
  }

  return (
    <div className="movie-grid">
      {movies.map(movie => (
        <MovieCard
          key={movie.id}
          movie={movie}
          onWatchlist={onWatchlist}
          saved={watchlist.some(item => item.id === movie.id)}
        />
      ))}
    </div>
  );
}
