-- 610. Triangle Judgement
-- Write an SQL query to report for every three line segments whether they can form a triangle.
-- Return the result table in any order.

-- The sum of two side lengths of a triangle is always greater than the third side

-- Using IF
SELECT x, y, z, IF(x + y > z AND x + z > y AND y + z > x, "Yes", "No") AS triangle 
FROM Triangle