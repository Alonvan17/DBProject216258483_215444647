DO $$
DECLARE
    ref refcursor;
    rec RECORD;
    high_count INT := 0;
    medium_count INT := 0;
    low_count INT := 0;
BEGIN
    ref := fn_commander_performance();
    LOOP
        FETCH ref INTO rec;
        EXIT WHEN NOT FOUND;
        RAISE NOTICE 'Commander %: % tanks, % missions (% level)', 
            rec.commander_id, rec.num_tanks, rec.num_missions, rec.experience_level;

        IF rec.num_missions >= 5 THEN
            high_count := high_count + 1;
        ELSIF rec.num_missions >= 3 THEN
            medium_count := medium_count + 1;
        ELSE
            low_count := low_count + 1;
        END IF;
    END LOOP;
    CLOSE ref;

    RAISE NOTICE 'Summary: % high-level, % medium-level, % low-level commanders.',
        high_count, medium_count, low_count;
END;
$$;