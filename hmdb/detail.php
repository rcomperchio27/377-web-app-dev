<!-- print the name of the title of the movie for the given id -->
<?php

$servername = "localhost";
$username = "root";
$password = "password";
$dbname = "hmdb";

$connection = new mysqli($servername, $username, $password, $dbname);
if ($connection->connect_error) 
{
    die("Connection failed: " . $connection->connect_error);
}

extract($_REQUEST);
if (!isset($id)) {
    echo "<h1>No movie found</h1>";
} elseif ($id > 5118) {
    echo "<h1>No movie found</h1>";
} else {

$sql =<<<SQL
SELECT *
FROM movie
WHERE mov_id = $id
SQL;

$result = $connection->query($sql)->fetch_assoc();

echo "<h1>" . $result["mov_title"] . "</h1>";

?>

<table border="1">
            <tr>
                <th>Id</th>
                <th>Title</th>
                <th>Genre</th>
                <th>Rating</th>
                <th>Mpaa</th>
                <th>Durration</th>
                <th>Release</th>
            </tr>
            <tr>

<?php 
echo "<td><input type=''>" . $result["mov_id"] . "</input></td>";
echo "<td>" . $result["mov_title"] . "</td>";
echo "<td>" . $result["mov_genre"] . "</td>";
echo "<td>" . $result["mov_rating"] . "</td>";
echo "<td>" . $result["mov_mpaa"] . "</td>";
echo "<td>" . $result["mov_duration"] . "</td>";
echo "<td>" . $result["mov_release_year"] . "</td>";
echo "</tr>";
}
?>
</table>
