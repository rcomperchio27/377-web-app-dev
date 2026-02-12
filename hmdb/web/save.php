<?php

/*************************************************************************************************
 * save.php
 *
 * This page saves a single movie record based on the values submitted by the used
 *************************************************************************************************/

include("library.php");

$connection = get_connection();

$title = $connection->real_escape_string($title);
$genre = $connection->real_escape_string($genre);
$duration = $connection->real_escape_string($duration);
$mpaa = $connection->real_escape_string($mpaa);
$rating = $connection->real_escape_string($rating);
$release_year = $connection->real_escape_string($release_year);

$update =<<<SQL
UPDATE movie
   SET mov_title = '$title',
       mov_genre = '$genre',
       mov_rating = $rating,
       mov_mpaa = '$mpaa',
       mov_duration = $duration,
       mov_release_year = $release_year
 WHERE mov_id = $id
SQL;

$connection->query($update);

header('Location: index.php?content=list');
?>