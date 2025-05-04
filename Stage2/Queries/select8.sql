-- רשימת ספינות שתוקף ההשכרה שלהן יפוג תוך פחות מחצי שנה
SELECT 
    sea_ID, nickname, lease_expiration_date,
    EXTRACT(YEAR FROM lease_expiration_date) AS exp_year,
    EXTRACT(MONTH FROM lease_expiration_date) AS exp_month
FROM Sea_vessel
WHERE lease_expiration_date IS NOT NULL
  AND lease_expiration_date < CURRENT_DATE + INTERVAL '6 months';
