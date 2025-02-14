import PyPDF2
import fitz  # PyMuPDF module problem

File_path = 'Examable.1.0/搜题题库/9618.qus/9618_s21_qp_12.pdf'


def getPdf_text(Pdf_path, page):
    # PDF处理获取页数
    doc = fitz.open(Pdf_path)
    page_text = doc.get_page_text(page)
    page_text = ''.join(page_text)
    return page_text
