BEGIN;

UPDATE Soldier
SET name = LEFT('Mr.' || name, 15)
WHERE rank = 'admiral';

SELECT s_id, name, rank FROM Soldier WHERE rank = 'admiral';

COMMIT;

SELECT s_id, name, rank FROM Soldier WHERE rank = 'admiral';
    
