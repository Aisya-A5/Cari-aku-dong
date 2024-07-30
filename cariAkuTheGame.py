
import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from cari_aku_dong import *

class GuessingGame(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        #window icon
        self.icon = QIcon('cari_aku.jpg')  
        self.setWindowIcon(self.icon)

        # Initialize game variables
        self.tombol_bener = random.randint(0, 8)  # Randomly select a button
        self.percobaan = 0

        # Connect button clicks to the handler function
        self.ui.pushButton_1.clicked.connect(lambda: self.handle_button_click(0))
        self.ui.pushButton_2.clicked.connect(lambda: self.handle_button_click(1))
        self.ui.pushButton_3.clicked.connect(lambda: self.handle_button_click(2))
        self.ui.pushButton_4.clicked.connect(lambda: self.handle_button_click(3))
        self.ui.pushButton_5.clicked.connect(lambda: self.handle_button_click(4))
        self.ui.pushButton_6.clicked.connect(lambda: self.handle_button_click(5))
        self.ui.pushButton_7.clicked.connect(lambda: self.handle_button_click(6))
        self.ui.pushButton_8.clicked.connect(lambda: self.handle_button_click(7))
        self.ui.pushButton_9.clicked.connect(lambda: self.handle_button_click(8))
        self.ui.btn_lanjut.clicked.connect(lambda: self.start_over())

        # Initialize the dialog text
        self.update_dialog()
        
    def update_button_text(self, idx):
        tombol = getattr(self.ui, f'pushButton_{idx + 1}')
        tombol_salah_style = """
            QPushButton {
                background-color: #8A0303;
                color: white;
                text-align: center;
                text-decoration: none;
            }
            QPushButton:hover {
                background-color: #4B0101;
            }
            """
        tombol.setStyleSheet(tombol_salah_style)
        tombol.setText("Bukan")
        tombol.setEnabled(False)

    def handle_button_click(self, idx):
        self.percobaan += 1
        if idx == self.tombol_bener:
            self.update_dialog(f'Hebat, hanya {self.percobaan} percobaan!')
            button = getattr(self.ui, f'pushButton_{self.tombol_bener+1}')
            button.setStyleSheet("QPushButton{background-color: green; color: white}")
            button.setText(":)")
            self.disable_buttons()

        elif self.percobaan >= 8:
            self.disable_buttons()
            self.ui.dialog.setText("Kamu gagal...")
            tombol = getattr(self.ui, f'pushButton_{self.tombol_bener+1}')
            tombol.setStyleSheet("QPushButton{background-color: white; color: black}")
            tombol.setText(":(")

        else:
            self.update_dialog(f'cari lagi! Percobaan: {self.percobaan}')
            self.update_button_text(idx)

    def update_dialog(self, text=None):
        if text:
            self.ui.dialog.setText(text)
        else:
            self.ui.dialog.setText("Cari aku dengan 8 percobaan")


    def disable_buttons(self):
        for i in range(1, 10):
            button = getattr(self.ui, f'pushButton_{i}')
            button.setEnabled(False)

    def start_over(self):
        self.tombol_bener = random.randint(0, 8)
        self.percobaan = 0
        self.ui.dialog.setText("Cari aku dengan\n 8 percobaan!")
        tombol_normal_style = """
        QPushButton {
                background-color: white;
                border: none;
                color: white;
                text-align: center;
                text-decoration: none;
                }
                """

        for i in range(1, 10):
            button = getattr(self.ui, f'pushButton_{i}')
            button.setText("")
            button.setStyleSheet(tombol_normal_style)
            button.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GuessingGame()
    window.show()
    sys.exit(app.exec_())
