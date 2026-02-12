<html>
    <head>
        <title>Detail</title>
    </head>

    <body>
<?php

$connection = get_connection();

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
echo "<td><input type='text' value='$result[mov_id]' /></td>";
echo "<td><input type='text' value='$result[mov_title]' /></input></td>";
echo "<td><input type='text' value='$result[mov_genre]' /></td>";
echo "<td><input type='text' value='$result[mov_rating]' /></td>";
echo "<td><input type='text' value='$result[mov_mpaa]' /></td>";
echo "<td><input type='text' value='$result[mov_duration]' /></td>";
echo "<td><input type='text' value='$result[mov_release_year]' /></td>";
}
?>
</tr>
</table>
</body>
</html>