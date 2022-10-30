<!DOCTYPE html>
<html>
<head>
    <titele>Hinzufügen</title>
</head>
<body>

<form action="insert.php" method="post"
<label>Name</lable>
<input type="text" name="Hinzufügen">
<br>
<label>Vorname</lable>
<input type="text" name="Hinzufügen">
<br>
<label>Wohnort</lable>
<input type="text" name="Hinzufügen">
<br>
<label>Straße</lable>
<input type="text" name="Hinzufügen">
<br>
<input type="submit" name="submit">

</form>
</body>
</html>

<?php
include 'connect2.php';
$sql = "INSERT INTO test (Vorname, Nachname, Wohnort, Strasse)
VALUES ('')";




?>