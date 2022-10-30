import openpyxl
import mysql.connector
from openpyxl import Workbook
wb = Workbook ()
# grab the active worksheet
ws = wb.active


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
    ws.append([x[1], x[2], x[3], x[4]])
    print ("    ")
    print ("Datum: " + (x[1]))
    print ("Anfangszeit: "+ (x[2]))
    print ("Aufgabe: "      + (x[3]))
    print ("Endzeit: "          + (x[4]))
    print("     ")

wb.save("excell.xlsx")