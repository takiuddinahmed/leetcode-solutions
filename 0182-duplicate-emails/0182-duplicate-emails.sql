# Write your MySQL query statement below
SELECT DISTINCT p1.email as Email from Person as p1 JOIN Person as p2 WHERE p1.email=p2.email and p1.id!=p2.id;