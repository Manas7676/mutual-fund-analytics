import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ==========================================
# Create Output Folder
# ==========================================

os.makedirs("dashboard/assets/advanced", exist_ok=True)

# ==========================================
# Load NAV History
# ==========================================

nav = pd.read_csv("data/processed/nav_history_clean.csv")

funds = pd.read_csv("data/raw/01_fund_master.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

# ==========================================
# Daily Returns
# ==========================================

nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
       .pct_change()
)

# ==========================================
# Rolling Sharpe
# ==========================================

nav["rolling_sharpe"] = (
    nav.groupby("amfi_code")["daily_return"]
       .transform(
           lambda x:
           (
               x.rolling(90).mean()
               /
               x.rolling(90).std()
           )
           * np.sqrt(252)
       )
)

# ==========================================
# Select 5 Key Funds
# ==========================================

selected_codes = [
    119551,   # SBI Bluechip
    120503,   # ICICI Bluechip
    118632,   # Nippon Large Cap
    119092,   # Axis Bluechip
    120841    # Kotak Bluechip
]

plot_df = nav[
    nav["amfi_code"].isin(selected_codes)
]

plot_df = plot_df.merge(
    funds[["amfi_code", "scheme_name"]],
    on="amfi_code",
    how="left"
)

# ==========================================
# Plot
# ==========================================

plt.figure(figsize=(15,7))

for scheme in plot_df["scheme_name"].unique():

    temp = plot_df[
        plot_df["scheme_name"] == scheme
    ]

    plt.plot(
        temp["date"],
        temp["rolling_sharpe"],
        label=scheme,
        linewidth=2
    )

plt.title(
    "Rolling 90-Day Sharpe Ratio"
)

plt.xlabel("Date")

plt.ylabel("Sharpe Ratio")

plt.legend(fontsize=8)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "dashboard/assets/advanced/rolling_sharpe_chart.png",
    dpi=300
)

plt.show()

print("="*60)
print("Rolling Sharpe Analysis Completed")
print("Chart Saved Successfully")
print("="*60)