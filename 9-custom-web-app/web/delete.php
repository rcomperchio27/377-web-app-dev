<?php

/*************************************************************************************************
 * delete.php
 *
 * This page saves a single country record based on the values submitted by the used
 *************************************************************************************************/

include("library.php");

$connection = get_connection();

$id = $connection->real_escape_string($id);

$delete =<<<SQL
DELETE
  FROM country
 WHERE country_id = $id
SQL;

$connection->query($delete);

header('Location: index.php?content=list');
?>