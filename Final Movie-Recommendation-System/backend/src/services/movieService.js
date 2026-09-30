const fs = require("fs");
const path = require("path");
const { parse } = require("csv-parse/sync");

async function loadMovies() {
  const csvPath = path.join(__dirname, "../../../dataset/movies.csv");
  const csv = fs.readFileSync(csvPath, "utf8");

  const records = parse(csv, {
    columns: true,
    skip_empty_lines: true,
    trim: true
  });

  return records.map(row => ({
    id: Number(row.id),
    title: row.title,
    genres: row.genres,
    description: row.description,
    year: Number(row.year),
    language: row.language,
    rating: Number(row.rating)
  }));
}

module.exports = { loadMovies };
