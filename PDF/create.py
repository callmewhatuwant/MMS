from fpdf import FPDF

#create FDPDF object
# Layout ('P', 'L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4'(default), 'A5', 'Letter', 'Legal', (100,500))

pdf = FPDF ('P', 'mm', 'Letter')

#Add a page

pdf.add_page()

#specify font
# fonts ('time', 'curier', 'helvetica', 'symbol', 'zpdfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination
pdf.set_font('helvetica', '', 16)

# Add text
# w = width
# h = hight
pdf.cell(40, 10, 'Hello World!')
pdf.output('create.pdf')