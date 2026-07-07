import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 60)
print("Original Shape:", df.shape)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by AMFI code and date
df = df.sort_values(by=["amfi_code", "date"])

# Forward fill missing NAV values within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove duplicate rows
df = df.drop_duplicates()

# Validate NAV values
invalid_nav = df[df["nav"] <= 0]

if len(invalid_nav) == 0:
    print("✅ All NAV values are valid.")
else:
    print(f"❌ Found {len(invalid_nav)} invalid NAV values.")

print("Cleaned Shape:", df.shape)

# Save cleaned dataset
df.to_csv("data/processed/nav_history_clean.csv", index=False)

print("\n✅ Cleaned file saved to:")
print("data/processed/nav_history_clean.csv")