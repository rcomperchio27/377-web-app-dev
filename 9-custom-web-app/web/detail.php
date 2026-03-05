<?php
/*************************************************************************************************
 * detail.php
 *
 * Displays the details for a single movie. This page expects to be included within index.php.
 *************************************************************************************************/

$sql =<<<SQL
SELECT *
  FROM country
 WHERE country_id = $id
SQL;

$connection = get_connection();

// Run the query on the database
$result = $connection->query($sql);

// Store the ONE result in an associative array
$row = $result->fetch_assoc();
echo '<h2>' . $row["country_name"] . '   (' . $row["country_abbreviation"]. ')</h2>';

?>

<input type="hidden" class="form-control" name="id" value="<?php echo $row["country_id"]; ?>">
<img height="200" src='<?php echo $row["country_flag"]; ?>'></img>
<br>
<br>

<div class="mb-3" bordered="true">
    <label for="continent" class="form-label">Continent</label>
    <p class="form-text"> <?php echo $row["country_continent"]; ?></p>
</div>


<div class="mb-3">
    <label for="mpaa" class="form-label">Capital</label>
    <input type="text" class="form-control" name="capital" value="<?php echo $row["country_capital"]; ?>">
</div>

<div class="mb-3">
    <label for="duration" class="form-label">President</label>
    <input type="text" class="form-control" name="leader" value="<?php echo $row["country_leader"]; ?>">
</div>

<div class="mb-3">
    <label for="release_year" class="form-label">Independence</label>
    <input type="text" class="form-control" name="independence_year" value="<?php echo $row["country_independence_year"]; ?>">
</div>
<a href="index.php?content=list" class="btn btn-secondary" role="button">Back</a>