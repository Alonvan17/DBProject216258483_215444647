-- השאילתה מעדכנת את שמות החיילים בדרגת אדמירל בצוותים שלהם יש כלי שיט שנבדקו לפני שנת 2023 ובעלי קיבולת מצטברת גבוהה מ-1, על ידי הוספת תחילית לשם
UPDATE Soldier s
SET name = 'old_' || s.name
WHERE rank = 'captain'
AND c_ID IN (
    SELECT sv.c_ID
    FROM Sea_vessel sv
    WHERE EXTRACT(YEAR FROM sv.test_date) < 2023
    GROUP BY sv.c_ID
    HAVING SUM(sv.capacity) > 1
);
