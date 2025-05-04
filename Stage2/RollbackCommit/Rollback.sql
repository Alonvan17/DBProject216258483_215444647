BEGIN;

UPDATE Soldier
SET name = LEFT('WOW_' || name, 15)
WHERE rank = 'captain';

SELECT s_id, name, rank
FROM Soldier
WHERE rank = 'captain';

ROLLBACK;

SELECT s_id, name, rank
FROM Soldier
WHERE rank = 'captain';
