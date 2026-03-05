<h2>Countries <span id="record-count"></span></h2>

<a href='index.php?content=list'>All</a>

<?php

for ($i = 0; $i < 26; $i++)
{
    $letter = chr($i + ord("A"));
    echo "<a href='index.php?content=list&filter=$letter'>$letter</a> ";
}
?>

<table class="table table-bordered table-hover">
    <thead class="thead-dark">
        <tr>
            <th>Name</th>
            <th>Abbreviation</th>
            <th>Continent</th>
        </tr>
    </thead>
    <tbody>
<?php

$connection = get_connection();

if (!isset($filter))
{
    $filter = '';
}
else
{
    $filter = $connection->real_escape_string($filter);
}

$sql =<<<SQL
SELECT *
  FROM country
 WHERE country_name LIKE '$filter%'
 ORDER BY country_name
SQL;

$result = $connection->query($sql);

while ($row = $result->fetch_assoc())
{
    echo "<tr>";
    echo "<td><a href='index.php?content=detail&id=". $row["country_id"] . "'>" . $row["country_name"] . "</a></td>";
    echo "<td>" . $row["country_abbreviation"] . "</td>";
    echo "<td>" . $row["country_continent"] . "</td>";
    echo "</tr>";
}
?>
    </tbody>
</table>