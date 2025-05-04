--  מוחק כל כלי שיט שתאריך הבדיקה והתאריך שבו מסתיים החוזה הם באותו חודש ושנה והתאריך שבו מסתיים החוזה מאוחר יותר מתאריך הבדיקה
DELETE FROM Sea_vessel
WHERE sea_ID IN (
  SELECT sv.sea_ID
  FROM Sea_vessel sv
  WHERE EXTRACT(YEAR FROM sv.lease_expiration_date) = EXTRACT(YEAR FROM sv.test_date)
    AND EXTRACT(MONTH FROM sv.lease_expiration_date) = EXTRACT(MONTH FROM sv.test_date)
    AND sv.lease_expiration_date > sv.test_date
);
