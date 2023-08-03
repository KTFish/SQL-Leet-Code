-- 1890-The-Latest-Login-In-2020
-- Exercise from: https://leetcode.com/problems/the-latest-login-in-2020/
SELECT
    DISTINCT user_id,
    FIRST_VALUE(time_stamp) OVER(
        PARTITION BY user_id
        ORDER BY
            time_stamp DESC
    ) AS last_stamp
FROM
    Logins
WHERE
    YEAR(time_stamp) = 2020