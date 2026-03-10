<?php
/*************************************************************************************************
 * detail.php
 *
 * Displays the details for a single country. This page expects to be included within index.php.
 *************************************************************************************************/

if ($id == -1) {
$row['country_id'] = -1;
$row['country_name'] = '';
$row['country_abbreviation'] = '';
$row['country_continent'] = '';
$row['country_flag'] = '';
$row['country_capital'] = '';
$row['country_leader'] = '';
$row['country_independence_year'] = NULL;
$row['country_area'] = NULL;
$row['country_population'] = NULL;

echo '<h2>New Country</h2>';

} else {

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
echo '<h2>' . $row["country_name"] . '</h2>';

}
?>

<form action="save.php" method="POST">

    <div class="input-group mb-3" bordered="true">
        <input type="hidden" class="form-control" name="country_id" value="<?php echo $row["country_id"]; ?>">
    </div>

    <div class="input-group mb-3" bordered="true">
        <input type="text" class="form-control" name="country_name" value='<?php echo $row["country_name"]; ?>'>
        <span class="input-group-text">(</span>
        <input type="text" class="form-control" name="country_abbreviation" value='<?php echo $row["country_abbreviation"]; ?>'>
        <span class="input-group-text">)</span>
    </div>

    <div class="mb-3" bordered="true">
        <img height="200" name="country_flag" src='<?php echo $row["country_flag"]; ?>'></img>
        <input type="text" class="form-control" name="country_flag" value="<?php echo $row["country_flag"]; ?>">
    </div>
    <!-- <br>
    <br> -->

    <div class="mb-3" bordered="true">
        <label for="country_continent" class="form-label">Continent</label>
        <input type="text" class="form-control" name="country_continent" value="<?php echo $row["country_continent"]; ?>">
    </div>

    <div class="mb-3">
        <label for="country_capital" class="form-label">Capital</label>
        <input type="text" class="form-control" name="country_capital" value="<?php echo $row["country_capital"]; ?>">
    </div>

    <div class="mb-3">
        <label for="country_leader" class="form-label">President</label>
        <input type="text" class="form-control" name="country_leader" value="<?php echo $row["country_leader"]; ?>">
    </div>

    <div class="mb-3">
        <label for="country_independence_year" class="form-label">Independence</label>
        <input type="text" class="form-control" name="country_independence_year" value="<?php echo $row["country_independence_year"]; ?>">
    </div>

    <div class="mb-3">
        <label for="country_area" class="form-label">Area</label>
        <input type="text" class="form-control" name="country_area" value="<?php echo $row["country_area"]; ?>">
    </div>
    
    <div class="mb-3">
        <label for="country_population" class="form-label">Population</label>
        <input type="text" class="form-control" name="country_population" value="<?php echo $row["country_population"]; ?>">
    </div>
    
    <button type="sumbit" class="btn btn-primary">Save</button>
    
    <?php 
    if ($id > 0) {
        echo '<a href=delete.php?id=';
        echo "$id";
        echo ' class="btn btn-danger" role="button">Delete</a>';   
    }
    ?>
    <a href="index.php?content=list" class="btn btn-secondary" role="button">Back</a>
</form>