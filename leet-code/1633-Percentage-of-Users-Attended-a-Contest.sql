-- 1633. Percentage of Users Attended a Contest
-- Write an SQL query to find the percentage of the users registered in each contest rounded to two decimals.
-- Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.
-- The query result format is in the following example.
SELECT
    contest_id,
    ROUND(
        COUNT(DISTINCT(user_id)) / (
            SELECT
                COUNT(user_id)
            FROM
                Users
        ) * 100,
        2
    ) AS percentage
FROM
    Register
GROUP BY
    contest_id
ORDER BY
    percentage DESC,
    contest_id ASC