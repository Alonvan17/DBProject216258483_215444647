CREATE OR REPLACE VIEW ARMOR_TANKS_MISSIONS_VIEW AS
SELECT
    t.tID AS tank_id,
    u.uName AS unit_name,
    m.mID AS mission_id,
    m.mdate AS mission_date
FROM
    TANK t
    JOIN UNIT u ON t.unID = u.unID
    JOIN participates p ON u.unID = p.unID
    JOIN MISSION m ON p.mID = m.mID;