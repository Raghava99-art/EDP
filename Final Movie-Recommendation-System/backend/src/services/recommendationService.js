let movies = [];
let vocabulary = [];
let movieVectors = [];

function tokenize(text) {
  return String(text)
    .toLowerCase()
    .replace(/[^a-z0-9\s|]/g, " ")
    .split(/\s+/)
    .filter(word => word.length > 1);
}

function documentText(movie) {
  // Repeating genres gives genre information more weight.
  return [
    movie.title,
    movie.genres,
    movie.genres,
    movie.description,
    movie.language
  ].join(" ");
}

function buildModel(movieList) {
  movies = movieList;

  const tokenized = movies.map(movie => tokenize(documentText(movie)));

  const vocabularySet = new Set();
  tokenized.forEach(tokens => tokens.forEach(token => vocabularySet.add(token)));
  vocabulary = Array.from(vocabularySet);

  const documentFrequency = {};
  vocabulary.forEach(term => {
    documentFrequency[term] = tokenized.reduce(
      (count, tokens) => count + (tokens.includes(term) ? 1 : 0),
      0
    );
  });

  movieVectors = tokenized.map(tokens => {
    const counts = {};
    tokens.forEach(token => {
      counts[token] = (counts[token] || 0) + 1;
    });

    const totalTerms = tokens.length || 1;

    return vocabulary.map(term => {
      const tf = (counts[term] || 0) / totalTerms;
      const df = documentFrequency[term] || 0;
      const idf = Math.log((movies.length + 1) / (df + 1)) + 1;
      return tf * idf;
    });
  });
}

function cosineSimilarity(a, b) {
  let dot = 0;
  let normA = 0;
  let normB = 0;

  for (let i = 0; i < a.length; i++) {
    dot += a[i] * b[i];
    normA += a[i] * a[i];
    normB += b[i] * b[i];
  }

  if (!normA || !normB) return 0;
  return dot / (Math.sqrt(normA) * Math.sqrt(normB));
}

function genreOverlap(a, b) {
  const first = new Set(a.genres.split("|"));
  const second = new Set(b.genres.split("|"));
  let common = 0;

  second.forEach(g => {
    if (first.has(g)) common++;
  });

  return common;
}

function getRecommendations(movieId, limit = 6) {
  const index = movies.findIndex(movie => movie.id === movieId);

  if (index === -1) return null;

  const baseMovie = movies[index];
  const baseVector = movieVectors[index];

  const scored = movies
    .map((movie, i) => {
      if (i === index) return null;

      const similarity = cosineSimilarity(baseVector, movieVectors[i]);
      const overlap = genreOverlap(baseMovie, movie);

      // Small rating contribution makes high-rated similar movies slightly more visible.
      const score =
        similarity * 0.80 +
        Math.min(overlap / 3, 1) * 0.15 +
        (movie.rating / 10) * 0.05;

      return {
        ...movie,
        similarity: Number(similarity.toFixed(4)),
        recommendationScore: Number(score.toFixed(4))
      };
    })
    .filter(Boolean)
    .sort((a, b) => b.recommendationScore - a.recommendationScore)
    .slice(0, limit);

  return {
    basedOn: baseMovie,
    recommendations: scored
  };
}

module.exports = {
  buildModel,
  getRecommendations
};
