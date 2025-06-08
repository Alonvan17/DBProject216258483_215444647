SELECT * FROM ARMOR_TANKS_MISSIONS_VIEW;

SELECT tank_id, unit_name, mission_id, mission_date
FROM ARMOR_TANKS_MISSIONS_VIEW
WHERE mission_date > '2025-01-01';