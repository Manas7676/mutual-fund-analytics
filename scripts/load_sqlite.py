import pandas as pd
from sqlalchemy import create_engine

# ==========================================
# Create SQLite Database
# ==========================================

engine = create_engine("sqlite:///mutual_fund_analytics.db")

print("SQLite Database Created Successfully!\n")

# ==========================================
# Dataset Mapping
# ==========================================

datasets = {
    "fund_master": "data/raw/01_fund_master.csv",
    "nav_history": "data/processed/nav_history_clean.csv",
    "aum_by_fund_house": "data/raw/03_aum_by_fund_house.csv",
    "monthly_sip_inflows": "data/raw/04_monthly_sip_inflows.csv",
    "category_inflows": "data/raw/05_category_inflows.csv",
    "industry_folio_count": "data/raw/06_industry_folio_count.csv",
    "scheme_performance": "data/processed/scheme_performance_clean.csv",
    "investor_transactions": "data/processed/investor_transactions_clean.csv",
    "portfolio_holdings": "data/raw/09_portfolio_holdings.csv",
    "benchmark_indices": "data/raw/10_benchmark_indices.csv"
}

# ==========================================
# Load All Tables
# ==========================================

for table_name, file_path in datasets.items():

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded: {table_name} ({len(df)} rows)")

print("\nAll 10 datasets loaded successfully!")