from PyQt6 import QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore


class Ui_result_ui(QWidget):
    def __init__(self, result, path=None):
        super(Ui_result_ui, self).__init__()
        self.setObjectName("result_ui")
        self.resize(800, 600)
        self.setStyleSheet("background-color: rgb(231, 247, 109);")
        self.result_logo = QtWidgets.QLabel(parent=self)
        self.result_logo.setGeometry(QtCore.QRect(290, 0, 241, 111))
        self.result_logo.setStyleSheet("color:rgb(32,48,64);\n"
                                       "font: 50pt \"DIN Alternate\";")
        self.result_logo.setObjectName("result_logo")
        self.result_label = QtWidgets.QLabel(parent=self)
        self.result_label.setGeometry(QtCore.QRect(60, 450, 681, 71))
        font = QtGui.QFont()
        font.setFamily("DIN Alternate")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.result_label.setFont(font)
        self.result_label.setStyleSheet("color:rgb(32,48,64);\n"
                                        "font: 40pt \"DIN Alternate\";")
        self.result_label.setObjectName("result_label")

        if path:
            self.result_label = QtWidgets.QLabel(parent=self)
            self.result_label.setGeometry(QtCore.QRect(60, 450, 681, 71))
            font = QtGui.QFont()
            font.setFamily("DIN Alternate")
            font.setPointSize(40)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            self.result_label.setFont(font)
            self.result_label.setStyleSheet("color:rgb(32,48,64);\n"
                                            "font: 40pt \"DIN Alternate\";")
            self.result_label.setObjectName("result_label")
            self.label = QtWidgets.QLabel(parent=self)
            self.label.setGeometry(QtCore.QRect(60, 100, 651, 301))
            self.label.setStyleSheet("")
            self.label.setText("")
            self.label.setObjectName("label")
            pixmap = QPixmap(path)
            pic = pixmap.scaled(512, 256)

            self.label.setPixmap(pic)

        else:
            self.result_label = QtWidgets.QLabel(parent=self)
            self.result_label.setGeometry(QtCore.QRect(60, 100, 651, 301))
            font = QtGui.QFont()
            font.setFamily("DIN Alternate")
            font.setPointSize(40)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(50)
            self.result_label.setFont(font)
            self.result_label.setStyleSheet("color:rgb(32,48,64);\n"
                                            "font: 40pt \"DIN Alternate\";")
            self.result_label.setObjectName("result_label")

        self.retranslateUi(self, result)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, result_ui, res):
        _translate = QtCore.QCoreApplication.translate
        result_ui.setWindowTitle(_translate("result_ui", "Form"))
        self.result_logo.setText(_translate("result_ui", "Результат"))
        self.result_label.setText(_translate("result_ui", res))
