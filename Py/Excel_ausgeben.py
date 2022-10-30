import openpyxl
wb = openpyxl.load_workbook(filename = 'excel - Kopie.xlsx')
sheet = wb.active

#a1 = sheet ['A1']
#a2 = sheet ['A2']
#a3 = sheet ['A3']

#print(a1.value)

cells = sheet ['A1': 'D8']
for c1, c2, c3, c4 in cells:
    print ("{0:8} {1:8} {2:8} {3:8}".format(c1.value, c2.value, c3.value, c4.value))
    
wb.save("excell.xlsx")