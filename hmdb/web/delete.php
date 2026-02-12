<?php

/*************************************************************************************************
 * delete.php
 *
 * This page saves a single movie record based on the values submitted by the used
 *************************************************************************************************/

include("library.php");

$connection = get_connection();

$id = $connection->real_escape_string($id);

$delete =<<<SQL
DELETE
  FROM movie
 WHERE mov_id = $id
SQL;

$connection->query($delete);

header('Location: index.php?content=list');
?>