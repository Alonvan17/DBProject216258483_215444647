DO $$
DECLARE
    ref refcursor;
    rec RECORD;
BEGIN
    ref := fn_commander_performance();
    LOOP
        FETCH ref INTO rec;
        EXIT WHEN NOT FOUND;

        RAISE NOTICE 'Commander ID: %, # Tanks: %, # Missions: %, Level: %',
            rec.commander_id, rec.num_tanks, rec.num_missions, rec.experience_level;

        IF rec.experience_level = 'Experienced' THEN
            RAISE NOTICE '>> Commander % is highly experienced.', rec.commander_id;
        ELSIF rec.experience_level = 'Intermediate' THEN
            RAISE NOTICE '>> Commander % has moderate experience.', rec.commander_id;
        ELSE
            RAISE NOTICE '>> Commander % is new or inexperienced.', rec.commander_id;
        END IF;
    END LOOP;

    CLOSE ref;
EXCEPTION
    WHEN OTHERS THEN
        RAISE WARNING 'Error in commander performance main program: %', SQLERRM;
END $$ LANGUAGE plpgsql;
