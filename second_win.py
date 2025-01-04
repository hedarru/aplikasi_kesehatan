# write a code for the second app
from PyQt5.QtCore import Qt  # alignment
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        # init object
        # Qlabel
        self.label_name = QLabel(txt_name)
        self.label_umur = QLabel(txt_age)
        self.label_ins1 = QLabel(txt_test1)
        self.label_ins2 = QLabel(txt_test2)
        self.label_ins3 = QLabel(txt_test3)
        self.label_timer = QLabel(txt_timer)

        # QLineEdit
        self.edit_name = QLineEdit(txt_hintname)
        self.edit_age = QLineEdit(txt_hintage)
        self.edit_tes1 = QLineEdit(txt_hinttest1)
        self.edit_tes2 = QLineEdit(txt_hinttest2)
        self.edit_tes3 = QLineEdit(txt_hinttest3)
        # QPushButton
        self.button_test1 = QPushButton(txt_starttest1)
        self.button_test1 = QPushButton(txt_starttest2)
        self.button_test1 = QPushButton(txt_starttest3)
        self.button_next = QPushButton(txt_sendresults)

        # init main layout
        self.layout_kiri = QVBoxLayout()
        self.layout_kiri.addWidget(self.label_name)
        self.layout_kiri.addWidget(self.edit_name)
        self.layout_kiri.addWidget(self.label_umur)
        self.layout_kiri.addWidget(self.edit_age)
        self.layout_kiri.addWidget(self.label_ins1)
        self.layout_kiri.addWidget(self.button_test1)
        self.layout_kiri.addWidget(self.edit_tes1)
        self.layout_kiri.addWidget(self.label_ins2)
        self.layout_kiri.addWidget(self.button_test2)
        self.layout_kiri.addWidget(self.edit_tes2)
        self.layout_kiri.addWidget(self.label_ins3)
        self.layout_kiri.addWidget(self.button_test3)
        self.layout_kiri.addWidget(self.edit_tes3)
        self.layout_kiri.addWidget(self.button_next, alignment=Qt.AlignCenter)

        # set main layout
        self.layout = QHBoxLayout
        self.layout.addLayout(self.layout_kiri)
        self.layout.addWidget(self.label_timer)

        self.setLayout(self.layout)
    def connects(self):
        self.button_next.clicked.connect(self.next_click)

    def next_click(self):
        print('screen ketiga')
        self.hide()
        self.tw = TestWin() # pindah next page