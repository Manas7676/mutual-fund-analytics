import requests
import pandas as pd
import os

funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

save_folder = "data/raw"

for fund_name, amfi_code in funds.items():

    try:
        url = f"https://api.mfapi.in/mf/{amfi_code}"

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            scheme_name = data["meta"]["scheme_name"]

            nav_df = pd.DataFrame(data["data"])

            file_name = f"{fund_name}_nav.csv"

            nav_df.to_csv(
                os.path.join(save_folder, file_name),
                index=False
            )

            print(f"\n✓ {fund_name}")
            print(f"Scheme: {scheme_name}")
            print(f"Rows: {len(nav_df)}")

        else:
            print(f"\n✗ Failed for {fund_name}")

    except Exception as e:
        print(f"\n✗ Error for {fund_name}")
        print(e)