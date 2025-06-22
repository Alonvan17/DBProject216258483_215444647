CREATE OR REPLACE FUNCTION fn_soldier_unit_summary(commander_id int)
RETURNS TABLE (
    soldier_id INT,
    unit_name VARCHAR,
    tank_id INT,
    crew_type VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        s.s_ID,
        u.uName,
        t.tID,
        cm.type
    FROM 
        Soldier s
        JOIN Crew cr ON s.c_ID = cr.c_ID
        JOIN Commander c ON cr.cID = c.s_ID
        JOIN Tank t ON t.c_ID = cr.c_ID
        JOIN Unit u ON t.unID = u.unID
        LEFT JOIN CrewMate cm ON cm.crID = s.s_ID
    WHERE c.s_ID = commander_id;
END;
$$ LANGUAGE plpgsql;
