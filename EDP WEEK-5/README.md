# Movie Recommendation System Using Cosine Similarity

## 📌 Overview

A simple **Content-Based Movie Recommendation System** developed using Python. It recommends movies similar to the movie selected by the user using **TF-IDF and Cosine Similarity**.

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF
* Cosine Similarity

## 📂 Project Structure

```text
EDP WEEK-5/
├── dataset/movies.csv
├── src/recommendation.py
└── README.md
```

## ⚙️ How It Works

```text
movies.csv
    ↓
Read Dataset
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity
    ↓
Find Similar Movies
    ↓
Top 5 Recommendations
```

## ▶️ How to Run

Install the required libraries:

```bash
pip install pandas scikit-learn
```

Run the program:

```bash
python movie_recommendation.py
```

Enter a movie name when prompted:

```text
Enter the movie name: Avatar
```

The system will display the **Top 5 similar movies** with their similarity scores.

## 📊 Dataset

The `movies.csv` file contains:

* `title` – Movie name
* `description` – Movie features/keywords

## 🎯 Objective

To implement a simple movie recommendation system using **Cosine Similarity** and an externally stored CSV dataset.

## 🚀 Future Scope

* Use a larger movie dataset
* Add movie ratings and genres
* Build a Streamlit GUI
* Implement a hybrid recommendation system
