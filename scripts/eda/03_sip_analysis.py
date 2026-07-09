import pandas as pd
import plotly.express as px
import os

# ==========================================
# Create Output Folder
# ==========================================

os.makedirs("dashboard/assets/sip", exist_ok=True)

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

# ==========================================
# Data Preparation
# ==========================================

df["month"] = pd.to_datetime(df["month"])

# Find Peak SIP Inflow
max_row = df.loc[df["sip_inflow_crore"].idxmax()]

# ==========================================
# Plot
# ==========================================

fig = px.line(
    df,
    x="month",
    y="sip_inflow_crore",
    markers=True,
    title="Monthly SIP Inflow Trend (2022–2025)",
    labels={
        "month": "Month",
        "sip_inflow_crore": "SIP Inflow (₹ Crore)"
    }
)

# Highlight highest SIP inflow
fig.add_annotation(
    x=max_row["month"].strftime("%Y-%m-%d"),
    y=float(max_row["sip_inflow_crore"]),
    text=f"Peak: ₹{int(max_row['sip_inflow_crore']):,} Cr",
    showarrow=True,
    arrowhead=2,
    bgcolor="yellow"
)

fig.update_layout(
    template="plotly_white",
    height=650,
    hovermode="x unified"
)

# ==========================================
# Save
# ==========================================

fig.write_html(
    "dashboard/assets/sip/sip_trend.html"
)

fig.write_image(
    "dashboard/assets/sip/sip_trend.png",
    width=1600,
    height=800,
    scale=2
)

print("=" * 60)
print("SIP Analysis Completed")
print(f"Peak SIP Inflow: ₹{max_row['sip_inflow_crore']} Cr")
peak_month = pd.to_datetime(max_row["month"])

print(f"Peak Month: {peak_month.strftime('%b %Y')}")
print("HTML Saved")
print("PNG Saved")
print("=" * 60)

fig.show()