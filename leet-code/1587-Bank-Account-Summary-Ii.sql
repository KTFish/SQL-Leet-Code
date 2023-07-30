-- 1587-Bank-Account-Summary-Ii
-- Exercise from: https://leetcode.com/problems/bank-account-summary-ii/
-- Write an SQL query to report the name and balance of users with a balance higher than 10000. 
-- The balance of an account is equal to the sum of the amounts of all transactions involving that account.
WITH calculate_balance AS (
    SELECT
        name,
        SUM(amount) AS balance
    FROM
        Users u
        JOIN Transactions t ON u.account = t.account
    GROUP BY
        u.account
)
SELECT
    name,
    balance
FROM
    calculate_balance
WHERE
    balance > 10000