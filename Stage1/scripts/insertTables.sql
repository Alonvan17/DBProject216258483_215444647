
-- Insert data into Base
INSERT INTO Base (base_ID, location) VALUES (1, 'Haifa');
INSERT INTO Base (base_ID, location) VALUES (2, 'Ashdod');
INSERT INTO Base (base_ID, location) VALUES (3, 'Eilat');

-- Insert data into Crew
INSERT INTO Crew (c_ID, c_size) VALUES (100, 25);
INSERT INTO Crew (c_ID, c_size) VALUES (101, 30);
INSERT INTO Crew (c_ID, c_size) VALUES (102, 20);

-- Insert data into Sea_vessel
INSERT INTO Sea_vessel (sea_ID, launcher_amount, nickname, capacity, test_date, c_ID, lease_expiration_date, base_ID)
VALUES (200, 4, 'Leviathan', 50, DATE '2022-01-01', 100, DATE '2030-01-01', 1);
INSERT INTO Sea_vessel (sea_ID, launcher_amount, nickname, capacity, test_date, c_ID, lease_expiration_date, base_ID)
VALUES (201, 2, 'Dolphin', 35, DATE '2021-06-15', 101, DATE '2028-06-15', 2);
INSERT INTO Sea_vessel (sea_ID, launcher_amount, nickname, capacity, test_date, c_ID, lease_expiration_date, base_ID)
VALUES (202, 6, 'TigerShark', 60, DATE '2023-03-10', 102, DATE '2032-03-10', 3);

-- Insert data into Soldier
INSERT INTO Soldier (s_ID, name, rank, c_ID) VALUES (300, 'David', 'captain', 100);
INSERT INTO Soldier (s_ID, name, rank, c_ID) VALUES (301, 'Yossi', 'sailor', 100);
INSERT INTO Soldier (s_ID, name, rank, c_ID) VALUES (302, 'Noa', 'admiral', 101);

-- Insert data into Warship
INSERT INTO Warship (sea_ID, cannons_amount) VALUES (200, 8);
INSERT INTO Warship (sea_ID, cannons_amount) VALUES (201, 4);
INSERT INTO Warship (sea_ID, cannons_amount) VALUES (202, 6);

-- Insert data into Submarine
INSERT INTO Submarine (sea_ID, oxygen_density, max_depth) VALUES (201, 0.85, 300);
INSERT INTO Submarine (sea_ID, oxygen_density, max_depth) VALUES (202, 0.9, 350);
INSERT INTO Submarine (sea_ID, oxygen_density, max_depth) VALUES (200, 0.8, 250);

-- Insert data into Missile_ship
INSERT INTO Missile_ship (sea_ID, missle_capacity) VALUES (200, 12);
INSERT INTO Missile_ship (sea_ID, missle_capacity) VALUES (201, 6);
INSERT INTO Missile_ship (sea_ID, missle_capacity) VALUES (202, 10);

-- Insert data into Destroyer
INSERT INTO Destroyer (sea_ID) VALUES (200);
INSERT INTO Destroyer (sea_ID) VALUES (201);
INSERT INTO Destroyer (sea_ID) VALUES (202);

-- Insert data into Commander
INSERT INTO Commander (s_ID, c_ID) VALUES (300, 100);
INSERT INTO Commander (s_ID, c_ID) VALUES (302, 101);
INSERT INTO Commander (s_ID, c_ID) VALUES (301, 100);
