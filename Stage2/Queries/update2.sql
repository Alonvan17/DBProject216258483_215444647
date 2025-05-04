--  השאילתה מעדכנת את תאריך סיום ההשכרה של כלי שיט שנבדקו לפני 2024 ושייכים לבסיסים שיש בהם לפחות שלושה צוותים שונים, על ידי הוספת חודשיים לתאריך.

UPDATE Sea_vessel sv
SET lease_expiration_date = lease_expiration_date + INTERVAL '2 months'
WHERE EXTRACT(YEAR FROM sv.test_date) < 2024
  AND sv.base_ID IN (
    SELECT sv2.base_ID
    FROM Sea_vessel sv2
    JOIN Crew c ON sv2.c_ID = c.c_ID
    GROUP BY sv2.base_ID
    HAVING COUNT(DISTINCT c.c_ID) >= 3
  )
  AND lease_expiration_date IS NOT NULL;
