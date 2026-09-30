import { useEffect, useMemo, useState } from "react";
import { Routes, Route, useNavigate, useParams, Link } from "react-router-dom";
import Navbar from "./components/Navbar";
import MovieGrid from "./components/MovieGrid";
import SearchBar from "./components/SearchBar";
import {
  getMovies,
  searchMovies,
  getMovie,
  getRecommendations
} from "./api";
import {
  getWatchlist,
  toggleWatchlist,
  getRatings,
  saveRating
} from "./storage";

function Home() {
  const [movies, setMovies] = useState([]);
  const [query, setQuery] = useState("");
  const [status, setStatus] = useState("Loading movies...");
  const [watchlist, setWatchlist] = useState(getWatchlist());

  useEffect(() => {
    getMovies()
      .then(data => {
        setMovies(data);
        setStatus("");
      })
      .catch(() => setStatus("Could not connect to backend. Start the backend first."));
  }, []);

  async function search() {
    setStatus("Searching...");
    try {
      const data = query.trim() ? await searchMovies(query) : await getMovies();
      setMovies(data);
      setStatus("");
    } catch {
      setStatus("Search failed.");
    }
  }

  function save(movie) {
    setWatchlist(toggleWatchlist(movie));
  }

  const popular = useMemo(
    () => [...movies].sort((a, b) => b.rating - a.rating),
    [movies]
  );

  return (
    <>
      <section className="hero">
        <div>
          <p className="eyebrow">AI-INSPIRED MOVIE DISCOVERY</p>
          <h1>Find your next<br /><span>favorite movie.</span></h1>
          <p className="hero-text">
            Search movies and discover similar titles using TF-IDF and cosine similarity.
          </p>
          <SearchBar
            value={query}
            onChange={setQuery}
            onSearch={search}
          />
        </div>
      </section>

      {status && <p className="status">{status}</p>}

      <section className="section">
        <div className="section-heading">
          <div>
            <p className="eyebrow">DISCOVER</p>
            <h2>Popular Movies</h2>
          </div>
          <span>{popular.length} movies</span>
        </div>

        <MovieGrid
          movies={popular}
          onWatchlist={save}
          watchlist={watchlist}
        />
      </section>
    </>
  );
}

function MovieDetails({ onWatchlist, watchlist }) {
  const { id } = useParams();
  const [movie, setMovie] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [rating, setRating] = useState(getRatings()[id] || 0);
  const [error, setError] = useState("");

  useEffect(() => {
    Promise.all([getMovie(id), getRecommendations(id, 6)])
      .then(([movieData, recommendationData]) => {
        setMovie(movieData);
        setRecommendations(recommendationData.data);
      })
      .catch(() => setError("Unable to load movie details."));
  }, [id]);

  if (error) return <div className="empty">{error}</div>;
  if (!movie) return <div className="status">Loading...</div>;

  const saved = watchlist.some(item => item.id === movie.id);

  function rate(value) {
    setRating(value);
    saveRating(movie.id, value);
  }

  return (
    <main className="details-page">
      <Link to="/" className="back">← Back to movies</Link>

      <section className="details">
        <img
          className="details-poster"
          src={`https://placehold.co/500x750/171717/ffffff?text=${encodeURIComponent(movie.title)}`}
          alt={movie.title}
        />

        <div>
          <p className="eyebrow">{movie.language} • {movie.year}</p>
          <h1>{movie.title}</h1>
          <div className="large-rating">⭐ {movie.rating}/10</div>
          <p className="genres">{movie.genres.replaceAll("|", " • ")}</p>
          <p className="description">{movie.description}</p>

          <div className="actions">
            <button onClick={() => onWatchlist(movie)}>
              {saved ? "✓ Remove from Watchlist" : "+ Add to Watchlist"}
            </button>
          </div>

          <div className="rating-box">
            <strong>Your rating</strong>
            <div className="stars">
              {[1, 2, 3, 4, 5].map(star => (
                <button
                  key={star}
                  className={star <= rating ? "star active" : "star"}
                  onClick={() => rate(star)}
                >
                  ★
                </button>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section className="section">
        <div className="section-heading">
          <div>
            <p className="eyebrow">CONTENT-BASED FILTERING</p>
            <h2>Recommended For You</h2>
          </div>
        </div>

        <MovieGrid
          movies={recommendations}
          onWatchlist={onWatchlist}
          watchlist={watchlist}
        />
      </section>
    </main>
  );
}

function Watchlist({ watchlist, onWatchlist }) {
  return (
    <main className="section">
      <div className="section-heading">
        <div>
          <p className="eyebrow">YOUR COLLECTION</p>
          <h2>Watchlist</h2>
        </div>
        <span>{watchlist.length} saved</span>
      </div>

      <MovieGrid
        movies={watchlist}
        onWatchlist={onWatchlist}
        watchlist={watchlist}
      />
    </main>
  );
}

function About() {
  return (
    <section id="about" className="about section">
      <p className="eyebrow">ABOUT THE PROJECT</p>
      <h2>Movie Recommendation System</h2>
      <p>
        This project demonstrates content-based movie recommendation using
        TF-IDF vectorization and cosine similarity. Movie metadata is stored
        in a CSV dataset and served through an Express REST API.
      </p>
      <div className="architecture">
        Dataset → Text Processing → TF-IDF → Cosine Similarity → Recommendations
      </div>
    </section>
  );
}

export default function App() {
  const [watchlist, setWatchlist] = useState(getWatchlist());
  const navigate = useNavigate();

  function save(movie) {
    setWatchlist(toggleWatchlist(movie));
    navigate(window.location.pathname);
  }

  return (
    <div>
      <Navbar watchlistCount={watchlist.length} />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route
          path="/movie/:id"
          element={
            <MovieDetails
              watchlist={watchlist}
              onWatchlist={save}
            />
          }
        />
        <Route
          path="/watchlist"
          element={
            <Watchlist
              watchlist={watchlist}
              onWatchlist={save}
            />
          }
        />
        <Route path="/about" element={<About />} />
      </Routes>

      <footer>
        <strong>MovieMatch</strong>
        <span>Content-Based Movie Recommendation System</span>
      </footer>
    </div>
  );
}
