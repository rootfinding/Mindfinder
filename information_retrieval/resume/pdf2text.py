# pip install pdfplumber
import pdfplumber

def pdf2text(filepath):
    pdf_text = ''
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            pdf_text += page.extract_text()

    print(pdf_text)

pdf2text('data/resumes/data_analyst_CV_template.pdf')