import PyPDF2

pdf_name = input("Enter the PDF name: ")
pdf_open = open(pdf_name + '.pdf', 'rb')
pdf_read = PyPDF2.PdfFileReader(pdf_open)
pdf_pages = pdf_read.numPages

print("Number of pages in the PDF:", pdf_pages)

for pg_no in range(0, pdf_pages):
    pdf_page = pdf_read.getPage(0)
    pdf_text = pdf_page.extractText()

with open(pdf_name + '.txt', "a") as pdf_to_text_file:
    pdf_to_text_file.write(pdf_text)