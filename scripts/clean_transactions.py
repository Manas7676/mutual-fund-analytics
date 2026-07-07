import pandas as pd

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("=" * 60)
print("Original Shape:", df.shape)

# ==========================================
# Convert Date
# ==========================================

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# ==========================================
# Standardize Transaction Types
# ==========================================

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

df["transaction_type"] = df["transaction_type"].replace(mapping)

# ==========================================
# Remove Duplicates
# ==========================================

duplicates = df.duplicated().sum()

print(f"\nDuplicate Rows Found: {duplicates}")

df = df.drop_duplicates()

# ==========================================
# Validate Amount
# ==========================================

invalid_amount = df[df["amount_inr"] <= 0]

print(f"Invalid Amount Rows: {len(invalid_amount)}")

df = df[df["amount_inr"] > 0]

# ==========================================
# Validate KYC Status
# ==========================================

print("\nKYC Status Counts:")

print(df["kyc_status"].value_counts())

# ==========================================
# Missing Values
# ==========================================

print("\nMissing Values:")

print(df.isnull().sum())

# ==========================================
# Final Shape
# ==========================================

print("\nCleaned Shape:", df.shape)

# ==========================================
# Save
# ==========================================

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("\n✅ Cleaned dataset saved successfully!")