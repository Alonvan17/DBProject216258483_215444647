DO $$
DECLARE
    sid INT := 502;
    cid INT := 301;
    role TEXT := 'engineer';
BEGIN
    BEGIN
        CALL pr_assign_crewmate(sid, cid, role);
    EXCEPTION
        WHEN OTHERS THEN
            RAISE NOTICE 'Failed to assign soldier % to commander % as %: %', sid, cid, role, SQLERRM;
    END;

    RAISE NOTICE 'Displaying crew members under commander %:', cid;

    FOR rec IN
        SELECT * FROM fn_soldier_unit_summary(cid)
    LOOP
        RAISE NOTICE 'Soldier % assigned to unit %, tank % as %',
            rec.soldier_id, rec.unit_name, rec.tank_id, rec.crew_type;
    END LOOP;
END;
$$;