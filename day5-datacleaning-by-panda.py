import pandas as pd

# -----------------------------
# 1. Load dataset
# -----------------------------
df = pd.read_csv("data.csv")   # replace with your file
print("🔹 Original Data:")
print(df.head())

# -----------------------------
# 2. Handle Missing Values
# -----------------------------
# Fill missing numeric with mean
df['age'] = df['age'].fillna(df['age'].mean())

# Fill missing categorical with "Unknown"
df['city'] = df['city'].fillna("Unknown")

# -----------------------------
# 3. Remove Duplicates
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# 4. Fix Data Types
# -----------------------------
df['date'] = pd.to_datetime(df['date'], errors='coerce')   # convert to datetime
df['age'] = df['age'].astype(int)                          # convert to integer

# -----------------------------
# 5. Clean Text Columns
# -----------------------------
df['name'] = df['name'].str.strip().str.lower()            # trim + lowercase
df['name'] = df['name'].str.replace(r'[^a-zA-Z ]', '', regex=True)  # remove special chars

# -----------------------------
# 6. Handle Outliers (IQR method)
# -----------------------------
if 'salary' in df.columns:
    Q1 = df['salary'].quantile(0.25)
    Q3 = df['salary'].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df['salary'] >= Q1 - 1.5*IQR) & (df['salary'] <= Q3 + 1.5*IQR)]

# -----------------------------
# 7. Rename & Reorder Columns
# -----------------------------
df.rename(columns={"oldName": "newName"}, inplace=True)    # example rename
df = df[['name', 'age', 'city', 'salary', 'date']]         # reorder columns (adjust as per your dataset)

# -----------------------------
# 8. Save Cleaned Data
# -----------------------------
df.to_csv("cleaned_data.csv", index=False)

print("\n✅ Cleaned Data Saved as 'cleaned_data.csv'")
print(df.head())
