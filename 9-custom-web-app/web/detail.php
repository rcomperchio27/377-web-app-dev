<?php
/*************************************************************************************************
 * detail.php
 *
 * Displays the details for a single country. This page expects to be included within index.php.
 *************************************************************************************************/

// If id = -1 is assumes it adding a new country
if ($id == -1) {
$row['country_id'] = -1;
$row['country_name'] = '';
$row['country_abbreviation'] = '';
$row['country_continent'] = '';
$row['country_flag'] = '';
$row['country_capital'] = '';
$row['country_leader'] = '';
$row['country_independence_year'] = 0;
$row['country_area'] = 0;
$row['country_population'] = 0;

echo '<h2>New Country</h2>';

} else {

// If current country get the data
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

// Displays country's name
echo '<h2>' . $row["country_name"] . '</h2>';
}

// Check if the country has a flag
if ($row["country_flag"] == NULL) {
    // If not uses placeholder
    $flag_url = 'https://png.pngtree.com/png-vector/20230407/ourmid/pngtree-placeholder-line-icon-vector-png-image_6691835.png';
} else {
    $flag_url = $row["country_flag"];
}
?>

<!-- Start of form -->
<form action="save.php" method="POST">
    <!-- Div for the id -->
    <div class="input-group mb-3" bordered="true">
        <input type="hidden" class="form-control" name="country_id" id="idform" value="<?php echo $row["country_id"]; ?>">
    </div>

    <!-- Div for the Name and Abbreviation fields -->
    <div class="input-group mb-3" bordered="true">
        <input id="nameform" onchange="isMissing()" type="text" class="form-control" name="country_name" value='<?php echo $row["country_name"]; ?>'>
        <span class="input-group-text">(</span>
        <input type="text" class="form-control abrev" id="abrevform" name="country_abbreviation"  maxlength="2" value='<?php echo $row["country_abbreviation"]; ?>'>
        <span class="input-group-text">)</span>
    </div>

    <!-- Div for Flag field -->
    <div class="mb-3" bordered="true">
        <img height="200" name="country_flag" onerror=this.src='https://png.pngtree.com/png-vector/20230407/ourmid/pngtree-placeholder-line-icon-vector-png-image_6691835.png'; src='<?php echo "$flag_url" ?>'></img>
        <br>
        <label for="country_flag" class="form-label">Flag</label>
        <input type="text" class="form-control" id="flagform" name="flagform" value="<?php echo $row["country_flag"]; ?>">
    </div>

    <!-- Div for the Continent field -->
    <div class="mb-3" bordered="true">
        <label for="country_continent" class="form-label">Continent</label>
        <input type="text" class="form-control" onchange="isMissing()" id="continentform" name="country_continent" value="<?php echo $row["country_continent"]; ?>">
    </div>

    <!-- Div for the Capital field -->
    <div class="mb-3">
        <label for="country_capital" class="form-label">Capital</label>
        <input type="text" class="form-control" id="capitalform" name="country_capital" value="<?php echo $row["country_capital"]; ?>">
    </div>

    <!-- Div for the Leader field -->
    <div class="mb-3">
        <label for="country_leader" class="form-label">President</label>
        <input type="text" class="form-control" id="leaderform" name="country_leader" value="<?php echo $row["country_leader"]; ?>">
    </div>

    <!-- Div for the Independence field -->
    <div class="mb-3">
        <label for="country_independence_year" class="form-label">Independence</label>
        <input type="number" min="0" step="1" id="independenceform" class="form-control" name="country_independence_year" value="<?php echo $row["country_independence_year"]; ?>">
    </div>

    <!-- Div for the Area field -->
    <div class="mb-3">
        <label for="country_area" class="form-label">Area</label>
        <input type="number" min="0" step="1" class="form-control" id="areaform" name="country_area" value="<?php echo $row["country_area"]; ?>">
    </div>

    <!-- Div for the Population field -->
    <div class="mb-3">
        <label for="country_population" class="form-label">Population</label>
        <input type="number" min="0" step="1" class="form-control" id="populationform" name="country_population" value="<?php echo $row["country_population"]; ?>">
    </div>

    <!-- Text for not filled necessary fields -->
    <p id="save-failed"></p>

    <!-- Save Button -->
    <button id="save-btn" type="button" disabled="true" onclick="save()" class="btn btn-primary">Save</button>
    <?php 

    // JS code to check the required fields and give feedback
    $code =<<<JS
    <script>
    function isMissing() {
        document.getElementById('save-btn').disabled = true;
        if (document.getElementById('continentform').value == '') {
            document.getElementById('save-failed').innerHTML = 'Field Continent necessary';
        }
        if (document.getElementById('nameform').value == '') {
            document.getElementById('save-failed').innerHTML = 'Field Name necessary';
        }
        if (document.getElementById('nameform').value == '' && document.getElementById('continentform').value == '') {
            document.getElementById('save-failed').innerHTML = 'Field Name and Continent necessary';
        }
        if (document.getElementById('nameform').value != '' && document.getElementById('continentform').value != '') {
            document.getElementById('save-btn').disabled = false;
            document.getElementById('save-failed').innerHTML = '';
        }
    }
    
    // Runs function inorder to check fields when it loads
    isMissing()
    </script>
    JS;

    echo $code;

    // If not adding will display a delete button
    if ($id > 0) {
        echo '<a href=delete.php?id=';
        echo "$id";
        echo ' class="btn btn-danger" role="button">Delete</a>';   
    }
    ?>
    
    <!--- Back button to return to list page --->
    <a href="index.php?content=list" class="btn btn-secondary" role="button">Back</a>
</form>

<script>

function save() {
    var settings = {
        'async': true,
        'url': 'save.php?country_id=' + $('#idform').val() +
        '&country_name=' + $('#nameform').val() +
        '&country_abbreviation=' + $('#abrevform').val() +
        '&country_flag=' + $('#flagform').val() +
        '&country_continent=' + $('#continentform').val() +
        '&country_capital=' + $('#capitalform').val() +
        '&country_leader=' + $('#leaderform').val() +
        '&country_independence_year=' + $('#independenceform').val() + 
        '&country_area=' + $('#areaform').val() + 
        '&country_population=' + $('#populationform').val(),



        'method': 'POST',
        'headers': {
            'Cache-Control': 'no-cache'
        }
    };

    $.ajax(settings).done(function(response) {        
        showAlert('success', 'Success!', 'Country saved successfully!');
    }).fail(function() {
        showAlert('danger', 'Error!', 'Error while saving country');
    });
}

</script>