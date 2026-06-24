import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("="*60)
print("Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicates")
print(df.duplicated().sum())

print("\nFirst 5 Rows")
print(df.head())