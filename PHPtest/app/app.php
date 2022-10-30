<?php
include 'connect.php';

$result = $conn->query("SELECT * FROM test");

#$all = $result->fetchAll();

#$col =$all[0];
print_r($result);

?>