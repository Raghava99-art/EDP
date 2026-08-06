# Healthcare Cost Prediction using Linear Regression

## Overview

This project demonstrates a simple implementation of **Linear Regression** using **Python**, **NumPy**, and **Pandas**. The model predicts a patient's **medical cost** based on their **blood pressure**.

The project does **not** use Scikit-learn. Instead, it calculates the regression line using the mathematical formula.

## Dataset

The dataset is stored in a CSV file named:

`healthcare_data.csv`

It contains the following columns:

* **Blood_Pressure** – Patient's blood pressure
* **Medical_Cost** – Patient's medical cost

## Requirements

Install the required libraries:

```bash
pip install pandas numpy
```

## Project Files

```
EDP WEEK-2/
│
├── Dataset
├── src
└── README.md
```

## How to Run

1. Save the dataset as `healthcare_data.csv`.
2. Save the Python program as `Train_Test.py`.
3. Open a terminal in the project folder.
4. Run the program:

```bash
python Train_Test.py
```

## Features

* Reads data from a CSV file.
* Splits the dataset into training and testing data.
* Trains a Linear Regression model manually.
* Predicts medical costs.
* Calculates:

  * Mean Absolute Error (MAE)
  * Mean Squared Error (MSE)
  * Root Mean Squared Error (RMSE)

## Technologies Used

* Python
* Pandas
* NumPy

## Output

The program displays:

* Healthcare dataset
* Training and testing data
* Regression equation
* Predicted medical costs
* Evaluation metrics (MAE, MSE, RMSE)
