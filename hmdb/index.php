<html>
    <head>
        <title>hMDB</title>
    </head>

    <body>
        <h1>hMDB: The Hanover Movie Database</h1>

        <h2>Movies</h2>

        <table border="1">
            <tr>
                <th>Id</th>
                <th>Title</th>
                <th>Durration</th>
                <th>Release</th>
            </tr>
<?php 

$servername = "192.168.25.236";
$username = "root";
$password = "password";
$dbname = "hmbd";

// connect to the database and make sure it was successful
$connection = new mysqli($servername, $username, $password, $dbname);
if ($connection->connection_error) 
{
    die("Connection failed: " . $connection->connection_error);
}

$sql = "SELECT * FROM movie";

$result = $connection->query($sql);

while ($row = $result->fetch_assoc()) {
    echo "<tr>";
    echo "<td>" . $row["mov_id"] . "</td>";
    echo "<td>" . $row["mov_title"] . "</td>";
    echo "<td>" . $row["mov_durration"] . "</td>";
    echo "<td>" . $row["mov_release"] . "</td>";
    echo "</tr>";
}

?>
        </table>
    </body>
</html>