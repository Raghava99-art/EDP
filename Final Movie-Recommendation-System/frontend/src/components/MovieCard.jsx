import { Link } from "react-router-dom";

function poster(title, id) {
  return `https://placehold.co/500x750/171717/ffffff?text=${encodeURIComponent(title)}`;
}

export default function MovieCard({ movie, onWatchlist, saved }) {
  return (
    <article className="movie-card">
      <Link to={`/movie/${movie.id}`}>
        <img src={poster(movie.title, movie.id)} alt={movie.title} />
      </Link>

      <div className="movie-info">
        <Link to={`/movie/${movie.id}`} className="movie-title">
          {movie.title}
        </Link>

        <div className="meta">
          <span>{movie.year}</span>
          <span>⭐ {movie.rating}</span>
        </div>

        <p>{movie.genres.replaceAll("|", " • ")}</p>

        <button
          className={saved ? "save-btn saved" : "save-btn"}
          onClick={() => onWatchlist(movie)}
        >
          {saved ? "✓ Saved" : "+ Watchlist"}
        </button>
      </div>
    </article>
  );
}
