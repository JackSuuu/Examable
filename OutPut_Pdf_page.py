import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
from Replace_to_answer import change
from Get_pdf_page import getPdf_page
from pathlib import Path

TestFile = "/Users/jack/Desktop/Python/project/Examable.1.0/搜题题库/9618.qus/9618_s21_qp_13.pdf"


def outputQue(File_path, Max_Page):
    with open(File_path, "rb") as file:
        reader = PdfFileReader(file)
        page = reader.getPage(Max_Page)
        writer = PdfFileWriter()
        writer.addPage(page)
        with open("Output_Que.pdf", "wb") as output:
            writer.write(output)


def outputAns(Question_file):
    OutputAns = change(Question_file)
    pages = getPdf_page(OutputAns)
    pdf_obj_reader = PdfFileReader(OutputAns)
    pdf_obj_writer = PdfFileWriter()
    for page_num in range(0, pages):  # 由于读取的页面是从0开始，所以开始页码进行减1操作
        pdf_obj_writer.addPage(pdf_obj_reader.getPage(
            page_num))  # 将符合条件的页码对应内容写入文件写入流
    # 最后，将提取好的文件流对象写入到新定义好的PDF文件中
    with open("Output_Ans.pdf", 'wb') as output_file_pdf:
        pdf_obj_writer.write(output_file_pdf)  # 写入到指定文件

