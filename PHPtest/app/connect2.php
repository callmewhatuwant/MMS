<?php
try {

    $con = NEW PDO('mysql:host=localhost;dbname=PHP','root','123456');
}catch(PDOException $e){

    die($e->getMessage());
}
?>
