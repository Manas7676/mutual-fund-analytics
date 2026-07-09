import pandas as pd
import numpy as np
import os

# ==========================================
# Create Reports Folder
# ==========================================

os.makedirs("reports", exist_ok=True)

# ==========================================
# Load Data
# ==========================================

nav = pd.read_csv("data/processed/nav_history_clean.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

# ==========================================
# Calculate Daily Returns
# ==========================================

nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
    .pct_change()
)

# Remove first row of each fund
returns = nav.dropna(subset=["daily_return"])

# ==========================================
# Calculate VaR & CVaR
# ==========================================

results = []

for code, group in returns.groupby("amfi_code"):

    var95 = np.percentile(group["daily_return"], 5)

    cvar95 = group.loc[
        group["daily_return"] <= var95,
        "daily_return"
    ].mean()

    results.append({
        "amfi_code": code,
        "VaR_95": round(var95, 5),
        "CVaR_95": round(cvar95, 5)
    })

risk_report = pd.DataFrame(results)

# ==========================================
# Merge Fund Names
# ==========================================

funds = pd.read_csv("data/raw/01_fund_master.csv")

risk_report = risk_report.merge(
    funds[["amfi_code", "scheme_name", "risk_category"]],
    on="amfi_code",
    how="left"
)

risk_report = risk_report[
    [
        "amfi_code",
        "scheme_name",
        "risk_category",
        "VaR_95",
        "CVaR_95"
    ]
]

# ==========================================
# Sort by Highest Risk
# ==========================================

risk_report = risk_report.sort_values("VaR_95")

# ==========================================
# Save Report
# ==========================================

risk_report.to_csv(
    "reports/var_cvar_report.csv",
    index=False
)

# ==========================================
# Console Output
# ==========================================

print("=" * 60)
print("Historical VaR & CVaR Report Generated")
print("=" * 60)

print("\nTop 10 Highest Risk Funds:\n")

print(risk_report.head(10))

print("\nReport saved to:")
print("reports/var_cvar_report.csv")