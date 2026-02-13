<?php

/*************************************************************************************************
 * detail.php
 *
 * Displays the details for a single movie. This page expects to be included within index.php.
 *************************************************************************************************/

if ($id == -1) {
$row['mov_id'] = -1;
$row['mov_title'] = '';
$row['mov_genre'] = '';
$row['mov_rating'] = NULL;
$row['mov_mpaa'] = '';
$row['mov_duration'] = NULL;
$row['mov_release_year'] = NULL;

echo '<h2>New Movie</h2>';

} else {
$sql =<<<SQL
SELECT *
  FROM movie
 WHERE mov_id = $id
SQL;

$connection = get_connection();

// Run the query on the database
$result = $connection->query($sql);

// Store the ONE result in an associative array
$row = $result->fetch_assoc();
echo '<h2>' . $row["mov_title"] . '</h2>';

}

?>
<!-- 
<h2><?php echo $row["mov_title"]; ?></h2> -->
<form action="save.php" method="POST">
    <input type="hidden" class="form-control" name="id" value="<?php echo $row["mov_id"]; ?>">

    <div class="mb-3">
        <label for="title" class="form-label">Title</label>
        <input type="text" class="form-control" name="title" value="<?php echo $row["mov_title"]; ?>">
    </div>

    <div class="mb-3">
        <label for="genre" class="form-label">Genre</label>
        <input type="text" class="form-control" name="genre" value="<?php echo $row["mov_genre"]; ?>">
    </div>

    <div class="mb-3">
        <label for="rating" class="form-label">Rating</label>
        <input type="text" class="form-control" name="rating" value="<?php echo $row["mov_rating"]; ?>">
    </div>

    <div class="mb-3">
        <label for="mpaa" class="form-label">MPAA</label>
        <input type="text" class="form-control" name="mpaa" value="<?php echo $row["mov_mpaa"]; ?>">
    </div>

    <div class="mb-3">
        <label for="duration" class="form-label">Duration</label>
        <input type="text" class="form-control" name="duration" value="<?php echo $row["mov_duration"]; ?>">
    </div>

    <div class="mb-3">
        <label for="release_year" class="form-label">Release Year</label>
        <input type="text" class="form-control" name="release_year" value="<?php echo $row["mov_release_year"]; ?>">
    </div>

    <button type="sumbit" class="btn btn-primary">Save</button>
    <a href="delete.php?id=<?php echo $row["mov_id"]; ?>" class="btn btn-danger" role="button">Delete</a>
    <a href="index.php?content=list" class="btn btn-secondary" role="button">Cancel</a>

</form>