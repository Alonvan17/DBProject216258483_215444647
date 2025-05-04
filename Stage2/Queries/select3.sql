-- מצא את הבסיס עם הכי הרבה כלי ים
SELECT b.base_ID, b.location, COUNT(sv.sea_ID) AS vessel_count
FROM Base b
JOIN Sea_vessel sv ON b.base_ID = sv.base_ID
GROUP BY b.base_ID, b.location
ORDER BY vessel_count DESC
FETCH FIRST 1 ROWS ONLY;