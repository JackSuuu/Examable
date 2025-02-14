from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, \
    QFileDialog, QMessageBox, QMainWindow, QAction, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import pyqtSlot
from Examable_source_code import search_answer
import sys
import subprocess
import os


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        # setting the Vbox layout
        layout = QVBoxLayout()
        self.setWindowTitle("Examable")
        self.setFixedWidth(700)
        self.setFixedHeight(600)
        self.setStyleSheet("background: #161515;")
        # menu bar to select different subjects
        bar = self.menuBar()
        subjects = bar.addMenu("Subjects")
        Mathmetics = QAction("Mathmetics", self)
        Mathmetics.setShortcut("Ctrl+1")
        subjects.addAction(Mathmetics)
        ComputerScience = QAction("ComputerScience", self)
        ComputerScience.setShortcut("Ctrl+2")
        subjects.addAction(ComputerScience)
        subjects.triggered[QAction].connect(self.processtrigger)
        # display logo
        image = QPixmap("Assets/Examable_4.png")
        logo = QLabel(self)
        logo.setPixmap(image)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        logo.setStyleSheet("margin-top: 0;")
        # create a text that display the current search subjects
        self.subjects_text = QLabel(self)
        self.subjects_text.setText("Please choose a subject")
        self.subjects_text.setStyleSheet(
            "color: '#FED7BE';" +
            "font-size: 16px;" +
            "font-weight: bold;"
            # "border: 3px solid '#FED7BE'"
        )
        self.subjects_text.setAlignment(QtCore.Qt.AlignCenter)

        # Create a BUTTON WIDGET for upload image
        # 如果由多个object在图像中，需要谨慎加padding， margin。
        button = QPushButton("UPLOAD")
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(
            "*{border: 6px solid '#FED7BE';" +
            "border-radius: 60px;" +
            "font-size: 30px;" +
            "color: 'white';" +
            "padding: 15px 0;" +
            "margin: 5px 15px}" +
            "*:hover{background: '#FED7BE';}"
        )
        button.clicked.connect(self.upload_button)
        # 直接等于函数名字，即可应用函数，不需要加括号

        # Create a BUTTON2 WIDGET for output the answer, and the corresponding question.
        button2 = QPushButton("OUTPUT")
        button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button2.setStyleSheet(
            "*{border: 6px solid '#FED7BE';" +
            "border-radius: 60px;" +
            "font-size: 30px;" +
            "color: 'white';" +
            "padding: 15px 0;" +
            "margin: 5px 15px}" +
            "*:hover{background: '#FED7BE';}"
        )
        button2.clicked.connect(self.on_click)

        # add the widget into layout
        layout.addWidget(logo)
        layout.addWidget(self.subjects_text)
        layout.addWidget(button)
        layout.addWidget(button2)

        main_frame = QWidget()
        self.setCentralWidget(main_frame)
        main_frame.setLayout(layout)

    def upload_button(self):
        subject_now = self.subjects_text.text()
        target_subject_list = subject_now.split(": ")
        if len(target_subject_list) == 2:
            target_subject = target_subject_list[1]
            # print(target_subject)
            image_file = QFileDialog.getOpenFileName(
                self, 'open file', '.../.../.../', 'Image files (*.jpg *jpeg *png)')
            # print(image_file)
            # print(image_file[0])
            image_file = str(image_file[0])
            if image_file != '':
                search_answer(image_file, target_subject)
        else:
            self.msg_box = QMessageBox(
                QMessageBox.Warning, 'ERROR', 'Please choose a subjects first')
            self.msg_box.exec_()

    @pyqtSlot()
    def on_click(self):
        if os.path.isfile("/Users/jack/Desktop/project/Examable.1.0/Output_Ans.pdf"):
            subprocess.call(('open', "/Users/jack/Desktop/project/Examable.1.0/Output_Ans.pdf",
                             "/Users/jack/Desktop/project/Examable.1.0/Output_Que.pdf"))
        else:
            self.msg_box = QMessageBox(
                QMessageBox.Warning, 'ERROR', 'No target answer yet')
            self.msg_box.setWindowIconText('􀇿')
            self.msg_box.exec_()

    def closeEvent(self, event):
        event.accept()
        # print('Window closed')
        if os.path.isfile("Output_Ans.pdf"):
            os.remove("Output_Ans.pdf")
        # if the Output_Ans is exist, so remove it, else close directly

    def processtrigger(self, q):
        # print(q.text() + " is triggered")
        current_subject = q.text()
        self.subjects_text.setText("Current subject is: " + current_subject)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

# /Users/jack/Desktop/project/Examable.1.0/搜题题库/9709.ans/9709_m18_ms_42.pdf
