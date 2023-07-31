-- 1731-The-Number-Of-Employees-Which-Report-To-Each-Employee
-- Exercise from: https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/
WITH subordinate_summary AS (
    SELECT
        reports_to,
        COUNT(employee_id) AS reports_count,
        ROUND(AVG(age), 0) AS average_age
    FROM
        Employees
    WHERE
        reports_to IS NOT NULL
    GROUP BY
        reports_to
)
SELECT
    e.employee_id,
    e.name,
    reports_count,
    average_age
FROM
    subordinate_summary c
    LEFT JOIN Employees e ON c.reports_to = e.employee_id
ORDER BY
    employee_id