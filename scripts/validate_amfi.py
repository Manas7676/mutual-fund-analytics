import pandas as pd

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav_history = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

master_codes = set(
    fund_master["amfi_code"]
)

nav_codes = set(
    nav_history["amfi_code"]
)

missing_codes = master_codes - nav_codes

extra_codes = nav_codes - master_codes

print("Fund Master Codes:", len(master_codes))
print("NAV History Codes:", len(nav_codes))

print("\nMissing Codes:")
print(missing_codes)

print("\nExtra Codes:")
print(extra_codes)