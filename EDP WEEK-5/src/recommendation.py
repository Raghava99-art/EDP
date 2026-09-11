import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------------------
# STEP 1: Read Dataset
# -----------------------------------------

df = pd.read_csv("movies.csv")


# -----------------------------------------
# STEP 2: Display Dataset Information
# -----------------------------------------

print("Total Movies:", len(df))

print("\nAvailable Movies:")
for movie in df["title"]:
    print("-", movie)


# -----------------------------------------
# STEP 3: Convert Movie Descriptions
#         into TF-IDF Vectors
# -----------------------------------------

vectorizer = TfidfVectorizer()

movie_vectors = vectorizer.fit_transform(df["description"])


# -----------------------------------------
# STEP 4: Calculate Cosine Similarity
# -----------------------------------------

similarity_matrix = cosine_similarity(movie_vectors)


# -----------------------------------------
# STEP 5: Recommendation Function
# -----------------------------------------

def recommend_movies(movie_name, number_of_recommendations=5):

    # Find movie
    movie_matches = df[
        df["title"].str.lower() == movie_name.lower()
    ]

    # Check movie exists
    if movie_matches.empty:
        print("\nMovie not found!")
        return

    # Get movie index
    movie_index = movie_matches.index[0]

    # Get similarity scores
    similarity_scores = list(
        enumerate(similarity_matrix[movie_index])
    )

    # Sort by similarity score
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\n================================")
    print("Recommendations for:", df.iloc[movie_index]["title"])
    print("================================")

    count = 0

    for index, score in similarity_scores:

        # Skip the selected movie
        if index == movie_index:
            continue

        print(
            f"{count + 1}. "
            f"{df.iloc[index]['title']} "
            f"(Similarity: {score:.3f})"
        )

        count += 1

        if count == number_of_recommendations:
            break


# -----------------------------------------
# STEP 6: Get Movie from User
# -----------------------------------------

movie_name = input(
    "\nEnter the movie name: "
)


# -----------------------------------------
# STEP 7: Generate Recommendations
# -----------------------------------------

recommend_movies(movie_name, 5)