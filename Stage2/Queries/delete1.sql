-- מחיקת צוללות שצפיפות החמצן שלהם נמוכה מהממוצע של כמות המשגרים בכלי השיט בתוספת 10
DELETE FROM Submarine
WHERE sea_ID IN (
  SELECT sea_ID
  FROM Submarine
  WHERE oxygen_density < (
    SELECT AVG(launcher_amount)
    FROM Sea_vessel
  ) + 10
);

