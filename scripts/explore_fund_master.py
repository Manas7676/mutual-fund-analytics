import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("="*60)
print("SHAPE")
print(df.shape)

print("\nCOLUMNS")
print(df.columns.tolist())

print("\nFIRST 5 ROWS")
print(df.head())

print("\nINFO")
print(df.info())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATES")
print(df.duplicated().sum())



import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses")
print(df["fund_house"].unique())

print("\nNumber of Fund Houses")
print(df["fund_house"].nunique())

print("\nCategories")
print(df["category"].value_counts())

print("\nSub Categories")
print(df["sub_category"].value_counts())

print("\nRisk Categories")
print(df["risk_category"].value_counts())

print("\nSEBI Category Codes")
print(df["sebi_category_code"].value_counts())