import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# Create Output Folder
# ==========================================

os.makedirs("dashboard/assets/category", exist_ok=True)

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/05_category_inflows.csv")

# ==========================================
# Data Preparation
# ==========================================

df["month"] = pd.to_datetime(df["month"])

# Format month for display
df["month"] = df["month"].dt.strftime("%b-%Y")

# Create Pivot Table
heatmap_data = df.pivot(
    index="category",
    columns="month",
    values="net_inflow_crore"
)

# ==========================================
# Plot Heatmap
# ==========================================

plt.figure(figsize=(16,8))

sns.heatmap(
    heatmap_data,
    cmap="YlGnBu",
    annot=True,
    fmt=".0f",
    linewidths=0.5
)

plt.title(
    "Monthly Net Inflow by Mutual Fund Category",
    fontsize=16,
    weight="bold"
)

plt.xlabel("Month")
plt.ylabel("Category")

plt.tight_layout()

# ==========================================
# Save
# ==========================================

plt.savefig(
    "dashboard/assets/category/category_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

print("="*60)
print("Category Heatmap Created Successfully")
print("Saved to dashboard/assets/category/")
print("="*60)

plt.show()