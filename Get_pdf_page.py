import PyPDF2

File_path = '/Users/jack/Desktop/project/Examable.1.0/搜题题库/9618.qus/9618_s21_qp_12.pdf'


def getPdf_page(Pdf_path):
    reader = PyPDF2.PdfFileReader(Pdf_path)
    page = reader.numPages
    return page

# print(getPdf_page(File_path))
