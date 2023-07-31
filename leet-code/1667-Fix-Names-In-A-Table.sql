-- 1667-Fix-Names-In-A-Table
-- Exercise from: https://leetcode.com/problems/fix-names-in-a-table/
SELECT
    user_id,
    CONCAT(
        UPPER(SUBSTRING(name, 1, 1)),
        LOWER(SUBSTRING(name, 2, LENGTH(name) - 1))
    ) as name
FROM
    Users
ORDER BY
    user_id