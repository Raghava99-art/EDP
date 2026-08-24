# ============================================================
# MOVIE RECOMMENDATION SYSTEM
# Parameter-Based Movie Recommendation
# Dataset is loaded from an external CSV file
# ============================================================

import pandas as pd
from pathlib import Path


# ============================================================
# 1. LOAD DATASET
# ============================================================

DATASET_FILE = "movies_dataset.csv"

try:
    movies = pd.read_csv(DATASET_FILE)
except FileNotFoundError:
    print("ERROR: movies_dataset.csv was not found.")
    print("Place the CSV file in the same folder as this Python file.")
    exit()


# ============================================================
# 2. CHECK REQUIRED COLUMNS
# ============================================================

required_columns = [
    "movieId",
    "title",
    "genre",
    "mood",
    "average_rating",
    "review_count"
]

missing_columns = [
    column for column in required_columns
    if column not in movies.columns
]

if missing_columns:
    print("ERROR: The following columns are missing:")
    print(missing_columns)
    exit()


# ============================================================
# 3. DISPLAY DATASET INFORMATION
# ============================================================

print("=" * 65)
print("           MOVIE RECOMMENDATION SYSTEM")
print("=" * 65)

print("\nDataset loaded successfully.")

print("\nNumber of Movies:", len(movies))

print("\nAvailable Movies:")
print(
    movies[
        [
            "movieId",
            "title",
            "genre",
            "mood",
            "average_rating"
        ]
    ].to_string(index=False)
)


# ============================================================
# 4. GET UNIQUE PARAMETERS FROM DATASET
# ============================================================

genres = sorted(
    movies["genre"].dropna().unique()
)

moods = sorted(
    movies["mood"].dropna().unique()
)


# ============================================================
# 5. ASK USER FOR PARAMETERS
# ============================================================

print("\n" + "=" * 65)
print("              ENTER YOUR PREFERENCES")
print("=" * 65)


# ------------------------------------------------------------
# Genre
# ------------------------------------------------------------

print("\nAvailable Genres:")

for number, genre in enumerate(genres, start=1):
    print(f"{number}. {genre}")

genre_choice = input(
    "\nEnter your preferred genre number: "
).strip()

try:
    genre_index = int(genre_choice) - 1
    preferred_genre = genres[genre_index]
except (ValueError, IndexError):
    print("\nInvalid genre selection.")
    exit()


# ------------------------------------------------------------
# Mood
# ------------------------------------------------------------

print("\nAvailable Moods:")

for number, mood in enumerate(moods, start=1):
    print(f"{number}. {mood}")

mood_choice = input(
    "\nEnter your preferred mood number: "
).strip()

try:
    mood_index = int(mood_choice) - 1
    preferred_mood = moods[mood_index]
except (ValueError, IndexError):
    print("\nInvalid mood selection.")
    exit()


# ------------------------------------------------------------
# Minimum Rating
# ------------------------------------------------------------

try:
    minimum_rating = float(
        input(
            "\nEnter minimum rating you prefer (1-5): "
        )
    )
except ValueError:
    print("\nInvalid rating.")
    exit()

if not 1 <= minimum_rating <= 5:
    print("\nRating must be between 1 and 5.")
    exit()


# ------------------------------------------------------------
# Popularity
# ------------------------------------------------------------

print("\nDo you want a popular movie?")
print("1. Yes")
print("2. No")

popularity_choice = input(
    "Enter your choice: "
).strip()

if popularity_choice == "1":
    prefer_popular = True
elif popularity_choice == "2":
    prefer_popular = False
else:
    print("\nInvalid popularity selection.")
    exit()


# ============================================================
# 6. DISPLAY SELECTED PARAMETERS
# ============================================================

print("\n" + "=" * 65)
print("             YOUR SELECTED PARAMETERS")
print("=" * 65)

print("Genre          :", preferred_genre)
print("Mood           :", preferred_mood)
print("Minimum Rating :", minimum_rating)
print(
    "Popular Movie  :",
    "Yes" if prefer_popular else "No"
)


# ============================================================
# 7. FILTER MOVIES
# ============================================================

matching_movies = movies[
    (movies["genre"].str.lower() == preferred_genre.lower()) &
    (movies["mood"].str.lower() == preferred_mood.lower()) &
    (movies["average_rating"] >= minimum_rating)
].copy()


# ============================================================
# 8. APPLY POPULARITY CONDITION
# ============================================================

if prefer_popular:
    matching_movies = matching_movies[
        matching_movies["review_count"] >= 800
    ]


# ============================================================
# 9. RECOMMEND ONE MOVIE
# ============================================================

print("\n" + "=" * 65)
print("                 RECOMMENDATION")
print("=" * 65)

if matching_movies.empty:

    print("\nNo movie matches all your selected parameters.")
    print("Please try different preferences.")

else:

    # If multiple movies match, choose the one with:
    # 1. Highest average rating
    # 2. Highest number of reviews

    matching_movies = matching_movies.sort_values(
        by=["average_rating", "review_count"],
        ascending=[False, False]
    )

    recommended_movie = matching_movies.iloc[0]

    print("\nYour Recommended Movie:")
    print(
        "🎬",
        recommended_movie["title"]
    )

    print("\nMovie Details:")
    print(
        "Movie ID       :",
        recommended_movie["movieId"]
    )
    print(
        "Genre          :",
        recommended_movie["genre"]
    )
    print(
        "Mood           :",
        recommended_movie["mood"]
    )
    print(
        "Average Rating :",
        recommended_movie["average_rating"]
    )
    print(
        "Review Count   :",
        recommended_movie["review_count"]
    )

    print(
        "\nReason:"
    )
    print(
        "The movie matches your selected genre, mood, "
        "minimum rating, and popularity preference."
    )


# ============================================================
# 10. PROGRAM COMPLETED
# ============================================================

print("\n" + "=" * 65)
print("              PROGRAM COMPLETED")
print("=" * 65)
