# 🏥 Healthcare Data Analysis using Pandas

## 📌 Project Overview

This project demonstrates how to perform **basic healthcare data analysis using the Pandas library** in Python. The dataset is loaded from an external CSV file, cleaned by handling missing values, analyzed using descriptive statistics, and prepared for machine learning by separating **Features (X)** and **Label (y)**.

This project is designed for beginners who are learning **Pandas** and **Data Preprocessing**.

---

## 🎯 Objectives

- Load healthcare data from a CSV file.
- Display dataset information.
- Identify missing values.
- Clean missing data using the mean of each column.
- Separate Features (X) and Label (y).
- Generate statistical summaries.
- Calculate average health metrics.
- Count patients based on diagnosis.
- Filter diabetic patients.

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas

---

## 📂 Project Structure

```
Healthcare-Data-Analysis/
│
├── healthcare.csv
├── Cleaning.py
└── README.md
```

---

## 📋 Dataset Description

The dataset contains the following attributes:

| Column | Description |
|---------|-------------|
| Patient_ID | Unique patient identifier |
| Age | Age of the patient |
| Gender | Male/Female |
| Blood_Pressure | Patient's blood pressure |
| Heart_Rate | Heart rate (BPM) |
| Sugar_Level | Blood sugar level |
| Diagnosis | Health condition (Target Variable) |

---

## 📄 Sample Dataset

```csv
Patient_ID,Age,Gender,Blood_Pressure,Heart_Rate,Sugar_Level,Diagnosis
101,25,Male,120,72,95,Healthy
102,40,Female,140,85,140,Diabetes
103,35,Male,130,78,110,Healthy
104,,Female,135,80,,Hypertension
105,50,Male,,90,160,Diabetes
106,45,Female,145,88,150,Diabetes
107,32,Male,125,75,100,Healthy
108,60,Female,155,92,180,Diabetes
109,55,Male,150,89,170,Hypertension
110,29,Female,118,70,90,Healthy
```

---

## ⚙️ Features Used (X)

The following columns are used as input features:

- Age
- Gender
- Blood_Pressure
- Heart_Rate
- Sugar_Level

```python
X = df[["Age","Gender","Blood_Pressure","Heart_Rate","Sugar_Level"]]
```

---

## 🎯 Label (y)

The target variable is:

```python
y = df["Diagnosis"]
```

Possible values:

- Healthy
- Diabetes
- Hypertension

---

## 🔄 Workflow

```
Load CSV Dataset
        │
        ▼
Display Dataset
        │
        ▼
Check Dataset Information
        │
        ▼
Find Missing Values
        │
        ▼
Clean Missing Values
        │
        ▼
Display Cleaned Dataset
        │
        ▼
Separate Features (X)
        │
        ▼
Separate Label (y)
        │
        ▼
Generate Statistics
        │
        ▼
Calculate Average Values
        │
        ▼
Count Diagnosis Categories
        │
        ▼
Filter Diabetes Patients
```

---

## 📊 Pandas Functions Used

| Function | Purpose |
|----------|---------|
| `pd.read_csv()` | Load CSV file |
| `DataFrame()` | Create DataFrame |
| `info()` | Display dataset information |
| `isnull()` | Check missing values |
| `sum()` | Count missing values |
| `fillna()` | Replace missing values |
| `mean()` | Calculate average |
| `describe()` | Generate statistical summary |
| `value_counts()` | Count occurrences of each diagnosis |
| `print()` | Display output |
| `df[condition]` | Filter rows based on conditions |

---

## ▶️ How to Run

### Step 1

Install Pandas

```bash
pip install pandas
```

### Step 2

Place the following files in the same folder.

```
healthcare.csv
healthcare_analysis.py
```

### Step 3

Run the program.

```bash
python healthcare_analysis.py
```

---

## 📈 Expected Output

The program will display:

- Original Healthcare Dataset
- Missing Values
- Cleaned Dataset
- Features (X)
- Label (y)
- Average Health Values
- Diagnosis Count
- Diabetes Patient Details

---

## 📚 Learning Outcomes

After completing this project, you will understand:

- Reading CSV files using Pandas
- Working with DataFrames
- Data Cleaning
- Handling Missing Values
- Data Exploration
- Feature and Label Selection
- Healthcare Dataset Analysis

---

## 🚀 Future Enhancements

- Add data visualization using Matplotlib.
- Perform data analysis using Seaborn.
- Build machine learning models using Scikit-learn.
- Predict diseases using classification algorithms.
- Develop an interactive healthcare dashboard.

---

## 👨‍💻 Author

**Valaboju Raghava**

B.Tech - Information Technology

Institute of Aeronautical Engineering, Hyderabad

---

## 📄 License

This project is created for educational and learning purposes.
