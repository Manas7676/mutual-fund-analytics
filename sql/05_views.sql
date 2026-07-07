-- =====================================================
-- View 1: High Performing Funds
-- =====================================================

CREATE VIEW high_performance_funds AS
SELECT
    scheme_name,
    fund_house,
    return_5yr_pct,
    sharpe_ratio
FROM scheme_performance
WHERE return_5yr_pct > 15;

-- =====================================================
-- View 2: Low Expense Funds
-- =====================================================

CREATE VIEW low_expense_funds AS
SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- =====================================================
-- View 3: Verified Investors
-- =====================================================

CREATE VIEW verified_investors AS
SELECT *
FROM investor_transactions
WHERE kyc_status = 'Verified';

-- =====================================================
-- View 4: Large Transactions
-- =====================================================

CREATE VIEW large_transactions AS
SELECT *
FROM investor_transactions
WHERE amount_inr > 100000;

-- =====================================================
-- View 5: Average NAV
-- =====================================================

CREATE VIEW average_nav AS
SELECT
    amfi_code,
    ROUND(AVG(nav),2) AS average_nav
FROM nav_history
GROUP BY amfi_code;