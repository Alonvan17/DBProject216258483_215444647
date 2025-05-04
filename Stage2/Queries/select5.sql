--מחזיר את מספר ספינות מלחמה, צוללות, ספינות טילים ומשחתות לכל בסיס, מקובצים לפי מיקום הבסיס.
SELECT 
    b.location, 
    COUNT(DISTINCT w.sea_ID) AS warship_count, 
    COUNT(DISTINCT sub.sea_ID) AS submarine_count, 
    COUNT(DISTINCT ms.sea_ID) AS missile_ship_count, 
    COUNT(DISTINCT d.sea_ID) AS destroyer_count
FROM 
    Base b
LEFT JOIN 
    Sea_vessel sv ON b.base_ID = sv.base_ID
LEFT JOIN 
    Warship w ON sv.sea_ID = w.sea_ID
LEFT JOIN 
    Submarine sub ON sv.sea_ID = sub.sea_ID
LEFT JOIN 
    Missile_ship ms ON w.sea_ID = ms.sea_ID
LEFT JOIN 
    Destroyer d ON w.sea_ID = d.sea_ID
GROUP BY 
    b.location
ORDER BY 
    b.location;
