<html>
    <head>
        <title>PHP Lesson 1</title>
    </head>

    <body>
        <h1>PHP Lession 1</h1>

        <p>
            This is the first PHP lesson with simply PHP markup.

            <?php

            $count = 0;
            for ($i = 0; $i < 10; $i++) {
                echo "Hello";
                print('<br>');
                $count++;
            }
            echo $count;

            $firstName = "Will";
            $lastName = "Davidson";

            $fullName = $firstName . " " . $lastName;
            
            echo $fullName;

            // String Concatenation
            echo "<p>" . $fullName . " is in Web App Development" . "</p>";

            // String Interpolation
            echo "<p>$fullName is in Web App Development</p>";

            // String Interpolation only works wit hdouble quotes
            echo '<p>$fullName is in Web App Development</p>';




            ECHO "<p>case in-sensitive</p>";



            ?>

        </p>
    </body>
</html>