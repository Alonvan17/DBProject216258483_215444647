SELECT ship_type, COUNT(*) AS count
FROM V_ALL_SHIPS
GROUP BY ship_type;

SELECT COUNT(sea_id), base_location
FROM V_ALL_SHIPS
where ship_type = 'Destroyer'
GROUP BY base_location;
