--  מעדכן את תאריך סיום ההשאלה של כלי שיט שגודל הצוות שלהם גדול מ־90 והתוקף הנוכחי שלהם במהלך שנת 2023, על ידי הוספת 6 חודשים.
UPDATE Sea_vessel sv
SET lease_expiration_date = lease_expiration_date + INTERVAL '6 months'
WHERE sea_ID IN (
    SELECT sv_inner.sea_ID
    FROM Sea_vessel sv_inner
    JOIN Crew c ON sv_inner.c_ID = c.c_ID
    WHERE c.c_size > 90
      AND sv_inner.lease_expiration_date BETWEEN DATE '2023-01-01' AND DATE '2023-12-31'
)
AND lease_expiration_date IS NOT NULL;