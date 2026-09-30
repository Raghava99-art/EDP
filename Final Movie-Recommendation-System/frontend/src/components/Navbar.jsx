import { Link } from "react-router-dom";

export default function Navbar({ watchlistCount }) {
  return (
    <header className="navbar">
      <Link className="brand" to="/">
        🎬 MovieMatch
      </Link>

      <nav>
        <Link to="/">Home</Link>
        <Link to="/watchlist">
          Watchlist <span className="badge">{watchlistCount}</span>
        </Link>
        <a href="#about">About</a>
      </nav>
    </header>
  );
}
