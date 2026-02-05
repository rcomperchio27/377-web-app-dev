<html>
    <head>
        <title>hMDB</title>
    </head>

    <body>
        <h1>hMDB: The Hanover Movie Database</h1>

        <h2>Movies <span id="record-count"></span></h2>

<?php

for ($i = 1; $i < 10; $i++)
{
    echo "<a href='index.php?filter=$i'>$i</a> ";
}

for ($i = 0; $i < 26; $i++)
{
    $letter = chr($i + ord("A"));
    echo "<a href='index.php?filter=$letter'>$letter</a> ";
}
echo "<a href='index.php'>all</a>";

?>
        <table border="1">
            <tr>
                <th>Title</th>
                <th>Durration</th>
                <th>Release</th>
            </tr>
<?php 

$servername = "localhost";
$username = "root";
$password = "password";
$dbname = "hmdb";

// connect to the database and make sure it was successful
$connection = new mysqli($servername, $username, $password, $dbname);
if ($connection->connect_error) 
{
    die("Connection failed: " . $connection->connect_error);
}

extract($_REQUEST);
if (!isset($filter))
{
    $filter = '';
} else {
    $filter = $connection->real_escape_string($filter);
}

$sql =<<<SQL
SELECT *
FROM movie
WHERE mov_title LIKE '$filter%'
ORDER BY mov_title
SQL;

$result = $connection->query($sql);
$recordCount = 0;

while ($row = $result->fetch_assoc()) {
    echo "<tr>";
    echo "<td><a href='detail.php?id=$row[mov_id]'>" . $row["mov_title"] . "</a></td>";
    echo "<td>" . $row["mov_duration"] . "</td>";
    echo "<td>" . $row["mov_release_year"] . "</td>";
    echo "</tr>";
    $recordCount++;
}
?>

        </table>
<?php echo $recordCount . " records";
$code =<<<JS
<script>
document.getElementById('record-count').innerHTML = '(' + $recordCount + ' records)';
</script>
JS;

echo $code;

?>
    </body>
</html>