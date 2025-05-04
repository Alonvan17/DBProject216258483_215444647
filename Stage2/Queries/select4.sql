 -- המספר הממוצע של תותחים על ספינות מלחמה בשנה וחודש של תאריך הבדיקה שלהם.
 SELECT 
    EXTRACT(YEAR FROM sv.test_date) AS year,
    EXTRACT(MONTH FROM sv.test_date) AS month,
    AVG(w.cannons_amount) AS avg_cannons
FROM Warship w
JOIN Sea_vessel sv ON w.sea_ID = sv.sea_ID
GROUP BY EXTRACT(YEAR FROM sv.test_date), EXTRACT(MONTH FROM sv.test_date)
ORDER BY year, month;
