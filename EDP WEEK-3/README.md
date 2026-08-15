Healthcare Patient Record Spam Detection
Overview

This project demonstrates a simple implementation of Spam Detection using Python, Pandas, and Scikit-learn.

The system detects suspicious or mismatched healthcare patient records using the following machine learning concepts:

Text Preprocessing
TF-IDF (Term Frequency-Inverse Document Frequency)
Naive Bayes Classification

The valid patient records are stored in an external CSV file named patient_records.csv. The program reads the dataset, converts patient information into text, preprocesses the text, applies TF-IDF, and trains a Multinomial Naive Bayes model.

The system can then take an unknown patient record and classify it as NOT SPAM or SPAM / MISMATCH.

Dataset

The dataset is stored in a CSV file named:

patient_records.csv

It contains the following columns:

patient_id – Unique patient identification number
patient_name – Patient name
age – Patient age
gender – Patient gender
disease – Patient's disease
blood_group – Patient blood group

The dataset contains 10 valid patient records.

Example:

patient_id,patient_name,age,gender,disease,blood_group
P001,Rahul,45,male,diabetes,O positive
P002,Anita,32,female,hypertension,A positive
P003,Suresh,51,male,diabetes,B positive
P004,Priya,28,female,asthma,O positive
P005,Arjun,60,male,hypertension,A negative
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
Save the valid patient records as patient_records.csv.
Save the Python program as healthcare_spam_detector.py.
Place both files in the same project folder.
Open a terminal in the project folder.
Install the required libraries:
pip install pandas scikit-learn
Run the program:
python healthcare_spam_detector.py
Features
Reads patient records from an external CSV file.
Displays the patient dataset.
Converts patient records into text.
Performs text preprocessing.
Converts text into numerical features using TF-IDF.
Splits the dataset into training and testing data.
Trains a Multinomial Naive Bayes model.
Evaluates the classification model.
Checks whether a Patient ID exists in the database.
Accepts unknown patient records as user input.
Predicts whether the record is legitimate or suspicious.
Displays SPAM / MISMATCH for suspicious records.
Displays probability of SPAM and NOT SPAM.
Machine Learning Concepts Used
Text Preprocessing

The patient information is converted into text and cleaned by:

Converting text to lowercase
Removing special characters
Removing unnecessary spaces

Example:

Name Rahul Age 45 Gender Male Disease Diabetes Blood Group O Positive

becomes:

name rahul age 45 gender male disease diabetes bloodgroup o positive
TF-IDF

TF-IDF converts the preprocessed patient information into numerical features that can be used by the machine learning model.

The project uses:

TfidfVectorizer(ngram_range=(1, 2))
Naive Bayes

The project uses the Multinomial Naive Bayes algorithm to classify patient records into:

NOT SPAM – Legitimate record
SPAM – Suspicious or mismatched record
Working Process
Patient Records CSV
        ↓
Load Dataset using Pandas
        ↓
Convert Patient Record to Text
        ↓
Text Preprocessing
        ↓
TF-IDF Vectorization
        ↓
Naive Bayes Training
        ↓
Model Evaluation
        ↓
New Patient Record
        ↓
Text Preprocessing
        ↓
TF-IDF
        ↓
Naive Bayes Prediction
        ↓
SPAM / NOT SPAM
Patient Record Verification

The program also checks whether the entered Patient ID exists in the CSV dataset.

For example:

Patient ID: P001

If P001 exists:

Patient ID exists in the CSV database.

If an unknown ID is entered:

Patient ID: P999

The system reports:

WARNING: Patient ID does not exist!

and the final result can be:

SPAM / MISMATCH RECORD
Example Input
Enter Patient ID: P999
Enter Patient Name: Fake Patient
Enter Age: 999
Enter Gender: unknown
Enter Disease: unknown
Enter Blood Group: fake
Example Output
Naive Bayes Prediction:
SPAM / SUSPICIOUS


Legitimate Probability: XX.XX%
Spam Probability: XX.XX%


Patient ID Verification:
WARNING: Patient ID does not exist!


FINAL RESULT:
>>> SPAM / MISMATCH RECORD
>>> Manual verification required.
Model Evaluation

The model evaluates its performance using:

Accuracy
Precision
Recall
F1-Score

The program uses:

accuracy_score()

and:

classification_report()

to evaluate the Naive Bayes classifier.

Technologies Used
Python
Pandas
Scikit-learn
Regular Expressions
TF-IDF
Multinomial Naive Bayes
Output

The program displays:

Healthcare patient dataset
Dataset shape
Patient text representation
Preprocessed text
Features and labels
Training and testing data
TF-IDF features
Naive Bayes model status
Model accuracy
Classification report
Patient ID verification
Unknown patient prediction
SPAM / NOT SPAM probability
Final patient record status
