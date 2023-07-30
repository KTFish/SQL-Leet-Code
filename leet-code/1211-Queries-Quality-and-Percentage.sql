-- 1211. Queries Quality and Percentage
--
-- We define query quality as:
-- The average of the ratio between query rating and its position.
--
-- We also define poor query percentage as:
-- The percentage of all queries with rating less than 3.
--
-- Write an SQL query to find each query_name, the quality and poor_query_percentage.
-- Both quality and poor_query_percentage should be rounded to 2 decimal places.
-- Return the result table in any order.
-- The query result format is in the following example.
SELECT
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(
        (
            SUM(
                CASE
                    WHEN rating < 3 THEN 1
                    ELSE 0
                END
            ) / COUNT(*)
        ) * 100,
        2
    ) AS poor_query_percentage
FROM
    Queries
GROUP BY
    query_name;