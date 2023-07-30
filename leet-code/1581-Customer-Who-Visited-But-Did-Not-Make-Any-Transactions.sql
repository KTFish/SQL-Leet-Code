-- 1581-Customer-Who-Visited-But-Did-Not-Make-Any-Transactions
-- Exercise from: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
-- Write a SQL query to find the IDs of the users
-- who visited without making any transactions and the number of times they made these types of visits.
SELECT
    v.customer_id,
    COUNT(*) AS count_no_trans
FROM
    Visits v
    LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE
    t.transaction_id IS NULL
GROUP BY
    v.customer_id