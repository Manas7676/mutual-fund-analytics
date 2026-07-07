USE mutual_fund_analytics;

CREATE TABLE fund_master (
    amfi_code INT PRIMARY KEY,
    fund_house VARCHAR(100) NOT NULL,
    scheme_name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    sub_category VARCHAR(100),
    plan VARCHAR(50),
    launch_date DATE,
    benchmark VARCHAR(255),
    expense_ratio_pct DECIMAL(5,2),
    exit_load_pct DECIMAL(5,2),
    min_sip_amount INT,
    min_lumpsum_amount INT,
    fund_manager VARCHAR(100),
    risk_category VARCHAR(50),
    sebi_category_code VARCHAR(20)
);