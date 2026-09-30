# Methodology

## 1. Data Collection
Movie information is stored in `dataset/movies.csv`.

## 2. Feature Selection
The recommendation engine uses:
- Movie title
- Genres
- Description
- Language

Genres are repeated in the document text to give genre information additional weight.

## 3. Text Processing
Text is:
- converted to lowercase
- cleaned of punctuation
- split into tokens

## 4. TF-IDF
Term Frequency-Inverse Document Frequency converts each movie into a numerical vector.

Conceptually:

`TF-IDF(t,d) = TF(t,d) × IDF(t)`

## 5. Cosine Similarity

Similarity between two movie vectors is calculated as:

`cos(A,B) = (A·B) / (||A|| ||B||)`

A value closer to 1 indicates greater textual similarity.

## 6. Ranking
The system combines:
- TF-IDF cosine similarity
- genre overlap
- a small movie-rating contribution

The highest scoring movies are returned.

## 7. User Interface
The React frontend allows users to:
- search
- open movie details
- view recommendations
- save movies
- rate movies
