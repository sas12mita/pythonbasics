import pandas as pd

# ===== Create a Series (1D labeled data) =====
ser = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("Pandas Series:\n", ser)

# ===== Create a DataFrame (2D labeled data) =====
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# ===== Select a column =====
print("\nSelect 'Name' column:\n", df["Name"])

# ===== Filter rows =====
print("\nFilter Age > 28:\n", df[df["Age"] > 28])

# ===== Add a new column =====
df["Bonus"] = df["Salary"] * 0.1
print("\nWith Bonus column:\n", df)

# ===== Group by Age and get mean Salary =====
print("\nGroup by Age:\n", df.groupby("Age")["Salary"].mean())

# ===== Merge with another DataFrame =====
dept_data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Department": ["HR", "IT", "Finance"]
})
merged_df = pd.merge(df, dept_data, on="Name")
print("\nMerged DataFrame:\n", merged_df)

# ===== Handle missing data =====
df_with_nan = df.copy()
df_with_nan.loc[1, "Salary"] = None
print("\nWith NaN value:\n", df_with_nan)
print("\nFill NaN with 0:\n", df_with_nan.fillna(0))
