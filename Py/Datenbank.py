#SQL Import
import mysql.connector
import re

#Input
Datum=input("Datum angeben: ")
Anfangszeit=input("Anfangszeit angeben: ")
Aufgabe=input("Aufgabe beschreiben: ")
Endzeit=input("Endzeit angeben: ")


#Datum
if len (Datum) != 10:
  print("Bitte korrigieren: dd.mm.jjjj ")
  quit()

x = re.search ("^[0-3][0-9]\.[0-1][0-2]\.[1-9][0-9][0-9][0-9]$", Datum)
if not x:
  print ("Bitte korrigieren: dd.mm.jjjj ")
  quit()

#Anfangszeit
if len (Anfangszeit) != 5 :
  print("Bitte korrigiere Anfangszeit:00:00 ")
  quit()

x = re.search ("^[0-2][0-9]\:[0-5][0-9]$", Anfangszeit)
if not x:
  print ("Bitte korrigiere Anfangszeit:00:00 ")
  quit()

#Aufgabe
if len (Aufgabe) <10 :
  print ("Bitte korrigiere: mehr als 10 Zeichen ")
  quit()

#Endzeit
if len (Endzeit) != 5:
  print ("Bitte korrigiere Endzeit:00:00 ")
  quit()

x = re.search ("^[0-2][0-9]\:[010.12p0-5][0-9]$", Endzeit)
if not x:
  print ("Bitte korrigiere Endzeit :00:00 ")
  quit()
  
#wenn alles richtig verbinden mit localhost
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="my_secret_password",
  database="Wochenbericht"
)

mycursor = mydb.cursor()

#Daten in Datenbank eintragen
sql = "INSERT INTO Bericht (Datum, Anfangszeit, Aufgabe, Endzeit) VALUES (%s, %s, %s, %s)"

val = (Datum, Anfangszeit, Aufgabe, Endzeit)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
