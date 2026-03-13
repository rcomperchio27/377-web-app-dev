<?php

/*************************************************************************************************
 * delete.php
 *
 * This page deletes a single country record based on the values submitted by the user
 *************************************************************************************************/

include("library.php");

$connection = get_connection();

$id = $connection->real_escape_string($id);

// Deletes country with the specified id
$delete =<<<SQL
DELETE
  FROM country
 WHERE country_id = $id
SQL;

$connection->query($delete);

// Returns to the list page
header('Location: index.php?content=list');
?>