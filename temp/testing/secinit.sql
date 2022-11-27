CREATE TABLE teams(
    id int,
    school varchar(255),
    conference varchar(10),
    color varchar(7),
    logos text
);

CREATE TABLE players(
    id int,
    teamID int,
    firstName varchar(255),
    lastName varchar(255),
    team varchar(255),
    year_ int,
    position varchar(2),
    jerseyNumber varchar(2),
    height int,
    weight_ int,
    homeCity varchar(255),
    homeState varchar(255)
);

LOAD DATA LOCAL INFILE 'C:/Users/CJohn/Desktop/CPED1/temp/data/teamInfo.csv' INTO TABLE teams
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;