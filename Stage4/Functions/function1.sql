CREATE OR REPLACE FUNCTION fn_commander_performance()
RETURNS refcursor AS $$
DECLARE
    ref refcursor;
BEGIN
    OPEN ref FOR
    SELECT
        c.s_ID AS commander_id,
        COUNT(DISTINCT t.tID) AS num_tanks,
        COUNT(DISTINCT m.mID) AS num_missions,
        CASE 
            WHEN COUNT(DISTINCT m.mID) >= 5 THEN 'Experienced'
            WHEN COUNT(DISTINCT m.mID) >= 2 THEN 'Intermediate'
            ELSE 'Newbie'
        END AS experience_level
    FROM
        Commander c
        JOIN Crew cr ON c.c_ID = cr.c_ID
        JOIN Tank t ON t.c_ID = cr.c_ID
        JOIN Unit u ON t.unID = u.unID
        JOIN participates p ON u.unID = p.unID
        JOIN Mission m ON p.mID = m.mID
    GROUP BY c.s_ID;
    
    RETURN ref;
END;
$$ LANGUAGE plpgsql;
