BEGIN;

UPDATE Soldier
SET name = LEFT('Mr.' || name, 15)
WHERE rank = 'commander';

SELECT s_id, name, rank FROM Soldier WHERE rank = 'commander';

COMMIT;

SELECT s_id, name, rank FROM Soldier WHERE rank = 'commander';
