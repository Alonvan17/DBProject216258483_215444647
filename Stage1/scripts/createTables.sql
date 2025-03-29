-- Create Table    : 'Base'   
-- base_ID         :  
-- location        :  
--

CREATE TABLE Base 
(
    base_ID        NUMBER(38) NOT NULL,
   location       CHAR(15) NOT NULL,
CONSTRAINT pk_Base PRIMARY KEY (base_ID)
);

-- Create Table    : 'Crew'   
-- c_ID            :  
-- c_size          :  

CREATE TABLE Crew (
    c_ID           NUMBER(38) NOT NULL,
    c_size         NUMBER(38) NOT NULL,
CONSTRAINT pk_Crew PRIMARY KEY (c_ID)
);


-- Create Table    : 'Sea_vessel'   
-- sea_ID          :  
-- launcher_amount :  
-- nickname        :  
-- capacity        :  
-- test_date       :  
-- c_ID            :  (references Crew.c_ID)
-- lease_expiration_date :  
-- base_ID         :  (references Base.base_ID)

CREATE TABLE Sea_vessel (
    sea_ID         NUMBER(38) NOT NULL,
    launcher_amount NUMBER(38) NOT NULL,
    nickname       CHAR(15) NOT NULL,
    capacity       NUMBER(38) NOT NULL,
    test_date      DATE NOT NULL,
    c_ID           NUMBER(38) NOT NULL,
    lease_expiration_date DATE,
    base_ID        NUMBER(38) NOT NULL,
CONSTRAINT pk_Sea_vessel PRIMARY KEY (sea_ID),
CONSTRAINT fk_Sea_vessel2 FOREIGN KEY (c_ID)
    REFERENCES Crew (c_ID),
CONSTRAINT fk_Sea_vessel FOREIGN KEY (base_ID)
    REFERENCES Base (base_ID)
    ON DELETE CASCADE
);



-- Create Table    : 'Soldier'   
-- s_ID            :  
-- name            :  
-- rank            :  
-- c_ID            :  (references Crew.c_ID)

CREATE TABLE Soldier (
    s_ID           NUMBER(38) NOT NULL,
    name           CHAR(15) NOT NULL,
    rank           CHAR(15) NOT NULL CHECK(rank= 'sailor' or rank = 'captain' or rank = 'admiral'),
    c_ID           NUMBER(38) NOT NULL,
CONSTRAINT pk_Soldier PRIMARY KEY (s_ID),
CONSTRAINT fk_Soldier FOREIGN KEY (c_ID)
    REFERENCES Crew (c_ID)
    ON DELETE CASCADE
);

-- Create Table    : 'Warship'   
-- sea_ID          :  (references Sea_vessel.sea_ID)
-- cannons_amount  :  

CREATE TABLE Warship (
    sea_ID         NUMBER(38) NOT NULL,
    cannons_amount NUMBER(38) NOT NULL,
CONSTRAINT pk_Warship PRIMARY KEY (sea_ID),
CONSTRAINT fk_Warship FOREIGN KEY (sea_ID)
    REFERENCES Sea_vessel (sea_ID)
);


-- Create Table    : 'Submarine'   
-- sea_ID          :  (references Sea_vessel.sea_ID)
-- oxygen_density  :  
-- max_depth       :  

CREATE TABLE Submarine (
    sea_ID         NUMBER(38) NOT NULL,
    oxygen_density FLOAT NOT NULL,
    max_depth      NUMBER(38) NOT NULL,
CONSTRAINT pk_Submarine PRIMARY KEY (sea_ID),
CONSTRAINT fk_Submarine FOREIGN KEY (sea_ID)
    REFERENCES Sea_vessel (sea_ID)
);



-- Create Table    : 'Missile_ship'   
-- sea_ID          :  (references Warship.sea_ID)
-- missle_capacity :  

CREATE TABLE Missile_ship (
    sea_ID         NUMBER(38) NOT NULL,
    missle_capacity NUMBER(38) NOT NULL,
CONSTRAINT pk_Missile_ship PRIMARY KEY (sea_ID),
CONSTRAINT fk_Missile_ship FOREIGN KEY (sea_ID)
    REFERENCES Warship (sea_ID)
);


-- Create Table    : 'Destroyer'   
-- sea_ID          :  (references Warship.sea_ID)

CREATE TABLE Destroyer (
    sea_ID         NUMBER(38) NOT NULL,
CONSTRAINT pk_Destroyer PRIMARY KEY (sea_ID),
CONSTRAINT fk_Destroyer FOREIGN KEY (sea_ID)
    REFERENCES Warship (sea_ID)
);


-- Create Table    : 'Commander'   
-- s_ID            :  (references Soldier.s_ID)
-- c_ID            :  (references Crew.c_ID)

CREATE TABLE Commander (
    s_ID           NUMBER(38) NOT NULL,
    c_ID           NUMBER(38) NOT NULL,
CONSTRAINT pk_Commander PRIMARY KEY (s_ID),
CONSTRAINT fk_Commander2 FOREIGN KEY (s_ID)
    REFERENCES Soldier (s_ID),
CONSTRAINT fk_Commander FOREIGN KEY (c_ID)
    REFERENCES Crew (c_ID)
);
