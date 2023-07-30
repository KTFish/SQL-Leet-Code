-- 619. Biggest Single Number
-- cte - command table expression - CTE is one of the most powerful tools of SQL (Structured Query Language), and it also helps to clean the data. It is the concept of SQL (Structured Query Language) used to simplify coding and help to get the result as quickly as possible.
WITH cte AS (
    SELECT
        num
    FROM
        MyNumbers
    GROUP BY
        num
    HAVING
        COUNT(num) = 1
)
SELECT
    CASE
        WHEN COUNT(*) > 0 THEN MAX(num)
        ELSE NULL
    END AS num
FROM
    cte