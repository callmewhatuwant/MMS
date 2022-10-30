<?php
include 'connect2.php';

$result = $con->query("SELECT * FROM test");


$all = $result->fetchALL();
$col = $all[0];

$columns = array();

echo "<pre>";
foreach($col AS $key=>$value)
{
    if(is_string($key))
    {
        $columns[] = $key;
    }
}
#print_r($columns);

echo "<table border='1'>";
foreach($columns AS $value)
{
    echo "<th>$value</th>";
}

for ($x=0;$x<count($all);$x++)
{
    echo "<tr>";
        for($y=0;$y<count($columns);$y++)
        {
            echo "<td>".$all[$x][$y]."</td>";
        }
    echo "</tr>";

}
?>
