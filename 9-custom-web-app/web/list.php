<?php 

$connection = get_connection();
if (!isset($filtertypes)) {
    $filtertypes = '';
} else {
    $filtertypes = $connection->real_escape_string($filtertypes);
    $allfilters = explode(':', $filtertypes);
    $filters = [];
    $filterslist = [];
    for ($i = count($allfilters) - 1; $i > 0; $i--) {
        if ($allfilters[$i] != '') {
            $currentfilter = explode('=', $allfilters[$i])[0];
            $filtervalue = explode('=', $allfilters[$i])[1];
            if (in_array($currentfilter, $filterslist) == FALSE) {
                $filters[] = [$currentfilter, $filtervalue];
                $filterslist[] = $currentfilter;
            } else {
                header('Location: index.php?content=list&filtertypes=' . explode(":" . $allfilters[$i], $filtertypes)[0] . explode(":" . $allfilters[$i], $filtertypes)[1]);
                exit();
            }
        }
    }
}

?>


<h2>Countries <span id="record-count"></span></h2>

<table class="table table-bordered table-hover">
    <thead class="thead-dark">
        <tr>    
            <th>
                <a href='index.php?content=list' class="btn btn-danger" role="button">Clear Filters</a>
            </th>
            <th>
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
                </div></th>
        </tr>
    </thead>
    <tbody>
<?php
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
        // print_r($filters[$i]);
        // echo "<br>";
    }
}

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

$sql =<<<SQL
SELECT *
  FROM country
 WHERE country_name LIKE '$namefilter%'
 AND country_abbreviation LIKE '$abrevfilter%'
 AND country_continent LIKE '$continentfilter%' -- is an AND so when there is none selected it looks for one like '' same as no filter
 ORDER BY country_name
SQL;

$result = $connection->query($sql);
$recordCount = 0;


while ($row = $result->fetch_assoc())
{
    
    if ($row["country_flag"] == NULL) {
        $flag_url = 'https://png.pngtree.com/png-vector/20230407/ourmid/pngtree-placeholder-line-icon-vector-png-image_6691835.png';
    } else {
        $flag_url = $row["country_flag"];
    }
    echo "<tr>";
    echo "<td><img height='40' width='65' class='countryflag' name='country_flag' src='$flag_url' onerror=this.src='https://png.pngtree.com/png-vector/20230407/ourmid/pngtree-placeholder-line-icon-vector-png-image_6691835.png'></img></td>";
    echo "<td><a class='countrylink' href='index.php?content=detail&id=". $row["country_id"] . "'>" . $row["country_name"] . "</a></td>";
    echo "<td>" . $row["country_abbreviation"] . "</td>";
    echo "<td>" . $row["country_continent"] . "</td>";
    echo "</tr>";

    $recordCount++;
}
?>
    </tbody>
</table>
<a href="index.php?content=detail&id=-1" class="btn btn-primary" role="button">Add</a>

<?php

$code =<<<JS
<script>
document.getElementById('record-count').innerHTML = '(' + $recordCount + ' records)';
</script>
JS;

echo $code;

?>