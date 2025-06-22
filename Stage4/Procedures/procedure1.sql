CREATE OR REPLACE PROCEDURE pr_promote_commanders()
LANGUAGE plpgsql
AS $$
DECLARE
    rec RECORD;
BEGIN
    FOR rec IN 
        SELECT s.s_ID, COUNT(DISTINCT m.mID) AS missions
        FROM Commander c
        JOIN Crew cr ON c.c_ID = cr.c_ID
        JOIN Soldier s ON c.s_ID = s.s_ID
        JOIN Tank t ON t.c_ID = cr.c_ID
        JOIN Unit u ON t.unID = u.unID
        JOIN participates p ON u.unID = p.unID
        JOIN Mission m ON p.mID = m.mID
        GROUP BY s.s_ID
    LOOP
        IF rec.missions >= 5 THEN
            UPDATE Soldier SET rank = 'admiral' WHERE s_ID = rec.s_ID;
        ELSIF rec.missions >= 3 THEN
            UPDATE Soldier SET rank = 'captain' WHERE s_ID = rec.s_ID;
        ELSE
            UPDATE Soldier SET rank = 'sailor' WHERE s_ID = rec.s_ID;
        END IF;
    END LOOP;
END;
$$;
