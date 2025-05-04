-- מעדכן את גודל כל צוות לפי מספר החיילים בו ועוד עשירית מסך הקיבולת של כלי השיט המשויכים לו.
UPDATE Crew c
SET c_size = sub.new_size
FROM (
    SELECT 
        s.c_ID,
        COUNT(s.s_ID) + COALESCE(SUM(sv.capacity) / 10, 0) AS new_size
    FROM Soldier s
    LEFT JOIN Sea_vessel sv ON s.c_ID = sv.c_ID
    GROUP BY s.c_ID
) AS sub
WHERE c.c_ID = sub.c_ID;
