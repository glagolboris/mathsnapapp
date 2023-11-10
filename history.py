from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from database import Db
from PyQt6.QtWidgets import QListWidgetItem
import result_ui


class Ui_history(QMainWindow):
    def __init__(self):
        super(Ui_history, self).__init__()
        self.db = Db()
        self.setObjectName("history")
        self.resize(480, 640)
        self.setStyleSheet("background-color: rgb(231, 247, 109);")
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.history_logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.history_logo.setGeometry(QtCore.QRect(180, 10, 111, 51))
        self.history_logo.setStyleSheet("color:rgb(32,48,64);\n"
                                        "font: 30pt \"DIN Alternate\";")
        self.history_logo.setObjectName("history_logo")
        self.history_list = QtWidgets.QListWidget(parent=self.centralwidget)
        self.history_list.setGeometry(QtCore.QRect(40, 70, 411, 491))
        self.history_list.setObjectName("history_list")
        self.history_list.setStyleSheet("background-color: rgb(227, 229, 92);\n"
                                        "color: rgb(14, 11, 5);\n"
                                        "selection-background-color: rgb(210, 204, 16);\n"
                                        "font: 15pt \"DIN Alternate\";")
        self.clear_lable = QtWidgets.QLabel(parent=self.centralwidget)
        self.clear_lable.setGeometry(QtCore.QRect(205, 610, 111, 16))
        self.clear_lable.setObjectName("clear_lable")
        self.clear_lable.setStyleSheet('color:rgb(32,48,64);')
        self.clear_bttn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clear_bttn.setGeometry(QtCore.QRect(180, 570, 111, 41))
        self.clear_bttn.setStyleSheet("image: url(icon3.png);\n"
                                      "border: none;\n"
                                      "outline: none;")
        self.clear_bttn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.clear_bttn.setText("")

        self.clear_bttn.setObjectName("clear_bttn")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.updateItems()

        self.history_list.itemDoubleClicked.connect(self.itemClicked)
        self.clear_bttn.clicked.connect(self.clearall)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("history", "История решений"))
        self.history_logo.setText(_translate("history", "История"))
        self.clear_lable.setText(_translate("history", "Очистить"))

    def clearall(self):
        self.db.clearAll()
        self.history_list.clear()

    def itemClicked(self, item):
        textItem = item.text()
        self.res_ui = result_ui.Ui_result_ui(result=self.db.getSolution(textItem))
        self.res_ui.show()

    def updateItems(self):
        for elem in self.db.getEquationList()[::-1]:
            self.history_list.addItem(QListWidgetItem(elem[0]))
