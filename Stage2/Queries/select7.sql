--  כל הספינות שבדקו אותן בשנה הנוכחית, כולל שם הצוות, בסיס ומספר חיילים בצוות
SELECT 
    sv.sea_ID, sv.nickname, sv.test_date,
    b.location AS base_location,
    c.c_size,
    (SELECT COUNT(*) FROM Soldier s WHERE s.c_ID = c.c_ID) AS soldier_count
FROM Sea_vessel sv
JOIN Base b ON sv.base_ID = b.base_ID
JOIN Crew c ON sv.c_ID = c.c_ID
WHERE EXTRACT(YEAR FROM sv.test_date) = EXTRACT(YEAR FROM CURRENT_DATE);