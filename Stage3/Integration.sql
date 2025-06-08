-- =============================
-- קובץ אינטגרציה INT.sql
-- שילוב חיל הים + חיל השריון
-- Crew היא טבלה מקשרת
-- =============================

-- =============================
-- 1. ALTER TABLES EXISTING
-- =============================

-- Alter Soldier to match SOLDIERS
ALTER TABLE Soldier
  ADD COLUMN IF NOT EXISTS firstName VARCHAR(20);

ALTER TABLE Soldier
  ADD COLUMN IF NOT EXISTS lastName VARCHAR(20);

ALTER TABLE Soldier
  ALTER COLUMN rank DROP NOT NULL;

ALTER TABLE Soldier
  ADD COLUMN IF NOT EXISTS draftDate DATE DEFAULT CURRENT_DATE;

ALTER TABLE Soldier
  ADD COLUMN IF NOT EXISTS releaseDate DATE DEFAULT (CURRENT_DATE + INTERVAL '3 years');

ALTER TABLE Crew
  ADD COLUMN IF NOT EXISTS cID numeric(38,0);

ALTER TABLE Crew
  ADD CONSTRAINT fk_Crew_Commander FOREIGN KEY (cID)
    REFERENCES Commander (s_ID);

-- =============================
-- 2. CREATE NEW TABLES FROM ARMOR CORPS
-- =============================

CREATE TABLE IF NOT EXISTS CREWMATE
(
  type VARCHAR(20) NOT NULL,
  crID numeric(9) NOT NULL,
  cID numeric(9) NOT NULL,
  PRIMARY KEY (crID),
  FOREIGN KEY (crID) REFERENCES Soldier (s_ID),
  FOREIGN KEY (cID) REFERENCES Commander (s_ID)
);

CREATE TABLE IF NOT EXISTS UNIT
(
  unID numeric(9) NOT NULL,
  uName VARCHAR(20) NOT NULL,
  cID numeric(9) NOT NULL,
  PRIMARY KEY (unID),
  FOREIGN KEY (cID) REFERENCES Commander (s_ID)
);

CREATE TABLE IF NOT EXISTS TANK
(
  tID numeric(9) NOT NULL,
  unID numeric(9) NOT NULL,
  cID numeric(9), 
  PRIMARY KEY (tID),
  FOREIGN KEY (unID) REFERENCES UNIT (unID),
  FOREIGN KEY (cID) REFERENCES Crew (c_ID)
);

CREATE TABLE IF NOT EXISTS MISSION
(
  mdate DATE NOT NULL,
  mID numeric(9) NOT NULL,
  PRIMARY KEY (mID)
);

CREATE TABLE IF NOT EXISTS participates
(
  mID numeric(9) NOT NULL,
  unID numeric(9) NOT NULL,
  PRIMARY KEY (mID, unID),
  FOREIGN KEY (mID) REFERENCES MISSION (mID),
  FOREIGN KEY (unID) REFERENCES UNIT (unID)
);

-- =============================
-- 3. NO NEED TO CHANGE EXISTING NAVY TABLES
-- =============================
-- Base
-- Sea_vessel
-- Submarine
-- Warship
-- Missile_ship
-- Destroyer
-- Commander
-- Crew
-- Soldier