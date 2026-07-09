import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# Create Output Folder
# ==========================================

os.makedirs("dashboard/assets/correlation", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

# ==========================================
# Correlation Matrix
# ==========================================

corr_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "expense_ratio_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore"
]

corr = df[corr_columns].corr()

plt.figure(figsize=(12,10))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig(
    "dashboard/assets/correlation/correlation_matrix.png",
    dpi=300
)

plt.close()

# ==========================================
# Summary Statistics
# ==========================================

summary = df.describe()

summary.to_csv(
    "reports/summary_statistics.csv"
)

# ==========================================
# Business Insights
# ==========================================

top_return = df.loc[df["return_5yr_pct"].idxmax()]
lowest_expense = df.loc[df["expense_ratio_pct"].idxmin()]
highest_aum = df.loc[df["aum_crore"].idxmax()]

with open("reports/business_insights.txt", "w", encoding="utf-8") as f:

    f.write("MUTUAL FUND ANALYTICS - BUSINESS INSIGHTS\n")
    f.write("=" * 60 + "\n\n")

    f.write(
        f"Top Performing Fund (5-Year Return):\n"
        f"{top_return['scheme_name']} "
        f"({top_return['return_5yr_pct']}%)\n\n"
    )

    f.write(
        f"Lowest Expense Ratio Fund:\n"
        f"{lowest_expense['scheme_name']} "
        f"({lowest_expense['expense_ratio_pct']}%)\n\n"
    )

    f.write(
        f"Highest AUM Fund:\n"
        f"{highest_aum['scheme_name']} "
        f"(Rs. {highest_aum['aum_crore']} Crore)\n"
    )

print("=" * 60)
print("Correlation Matrix Created")
print("Summary Statistics Saved")
print("Business Insights Report Generated")
print("=" * 60)