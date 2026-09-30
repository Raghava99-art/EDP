require("dotenv").config();

const express = require("express");
const cors = require("cors");
const path = require("path");
const { loadMovies } = require("./services/movieService");
const recommendationService = require("./services/recommendationService");

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors({
  origin: process.env.FRONTEND_URL || "http://localhost:5173"
}));
app.use(express.json());

let movies = [];

async function start() {
  movies = await loadMovies();
  recommendationService.buildModel(movies);

  app.get("/api/health", (req, res) => {
    res.json({
      success: true,
      message: "Movie Recommendation API is running",
      movies: movies.length
    });
  });

  app.get("/api/movies", (req, res) => {
    const page = Math.max(parseInt(req.query.page || "1"), 1);
    const limit = Math.min(Math.max(parseInt(req.query.limit || "12"), 1), 100);
    const start = (page - 1) * limit;

    res.json({
      success: true,
      page,
      limit,
      total: movies.length,
      data: movies.slice(start, start + limit)
    });
  });

  app.get("/api/movies/search", (req, res) => {
    const q = String(req.query.q || "").trim().toLowerCase();

    if (!q) {
      return res.json({ success: true, data: movies });
    }

    const result = movies.filter(movie =>
      [movie.title, movie.genres, movie.description, movie.language]
        .join(" ")
        .toLowerCase()
        .includes(q)
    );

    res.json({ success: true, data: result });
  });

  app.get("/api/movies/:id", (req, res) => {
    const movie = movies.find(m => m.id === Number(req.params.id));

    if (!movie) {
      return res.status(404).json({
        success: false,
        message: "Movie not found"
      });
    }

    res.json({ success: true, data: movie });
  });

  app.get("/api/recommendations/:id", (req, res) => {
    const limit = Math.min(Math.max(parseInt(req.query.limit || "6"), 1), 20);
    const result = recommendationService.getRecommendations(
      Number(req.params.id),
      limit
    );

    if (!result) {
      return res.status(404).json({
        success: false,
        message: "Movie not found"
      });
    }

    res.json({
      success: true,
      basedOn: result.basedOn,
      data: result.recommendations
    });
  });

  app.post("/api/recommendations", (req, res) => {
    const { movieId, limit = 6 } = req.body;

    const result = recommendationService.getRecommendations(
      Number(movieId),
      Math.min(Math.max(Number(limit), 1), 20)
    );

    if (!result) {
      return res.status(404).json({
        success: false,
        message: "Movie not found"
      });
    }

    res.json({
      success: true,
      basedOn: result.basedOn,
      data: result.recommendations
    });
  });

  app.use((req, res) => {
    res.status(404).json({
      success: false,
      message: "API route not found"
    });
  });

  app.listen(PORT, () => {
    console.log(`Backend running at http://localhost:${PORT}`);
  });
}

start().catch(err => {
  console.error("Failed to start server:", err);
  process.exit(1);
});
