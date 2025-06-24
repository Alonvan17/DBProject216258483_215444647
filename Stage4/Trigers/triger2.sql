CREATE OR REPLACE FUNCTION trg_sync_delete_soldier_crewmate()
RETURNS TRIGGER AS $$
BEGIN
    DELETE FROM CrewMate WHERE crID = OLD.sid;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_delete_crewmate
AFTER DELETE ON soldiers
FOR EACH ROW
EXECUTE FUNCTION trg_sync_delete_soldier_crewmate();
