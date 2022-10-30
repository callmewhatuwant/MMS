#Eingabe
Zahl1=int(input("1. Zahl: "))
Zahl2=int(input("2. Zahl: "))
Rechenzeichen=input("Addieren? (+), Subtrahieren? (-), Multiplizieren? (*), Dividieren? (/): ")

#Rechnung
Ergebnis=0
if Rechenzeichen=="+":
    Ergebnis=Zahl1+Zahl2
if Rechenzeichen=="-":
    Ergebnis=Zahl1-Zahl2
if Rechenzeichen=="*":
    Ergebnis=Zahl1*Zahl2
if Rechenzeichen=="/":
    Ergebnis=Zahl1/Zahl2

#Ausgabe
print("Ergebnis ist:", Ergebnis)