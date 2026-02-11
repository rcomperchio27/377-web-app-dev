
<h2>Movies <span id="record-count"></span></h2>

<?php

for ($i = 1; $i < 10; $i++)
{
    echo "<a href='index.php?nav=list&filter=$i'>$i</a> ";
}

for ($i = 0; $i < 26; $i++)
{
    $letter = chr($i + ord("A"));
    echo "<a href='index.php?nav=list&filter=$letter'>$letter</a> ";
}
?>

<a href='index.php?nav=list'>all</a>
<table border="1">
    <tr>
        <th>Title</th>
        <th>Durration</th>
        <th>Release</th>
    </tr>
<?php 

$connection = get_connection();

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
    echo "<td><a href='index.php?nav=detail&id=$row[mov_id]'>" . $row["mov_title"] . "</a></td>";
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