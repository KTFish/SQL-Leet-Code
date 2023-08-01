-- 182-Duplicate-Emails
-- Exercise from: https://leetcode.com/problems/duplicate-emails/
SELECT
    email AS Email
FROM
    Person
WHERE
    email IS NOT NULL
GROUP BY
    email
HAVING
    COUNT(email) >= 2