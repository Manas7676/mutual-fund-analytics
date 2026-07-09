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

# ==========================================
# Filter SIP Transactions
# ==========================================

sip = df[
    df["transaction_type"] == "SIP"
].copy()

sip["transaction_date"] = pd.to_datetime(
    sip["transaction_date"]
)

sip = sip.sort_values(
    ["investor_id", "transaction_date"]
)

# ==========================================
# Investors with 6+ SIPs
# ==========================================

eligible = (
    sip.groupby("investor_id")
       .filter(lambda x: len(x) >= 6)
)

# ==========================================
# Average Gap Calculation
# ==========================================

results = []

for investor, group in eligible.groupby("investor_id"):

    group = group.sort_values("transaction_date")

    gaps = (
        group["transaction_date"]
        .diff()
        .dt.days
        .dropna()
    )

    avg_gap = gaps.mean()

    status = (
        "At Risk"
        if avg_gap > 35
        else "Regular"
    )

    results.append({
        "investor_id": investor,
        "sip_transactions": len(group),
        "avg_gap_days": round(avg_gap, 2),
        "status": status
    })

report = pd.DataFrame(results)

# ==========================================
# Save Report
# ==========================================

report.to_csv(
    "reports/sip_continuity_report.csv",
    index=False
)

print("=" * 60)
print("SIP Continuity Analysis Completed")
print("=" * 60)

print(report.head(10))

print("\nTotal Eligible Investors:", len(report))
print("At-Risk Investors:", (report["status"] == "At Risk").sum())