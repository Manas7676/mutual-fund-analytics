import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# Create Output Folder
# ==========================================

os.makedirs("dashboard/assets/demographics", exist_ok=True)

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/processed/investor_transactions_clean.csv")

plt.style.use("ggplot")

# ==========================================
# 1. Age Group Distribution
# ==========================================

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="age_group",
    order=["18-25","26-35","36-45","46-55","56+"]
)

plt.title("Investor Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of Investors")

plt.tight_layout()

plt.savefig(
    "dashboard/assets/demographics/age_distribution.png",
    dpi=300
)

plt.close()

# ==========================================
# 2. Gender Distribution
# ==========================================

plt.figure(figsize=(6,6))

df["gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.title("Gender Distribution")

plt.tight_layout()

plt.savefig(
    "dashboard/assets/demographics/gender_distribution.png",
    dpi=300
)

plt.close()

# ==========================================
# 3. Income Distribution
# ==========================================

plt.figure(figsize=(10,6))

sns.histplot(
    df["annual_income_lakh"],
    bins=20,
    kde=True
)

plt.title("Annual Income Distribution")
plt.xlabel("Annual Income (Lakhs)")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    "dashboard/assets/demographics/income_distribution.png",
    dpi=300
)

plt.close()

print("="*60)
print("Demographic Analysis Completed")
print("Generated Charts:")
print("✓ Age Distribution")
print("✓ Gender Distribution")
print("✓ Income Distribution")
print("="*60)