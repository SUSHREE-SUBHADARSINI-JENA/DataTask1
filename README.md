````markdown
# Task 1 – Data Cleaning and Preprocessing

## 🧠 Dataset: Personality Traits & Social Behavior

### 🎯 Objective
To clean and preprocess a personality traits dataset by addressing missing values, removing duplicates, standardizing column names, and preparing the data for analysis.

---

## 📂 Dataset Overview

- **Filename:** `personality_dataset.csv`
- **Records:** 2,900 rows
- **Columns:** 8
- **Features Include:**
  - Time spent alone
  - Stage fear
  - Social event attendance
  - Going outside
  - Drained after socializing
  - Friends circle size
  - Social media post frequency
  - Personality type (Introvert/Extrovert)

---

## 🛠 Tools Used

- Python 3.13
- Pandas library

---

## ⚙️ Steps Performed

### 1. **Loaded the Dataset**
```python
df = pd.read_csv('personality_dataset.csv')
````

### 2. **Checked Data Structure and Missing Values**

* Used `df.info()` and `df.isnull().sum()` to inspect the data
* Found missing values in several columns (63–77 rows missing in different columns)

### 3. **Handled Missing Values**

* Dropped rows with missing values using `df.dropna()`

  > *Note: You can also fill missing values using `fillna()` if you want to preserve more data.*

### 4. **Removed Duplicates**

```python
df = df.drop_duplicates()
```

### 5. **Renamed Columns**

* Standardized all column names by:

  * Converting to lowercase
  * Replacing spaces with underscores

```python
df.columns = df.columns.str.lower().str.replace(' ', '_')
```

### 6. **Exported the Cleaned Dataset**

```python
df.to_csv('cleaned_dataset.csv', index=False)
```

---

## ✅ Output Files

* `cleaned_dataset.csv` – The cleaned dataset
* `index.py` – Python script with data cleaning steps
* `README.md` – Task summary and documentation

---

## 📁 Project Structure

```
task-1-personality-cleaning/
├── personality_dataset.csv
├── cleaned_dataset.csv
├── index.py
└── README.md
```

