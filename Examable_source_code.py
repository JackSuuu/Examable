import spacy
import re
from OCR_img import convert_img
from Get_pdf_page import getPdf_page
from Get_PDF_text import getPdf_text
from go_thorugh_folder import Gothrough
from OutPut_Pdf_page import outputQue, outputAns
import en_core_web_lg


punc = '~`!#$%^&*()_+-=|\;":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'

# nlp = spacy.load('en_core_web_lg')
nlp = en_core_web_lg.load()


def search_answer(image_path, target_subject):
    # 图像处理
    image_code = convert_img(image_path)

    # define a global array to get the biggest value of each paper
    Max_value = []
    question_page = []

    # PDF处理获取所有PDF文件
    # 使用已经设定好的 Go through class 来对对象进行处理
    Files = Gothrough()
    Files_paths = []

    if target_subject == "Mathmetics":
        question_paper = Files.Mathmetics
        Mathmetics_paper = Gothrough.get_filepaths(question_paper)
        Files_paths = Mathmetics_paper[:]

    elif target_subject == "ComputerScience":
        question_paper = Files.Computer
        ComputerScience_paper = Gothrough.get_filepaths(question_paper)
        Files_paths = ComputerScience_paper[:]

    # for 循环开始搜索
    for File_path in Files_paths:
        # get the page of each individual paper
        PDF_page = getPdf_page(File_path)

        # this is a temporary list for store the similarity in one pdf file
        # we have to select the biggest value in the list as the Max_value
        similarity_list = []

        # iterate each one pdf file in a single for loop
        for i in range(PDF_page):
            page_text = getPdf_text(File_path, i)

            txt1 = re.sub(r"[%s] + " % punc, "", image_code)
            txt2 = re.sub(r"[%s] + " % punc, "", page_text)

            doc3 = nlp(txt1)
            doc4 = nlp(txt2)

            similarity_list.append(doc3.similarity(doc4))
            # print test
            # print(similarity_list)
            # print the list out for testing each loop

        # stored the biggest value in the list, which the index represent the page in this file
        each_max = max(similarity_list)
        each_page = similarity_list.index(max(similarity_list))

        # append the Max_value and page
        Max_value.append(each_max)
        question_page.append(each_page)

        # refreash the list for store the next file data
        similarity_list.clear()

    # 用最大值来寻址
    Max_index = Max_value.index(max(Max_value))
    Question_file = Files_paths[Max_index]
    Max_Page = question_page[Max_index]

    # test print
    # print('\n' * 3)
    # print("Num of Page: ", Max_Page)
    # print("Ques.file_path: ", Question_file)

    # 截取questions图片 output.pdf
    outputQue(Question_file, Max_Page)

    # 将Question_file 写出答案
    outputAns(Question_file)


# answer_paper = search_answer('/Users/jack/Desktop/截屏2022-06-04 20.25.27.png', 'ComputerScience')
# print(answer_paper)
