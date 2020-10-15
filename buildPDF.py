from fpdf import FPDF

header_title = 'None'
header_date = 'None'

def create_pdf(date, media, title, content, idx):
    pdf = PDF()
    print(content)
    pdf.build(media, content)
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
        self.set_font('Times', 'I', 8)
        # Add a page number
        page = 'Page ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def content(self, media, summary):
        # Read text file
        #with open(summary_file, 'rb') as fh:
            #txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, summary)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, media)

    def build(self, media, summary):
        self.add_page()
        self.content(media, summary)