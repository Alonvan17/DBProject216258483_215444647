 -- ממוצע עומק הצלילה של צוללות לפי דרגת המפקד של הצוות שלהן
SELECT 
    so.rank,
    AVG(sub.max_depth) AS avg_max_depth
FROM 
    Submarine sub
JOIN Sea_vessel sv ON sub.sea_ID = sv.sea_ID
JOIN Commander c ON sv.c_ID = c.c_ID
JOIN Soldier so ON c.s_ID = so.s_ID
GROUP BY so.rank;
