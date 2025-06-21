CREATE VIEW v_all_ships AS
SELECT 
    sv.sea_id,
    sv.nickname,
    sv.capacity,
    b.location AS base_location,
    CASE 
        WHEN d.sea_id IS NOT NULL THEN 'Destroyer'
        WHEN ms.sea_id IS NOT NULL THEN 'Missile Ship'
        WHEN sub.sea_id IS NOT NULL THEN 'Submarine'
        ELSE 'Sea Vessel'
    END AS ship_type
FROM sea_vessel sv
LEFT JOIN base b ON sv.base_id = b.base_id
LEFT JOIN warship ws ON sv.sea_id = ws.sea_id
LEFT JOIN destroyer d ON ws.sea_id = d.sea_id
LEFT JOIN missile_ship ms ON ws.sea_id = ms.sea_id
LEFT JOIN submarine sub ON sv.sea_id = sub.sea_id;
