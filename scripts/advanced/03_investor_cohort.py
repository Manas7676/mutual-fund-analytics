import pandas as pd
import os

# ==========================================
# Create Reports Folder
# ==========================================

os.makedirs("reports", exist_ok=True)

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

funds = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

# ==========================================
# Convert Date
# ==========================================

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# ==========================================
# First Transaction Year
# ==========================================

first_txn = (
    df.groupby("investor_id")["transaction_date"]
      .min()
      .dt.year
      .rename("cohort_year")
)

df = df.merge(
    first_txn,
    on="investor_id"
)

# ==========================================
# Average SIP Amount
# ==========================================

sip = df[
    df["transaction_type"] == "SIP"
]

avg_sip = (
    sip.groupby("cohort_year")["amount_inr"]
       .mean()
       .rename("avg_sip_amount")
)

# ==========================================
# Total Investment
# ==========================================

total_inv = (
    df.groupby("cohort_year")["amount_inr"]
      .sum()
      .rename("total_investment")
)

# ==========================================
# Top Fund Preference
# ==========================================

top_fund = (
    df.groupby(["cohort_year","amfi_code"])
      .size()
      .reset_index(name="count")
)

top_fund = (
    top_fund.sort_values(
        ["cohort_year","count"],
        ascending=[True,False]
    )
    .drop_duplicates("cohort_year")
)

top_fund = top_fund.merge(
    funds[["amfi_code","scheme_name"]],
    on="amfi_code",
    how="left"
)

# ==========================================
# Final Report
# ==========================================

report = pd.concat(
    [avg_sip, total_inv],
    axis=1
).reset_index()

report = report.merge(
    top_fund[
        ["cohort_year","scheme_name"]
    ],
    on="cohort_year",
    how="left"
)

report.rename(
    columns={
        "scheme_name":"top_fund_preference"
    },
    inplace=True
)

report.to_csv(
    "reports/investor_cohort_report.csv",
    index=False
)

print("="*60)
print("Investor Cohort Analysis Completed")
print(report)
print("="*60)