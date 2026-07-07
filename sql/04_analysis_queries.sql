-- =====================================================
-- 1. Total Mutual Fund Schemes
-- =====================================================

SELECT COUNT(*) AS total_funds
FROM fund_master;

-- =====================================================
-- 2. Funds by Risk Category
-- =====================================================

SELECT
risk_category,
COUNT(*) AS total_funds
FROM fund_master
GROUP BY risk_category
ORDER BY total_funds DESC;

-- =====================================================
-- 3. Top 10 Funds by 5-Year Return
-- =====================================================

SELECT
scheme_name,
return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- =====================================================
-- 4. Top 10 Funds by AUM
-- =====================================================

SELECT
scheme_name,
aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 10;

-- =====================================================
-- 5. Average Expense Ratio by Category
-- =====================================================

SELECT
category,
ROUND(AVG(expense_ratio_pct),2) AS avg_expense_ratio
FROM scheme_performance
GROUP BY category;

-- =====================================================
-- 6. Funds with Expense Ratio below 1%
-- =====================================================

SELECT
scheme_name,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- =====================================================
-- 7. Average NAV by Fund
-- =====================================================

SELECT
amfi_code,
ROUND(AVG(nav),2) AS avg_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY avg_nav DESC;

-- =====================================================
-- 8. Total Transactions by Type
-- =====================================================

SELECT
transaction_type,
COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY transaction_type;

-- =====================================================
-- 9. Total Transaction Amount by State
-- =====================================================

SELECT
state,
ROUND(SUM(amount_inr),2) AS total_amount
FROM investor_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- =====================================================
-- 10. Investor Distribution by City Tier
-- =====================================================

SELECT
city_tier,
COUNT(*) AS investors
FROM investor_transactions
GROUP BY city_tier;

-- =====================================================
-- 11. KYC Status Distribution
-- =====================================================

SELECT
kyc_status,
COUNT(*) AS total
FROM investor_transactions
GROUP BY kyc_status;

-- =====================================================
-- 12. Average Income by Age Group
-- =====================================================

SELECT
age_group,
ROUND(AVG(annual_income_lakh),2) AS avg_income
FROM investor_transactions
GROUP BY age_group;

-- =====================================================
-- 13. Top 10 Highest Sharpe Ratio Funds
-- =====================================================

SELECT
scheme_name,
sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- =====================================================
-- 14. Best Alpha Funds
-- =====================================================

SELECT
scheme_name,
alpha
FROM scheme_performance
ORDER BY alpha DESC
LIMIT 10;

-- =====================================================
-- 15. Average Return by Fund House
-- =====================================================

SELECT
fund_house,
ROUND(AVG(return_5yr_pct),2) AS avg_return
FROM scheme_performance
GROUP BY fund_house
ORDER BY avg_return DESC;