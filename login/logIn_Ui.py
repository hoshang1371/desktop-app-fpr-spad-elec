
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import res
import requests
from network import Network

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 481))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("border-image: url(:/images/4419038.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 321, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setFamily("Mikhak Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 65))
        font = QtGui.QFont()
        font.setFamily("Mikhak Bold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 25px;\n"
                                    "border: 1px solid black;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 65))
        font = QtGui.QFont()
        font.setFamily("Mikhak Bold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 25px;\n"
                                      "border: 1px solid black;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        # self.lineEdit_2.setEchoMode(QLieEdit.Password)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setEnabled(True)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.hide()
        font = QtGui.QFont()
        font.setFamily("Mikhak Bold")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.frame_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 301, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 65))
        #* event
        self.pushButton_2.clicked.connect(self.buttonClicked_exit)
        font = QtGui.QFont()
        font.setFamily("Mikhak Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
                                        "QPushButton{\n"
                                        "border-radius: 25px;\n"
                                        "background-color: rgb(255, 0, 0);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(195, 37, 37);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: #e7e7e7; \n"
                                        "color: black;\n"
                                        "}\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setFamily("Mikhak Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "border-radius: 25px;\n"
                                      "background-color: rgb(62, 96, 168);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgb(51, 80, 138);\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "background-color: #e7e7e7; \n"
                                      "color: black;\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.buttonClicked_login)

        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def buttonClicked_exit(self):
        # sender = self.sender()
        print(self.lineEdit.text())
        print(self.lineEdit_2.text())
        sys.exit()

    def buttonClicked_login(self):
        #todo
        Network.post_login(email=self.lineEdit.text(),password=self.lineEdit_2.text())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "به فروشگاه اسپاد خوش آمدید."))
        self.lineEdit.setPlaceholderText(_translate("Form", "ایمیل"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "پسوورد"))
        self.label_3.setText(_translate(
            "Form", "اطلاعات وارد شده صحیح نمی باشد."))
        self.pushButton_2.setText(_translate("Form", "خروج"))
        self.pushButton.setText(_translate("Form", "ورود"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     ex = Ui_MainWindow()
#     w = QtWidgets.QMainWindow()
#     ex.setupUi(w)
#     w.show()
#     sys.exit(app.exec_())