from PyQt6 import QtCore, QtGui, QtWidgets
from parser import Parser
import base64
import result_ui as r_ui
from translating import translate
from history import Ui_history
from database import Db


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        MainWindow.setStyleSheet("background-color: rgb(231, 247, 109);\n"
                                 "color:rgb(32,48,64);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 800, 1441, 101))
        self.label.setStyleSheet("background-color: rgb(32, 48, 64);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(440, 50, 531, 81))
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(90)
        self.logo.setFont(font)
        self.logo.setStyleSheet("color:rgb(32,48,64);")
        self.logo.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.logo.setObjectName("logo")
        self.history_bttn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.history_bttn.setGeometry(QtCore.QRect(30, 30, 111, 91))
        self.history_bttn.setStyleSheet("image: url(icons/icon1.png);\n"
                                        "border: none;\n"
                                        "outline: none;")
        self.history_bttn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.history_bttn.setText("")
        self.history_bttn.setObjectName("history_bttn")
        self.new_bttn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.new_bttn.setGeometry(QtCore.QRect(610, 280, 181, 151))
        self.new_bttn.setStyleSheet("image: url(icons/icon2.png);\n"
                                    "border: none;\n"
                                    "outline: none;")
        self.new_bttn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.new_bttn.setText("")
        self.new_bttn.setObjectName("new_bttn")
        self.history_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.history_label.setGeometry(QtCore.QRect(20, 120, 181, 21))
        self.history_label.setStyleSheet("font: 16pt \"DIN Alternate\";")
        self.history_label.setObjectName("history_label")
        self.new_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.new_label.setGeometry(QtCore.QRect(610, 450, 271, 21))
        self.new_label.setStyleSheet("font: 24pt \"DIN Alternate\";")
        self.new_label.setObjectName("new_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.new_bttn.clicked.connect(self.showImageFileDialog)
        self.history_bttn.clicked.connect(self.showHistoryDialog)

        self.db = Db()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MathSnapApp"))
        self.logo.setText(_translate("MainWindow", "MathSnapApp"))
        self.history_label.setText(_translate("MainWindow", "История уравнений"))
        self.new_label.setText(_translate("MainWindow", "Решить уравнение"))

    def showImageFileDialog(self):
        try:
            filePath, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Выберите изображение", "",
                                                                "Images (*.png *.jpg *.bmp *.gif);;All Files (*)")
            print(filePath)
            result = ''
            if filePath:
                with open(filePath, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                    parser = Parser(encoded_string)
                    equ = parser.get_equation()
                    result = parser.run_solve(equation=equ)
                    image_file.close()

            if result:
                self.db.add_to_db(str(equ), str(result))
                self.show_result_window(result, filePath)

        except Exception as e:
            self.show_result_window(res=str(translate(str(e))))

    def show_result_window(self, res, path=None):
        if path:
            self.res_ui = r_ui.Ui_result_ui(res, path)

        else:
            self.res_ui = r_ui.Ui_result_ui(res)

        self.res_ui.show()

    def showHistoryDialog(self):
        self.history = Ui_history()
        self.history.show()
