<?php 

/*************************************************************************************************
 * list.php
 *
 * Displays a list of countries. This page expects to be included within index.php.
 *************************************************************************************************/

$connection = get_connection();
// Sets Filters and overides previous filters if there are duplicates
// Checks if there are any filters selected
if (!isset($filtertypes)) {
    $filtertypes = '';
} else {
    // Sanitizes filter input
    $filtertypes = $connection->real_escape_string($filtertypes);
    // Splits the filter string into groups of filtername:filtervalue
    $allfilters = explode(':', $filtertypes);
    // Creates empty lists one to store filtername, filtervalue ($filters) and other to store just the names ($filterlist)
    $filters = [];
    $filterslist = [];
    // Loops through all the groups of filters
    for ($i = count($allfilters) - 1; $i > 0; $i--) {
        if ($allfilters[$i] != '') {
            $currentfilter = explode('=', $allfilters[$i])[0];
            $filtervalue = explode('=', $allfilters[$i])[1];
            // Checks if the current filter is already in the list to overide old filters
            if (in_array($currentfilter, $filterslist) == FALSE) {
                $filters[] = [$currentfilter, $filtervalue];
                $filterslist[] = $currentfilter;
            } else {
                // If there is a duplicate splits url on filter and concatinates it back to remove the filter
                header('Location: index.php?content=list&filtertypes=' . explode(":" . $allfilters[$i], $filtertypes)[0] . explode(":" . $allfilters[$i], $filtertypes)[1]);
                exit();
            }
        }
    }
}

?>
<!-- Header showing record count -->
<h2>Countries <span id="record-count"></span></h2>

<table id="main" class="stripe hover row-border compact"></table>

<?php 

$sql =<<<SQL
SELECT *
FROM country
ORDER BY country_name
SQL;

// Runs the query
$row = [];
$result = $connection->query($sql);

while ($row = $result->fetch_assoc()) {
    $rows[] = $row;
}

print('<script>');
print('var data = ' . json_encode($rows, JSON_PARTIAL_OUTPUT_ON_ERROR) . ';');
print('</script>');

?>

<script>
    var dataTable = $('#main').DataTable({
        data: data,
        columns: [
            { data: 'country_name', title: 'Country Name', render: function(data, type, row) {
                return ('<a class="countrylink" href="index.php?content=detail&id=' + row.country_id + '">' + row.country_name + '</a>');
            } 
            },
            { data: 'country_abbreviation', title: 'Country Abrev' },
            { data: 'country_continent', title: 'Country Continent' },
            { data: 'country_flag', title: 'Country Flag' },
            { data: 'country_independence', title: 'Independence Date', render: function(data, type, row) {
                var date = new Date(data);
                return date.toLocaleDateString();
            }}
        ]});
</script>


<!-- Table showing the countries -->
<!-- <table class="table table-bordered table-hover">
    <thead class="thead-dark">
        <tr>    
            <th>
                <!-- Button to clear all the filters selected -->
                <a href='index.php?content=list' class="btn btn-danger" role="button">Clear Filters</a>
            </th>
            <th>
                <!-- Name header with a-z filters -->
            <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Name
                </button>
                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <?php
                    echo "<a href='index.php?content=list&filtertypes=" . $filtertypes . ":name=" . "none'>Clear</a><br> ";
                    for ($i = 0; $i < 26; $i++)
                    {
                        $letter = chr($i + ord("A"));
                        echo "<a href='index.php?content=list&filtertypes=" . $filtertypes . ":name=" . "$letter'>$letter</a> ";
                    }
                    ?>
                </div>
            </div>
            </th>
            <th>
                <!-- Abbreviation header with a-z filters -->
            <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Abbreviation
                </button>
                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <?php
                    echo "<a href='index.php?content=list&filtertypes=" . $filtertypes . ":abrev=" . "none'>Clear</a><br> ";
                    for ($i = 0; $i < 26; $i++)
                    {
                        $letter = chr($i + ord("A"));
                        echo "<a href='index.php?content=list&filtertypes=" . $filtertypes . ":abrev=" . "$letter'>$letter</a> ";
                    }
                    ?>
                </div>
            </div>
            </th>
            <!-- Continent header with filters -->
            <th><div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Continent
                </button>
                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <?php
                        echo "<a href='index.php?content=list&filtertypes=" . $filtertypes . ":continent=" . "none'>Clear</a><br> ";
                        echo "<a href='index.php?content=list&filtertypes=" . $filtertypes . ":continent=" . "North America'>North America</a><br> ";
                        echo "<a href='index.php?content=list&filtertypes=" . $filtertypes . ":continent=" . "South America'>South America</a><br> ";
                        echo "<a href='index.php?content=list&filtertypes=" . $filtertypes . ":continent=" . "Europe'>Europe</a><br> ";
                        echo "<a href='index.php?content=list&filtertypes=" . $filtertypes . ":continent=" . "Asia'>Asia</a><br> ";
                        echo "<a href='index.php?content=list&filtertypes=" . $filtertypes . ":continent=" . "Africa'>Africa</a><br> ";
                        echo "<a href='index.php?content=list&filtertypes=" . $filtertypes . ":continent=" . "Oceania'>Oceania</a><br> ";
                    ?>
                </div>
            </th>
        </tr>
    </thead>
    <tbody>
<?php -->

// Goes through list of filters changing them into thier variables for the query
if (isset($filters)) {
    for ($i = 0; $i < count($filters); $i++) {
        if ($filters[$i][0] == 'abrev') {
            $abrevfilter = $filters[$i][1];
            if ($abrevfilter == 'none') {
                $abrevfilter = '';
            }
        }
        if ($filters[$i][0] == 'name') {
            $namefilter = $filters[$i][1];
            if ($namefilter == 'none') {
                $namefilter = '';
            }
        }
        if ($filters[$i][0] == 'continent') {
            $continentfilter = $filters[$i][1];
            if ($continentfilter == 'none') {
                $continentfilter = '';
            }
        }
    }
}

// Confirms all filters are set or '' as none
if (!isset($namefilter)){
    $namefilter = '';
}else{
    $namefilter = $connection->real_escape_string($namefilter);
}

if (!isset($abrevfilter)){
    $abrevfilter = '';
}else{
    $abrevfilter = $connection->real_escape_string($abrevfilter);
}

if (!isset($continentfilter)){
    $continentfilter = '';
}else{
    $continentfilter = $connection->real_escape_string($continentfilter);
}

// SQL query for results including filters
$sql =<<<SQL
SELECT *
  FROM country
 WHERE country_name LIKE '$namefilter%'
 AND country_abbreviation LIKE '$abrevfilter%'
 AND country_continent LIKE '$continentfilter%' -- Uses an LIKE so when there is none selected it looks for one like '' and acts the same as no filter
 ORDER BY country_name
SQL;

// Runs the query
$result = $connection->query($sql);
$recordCount = 0;

// Goes through countries from resulted query and display them with thier correct abbreviation and flag
while ($row = $result->fetch_assoc())
{
    // If no flag results to placeholder
    if ($row["country_flag"] == NULL) {
        $flag_url = 'https://png.pngtree.com/png-vector/20230407/ourmid/pngtree-placeholder-line-icon-vector-png-image_6691835.png';
    } else {
        $flag_url = $row["country_flag"];
    }
    
    // Creates a new table row
    echo "<tr>";
    echo "<td><img height='60' width='95' class='countryflag' name='country_flag' src='$flag_url' onerror=this.src='https://png.pngtree.com/png-vector/20230407/ourmid/pngtree-placeholder-line-icon-vector-png-image_6691835.png'></img></td>";
    echo "<td><a class='countrylink' href='index.php?content=detail&id=". $row["country_id"] . "'>" . $row["country_name"] . "</a></td>";
    echo "<td>" . $row["country_abbreviation"] . "</td>";
    echo "<td>" . $row["country_continent"] . "</td>";
    echo "</tr>";

    // Adds to the record count
    $recordCount++;
}
?>
    </tbody>
</table>
<!-- Add Button -->
<a href="index.php?content=detail&id=-1" class="btn btn-primary" role="button">Add</a>

<?php

// JS code to display the record count
$code =<<<JS
<script>
document.getElementById('record-count').innerHTML = '(' + $recordCount + ' records)';
</script>
JS;

echo $code;

?>