import pandas as pd
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


# ============================================================
# 1. LOAD VALID PATIENT RECORDS FROM EXTERNAL CSV
# ============================================================

FILE_NAME = "patient_records.csv"

try:

    df = pd.read_csv(FILE_NAME)

except FileNotFoundError:

    print("ERROR: patient_records.csv was not found.")

    print(
        "Please place patient_records.csv "
        "in the same folder as this Python file."
    )

    exit()


# ============================================================
# 2. DISPLAY DATASET
# ============================================================

print("=" * 75)
print("          HEALTHCARE PATIENT RECORD SYSTEM")
print("=" * 75)

print("\nVALID PATIENT RECORDS:")
print(df)

print("\nDataset Shape:")
print(df.shape)

print("\nNumber of Valid Patients:")
print(len(df))


# ============================================================
# 3. CHECK REQUIRED COLUMNS
# ============================================================

required_columns = [
    "patient_id",
    "patient_name",
    "age",
    "gender",
    "disease",
    "blood_group"
]


for column in required_columns:

    if column not in df.columns:

        print(
            "\nERROR: Missing column:",
            column
        )

        exit()


# ============================================================
# 4. CREATE TEXT REPRESENTATION
# ============================================================

df["patient_text"] = (

    "name " +
    df["patient_name"].astype(str) +

    " age " +
    df["age"].astype(str) +

    " gender " +
    df["gender"].astype(str) +

    " disease " +
    df["disease"].astype(str) +

    " bloodgroup " +
    df["blood_group"].astype(str)
)


print("\n" + "=" * 75)
print("             PATIENT TEXT REPRESENTATION")
print("=" * 75)

print(
    df[
        [
            "patient_id",
            "patient_text"
        ]
    ]
)


# ============================================================
# 5. CREATE LEGITIMATE TRAINING DATA
# ============================================================

valid_training = pd.DataFrame({

    "text": df["patient_text"],

    "label": [
        "ham"
        for _ in range(len(df))
    ]
})


# ============================================================
# 6. GENERATE SYNTHETIC SPAM RECORDS
# ============================================================
#
# The external CSV contains ONLY valid patient records.
#
# Naive Bayes requires examples of both:
#
# HAM  = legitimate
# SPAM = suspicious
#
# Therefore, we generate suspicious records by deliberately
# modifying some patient information.
# ============================================================


spam_records = [

    "name fake patient age 999 gender unknown disease unknown bloodgroup fake",

    "name unknown patient age 300 gender unknown disease unknown bloodgroup fake",

    "name fake record age 500 gender unknown disease diabetes bloodgroup fake",

    "name suspicious patient age 999 gender unknown disease unknown bloodgroup unknown",

    "name invalid patient age 200 gender unknown disease hypertension bloodgroup fake",

    "name fake person age 999 gender unknown disease heart disease bloodgroup unknown",

    "name unknown person age 250 gender unknown disease asthma bloodgroup fake",

    "name invalid record age 1000 gender unknown disease diabetes bloodgroup unknown",

    "name suspicious record age 500 gender unknown disease unknown bloodgroup fake",

    "name fake patient age 999 gender unknown disease hypertension bloodgroup fake"
]


spam_training = pd.DataFrame({

    "text": spam_records,

    "label": [
        "spam"
        for _ in range(len(spam_records))
    ]
})


# ============================================================
# 7. COMBINE HAM + SPAM TRAINING DATA
# ============================================================

training_df = pd.concat(
    [
        valid_training,
        spam_training
    ],
    ignore_index=True
)


print("\n" + "=" * 75)
print("             TRAINING DATA")
print("=" * 75)

print(training_df)

print("\nTraining Class Distribution:")

print(
    training_df["label"].value_counts()
)


# ============================================================
# 8. TEXT PREPROCESSING
# ============================================================

def preprocess_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(
        r'[^a-z0-9\s]',
        ' ',
        text
    )

    # Remove extra spaces
    text = re.sub(
        r'\s+',
        ' ',
        text
    ).strip()

    return text


# Apply preprocessing
training_df["clean_text"] = (
    training_df["text"]
    .apply(preprocess_text)
)


print("\n" + "=" * 75)
print("             TEXT PREPROCESSING")
print("=" * 75)

print(
    training_df[
        [
            "text",
            "clean_text"
        ]
    ].head(15)
)


# ============================================================
# 9. FEATURES AND LABELS
# ============================================================

X = training_df["clean_text"]

y = training_df["label"]


print("\n" + "=" * 75)
print("             FEATURES AND LABELS")
print("=" * 75)

print("\nFEATURES:")

print(
    X.head()
)


print("\nLABELS:")

print(
    y.head()
)


# ============================================================
# 10. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.25,

    random_state=42,

    stratify=y
)


print("\n" + "=" * 75)
print("             TRAIN / TEST SPLIT")
print("=" * 75)

print(
    "\nTraining records:",
    len(X_train)
)

print(
    "Testing records:",
    len(X_test)
)


# ============================================================
# 11. TF-IDF
# ============================================================

vectorizer = TfidfVectorizer(

    ngram_range=(1, 2),

    lowercase=True
)


# Learn vocabulary from training data
X_train_tfidf = vectorizer.fit_transform(
    X_train
)


# Transform testing data
X_test_tfidf = vectorizer.transform(
    X_test
)


print("\n" + "=" * 75)
print("             TF-IDF VECTORIZATION")
print("=" * 75)

print(
    "\nTraining TF-IDF shape:"
)

print(
    X_train_tfidf.shape
)


print(
    "\nTesting TF-IDF shape:"
)

print(
    X_test_tfidf.shape
)


print(
    "\nNumber of TF-IDF features:"
)

print(
    len(
        vectorizer.get_feature_names_out()
    )
)


# ============================================================
# 12. TRAIN NAIVE BAYES
# ============================================================

model = MultinomialNB(
    alpha=0.1
)


model.fit(
    X_train_tfidf,
    y_train
)


print("\n" + "=" * 75)
print("             NAIVE BAYES MODEL")
print("=" * 75)

print(
    "\nNaive Bayes model trained successfully."
)


# ============================================================
# 13. MODEL PREDICTION
# ============================================================

y_pred = model.predict(
    X_test_tfidf
)


# ============================================================
# 14. MODEL EVALUATION
# ============================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)


print("\n" + "=" * 75)
print("             MODEL EVALUATION")
print("=" * 75)

print(
    "\nAccuracy:",
    f"{accuracy * 100:.2f}%"
)


print(
    "\nClassification Report:"
)


print(
    classification_report(
        y_test,
        y_pred,
        labels=[
            "ham",
            "spam"
        ],
        target_names=[
            "NOT SPAM",
            "SPAM"
        ],
        zero_division=0
    )
)


# ============================================================
# 15. UNKNOWN PATIENT RECORD FUNCTION
# ============================================================

def check_patient_record(

    patient_id,

    patient_name,

    age,

    gender,

    disease,

    blood_group
):


    # --------------------------------------------------------
    # STEP 1: CREATE TEXT
    # --------------------------------------------------------

    patient_text = (

        "name " +
        str(patient_name) +

        " age " +
        str(age) +

        " gender " +
        str(gender) +

        " disease " +
        str(disease) +

        " bloodgroup " +
        str(blood_group)
    )


    # --------------------------------------------------------
    # STEP 2: TEXT PREPROCESSING
    # --------------------------------------------------------

    clean_text = preprocess_text(
        patient_text
    )


    # --------------------------------------------------------
    # STEP 3: TF-IDF
    # --------------------------------------------------------

    patient_tfidf = vectorizer.transform(
        [clean_text]
    )


    # --------------------------------------------------------
    # STEP 4: NAIVE BAYES
    # --------------------------------------------------------

    prediction = model.predict(
        patient_tfidf
    )[0]


    probabilities = model.predict_proba(
        patient_tfidf
    )[0]


    # --------------------------------------------------------
    # GET PROBABILITIES
    # --------------------------------------------------------

    ham_index = list(
        model.classes_
    ).index("ham")


    spam_index = list(
        model.classes_
    ).index("spam")


    ham_probability = probabilities[
        ham_index
    ]


    spam_probability = probabilities[
        spam_index
    ]


    # --------------------------------------------------------
    # CHECK PATIENT ID
    # --------------------------------------------------------

    patient_exists = (

        patient_id in
        df["patient_id"].values
    )


    # ========================================================
    # DISPLAY PATIENT INFORMATION
    # ========================================================

    print("\n" + "=" * 75)

    print(
        "             PATIENT RECORD ANALYSIS"
    )

    print("=" * 75)


    print(
        "\nPatient ID:",
        patient_id
    )

    print(
        "Patient Name:",
        patient_name
    )

    print(
        "Age:",
        age
    )

    print(
        "Gender:",
        gender
    )

    print(
        "Disease:",
        disease
    )

    print(
        "Blood Group:",
        blood_group
    )


    # ========================================================
    # NAIVE BAYES RESULT
    # ========================================================

    print(
        "\nNaive Bayes Prediction:"
    )


    if prediction == "spam":

        print(
            "SPAM / SUSPICIOUS"
        )

    else:

        print(
            "NOT SPAM / LEGITIMATE"
        )


    print(
        "\nLegitimate Probability:",
        f"{ham_probability * 100:.2f}%"
    )


    print(
        "Spam Probability:",
        f"{spam_probability * 100:.2f}%"
    )


    # ========================================================
    # PATIENT ID VERIFICATION
    # ========================================================

    print(
        "\nPatient ID Verification:"
    )


    if patient_exists:

        print(
            "Patient ID exists in the CSV database."
        )

    else:

        print(
            "WARNING: Patient ID does not exist!"
        )


    # ========================================================
    # FINAL DECISION
    # ========================================================

    print(
        "\nFINAL RESULT:"
    )


    if (
        prediction == "spam"
        or
        not patient_exists
    ):

        print(
            ">>> SPAM / MISMATCH RECORD"
        )

        print(
            ">>> Manual verification required."
        )

    else:

        print(
            ">>> VALID PATIENT RECORD"
        )


# ============================================================
# 16. TEST VALID PATIENT
# ============================================================

print("\n\n")

print("=" * 75)

print(
    "             TESTING VALID PATIENT"
)

print("=" * 75)


check_patient_record(

    "P001",

    "Rahul",

    45,

    "male",

    "diabetes",

    "O positive"
)


# ============================================================
# 17. TEST UNKNOWN PATIENT
# ============================================================

print("\n\n")

print("=" * 75)

print(
    "             TESTING UNKNOWN PATIENT"
)

print("=" * 75)


check_patient_record(

    "P999",

    "Fake Patient",

    999,

    "unknown",

    "unknown",

    "fake"
)


# ============================================================
# 18. LIVE PATIENT RECORD CHECKER
# ============================================================

print("\n\n")

print("=" * 75)

print(
    "             LIVE PATIENT RECORD CHECKER"
)

print("=" * 75)


print(
    "\nEnter a patient record."
)

print(
    "Type 'exit' as Patient ID to stop."
)


while True:


    # --------------------------------------------------------
    # Patient ID
    # --------------------------------------------------------

    patient_id = input(
        "\nEnter Patient ID: "
    )


    if patient_id.lower() == "exit":

        print(
            "\nProgram terminated."
        )

        break


    # --------------------------------------------------------
    # Patient Name
    # --------------------------------------------------------

    patient_name = input(
        "Enter Patient Name: "
    )


    # --------------------------------------------------------
    # Age
    # --------------------------------------------------------

    age = input(
        "Enter Age: "
    )


    try:

        age = int(age)

    except ValueError:

        print(
            "Invalid age. Please enter a number."
        )

        continue


    # --------------------------------------------------------
    # Gender
    # --------------------------------------------------------

    gender = input(
        "Enter Gender: "
    )


    # --------------------------------------------------------
    # Disease
    # --------------------------------------------------------

    disease = input(
        "Enter Disease: "
    )


    # --------------------------------------------------------
    # Blood Group
    # --------------------------------------------------------

    blood_group = input(
        "Enter Blood Group: "
    )


    # --------------------------------------------------------
    # CHECK RECORD
    # --------------------------------------------------------

    check_patient_record(

        patient_id,

        patient_name,

        age,

        gender,

        disease,

        blood_group
    )