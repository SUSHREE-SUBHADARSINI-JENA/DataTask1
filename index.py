import pandas as pd

# Load dataset
df = pd.read_csv('personality_dataset.csv')

# Preview data
print(df.head())
print(df.info())

# 1. Handle missing values
print(df.isnull().sum())
df = df.dropna()  # You can replace this with df.fillna() if you want to preserve data

# 2. Remove duplicates
df = df.drop_duplicates()

# 3. No gender or timestamp columns to clean/standardize

# 4. Rename columns
df.columns = df.columns.str.lower().str.replace(' ', '_')

# 5. Check data types
print(df.dtypes)

# 6. Save cleaned dataset
df.to_csv('cleaned_dataset.csv', index=False)
