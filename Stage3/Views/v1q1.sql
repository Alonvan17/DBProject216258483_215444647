SELECT * FROM NAVY_VESSELS_COMMANDERS_VIEW;

SELECT vessel_id, nickname, capacity, commander_name
FROM NAVY_VESSELS_COMMANDERS_VIEW
WHERE capacity > 100 AND commander_id IS NOT NULL;