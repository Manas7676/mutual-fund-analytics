import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.style.use("ggplot")

# =====================================
# Create folders
# =====================================

os.makedirs("dashboard/assets/geography", exist_ok=True)
os.makedirs("dashboard/assets/folio", exist_ok=True)
os.makedirs("dashboard/assets/sector", exist_ok=True)

# =====================================
# Load datasets
# =====================================

transactions = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

folios = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

holdings = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

# =====================================
# Chart 1
# State-wise Investment
# =====================================

state_data = (
    transactions.groupby("state")["amount_inr"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

sns.barplot(
    x=state_data.values,
    y=state_data.index
)

plt.title("Top 10 States by Investment Amount")

plt.xlabel("Investment (₹)")
plt.ylabel("State")

plt.tight_layout()

plt.savefig(
    "dashboard/assets/geography/geographic_distribution.png",
    dpi=300
)

plt.close()

# =====================================
# Chart 2
# Folio Growth
# =====================================

folios["month"] = pd.to_datetime(folios["month"])

plt.figure(figsize=(12,6))

plt.plot(
    folios["month"],
    folios["total_folios_crore"],
    linewidth=3
)

plt.title("Industry Folio Growth")

plt.xlabel("Month")

plt.ylabel("Folios (Crore)")

plt.tight_layout()

plt.savefig(
    "dashboard/assets/folio/folio_growth.png",
    dpi=300
)

plt.close()

# =====================================
# Chart 3
# Sector Allocation
# =====================================

sector = (
    holdings.groupby("sector")["weight_pct"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

sns.barplot(
    x=sector.values,
    y=sector.index
)

plt.title("Top 10 Portfolio Sectors")

plt.xlabel("Average Weight (%)")

plt.ylabel("Sector")

plt.tight_layout()

plt.savefig(
    "dashboard/assets/sector/sector_allocation.png",
    dpi=300
)

plt.close()

print("="*60)
print("Market Analysis Completed")
print("✓ Geographic Distribution")
print("✓ Folio Growth")
print("✓ Sector Allocation")
print("="*60)