DROP TABLE country;

CREATE TABLE `countries`.`country` (
  `country_id` INT NOT NULL AUTO_INCREMENT,
  `country_name` VARCHAR(100) NOT NULL,
  `country_abbreviation` VARCHAR(10) NULL,
  `country_continent` VARCHAR(45) NOT NULL,
  `country_flag` VARCHAR(100) NULL,
  `country_capital` VARCHAR(45) NULL,
  `country_leader` VARCHAR(45) NULL,
  `country_independence_year` INT NULL,
  `country_area` INT NULL,
  `country_population` INT NULL,
  PRIMARY KEY (`country_id`));

-- INSERT INTO country (country_name, country_abbreviation, country_continent, country_flag, country_capital, country_leader, country_independence_year, country_area, country_population) VALUES ('United States of America', 'US', 'North America', NULL, 'Washington D.C.', 'President Donald Trump', 1776, 3796742, 331449281);
-- INSERT INTO country (country_name, country_abbreviation, country_continent, country_flag, country_capital, country_leader, country_independence_year, country_area, country_population) VALUES ('Canada', 'CA', 'North America', NULL, 'Ottawa', 'Prime Minister Mark Carney', 1867, 3855100, 36991981); 
-- INSERT INTO country (country_name, country_abbreviation, country_continent, country_flag, country_capital, country_leader, country_independence_year, country_area, country_population) VALUES ('Mexico', 'MX', 'North America', NULL, 'Mexico City', 'President Claudia Sheinbaum', 1836, 761610, 126014024); 
-- INSERT INTO country (country_name, country_abbreviation, country_continent, country_flag, country_capital, country_leader, country_independence_year, country_area, country_population) VALUES ('France', 'FR', 'Europe', NULL, 'Paris', 'President Emmanuel Macron', , ' sq mi', ''); 

INSERT INTO country (country_name, country_abbreviation, country_continent, country_flag, country_capital, country_leader, country_independence_year, country_area, country_population) VALUES
('United States', 'USA', 'North America', NULL, 'Washington, D.C.', 'Joe Biden', 1776, 9833520, 331000000),
('Canada', 'CAN', 'North America', NULL, 'Ottawa', 'Justin Trudeau', 1867, 9984670, 38000000),
('United Kingdom', 'UK', 'Europe', NULL, 'London', 'Rishi Sunak', 1707, 243610, 67000000),
('Australia', 'AUS', 'Oceania', NULL, 'Canberra', 'Anthony Albanese', 1901, 7692024, 26000000),
('India', 'IND', 'Asia', NULL, 'New Delhi', 'Narendra Modi', 1947, 3287263, 1400000000),
('Brazil', 'BRA', 'South America', NULL, 'Brasília', 'Luiz Inácio Lula da Silva', 1822, 8515767, 214000000),
('Germany', 'DEU', 'Europe', NULL, 'Berlin', 'Olaf Scholz', 1871, 357022, 83000000),
('Japan', 'JPN', 'Asia', NULL, 'Tokyo', 'Fumio Kishida', 660, 377975, 125000000),
('South Africa', 'ZAF', 'Africa', NULL, 'Pretoria', 'Cyril Ramaphosa', 1910, 1221037, 60000000),
('France', 'FRA', 'Europe', NULL, 'Paris', 'Emmanuel Macron', 843, 551695, 67000000);

SELECT *
FROM country
;