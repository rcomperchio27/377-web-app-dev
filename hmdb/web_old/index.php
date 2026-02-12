<html>
    <head>
        <title>hMDB</title>
    </head>

    <body>
        <h1>hMDB: The Hanover Movie Database</h1>
        <?php
        // include library
        include("library.php");

        // include proper content based on the `nav` request parameter
        if (!isset($nav)) {
            $nav = "list";
        }
        include("$nav.php");
        ?>
    </body>
</html>