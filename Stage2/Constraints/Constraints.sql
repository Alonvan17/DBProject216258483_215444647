ALTER TABLE Submarine
ADD CONSTRAINT chk_max_depth_positive CHECK (max_depth > 0);

ALTER TABLE Sea_vessel
ALTER COLUMN lease_expiration_date SET NOT NULL;

ALTER TABLE Soldier
ALTER COLUMN rank SET DEFAULT 'sailor';
