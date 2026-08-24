# 🎬 Movie Recommendation System

> A simple parameter-based movie recommendation system built using **Python and Pandas**. The system loads movie information from an external CSV dataset, asks the user for movie preferences, and recommends **one movie that best matches the selected parameters**.

---

## 📌 Project Overview

Movie recommendation systems help users discover movies based on their interests and preferences.

This project implements a simple **parameter-based movie recommendation system**. Instead of displaying multiple movies, the system asks the user for specific preferences such as:

* Movie genre
* Movie mood
* Minimum rating
* Popularity preference

The program then compares these parameters with the movies available in the dataset and recommends **one movie that satisfies all the selected conditions**.

If multiple movies match the parameters, the movie with the **highest average rating** is selected. If the ratings are equal, the number of reviews is used as the next criterion.

---

## 🎯 Project Objective

The main objective of this project is to develop an interactive movie recommendation system that can:

* Load movie data from an external CSV file.
* Display available movies and their information.
* Ask the user for movie preferences.
* Match user preferences with the dataset.
* Filter movies according to the selected parameters.
* Consider movie ratings and review counts.
* Recommend exactly **one movie**.
* Display the reason for the recommendation.
* Handle cases where no movie matches the selected parameters.

---

## 🛠️ Technologies Used

| Technology     | Purpose                                    |
| -------------- | ------------------------------------------ |
| 🐍 **Python**  | Main programming language                  |
| 🐼 **Pandas**  | Dataset loading, filtering, and processing |
| 📄 **CSV**     | Stores the movie dataset                   |
| 💻 **VS Code** | Development environment                    |

---

## 📊 Dataset

The project uses a separate CSV file named:

```text
movies_dataset.csv
```

The dataset contains information about movies and their review patterns.

### Dataset Columns

| Column           | Description                     |
| ---------------- | ------------------------------- |
| `movieId`        | Unique ID of the movie          |
| `title`          | Movie title                     |
| `genre`          | Movie genre                     |
| `mood`           | General mood of the movie       |
| `average_rating` | Average rating given by viewers |
| `review_count`   | Number of reviews received      |

### Example

```text
movieId,title,genre,mood,average_rating,review_count
101,Titanic,Romance,Emotional,4.8,950
102,Avatar,Sci-Fi,Exciting,4.7,900
103,Inception,Sci-Fi,Suspenseful,4.9,1000
104,Interstellar,Sci-Fi,Emotional,4.8,920
```

---

## 🔄 Project Workflow

```text
                 MOVIE CSV DATASET
                        │
                        ▼
                  LOAD DATASET
                        │
                        ▼
                DATASET VALIDATION
                        │
                        ▼
             DISPLAY AVAILABLE MOVIES
                        │
                        ▼
               ASK USER PREFERENCES
                        │
            ┌───────────┼───────────┐
            ▼           ▼           ▼
          Genre        Mood      Min Rating
            │           │           │
            └───────────┼───────────┘
                        │
                        ▼
              POPULARITY PREFERENCE
                        │
                        ▼
                 FILTER MOVIES
                        │
                        ▼
              MATCH ALL PARAMETERS
                        │
                 ┌──────┴──────┐
                 ▼             ▼
               Match        No Match
                 │             │
                 ▼             ▼
          Select Best Movie   Show Message
                 │
                 ▼
          ONE MOVIE OUTPUT
```

---

## ⚙️ How the System Works

### 1. Load the Dataset

The program reads the external CSV file using Pandas:

```python
movies = pd.read_csv("movies_dataset.csv")
```

---

### 2. Validate the Dataset

The program checks whether the required columns are present:

```text
movieId
title
genre
mood
average_rating
review_count
```

If a required column is missing, the program displays an error message.

---

### 3. Ask User Preferences

The user is asked to provide four parameters:

```text
Genre
Mood
Minimum Rating
Popularity
```

For example:

```text
Genre: Sci-Fi
Mood: Exciting
Minimum Rating: 4.5
Popular Movie: Yes
```

---

### 4. Filter Movies

The program filters the dataset based on the selected parameters.

For example:

```python
matching_movies = movies[
    (movies["genre"] == preferred_genre) &
    (movies["mood"] == preferred_mood) &
    (movies["average_rating"] >= minimum_rating)
]
```

If the user selects popular movies, the program additionally checks the number of reviews.

---

### 5. Select One Movie

If several movies satisfy the conditions, the system sorts them using:

1. Highest average rating
2. Highest review count

The first movie after sorting becomes the recommendation.

---

## 🧠 Recommendation Logic

The recommendation process can be represented as:

```text
User Parameters
      │
      ▼
Genre Match?
      │
      ▼
Mood Match?
      │
      ▼
Rating ≥ User Requirement?
      │
      ▼
Popularity Requirement?
      │
      ▼
Matching Movies
      │
      ▼
Highest Rating
      │
      ▼
Highest Review Count
      │
      ▼
ONE RECOMMENDED MOVIE
```

---

## 💡 Example

Suppose the user enters:

```text
Preferred Genre: Sci-Fi
Preferred Mood: Exciting
Minimum Rating: 4.5
Popular Movie: Yes
```

The dataset may contain:

| Movie        | Genre  | Mood        | Rating | Reviews |
| ------------ | ------ | ----------- | -----: | ------: |
| Avatar       | Sci-Fi | Exciting    |    4.7 |     900 |
| Inception    | Sci-Fi | Suspenseful |    4.9 |    1000 |
| Interstellar | Sci-Fi | Emotional   |    4.8 |     920 |

Only **Avatar** satisfies all the selected conditions.

Therefore, the final output is:

```text
Your Recommended Movie:
🎬 Avatar

Movie Details:
Movie ID       : 102
Genre          : Sci-Fi
Mood           : Exciting
Average Rating : 4.7
Review Count   : 900

Reason:
The movie matches your selected genre, mood,
minimum rating, and popularity preference.
```

---

## 📁 Project Structure

```text
EDP WEEK-4/
│
├── src/movie_recommendation.py
├── dataset/movies_dataset.csv
└── README.md
```

### File Description

**`movie_recommendation.py`**

Contains the complete recommendation system.

**`movies_dataset.csv`**

Contains the movie information used by the program.

**`requirements.txt`**

Contains the required Python libraries.

**`README.md`**

Contains project documentation and instructions.

---

## 🚀 Installation

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation:

```bash
python --version
```

---

### Step 2: Install Pandas

Open the terminal in the project folder and run:

```bash
pip install pandas
```

Alternatively, install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Make sure the following files are in the same folder:

```text
movie_recommendation.py
movies_dataset.csv
```

Then run:

```bash
python movie_recommendation.py
```

---

## 🖥️ Sample User Interaction

```text
=================================================================
           MOVIE RECOMMENDATION SYSTEM
=================================================================

Dataset loaded successfully.

Number of Movies: 15

Available Genres:
1. Action
2. Adventure
3. Animation
4. Drama
5. Horror
6. Romance
7. Sci-Fi

Enter your preferred genre number: 7

Available Moods:
1. Emotional
2. Exciting
3. Funny
4. Suspenseful

Enter your preferred mood number: 2

Enter minimum rating you prefer (1-5): 4.5

Do you want a popular movie?
1. Yes
2. No

Enter your choice: 1
```

The program then processes the selected parameters and returns a single movie.

---

## 📌 Features

* ✅ External CSV dataset
* ✅ Interactive user input
* ✅ Genre-based filtering
* ✅ Mood-based filtering
* ✅ Rating-based filtering
* ✅ Popularity-based filtering
* ✅ Single movie recommendation
* ✅ Highest-rated movie selection
* ✅ Review count consideration
* ✅ Dataset validation
* ✅ Handles invalid input
* ✅ Handles no-match situations
* ✅ Simple and beginner-friendly implementation

---

## ⚠️ No-Match Case

If no movie satisfies all the selected parameters, the system does not randomly recommend a movie.

Instead, it displays:

```text
No movie matches all your selected parameters.
Please try different preferences.
```

This ensures that the final recommendation actually follows the user's requirements.

---

## 🔮 Future Enhancements

The current project uses structured movie parameters. It can be extended into a more advanced recommendation system by adding:

* ⭐ User rating history
* 📝 Review text analysis
* 🧠 Natural Language Processing
* 🔍 TF-IDF
* 📐 Cosine Similarity
* 🤝 Collaborative Filtering
* 🎭 Actor and director preferences
* 🎬 Multiple genre support
* 😊 Sentiment analysis of reviews
* 🎯 Personalized user profiles
* 📊 Recommendation confidence scores
* 🌐 Web-based recommendation interface
* 🤖 Machine Learning-based recommendations

---

## 📈 Future Advanced Workflow

A more advanced version can use actual review text:

```text
              MOVIE DATASET
                    │
                    ▼
             USER ENTERS REVIEW
                    │
                    ▼
             TEXT PREPROCESSING
                    │
                    ▼
                TF-IDF
                    │
                    ▼
           COSINE SIMILARITY
                    │
                    ▼
        COMPARE WITH MOVIE REVIEWS
                    │
                    ▼
          FIND BEST MATCHING MOVIE
                    │
                    ▼
             ONE RECOMMENDATION
```

For example:

```text
User Review:
"I like exciting science fiction movies
with amazing visuals and suspense."

                    ↓

Review Analysis

                    ↓

Best Matching Movie:
🎬 Inception
```

---

## 👨‍💻 Author

**Valaboju Raghava**

B.Tech – Information Technology

---

## 📄 License

This project is created for **educational and academic purposes**.
