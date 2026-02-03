-- The hMDB schema
CREATE TABLE `hmdb`.`movie` (
  `mov_id` INT NOT NULL AUTO_INCREMENT,
  `mov_title` VARCHAR(100) NOT NULL,
  `mov_rating` INT NULL,
  `mov_mpaa` VARCHAR(5) NULL,
  `mov_duration` INT NOT NULL,
  `mov_release` DATETIME NULL,
  PRIMARY KEY (`mov_id`));
  
  CREATE TABLE `hmdb`.`actor` (
  `act_id` INT NOT NULL AUTO_INCREMENT,
  `act_first_name` VARCHAR(100) NULL,
  `act_last_name` VARCHAR(100) NULL,
  `act_dob` DATETIME NULL,
  PRIMARY KEY (`act_id`));

CREATE TABLE `hmdb`.`movie_role` (
  `maj_id` INT NOT NULL AUTO_INCREMENT,
  `maj_mov_id` INT NOT NULL,
  `maj_act_id` INT NOT NULL,
  `maj_character` VARCHAR(200) NULL,
  PRIMARY KEY (`maj_id`));

-- Adding data to the hMDB schema

TRUNCATE TABLE movie;

INSERT INTO movie (mov_title, mov_duration) VALUES ('Sinners', 120);
INSERT INTO movie (mov_title, mov_duration) VALUES ('Wicked Part 2', 180);
INSERT INTO movie (mov_title, mov_duration) VALUES ('Marty Supreme', 106);
INSERT INTO movie (mov_title, mov_duration) VALUES ('Knives Out, Wake Up Dead Man', 115);
INSERT INTO movie (mov_title, mov_duration) VALUES ('The Rip', 132);
INSERT INTO movie (mov_title, mov_duration) VALUES ('Good Will Hunting', 114);

SELECT * FROM movie;

TRUNCATE TABLE actor;

INSERT INTO actor (act_first_name, act_last_name) VALUES ('Michael B.', 'Jordan');
INSERT INTO actor (act_first_name, act_last_name) VALUES ('Timothee', 'Chalamet');
INSERT INTO actor (act_first_name, act_last_name) VALUES ('Ariana', 'Grande');
INSERT INTO actor (act_first_name, act_last_name) VALUES ('Matt', 'Damon');
INSERT INTO actor (act_first_name, act_last_name) VALUES ('Ben', 'Affleck');

SELECT * FROM actor;

TRUNCATE TABLE movie_role;

-- Matt Damon was in goodwill hunting and the rip

INSERT INTO movie_role (maj_mov_id, maj_act_id, maj_character) VALUES (5, 4, 'L.T');
INSERT INTO movie_role (maj_mov_id, maj_act_id, maj_character) VALUES (6, 4, 'Will');
INSERT INTO movie_role (maj_mov_id, maj_act_id, maj_character) VALUES (, , '');
INSERT INTO movie_role (maj_mov_id, maj_act_id, maj_character) VALUES (, , '');
INSERT INTO movie_role (maj_mov_id, maj_act_id, maj_character) VALUES (, , '');

SELECT * FROM movie_role;

SELECT mov_title AS `Movie Name`, maj_character AS `Character`
FROM movie
JOIN movie_role ON maj_mov_id = mov_id
JOIN actor ON maj_act_id = act_id
WHERE act_first_name = 'Matt'
AND act_last_name = 'Damon'
ORDER BY mov_title
;

-- update data whithin the hMDB schema

SELECT *
FROM movie 
WHERE mov_id = 3
;

-- Updates a single record with the WHERE clause
UPDATE movie
	SET mov_mpaa = 'R', mov_release = '2025-12-01'
WHERE mov_id = 3
;

-- Updates all records by omiting the where clause
UPDATE movie
   SET mov_rating = 0
;
