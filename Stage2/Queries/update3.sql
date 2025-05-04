UPDATE Soldier s
SET name = 'Veteran_' || s.name
WHERE rank = 'admiral'
AND c_ID IN (
    SELECT sv.c_ID
    FROM Sea_vessel sv
    WHERE EXTRACT(YEAR FROM sv.test_date) < 2020
    GROUP BY sv.c_ID
    HAVING SUM(sv.capacity) > 500
);
