import pandas as pd

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("=" * 60)
print("Original Shape:", df.shape)

# ==========================================
# Remove Duplicates
# ==========================================

duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows Found: {duplicates}")

df = df.drop_duplicates()

# ==========================================
# Check Missing Values
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================================
# Validate Return Columns
# ==========================================

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nReturn Columns Successfully Converted to Numeric.")

# ==========================================
# Expense Ratio Validation
# Expected Range: 0.1% to 2.5%
# ==========================================

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print(f"\nInvalid Expense Ratios: {len(invalid_expense)}")

# ==========================================
# Morningstar Rating Validation
# ==========================================

invalid_rating = df[
    (df["morningstar_rating"] < 1) |
    (df["morningstar_rating"] > 5)
]

print(f"Invalid Morningstar Ratings: {len(invalid_rating)}")

# ==========================================
# Final Shape
# ==========================================

print("\nCleaned Shape:", df.shape)

# ==========================================
# Save Clean Dataset
# ==========================================

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("\n✅ Cleaned dataset saved successfully!")