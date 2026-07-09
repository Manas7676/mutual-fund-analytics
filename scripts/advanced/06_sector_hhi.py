import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# Create Folders
# ==========================================

os.makedirs("reports", exist_ok=True)
os.makedirs("dashboard/assets/advanced", exist_ok=True)

# ==========================================
# Load Data
# ==========================================

holdings = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

funds = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

# ==========================================
# HHI Calculation
# ==========================================

hhi = (
    holdings.groupby("amfi_code")["weight_pct"]
    .apply(lambda x: ((x / 100) ** 2).sum())
    .reset_index(name="HHI")
)

# ==========================================
# Merge Scheme Names
# ==========================================

hhi = hhi.merge(
    funds[["amfi_code", "scheme_name"]],
    on="amfi_code",
    how="left"
)

hhi = hhi.sort_values(
    "HHI",
    ascending=False
)

# ==========================================
# Save CSV
# ==========================================

hhi.to_csv(
    "reports/sector_hhi_report.csv",
    index=False
)

# ==========================================
# Plot
# ==========================================

plt.figure(figsize=(14,7))

top10 = hhi.head(10)

sns.barplot(
    data=top10,
    x="HHI",
    y="scheme_name"
)

plt.title("Top 10 Most Concentrated Portfolios (HHI)")
plt.xlabel("HHI")
plt.ylabel("Scheme")

plt.tight_layout()

plt.savefig(
    "dashboard/assets/advanced/sector_hhi_chart.png",
    dpi=300
)

plt.show()

print("=" * 60)
print("Sector HHI Analysis Completed")
print("=" * 60)

print(top10)