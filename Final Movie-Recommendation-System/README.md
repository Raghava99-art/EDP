# 🎬 Movie Recommendation System

A full-stack movie recommendation system inspired by the structure and user experience of the reference Movie App repository.

## Features
- React frontend with responsive dark UI
- Express.js backend
- Movie search
- Movie details
- Content-based recommendations
- TF-IDF vectorization
- Cosine similarity
- Watchlist using browser localStorage
- Ratings using browser localStorage
- CSV movie dataset
- REST APIs
- No database required for the basic version

## Project Structure

```text
Final Movie-Recommendation-System/
├── frontend/
├── backend/
├── dataset/
├── docs/
└── README.md
```

## Requirements
- Node.js 18+
- npm
- Python is NOT required for the application

## Run Backend

```bash
cd backend
npm install
npm start
```

Backend runs at:
`http://localhost:5000`

## Run Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:
`http://localhost:5173`

## API Endpoints

- `GET /api/health`
- `GET /api/movies`
- `GET /api/movies/:id`
- `GET /api/movies/search?q=`
- `GET /api/recommendations/:id`
- `POST /api/recommendations`

Example:

```text
GET http://localhost:5000/api/recommendations/1?limit=6
```

## Recommendation Method

The system uses content-based filtering:

```text
Movie Title + Genres + Description
              ↓
       Text preprocessing
              ↓
        TF-IDF vectors
              ↓
      Cosine similarity
              ↓
    Similarity calculation
              ↓
       Top-N movies
```

## Dataset

`dataset/movies.csv` contains movie ID, title, genres, description, year, language and rating.

## Academic Topics Covered
- Content-Based Filtering
- TF-IDF
- Cosine Similarity
- REST API
- React
- Express.js
- Client-side storage
- CSV data processing
- Full-stack architecture
