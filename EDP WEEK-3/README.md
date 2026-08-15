Healthcare Patient Record Spam Detection
Overview

This project detects suspicious or mismatched healthcare patient records using Text Preprocessing, TF-IDF, and Naive Bayes.

The valid patient records are stored in an external CSV file. The program reads the records, processes the patient information, trains a Naive Bayes model, and predicts whether a new patient record is SPAM or NOT SPAM.

Dataset

The dataset is stored in:

patient_records.csv

It contains:

patient_id
patient_name
age
gender
disease
blood_group

The dataset contains 10 valid patient records.

Requirements

Install the required libraries:

pip install pandas scikit-learn
Project Files
EDP WEEK-3/
│
├── Dataset/patient_records.csv
├── src/healthcare_spam_detector.py
└── README.md
How to Run
Place patient_records.csv and healthcare_spam_detector.py in the same folder.
Open the terminal in the project folder.
Install the required libraries.
Run the program:
python healthcare_spam_detector.py
Concepts Used
Text Preprocessing – Cleans and prepares patient information.
TF-IDF – Converts text into numerical features.
Naive Bayes – Classifies patient records as SPAM or NOT SPAM.
Pandas – Loads and manages the CSV dataset.
Features
Reads patient records from CSV.
Processes patient information.
Trains a Naive Bayes classifier.
Checks Patient IDs.
Accepts new patient records.
Detects suspicious/mismatched records.
Displays SPAM/NOT SPAM prediction.
Output

The program displays:

Patient records
Text preprocessing results
TF-IDF information
Model accuracy
Classification report
Patient record prediction
SPAM / NOT SPAM result
Author

Valaboju Raghava
