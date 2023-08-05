-- 2356-Number-Of-Unique-Subjects-Taught-By-Each-Teacher
-- Exercise from: https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/
SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM
    Teacher
GROUP BY
    teacher_id