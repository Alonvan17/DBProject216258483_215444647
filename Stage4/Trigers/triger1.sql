CREATE OR REPLACE FUNCTION trg_block_tank_without_unit()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.unID IS NULL THEN
        RAISE EXCEPTION 'Cannot insert Tank without associated unit (unID)';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_block_tank
BEFORE INSERT ON Tank
FOR EACH ROW
EXECUTE FUNCTION trg_block_tank_without_unit();
