<?php
/*************************************************************************************************
 * save.php
 *
 * This page saves a single country record based on the values submitted by the user
 *************************************************************************************************/

include("library.php");

$connection = get_connection();

// Sanitizes the inputed values
$country_name = $connection->real_escape_string($country_name);
$country_abbreviation = $connection->real_escape_string($country_abbreviation);
$country_continent = $connection->real_escape_string($country_continent);
$country_flag = $connection->real_escape_string($country_flag);
$country_capital = $connection->real_escape_string($country_capital);
$country_leader = $connection->real_escape_string($country_leader);
$country_independence_year = $connection->real_escape_string($country_independence_year);
$country_area = $connection->real_escape_string($country_area);
$country_population = $connection->real_escape_string($country_population);

// SQL statement for adding a country
$add =<<<SQL
INSERT INTO country
(country_name, country_abbreviation, country_continent, country_flag, country_capital, country_leader, country_independence_year, country_area, country_population)
VALUES 
('$country_name', '$country_abbreviation', '$country_continent', '$country_flag', '$country_capital', '$country_leader', $country_independence_year, $country_area, $country_population)
SQL;

// SQL statement for updating a country
$update =<<<SQL
UPDATE country
   SET country_name = '$country_name',
       country_abbreviation = '$country_abbreviation',
       country_continent = '$country_continent',
       country_flag = '$country_flag',
       country_capital = '$country_capital',
       country_leader = '$country_leader',
       country_independence_year = $country_independence_year,
       country_area = $country_area,
       country_population = $country_population
 WHERE country_id = $country_id
SQL;

// If country doesn't have an id else it will update it
if ($country_id == -1) {
$connection->query($add);
} else {
$connection->query($update);
}

// Returns to the list page
header('Location: index.php?content=list');
?>