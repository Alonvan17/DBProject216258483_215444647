--  השאילתה מוחקת חיילים בדרגת סיילור שלא משמשים כמפקדים וששייכים לצוותים שלהם כלי שיט שנבדק לפני 2015.

DELETE FROM Soldier s
WHERE s.rank = 'sailor'
  AND s.s_ID NOT IN (SELECT s_id FROM Commander)
  AND s.c_ID IN (
    SELECT DISTINCT sv.c_ID
    FROM Sea_vessel sv
    WHERE sv.test_date < DATE '2023-01-01'
  );
