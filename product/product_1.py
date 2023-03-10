# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import QPoint
import icons


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 654)
        MainWindow.setMinimumSize(QtCore.QSize(897, 0))
        MainWindow.setStyleSheet("background-color: rgb(255, 85, 0);")
        #!
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # MainWindow.setGeometry(0,0,100,500)
        # MainWindow.move(50, 50)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_9.setStyleSheet("background-color: rgb(112, 117, 102);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_9)
        self.frame_7.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_7)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton.setStyleSheet("border: none;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        #* print_btn():
        self.pushButton.clicked.connect(self.print_btn)

        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setMaximumSize(QtCore.QSize(110, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.minimize_btn = QtWidgets.QPushButton(self.frame_10)
        self.minimize_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.minimize_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.minimize_btn.setStyleSheet("QPushButton[objectName^=\"minimize_btn\"]{\n"
                                        "border-image: url(:/minimize/noun-minimize-2248799.svg);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover[objectName^=\"minimize_btn\"]{\n"
                                        "background-color: rgb(237, 221, 255);\n"
                                        "}\n"
                                        "QPushButton:pressed[objectName^=\"minimize_btn\"]{\n"
                                        "background-color: #e7e7e7; \n"
                                        "color: black;\n"
                                        "}\n"
                                        "")
        self.minimize_btn.setText("")
        self.minimize_btn.setObjectName("minimize_btn")
        self.horizontalLayout_6.addWidget(self.minimize_btn)
        self.maximaze_btn = QtWidgets.QPushButton(self.frame_10)
        self.maximaze_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.maximaze_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.maximaze_btn.setStyleSheet("QPushButton[objectName^=\"maximaze_btn\"]{\n"
                                        "border-image: url(:/full screen/noun-full-screen-1222772.svg);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover[objectName^=\"maximaze_btn\"]{\n"
                                        "background-color: rgb(237, 221, 255);\n"
                                        "}\n"
                                        "QPushButton:pressed[objectName^=\"maximaze_btn\"]{\n"
                                        "background-color: #e7e7e7; \n"
                                        "color: black;\n"
                                        "}\n"
                                        "")
        self.maximaze_btn.setText("")
        self.maximaze_btn.setObjectName("maximaze_btn")
        self.horizontalLayout_6.addWidget(self.maximaze_btn)
        self.close_btn = QtWidgets.QPushButton(self.frame_10)
        self.close_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.close_btn.setMaximumSize(QtCore.QSize(40, 40))

        # *event
        self.close_btn.clicked.connect(self.closButtonClicked_exit)

        font = QtGui.QFont()
        font.setFamily("Mikhak Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setStyleSheet("QPushButton[objectName^=\"close_btn\"]{\n"
                                     "border-image: url(:/close/noun-close-1146383.svg);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover[objectName^=\"close_btn\"]{\n"
                                     "background-color: rgb(255, 0, 0);\n"
                                     "}\n"
                                     "QPushButton:pressed[objectName^=\"close_btn\"]{\n"
                                     "background-color: #e7e7e7; \n"
                                     "color: black;\n"
                                     "}\n"
                                     "")
        self.close_btn.setText("")
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_6.addWidget(self.close_btn)
        self.horizontalLayout_2.addWidget(self.frame_10)
        self.verticalLayout.addWidget(self.frame_9)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_2.setStyleSheet("background-color: rgb(161, 164, 224);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(40, 40, 40, 40)
        self.horizontalLayout_3.setSpacing(40)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setStyleSheet(
            "border-image: url(:/product details/noun-product-detail-3480441.svg);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setStyleSheet(
            "border-image: url(:/qr code /noun-qr-code-1216158.svg);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet(
            "border-image: url(:/product_list/noun-list-product-3434625.svg);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet(
            "border-image: url(:/calender/noun-calender-3455260.svg);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 500))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setMaximumSize(QtCore.QSize(500, 500))
        self.frame_8.setStyleSheet("")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_8)
        self.scrollArea.setStyleSheet("\n"
                                      "/*vertical SCrollbar*/\n"
                                      "QScrollBar:vertical{\n"
                                      "border:none;\n"
                                      "background-color: rgb(161, 164, 224);\n"
                                      "width:14px;\n"
                                      "/*margin: 15px 0 15px 0;*/\n"
                                      "border-radius:0px\n"
                                      "}\n"
                                      "/* Handle Bar Vertiacal */\n"
                                      "\n"
                                      "QScrollBar::handle:vertical{\n"
                                      "background-color:  rgb(161, 164, 224);\n"
                                      "min-height: 30px;\n"
                                      "border-radius: 7px;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::handle:vertical:hover{\n"
                                      "background-color: rgb(255,0,127);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::handle:pressed{\n"
                                      "background-color: rgb(185,0,92);\n"
                                      "}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(
            QtCore.QRect(0, 0, 482, 642))
        self.scrollAreaWidgetContents_5.setObjectName(
            "scrollAreaWidgetContents_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_29 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_29.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_29.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.title = QtWidgets.QLineEdit(self.frame_29)
        self.title.setGeometry(QtCore.QRect(40, 0, 170, 50))
        self.title.setStyleSheet("border-radius: 25px;\n"
                                 "border: 1px solid black;")
        self.title.setObjectName("title")
        self.label_41 = QtWidgets.QLabel(self.frame_29)
        self.label_41.setGeometry(QtCore.QRect(310, 0, 91, 31))
        self.label_41.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_4.addWidget(self.frame_29)
        self.frame_34 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_34.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_34.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.code = QtWidgets.QLineEdit(self.frame_34)
        self.code.setGeometry(QtCore.QRect(40, 0, 170, 50))
        self.code.setStyleSheet("border-radius: 25px;\n"
                                "border: 1px solid black;")
        self.code.setObjectName("code")
        self.label_46 = QtWidgets.QLabel(self.frame_34)
        self.label_46.setGeometry(QtCore.QRect(320, 10, 91, 31))
        self.label_46.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_4.addWidget(self.frame_34)
        self.frame_33 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_33.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_33.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.place = QtWidgets.QLineEdit(self.frame_33)
        self.place.setGeometry(QtCore.QRect(40, 0, 170, 50))
        self.place.setStyleSheet("border-radius: 25px;\n"
                                 "border: 1px solid black;")
        self.place.setObjectName("place")
        self.label_45 = QtWidgets.QLabel(self.frame_33)
        self.label_45.setGeometry(QtCore.QRect(300, 10, 91, 31))
        self.label_45.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_45.setFont(font)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_4.addWidget(self.frame_33)
        self.frame_32 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_32.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_32.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.number = QtWidgets.QLineEdit(self.frame_32)
        self.number.setGeometry(QtCore.QRect(40, 0, 170, 50))
        self.number.setStyleSheet("border-radius: 25px;\n"
                                  "border: 1px solid black;")
        self.number.setObjectName("number")
        self.label_44 = QtWidgets.QLabel(self.frame_32)
        self.label_44.setGeometry(QtCore.QRect(310, 10, 91, 31))
        self.label_44.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_4.addWidget(self.frame_32)
        self.frame_31 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_31.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_31.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.brand = QtWidgets.QLineEdit(self.frame_31)
        self.brand.setGeometry(QtCore.QRect(40, 0, 170, 50))
        self.brand.setStyleSheet("border-radius: 25px;\n"
                                 "border: 1px solid black;")
        self.brand.setObjectName("brand")
        self.label_43 = QtWidgets.QLabel(self.frame_31)
        self.label_43.setGeometry(QtCore.QRect(320, 10, 91, 31))
        self.label_43.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_43.setFont(font)
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_4.addWidget(self.frame_31)
        self.frame_30 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_30.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_30.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.description = QtWidgets.QLineEdit(self.frame_30)
        self.description.setGeometry(QtCore.QRect(40, 0, 170, 50))
        self.description.setStyleSheet("border-radius: 25px;\n"
                                       "border: 1px solid black;")
        self.description.setObjectName("description")
        self.label_42 = QtWidgets.QLabel(self.frame_30)
        self.label_42.setGeometry(QtCore.QRect(290, 10, 91, 31))
        self.label_42.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_4.addWidget(self.frame_30)
        self.frame_28 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_28.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_28.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.smallDescription = QtWidgets.QLineEdit(self.frame_28)
        self.smallDescription.setGeometry(QtCore.QRect(40, 0, 170, 50))
        self.smallDescription.setStyleSheet("border-radius: 25px;\n"
                                            "border: 1px solid black;")
        self.smallDescription.setObjectName("smallDescription")
        self.label_40 = QtWidgets.QLabel(self.frame_28)
        self.label_40.setGeometry(QtCore.QRect(240, 10, 161, 31))
        self.label_40.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_4.addWidget(self.frame_28)
        self.frame_35 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_35.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_35.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.price = QtWidgets.QLineEdit(self.frame_35)
        self.price.setGeometry(QtCore.QRect(40, 0, 170, 50))
        self.price.setStyleSheet("border-radius: 25px;\n"
                                 "border: 1px solid black;")
        self.price.setObjectName("price")
        self.label_47 = QtWidgets.QLabel(self.frame_35)
        self.label_47.setGeometry(QtCore.QRect(320, 10, 91, 31))
        self.label_47.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_47.setFont(font)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_4.addWidget(self.frame_35)
        self.frame_36 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_36.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_36.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.priceOff = QtWidgets.QLineEdit(self.frame_36)
        self.priceOff.setGeometry(QtCore.QRect(40, 0, 170, 50))
        self.priceOff.setStyleSheet("border-radius: 25px;\n"
                                    "border: 1px solid black;")
        self.priceOff.setObjectName("priceOff")
        self.label_48 = QtWidgets.QLabel(self.frame_36)
        self.label_48.setGeometry(QtCore.QRect(270, 10, 141, 31))
        self.label_48.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_48.setFont(font)
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.verticalLayout_4.addWidget(self.frame_36)
        self.frame_37 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_37.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_37.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.label_49 = QtWidgets.QLabel(self.frame_37)
        self.label_49.setGeometry(QtCore.QRect(330, 10, 91, 31))
        self.label_49.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_49.setFont(font)
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.active = QtWidgets.QCheckBox(self.frame_37)
        self.active.setGeometry(QtCore.QRect(120, 10, 81, 20))
        self.active.setText("")
        self.active.setObjectName("active")
        self.verticalLayout_4.addWidget(self.frame_37)
        self.frame_38 = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_38.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_38.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.label_50 = QtWidgets.QLabel(self.frame_38)
        self.label_50.setGeometry(QtCore.QRect(320, 0, 91, 31))
        self.label_50.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_50.setFont(font)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.vige = QtWidgets.QCheckBox(self.frame_38)
        self.vige.setGeometry(QtCore.QRect(120, 10, 81, 20))
        self.vige.setText("")
        self.vige.setObjectName("vige")
        self.verticalLayout_4.addWidget(self.frame_38)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout_4.addWidget(self.frame_8)
        self.frameRight = QtWidgets.QFrame(self.frame)
        self.frameRight.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frameRight.setStyleSheet("border: 1px solid black;")
        self.frameRight.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRight.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameRight.setObjectName("frameRight")
        self.horizontalLayout_4.addWidget(self.frameRight)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_41.setText(_translate("MainWindow", "??????????"))
        self.label_46.setText(_translate("MainWindow", "????"))
        self.label_45.setText(_translate("MainWindow", "???????? ????????"))
        self.label_44.setText(_translate("MainWindow", "??????????"))
        self.label_43.setText(_translate("MainWindow", "????????"))
        self.label_42.setText(_translate("MainWindow", "??????????????"))
        self.label_40.setText(_translate("MainWindow", "?????????????? ??????????"))
        self.label_47.setText(_translate("MainWindow", "????????"))
        self.label_48.setText(_translate("MainWindow", "???????? ??????????"))
        self.label_49.setText(_translate("MainWindow", "????????"))
        self.label_50.setText(_translate("MainWindow", "????????"))

    def print_btn(self):
        print("ok")

    def closButtonClicked_exit(self):
        sys.exit()
        
     # action1

    def mousePressEvent(self, event):
        self.oldPsition = event.globalPos()
    # action2

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos - self.oldPsition)
        print(delta)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
