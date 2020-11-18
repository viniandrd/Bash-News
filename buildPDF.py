import fpdf
from fpdf import FPDF
import os
fpdf.set_global("SYSTEM_TTFONTS", os.path.join(os.path.dirname(__file__),'fonts'))

header_title = None
header_date = None

def create_pdf(idx, list):
    global header_title
    global header_date
    header_title = list[idx]['Title']
    header_date = list[idx]['Date']
    pdf = PDF()
    pdf.add_font("NotoSans", style="", fname="NotoSans-Regular.ttf", uni=True)
    pdf.add_font("NotoSans", style="B", fname="NotoSans-Bold.ttf", uni=True)
    pdf.add_font("NotoSans", style="I", fname="NotoSans-Italic.ttf", uni=True)
    pdf.add_font("NotoSans", style="BI", fname="NotoSans-BoldItalic.ttf", uni=True)
    #print(content)
    pdf.build(idx, list)
    pdf.output('./PDFS/Noticia-{}.pdf'.format(idx), 'F')


class PDF(FPDF):

    def header(self):
        # Set up a logo
        self.image('./images/Logo.png', 10, 8, 33)
        self.set_font('Arial', 'B', 15)
        # Add an address
        self.cell(100)
        self.cell(0, 5, header_title, ln=1)
        self.cell(100)
        self.cell(0, 5, header_date, ln=1)
        self.cell(100)
        #self.cell(0, 5, 'Any Town, USA', ln=1)

        # Line break
        self.ln(20)

    def footer(self):
        self.set_y(-10)
        self.set_font('NotoSans', 'I', 8)
        # Add a page number
        page = 'Page ' + str(self.page_no())
        self.cell(0, 10, page, 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('NotoSans', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def content(self, idx, list):
        # Read text file
        '''with open(summary_file, 'r') as f:
            txt = f.read()
        print(txt)'''
        # Times 12
        self.set_font('NotoSans', '', 14)
        # Output justified text
        print(list[idx]['Summary'])
        self.multi_cell(0, 5, list[idx]['Summary'])
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, list[idx]['Media'])

    def build(self, idx, list):
        #self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.add_page()
        self.content(idx, list)