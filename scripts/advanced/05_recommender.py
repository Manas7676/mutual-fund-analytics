import pandas as pd

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

# ==========================================
# User Input
# ==========================================

print("=" * 60)
print(" MUTUAL FUND RECOMMENDER ")
print("=" * 60)

print("\nRisk Appetite Options:")
print("1. Low")
print("2. Moderate")
print("3. High")

choice = input("\nEnter Risk Appetite: ").strip().lower()

mapping = {
    "low": ["Low"],
    "moderate": ["Moderate", "Moderately High"],
    "high": ["High", "Very High"]
}

if choice not in mapping:
    print("\n❌ Invalid Choice")
    exit()

# ==========================================
# Filter Funds
# ==========================================

filtered = df[
    df["risk_grade"].isin(mapping[choice])
]

recommended = (
    filtered
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

# ==========================================
# Display
# ==========================================

print("\n")
print("=" * 75)
print("Recommended Funds")
print("=" * 75)

print(
    recommended[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_5yr_pct",
            "expense_ratio_pct"
        ]
    ].to_string(index=False)
)

print("=" * 75)