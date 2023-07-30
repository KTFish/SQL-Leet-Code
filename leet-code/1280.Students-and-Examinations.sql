-- COALESCE function to handle the case when there are
-- no matching records in the cte2 CTE (i.e., no attended exams).
-- This ensures that the output shows 0 for attended_exams instead of NULL.
WITH cte AS (
    SELECT
        s.student_id,
        s.student_name,
        sub.subject_name
    FROM
        Students s
        CROSS JOIN Subjects sub
),
cte2 AS (
    SELECT
        student_id,
        subject_name,
        COUNT(subject_name) AS attended_exams
    FROM
        Examinations
    GROUP BY
        student_id,
        subject_name
)
SELECT
    cte.student_id,
    cte.student_name,
    cte.subject_name,
    COALESCE(cte2.attended_exams, 0) AS attended_exams
FROM
    cte
    LEFT JOIN cte2 ON cte.student_id = cte2.student_id
    AND cte.subject_name = cte2.subject_name
ORDER BY
    cte.student_id,
    cte.subject_name