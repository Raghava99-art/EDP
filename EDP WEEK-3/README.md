Healthcare Patient Record Spam Detection

A simple machine learning project that detects suspicious or mismatched healthcare patient records using Text Preprocessing, TF-IDF, and Naive Bayes.

The project reads valid patient records from an external CSV file and analyzes new patient records to determine whether they are legitimate or SPAM/SUSPICIOUS.

📌 Project Overview

Healthcare systems maintain large amounts of patient information such as:

Patient ID
Patient Name
Age
Gender
Disease
Blood Group

Incorrect, fake, or suspicious records can cause problems in healthcare databases.

This project demonstrates a simple machine learning approach where patient records are converted into text and processed using:

Text Preprocessing
TF-IDF Vectorization
Multinomial Naive Bayes
Patient ID Verification
SPAM / Mismatch Detection
🎯 Objectives

The main objectives of this project are:

Read patient records from an external CSV file.
Maintain valid patient records.
Convert patient information into text.
Clean and preprocess the text.
Convert text into numerical features using TF-IDF.
Train a Naive Bayes classifier.
Detect suspicious patient records.
Check whether a Patient ID exists in the database.
Allow users to enter unknown patient records.
Report suspicious records as SPAM / MISMATCH.
🧠 Concepts Used
1. Text Preprocessing

Patient information is converted into text and cleaned before machine learning.

The preprocessing includes:

Converting text to lowercase.
Removing special characters.
Removing unnecessary spaces.

Example:

Name Rahul Age 45 Gender Male Disease Diabetes Blood Group O Positive

After preprocessing:

name rahul age 45 gender male disease diabetes bloodgroup o positive
2. TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) converts the patient text into numerical features that can be understood by the machine learning model.

The project uses:

TfidfVectorizer(
    ngram_range=(1, 2),
    lowercase=True
)

The ngram_range=(1,2) allows the model to learn both individual words and pairs of words.

For example:

diabetes
bloodgroup
medical
health

and:

blood group
patient name
heart disease
3. Naive Bayes

The project uses:

MultinomialNB(alpha=0.1)

Naive Bayes learns patterns from:

HAM  → Legitimate records
SPAM → Suspicious records

It then predicts the class of an unknown patient record.

🏗️ Project Architecture
                 patient_records.csv
                         │
                         ▼
                  Load using Pandas
                         │
                         ▼
                  Valid Patient Data
                         │
                         ▼
               Convert Records to Text
                         │
                         ▼
                 Text Preprocessing
                         │
                         ▼
                       TF-IDF
                         │
                         ▼
                  Naive Bayes Model
                         │
                         ▼
                    Trained Model
                         │
                         ▼
                New Patient Record
                         │
                ┌────────┴────────┐
                ▼                 ▼
          Patient ID Check     ML Prediction
                │                 │
                │              TF-IDF
                │                 │
                │           Naive Bayes
                │                 │
                └────────┬────────┘
                         ▼
                   Final Decision
                         │
                ┌────────┴────────┐
                ▼                 ▼
             VALID          SPAM / MISMATCH
📁 Project Structure
Healthcare_Spam_Detection/
│
├── healthcare_spam_detector.py
│
├── patient_records.csv
│
└── README.md
Files
File	Description
healthcare_spam_detector.py	Main Python machine learning program
patient_records.csv	External dataset containing valid patient records
README.md	Project documentation
📊 Dataset

The project uses an external CSV file named:

patient_records.csv

The dataset contains 10 valid patient records.

Dataset Columns
Column	Description
patient_id	Unique patient identification number
patient_name	Patient name
age	Patient age
gender	Patient gender
disease	Patient's disease
blood_group	Patient blood group
Sample Dataset
patient_id,patient_name,age,gender,disease,blood_group
P001,Rahul,45,male,diabetes,O positive
P002,Anita,32,female,hypertension,A positive
P003,Suresh,51,male,diabetes,B positive
P004,Priya,28,female,asthma,O positive
P005,Arjun,60,male,hypertension,A negative
P006,Neha,37,female,diabetes,B positive
P007,Ravi,49,male,heart disease,O positive
P008,Kiran,41,male,asthma,AB positive
P009,Meena,35,female,diabetes,A positive
P010,Vijay,55,male,hypertension,B negative
⚙️ Technologies Used
Python
Pandas
NumPy / Python standard library
Scikit-learn
Regular Expressions
Machine Learning
TF-IDF Vectorization
Multinomial Naive Bayes
Train/Test Split
Accuracy
Classification Report
💻 Requirements

Make sure Python is installed on your computer.

Check Python:

python --version

Install the required libraries:

pip install pandas scikit-learn
🚀 How to Run
Step 1: Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
Step 2: Open the project
cd Healthcare_Spam_Detection
Step 3: Install dependencies
pip install pandas scikit-learn
Step 4: Check the files

Make sure the folder contains:

healthcare_spam_detector.py
patient_records.csv
Step 5: Run the program
python healthcare_spam_detector.py
🔄 Working Process
Step 1 — Load Dataset

The program reads the external CSV using Pandas:

df = pd.read_csv("patient_records.csv")
Step 2 — Create Patient Text

The different patient fields are combined into a single text representation:

name rahul age 45 gender male disease diabetes bloodgroup o positive

This allows the project to apply NLP techniques to structured patient information.

Step 3 — Text Preprocessing

The text is converted into lowercase and special characters are removed.

text = text.lower()

Regular expressions are used to clean unwanted characters.

Step 4 — Create Training Classes

Valid records are treated as:

HAM

Suspicious records are treated as:

SPAM

Since the external CSV contains only legitimate records, the program generates a small set of synthetic suspicious examples for Naive Bayes training.

Step 5 — TF-IDF

The cleaned text is transformed into numerical vectors:

X_train_tfidf = vectorizer.fit_transform(X_train)
Step 6 — Naive Bayes Training

The classifier is trained using:

model = MultinomialNB(alpha=0.1)


model.fit(X_train_tfidf, y_train)
Step 7 — Model Evaluation

The model is evaluated using:

accuracy_score()

and:

classification_report()

The classification report provides:

Precision
Recall
F1-score
Support
Step 8 — Unknown Patient Detection

The user can enter a new patient record.

For example:

Patient ID: P999
Patient Name: Fake Patient
Age: 999
Gender: unknown
Disease: unknown
Blood Group: fake

The system processes the record through:

Preprocessing
      ↓
TF-IDF
      ↓
Naive Bayes
      ↓
Prediction
🧪 Example 1 — Valid Patient

Input:

Patient ID: P001
Patient Name: Rahul
Age: 45
Gender: male
Disease: diabetes
Blood Group: O positive

Possible result:

Naive Bayes Prediction:
NOT SPAM / LEGITIMATE


Patient ID Verification:
Patient ID exists in the CSV database.


FINAL RESULT:
>>> VALID PATIENT RECORD
🧪 Example 2 — Unknown Patient

Input:

Patient ID: P999
Patient Name: Fake Patient
Age: 999
Gender: unknown
Disease: unknown
Blood Group: fake

Possible result:

Naive Bayes Prediction:
SPAM / SUSPICIOUS


Patient ID Verification:
WARNING: Patient ID does not exist!


FINAL RESULT:
>>> SPAM / MISMATCH RECORD
>>> Manual verification required.
🧪 Example 3 — Live Input

The program provides an interactive system:

Enter a patient record.
Type 'exit' as Patient ID to stop.


Enter Patient ID:
Enter Patient Name:
Enter Age:
Enter Gender:
Enter Disease:
Enter Blood Group:

The entered record is then analyzed by the model.

📈 Model Evaluation

The project evaluates the Naive Bayes classifier using:

accuracy_score()

and:

classification_report()

Example output:

Accuracy: XX.XX%


Classification Report:


              precision    recall    f1-score


NOT SPAM          ...
SPAM              ...

The exact accuracy can change because the dataset is small and the train/test split is randomized using a fixed random_state.

🔍 Important Features
External Dataset

Unlike a hard-coded dataset, the valid patient records are stored separately:

patient_records.csv

This makes it easy to update patient information without changing the Python code.

Automatic Text Processing

Patient information is automatically converted into a format suitable for NLP.

Machine Learning

The system uses:

TF-IDF + Multinomial Naive Bayes

to classify suspicious records.

Patient ID Verification

The system checks whether the entered Patient ID exists in the CSV database.

Interactive Prediction

Users can enter new patient records directly through the terminal.

⚠️ Important Limitation

This project is designed as an educational machine learning project.

It should not be used as an actual healthcare fraud detection or patient verification system.

The dataset contains only 10 legitimate records, so it is too small for a real-world healthcare application.

Also, "SPAM" in this project means:

Suspicious / Mismatched Record

It does not prove that a patient record is fraudulent.

A real healthcare system would require:

Large validated datasets
Strong authentication
Secure databases
Encryption
Access control
Audit logs
Privacy protection
Robust anomaly detection
Human verification
🔮 Future Improvements

The project can be extended by:

Increasing the patient dataset from 10 records to thousands of records.
Adding more healthcare fields.
Implementing exact field-by-field record comparison.
Adding duplicate patient detection.
Adding anomaly detection.
Adding a graphical user interface.
Connecting the system to MySQL.
Creating a Flask or FastAPI backend.
Adding a web-based patient verification system.
Using advanced NLP models for better classification.
Adding authentication and authorization.
Generating an automatic mismatch report.
🎓 Learning Outcomes

After completing this project, you will understand:

How to load external CSV datasets using Pandas.
How structured healthcare data can be represented as text.
Basic text preprocessing.
TF-IDF feature extraction.
Training a Naive Bayes classifier.
Training/testing dataset splitting.
Model evaluation.
Classification of unknown records.
Patient ID verification.
Basic healthcare anomaly/spam detection.
📚 Machine Learning Workflow
Dataset
   ↓
Data Loading
   ↓
Data Preparation
   ↓
Text Representation
   ↓
Text Preprocessing
   ↓
Train/Test Split
   ↓
TF-IDF
   ↓
Naive Bayes
   ↓
Model Evaluation
   ↓
Unknown Patient Record
   ↓
Prediction
   ↓
SPAM / NOT SPAM
👨‍💻 Author

Valaboju Raghava

B.Tech – Information Technology

⭐ Conclusion

The Healthcare Patient Record Spam Detection project demonstrates how basic Natural Language Processing and Machine Learning techniques can be combined to identify suspicious patient records.

The project follows:

Text Preprocessing
        +
TF-IDF
        +
Naive Bayes
        ↓
Healthcare Patient Record
Spam Detection

It provides a simple foundation that can later be extended into a complete healthcare record verification and anomaly detection system.
