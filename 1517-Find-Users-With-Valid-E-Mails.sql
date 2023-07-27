-- 1517. Find Users With Valid E-Mails
-- A valid e-mail has a prefix name and a domain where:
-- The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
-- The domain is '@leetcode.com'.
SELECT
    *
FROM
    Users
WHERE
    REGEXP_LIKE mail LIKE '^[a-z0-9]*@leetcode.com$';