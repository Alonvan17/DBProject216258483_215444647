-- מחיקת חיילים שמשרתים בצוותים שלא משויכים לאף כלי שיט, ושדרגתם היא סיילור ושלא משתמשים כמפקדים
DELETE FROM Soldier s
WHERE s.rank = 'sailor'
  AND NOT EXISTS (
    SELECT 1 
    FROM Sea_vessel sv
    WHERE sv.c_ID = s.c_ID
  )
  AND NOT EXISTS (
    SELECT 1 
    FROM Commander c
    WHERE c.s_ID = s.s_ID
  );
