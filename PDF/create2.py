from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import mysql.connector

#Datenbank verbinden
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="my_secret_password",
  database="Wochenbericht"
)

mycursor = mydb.cursor()

#SQL
mycursor.execute("SELECT * FROM Bericht")

myresult = mycursor.fetchall()
abstand = 565
#Was geschieht?
for x in myresult:
    ausgabe =x[1] + " " + x[3]
    test = x[1]
    #abstand = abstand -5
# Wo schreiben
packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(110, abstand, ausgabe)
can.drawString(60, abstand +2, test [0:2])
can.drawString(60, abstand -85, test [0:2])
can.drawString(60, abstand -165, test [0:2])
can.drawString(60, abstand -248, test [0:2])
can.drawString(60, abstand -334, test [0:2])
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)

# create a new PDF with Reportlab
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("Vorlage.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("Vorlage1.pdf", "wb")
output.write(outputStream)
outputStream.close()


