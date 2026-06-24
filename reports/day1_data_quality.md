# Day 1 Data Quality Report

## 01_fund_master.csv

Rows: 40
Columns: 15

Findings:
- No missing values
- No duplicate records
- launch_date stored as object datatype

## 02_nav_history.csv

Rows: 46,000
Columns: 3

Findings:
- No missing values
- No duplicate records
- date stored as object datatype

## AMFI Validation

Fund Master Codes: 40
NAV History Codes: 40

Results:
- No missing AMFI codes
- No extra AMFI codes
- 100% mapping consistency between datasets

## MFAPI Validation

The AMFI codes provided in the assignment were verified using MFAPI.

Findings:
- Several provided AMFI codes did not correspond to the expected mutual fund schemes.
- Example:
  - Expected: SBI Bluechip
  - Returned: Aditya Birla Sun Life Banking & PSU Debt Fund

Conclusion:
- Assignment-provided AMFI mappings appear outdated or incorrect.
- API integration was successful.
- Further validation of scheme codes is required before production use.



## API Validation Findings

The MFAPI integration was successfully implemented and data was retrieved for all requested scheme codes.

During validation, several AMFI codes returned scheme names that did not match the scheme names present in the provided fund master dataset.

Examples:

* AMFI 119551

  * Dataset: SBI Bluechip Fund - Regular Plan - Growth
  * MFAPI Response: Aditya Birla Sun Life Banking & PSU Debt Fund

* AMFI 120503

  * Dataset: ICICI Pru Bluechip Fund - Regular - Growth
  * MFAPI Response: Axis ELSS Tax Saver Fund

Conclusion:

The API integration works correctly, but the AMFI code mappings between the provided dataset and MFAPI appear inconsistent or outdated. Additional validation would be required before using live API data in production.
