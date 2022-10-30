import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="my_secret_password",
  database="Wochenbericht"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Bericht")

myresult = mycursor.fetchall()

for x in myresult:
    print ("    ")
    print ("Datum: " + (x[1]))
    print ("Anfangszeit: "+ (x[2]))
    print ("Aufgabe: "      + (x[3]))
    print ("Endzeit: "          + (x[4]))
    print("     ")