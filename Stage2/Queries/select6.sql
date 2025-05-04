-- מחשב את המספר הממוצע של תותחים על ספינות מלחמה לכל בסיס
SELECT b.base_ID, b.location, AVG(w.cannons_amount) AS average_cannons
FROM Base b
JOIN Sea_vessel sv ON b.base_ID = sv.base_ID
JOIN Warship w ON sv.sea_ID = w.sea_ID
GROUP BY b.base_ID, b.location
ORDER BY average_cannons DESC;
