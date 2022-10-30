<?php
include_once('connect2.php');
if(isset($_POST['submit']));
{
    if(!empty($_POST['Vorname']) && ($_POST['Nachname']) && ($_POST['Wohnort']) && ($_POST['Strasse']))
    {
        $Vorname=$_POST['Vorname'];
        $Nachname=$_POST['Nachname'];
        $Wohnort=$_POST['Wohnort'];
        $Strasse=$_POST['Strasse'];

        #mysql_query("INSERT into test (Vorname, Nachname, Wohnort, Strasse) values ('Vorname', 'Nachname', 'Wohnort', 'Strasse','')");
        
        $stmt= $con->prepare("INSERT into test (Vorname, Nachname, Wohnort, Strasse) 
        values ('".$Vorname."', '".$Nachname."', '".$Wohnort."', '".$Strasse."')");
        $stmt->execute();
            echo "Deine daten wurden in der Datenbank gespeichert";
            header("refresh:2=insert.php");
        
            
    
    }
    else
    {
        echo "Bitte Eingabe prüfen";
    }
    

    
    
    

}




?>