import PyQt6
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
import main_menu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = main_menu.Ui_MainWindow()
        self.main_window.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
