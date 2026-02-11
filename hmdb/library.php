<?php

// This is the repository of all common functions for the hMDB website
extract($_REQUEST);

function get_connection(){
        
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
    return $connection;
}