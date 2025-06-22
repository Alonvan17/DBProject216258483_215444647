CREATE OR REPLACE PROCEDURE pr_auto_assign_crewmate(soldier_id int, commander_id int, crew_type VARCHAR)
LANGUAGE plpgsql
AS $$
DECLARE
    crew_id INT;
BEGIN
    SELECT c_ID INTO crew_id
    FROM Crew
    WHERE cID = commander_id
    LIMIT 1;

    IF crew_id IS NULL THEN
        RAISE EXCEPTION 'No crew exists for commander ID %', commander_id;
    END IF;

    INSERT INTO CrewMate (crID, cID, type)
    VALUES (soldier_id, commander_id, crew_type);
    
    RAISE NOTICE 'Soldier % assigned to crew % under commander % as %', 
        soldier_id, crew_id, commander_id, crew_type;
END;
$$;
