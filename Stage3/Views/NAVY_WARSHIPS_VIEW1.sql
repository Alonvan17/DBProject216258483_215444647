CREATE OR REPLACE VIEW NAVY_VESSELS_COMMANDERS_VIEW AS
SELECT
    sv.sea_ID AS vessel_id,
    sv.nickname,
    sv.capacity,
    c.c_ID AS crew_id,
    com.s_ID AS commander_id,
    s.name AS commander_name
FROM
    Sea_vessel sv
    JOIN Crew c ON sv.c_ID = c.c_ID
    LEFT JOIN Commander com ON c.c_ID = com.c_ID
    LEFT JOIN Soldier s ON com.s_ID = s.s_ID;