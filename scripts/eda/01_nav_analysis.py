import pandas as pd
import plotly.express as px
import os

# ==========================================
# Create Output Folder
# ==========================================

os.makedirs("dashboard/assets/nav", exist_ok=True)

# ==========================================
# Load Data
# ==========================================

nav = pd.read_csv("data/processed/nav_history_clean.csv")

fund = pd.read_csv("data/raw/01_fund_master.csv")

# ==========================================
# Data Preparation
# ==========================================

nav["date"] = pd.to_datetime(nav["date"])

# Merge scheme names
nav = nav.merge(
    fund[["amfi_code", "scheme_name"]],
    on="amfi_code",
    how="left"
)

# ==========================================
# Interactive Plot
# ==========================================

fig = px.line(
    nav,
    x="date",
    y="nav",
    color="scheme_name",
    title="Daily NAV Trend of 40 Mutual Fund Schemes (2022–2026)",
    labels={
        "nav": "NAV",
        "date": "Date",
        "scheme_name": "Scheme"
    }
)

# Highlight Bull Run
fig.add_vrect(
    x0="2023-01-01",
    x1="2023-12-31",
    fillcolor="green",
    opacity=0.08,
    line_width=0,
    annotation_text="2023 Bull Run",
    annotation_position="top left"
)

# Highlight Correction
fig.add_vrect(
    x0="2024-01-01",
    x1="2024-12-31",
    fillcolor="red",
    opacity=0.08,
    line_width=0,
    annotation_text="2024 Market Correction",
    annotation_position="top left"
)

fig.update_layout(
    template="plotly_white",
    height=700,
    legend_title="Scheme",
    hovermode="x unified"
)

# ==========================================
# Save Outputs
# ==========================================

fig.write_html(
    "dashboard/assets/nav/nav_trend.html"
)

fig.write_image(
    "dashboard/assets/nav/nav_trend.png",
    width=1800,
    height=900,
    scale=2
)

print("="*60)
print("NAV Trend Analysis Completed")
print("Interactive HTML Saved")
print("PNG Saved")
print("="*60)

fig.show()