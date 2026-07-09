import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# Create Output Folder
# ==========================================

os.makedirs("dashboard/assets/aum", exist_ok=True)

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# ==========================================
# Data Preparation
# ==========================================

df["date"] = pd.to_datetime(df["date"])

df["year"] = df["date"].dt.year

# Aggregate yearly AUM
yearly_aum = (
    df.groupby(["year", "fund_house"])["aum_crore"]
      .sum()
      .reset_index()
)

# ==========================================
# Plot
# ==========================================

plt.figure(figsize=(16,8))

palette = []

for fund in yearly_aum["fund_house"]:
    if fund == "SBI Mutual Fund":
        palette.append("green")
    else:
        palette.append("steelblue")

sns.barplot(
    data=yearly_aum,
    x="year",
    y="aum_crore",
    hue="fund_house",
    palette=palette
)

plt.title(
    "Year-wise AUM by Fund House (2022–2025)",
    fontsize=16,
    weight="bold"
)

plt.xlabel("Year")
plt.ylabel("AUM (Crore ₹)")

plt.xticks(rotation=0)

plt.legend(
    bbox_to_anchor=(1.02,1),
    loc="upper left"
)

plt.tight_layout()

# ==========================================
# Save
# ==========================================

plt.savefig(
    "dashboard/assets/aum/aum_growth.png",
    dpi=300,
    bbox_inches="tight"
)

print("="*60)
print("AUM Analysis Completed")
print("Chart Saved Successfully")
print("="*60)

plt.show()