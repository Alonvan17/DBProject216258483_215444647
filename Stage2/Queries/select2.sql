-- סכום תותחים מחולק במספר כלי שיט בכל בסיס
SELECT 
    b.location,
    SUM(w.cannons_amount) AS total_cannons,
    COUNT(sv.sea_ID) AS vessel_count,
    ROUND(SUM(w.cannons_amount) / NULLIF(COUNT(sv.sea_ID), 0), 2) AS avg_cannons_per_vessel
FROM Warship w
JOIN Sea_vessel sv ON w.sea_ID = sv.sea_ID
JOIN Base b ON sv.base_ID = b.base_ID
GROUP BY b.location;
