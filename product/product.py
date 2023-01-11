from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import icons
from widgets_product import MyLineEdit, FormWidget, SideGrip, Frame, Image

import os
from PyQt5.QtGui import QPixmap, QImage, QPainter

from PyQt5.QtWidgets import (
    QLineEdit,
    QMainWindow,
    QFileDialog,
    QWidget,
)

from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal, Qt)

import threading
import socket
import qrcode

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


from network.network import Network
from extention.massegeBox import addProductSuccesMessege,notEnteredMessege,\
                                 isEmpty,notEnterednumber


stop_threads =False
dataGetFromscript =""



class Main(QMainWindow):
    _gripSize = 8

    def __init__(self):
        super().__init__()
        # w = QtWidgets.QMainWindow()
        # ex.setupUi(w)
        # w.show()
        self.setupUi(self)
        self.picDirectory =""
        # # # showing all the widgets
        self.show()
        # self.thr = threading.Thread(target=network.server)


    def setupUi(self, MainWindow):
        # MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(897, 654)
        MainWindow.resize(980, 654)
        MainWindow.setMinimumSize(QtCore.QSize(897, 0))
        MainWindow.setStyleSheet("background-color: rgb(255, 85, 0);")
        #!
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # MainWindow.setWindowOpacity(0.5)
        MainWindow.setAttribute(QtCore.Qt.WA_NoSystemBackground)

        MainWindow.setMouseTracking(True)
        MainWindow.setContentsMargins(0, 0, 0, 0)

        self.sideGrips = [
            SideGrip(self, QtCore.Qt.LeftEdge),
            SideGrip(self, QtCore.Qt.TopEdge),
            SideGrip(self, QtCore.Qt.RightEdge),
            SideGrip(self, QtCore.Qt.BottomEdge),
        ]

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setContentsMargins(0, 0, 0, 0)
        # self.form_widget1 = FormWidget(self,MainWindow) #addWidget setContentsMargins

        # self.form_widget1.setStyleSheet("""
        #         background-color: red;
        # """)

        # self.centralwidget(self.form_widget1)

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
        # *push button
        # self.pushButton = QtWidgets.QPushButton(self.frame_7)
        # self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        # self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        # self.pushButton.setStyleSheet("border: none;")
        # self.pushButton.setText("")
        # self.pushButton.setObjectName("pushButton")
        # * print_btn():
        # self.pushButton.pressed.connect(lambda: self.move_window_btn(MainWindow))
        # self.pushButton.released.connect(lambda: self.mouseReleaseEvent(MainWindow))
        self.form_widget = FormWidget(self, MainWindow)

        # self.horizontalLayout.addWidget(self.form_widget)
        # self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayout_2.addWidget(self.form_widget)

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

        self.minimize_btn.clicked.connect(self.showMinimized)

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
                                        "border-image: url(:/box/box.svg);\n"
                                        "}\n"

                                        # "QPushButton[img=\"0\"]{\n"
                                        #     "border-image: url(:/full screen/noun-full-screen-1222772.svg);\n"
                                        # "}\n"
                                        # "QPushButton[img=\"1\"]{\n"
                                        #     "border-image: url(:/box/box.svg);\n"
                                        #     "margin: 7;\n"
                                        # "}\n"
                                        "")

        # self.maximaze_btn.setProperty("img", "1")
        self.maximaze_btn.setText("")
        self.maximaze_btn.setObjectName("maximaze_btn")

        # self.maximaze_btn.clicked.connect(self.showMaximized)
        # self.maximaze_btn.clicked.connect(self.showFullScreen)
        self.maximaze_btn.clicked.connect(self.changeWindow)
        # self.maximaze_btn.hide()

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
        # self.frame_2.setMaximumSize(QtCore.QSize(16777215, 200))
        
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("background-color: rgb(161, 164, 224);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(40)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # self.frame_6 = QtWidgets.QFrame(self.frame_2)

        self.frame_6 =Frame(self.frame_2)
        
        self.frame_6.setStyleSheet(
            "border-image: url(:/product details/noun-product-detail-3480441.svg);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        
        self.frame_6.clicked.connect(self.addProduct)


        self.horizontalLayout_3.addWidget(self.frame_6)
        # self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5 = Frame(self.frame_2)
        self.frame_5.setStyleSheet(
            "border-image: url(:/qr code /noun-qr-code-1216158.svg);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")

        self.frame_5.clicked.connect(self.qrCodeclicked)
        
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
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        # self.horizontalLayout_4.hide()

        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_8.setStyleSheet("")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")

        # self.frame_8.hide()
        # self.frameRight.hide()
        # self.frame_8.show()

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
        self.cornerGrips = [QtWidgets.QSizeGrip(self) for i in range(4)]
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
        #ToDo add unclickable
        # self.tc = wx.TextCtrl(self.parent, -1, str(field[con.ConfigFields.VALUE]), pos=(x+220, y-3), size=(200, -1))
        self.description = MyLineEdit(self.frame_30)
        # self.description.mousePressed[QtGui.QMouseEvent].connect(self.mousePressEvent)
        # self.description.mousePressEvent[QtGui.QMouseEvent].connect(self.desc)
        self.description.clicked.connect(lambda: self.desc(self.description))
        # self.description = QtWidgets.QLineEdit(self.frame_30)
        self.description.setGeometry(QtCore.QRect(40, 0, 170, 50))
        self.description.setStyleSheet("border-radius: 25px;\n"
                                       "border: 1px solid black;")
        self.description.setObjectName("description")
        # self.description.setText("hhhhhh")

        # self.description.clicked.connect(self.desc)
        # .clicked.connect(self.browsImage)

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
        #ToDo

        self.smallDescription = MyLineEdit(self.frame_28)
        # self.smallDescription = QtWidgets.QLineEdit(self.frame_28)
        self.smallDescription.setGeometry(QtCore.QRect(40, 0, 170, 50))
        self.smallDescription.setStyleSheet("border-radius: 25px;\n"
                                            "border: 1px solid black;")
        self.smallDescription.setObjectName("smallDescription")
        # d= self.smallDescription
        # print(self.smallDescription.objectName())
        # self.smallDescription.getObjectName
        self.smallDescription.clicked.connect(lambda: self.desc(self.smallDescription))
        # self.smallDescription.clicked.connect(lambda: print('ok'))
        #********************
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
#!
        # self.frameRight.hide()
        # self.frame_8.hide()
        # self.scrollArea.hide()
        # self.scrollAreaWidgetContents_5.hide()
        # self.frameQrcode.hide() self.scrollArea.setWidgetResizable(True)
#*=========================================================================
        self.frameQrcode = QtWidgets.QFrame(self.frame)
        self.frameQrcode.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frameQrcode.setStyleSheet("border: 1px solid black;")
        self.frameQrcode.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameQrcode.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameQrcode.setObjectName("frameQrcode")
        
        self.scrollArea_Qr = QtWidgets.QScrollArea(self.frameQrcode)
        self.scrollArea_Qr.setWidgetResizable(True)
        self.scrollArea_Qr.setObjectName("scrollArea_Qr")
        self.frameQrcode.hide()

        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frameQrcode)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.verticalLayout_8.addWidget(self.scrollArea_Qr)


        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollArea_Qr)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_8")

        self.qrLabel = QtWidgets.QLabel('This is qrLabel' ,self.frameQrcode)
        self.qrLabel.setAlignment(Qt.AlignCenter)
        self.qrTitle = QtWidgets.QLineEdit(self.frameQrcode)
        self.qrTitle.setGeometry(QtCore.QRect(40, 0, 170, 50))
        self.qrTitle.setStyleSheet("border-radius: 25px;\n"
                                    "border: 1px solid black;")
        self.qrTitle.setObjectName("QrTitle")
        self.qrTitle.setAlignment(Qt.AlignCenter)

        self.qrTitle.returnPressed.connect(self.handleTextEntered)

        self.verticalLayout_9.addWidget(self.qrLabel)
        self.verticalLayout_9.addWidget(self.qrTitle)

 
#*=========================================================================
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frameRight)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_11 = QtWidgets.QFrame(self.frameRight)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pic = QtWidgets.QLabel(self.frame_11)
        self.pic.setText("")
        self.pic.setObjectName("pic")
        self.verticalLayout_7.addWidget(self.pic)
        self.verticalLayout_6.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frameRight)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.addPic = QtWidgets.QPushButton(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        self.addPic.setFont(font)
        self.addPic.setStyleSheet("QPushButton:hover[objectName^=\"addPic\"]{\n"
                                  "background-color: rgb(228, 226, 255);\n"
                                  "}\n"
                                  "QPushButton:pressed[objectName^=\"addPic\"]{\n"
                                  "background-color: rgb(161, 164, 224);\n"
                                  "color: black;\n"
                                  "}")
        self.addPic.setObjectName("addPic")
        self.addPic.clicked.connect(self.browsImage) 
        # self.addPic.clicked.connect(lambda: self.browsImage())

        self.horizontalLayout_7.addWidget(self.addPic)
        self.send = QtWidgets.QPushButton(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Mikhak Medium")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.send.setFont(font)
        self.send.setStyleSheet("QPushButton:hover[objectName^=\"send\"]{\n"
                                "background-color: rgb(226, 255, 213);\n"
                                "}\n"
                                "QPushButton:pressed[objectName^=\"send\"]{\n"
                                "background-color: rgb(0, 170, 0);\n"
                                "color: black;\n"
                                "}")
        self.send.setObjectName("send")
        self.send.clicked.connect(self.sendProduct)

        self.horizontalLayout_7.addWidget(self.send)
        self.verticalLayout_6.addWidget(self.frame_12)
#*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.horizontalLayout_4.addWidget(self.frameRight)
        self.horizontalLayout_4.addWidget(self.frameQrcode)
#*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_41.setText(_translate("MainWindow", "عنوان"))
        self.label_46.setText(_translate("MainWindow", "کد"))
        self.label_45.setText(_translate("MainWindow", "مکان کالا"))
        self.label_44.setText(_translate("MainWindow", "تعداد"))
        self.label_43.setText(_translate("MainWindow", "برند"))
        self.label_42.setText(_translate("MainWindow", "توضیحات"))
        self.label_40.setText(_translate("MainWindow", "توضیحات کوتاه"))
        self.label_47.setText(_translate("MainWindow", "قیمت"))
        self.label_48.setText(_translate("MainWindow", "قیمت تخفیف"))
        self.label_49.setText(_translate("MainWindow", "فعال"))
        self.label_50.setText(_translate("MainWindow", "ویژه"))
        self.addPic.setText(_translate("MainWindow", "افزودن عکس"))
        self.send.setText(_translate("MainWindow", "ارسال"))

    def desc(self ,child):
        # global dataGetFromscript
        # print(dataGetFromscript)
        # # global data
        # print("dis")
        # print(data)
        # self.description.setText(str(data))

        network = NetworkServer(self,child)
        threading.Thread(target=network.server).start()
        # try:
        #     self.smallDescription.clicked.disconnect()
        #     self.description.clicked.disconnect()
        # except:
        #     pass
        print("endof thread")
        # a.start()
        # a.join() 
        # self.thr.start()
        print(child.objectName())
        if child.objectName() == 'description':
            os.system('python product\descript.py توضیحات')
        elif child.objectName() == 'smallDescription':
            os.system('python product\descript.py توضیحات کوتاه ')
        # print(a.)

    def closButtonClicked_exit(self):
        global stop_threads
        stop_threads =True
        print("exit")
        sys.exit()

    def changeWindow(self):
        if self.isMaximized():
            self.showNormal()
            # self.maximaze_btn.setProperty("img", "1")
        else:
            self.showMaximized()
            # self.maximaze_btn.setProperty("img", "0")

    def browsImage(self):
        print("every tink is Ok")
        fname = QFileDialog.getOpenFileName(
            self, 'open File', 'c\\', 'Image files (*.jpg *.gif)')
        imagePath = fname[0]
        self.picDirectory = imagePath
        # print(fname)
        # with open(imagePath, 'rb') as f:
        #     img = f.read()
        # print(img)
        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        # self.resize(pixmap.width(), pixmap.height())
        self.pic.setPixmap(QPixmap(pixmap))

    def setEmptyProduct(self):
        self.title.setText("")
        self.code.setText(""),
        self.place.setText(""),
        self.number.setText(""),
        self.brand.setText(""),
        self.description.setText(""),
        self.smallDescription.setText(""),
        self.price.setText(""),
        self.priceOff.setText(""),#
        self.active.setChecked(False)
        self.vige.setChecked(False)

        # pixmap = QPixmap(imagePath)
        # pixmap = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        # self.resize(pixmap.width(), pixmap.height())
        self.pic.setPixmap(QtGui.QPixmap())

    def sendProduct(self):

        if self.title.text() == "":
            notEnteredMessege("عنوان")
        elif self.code.text() == "":
            notEnteredMessege("کد")
        elif self.place.text() == "":
            notEnteredMessege("مکان کالا")
        elif self.number.text() == "":
            notEnteredMessege("تعداد")
        elif not self.number.text().isnumeric():
            notEnterednumber("تعداد")
        elif self.brand.text() == "":
            notEnteredMessege("برند")
        elif self.description.text() == "":
            notEnteredMessege("توضیحات")
        elif self.smallDescription.text() == "":
            notEnteredMessege("توضیحات کوتاه")
        elif self.price.text() == "":
            notEnteredMessege("قیمت")
        elif not self.price.text().isnumeric():
            notEnterednumber("قیمت")
        elif self.picDirectory == "":
            notEnteredMessege("عکس")
        elif not self.priceOff.text().isnumeric() and not self.priceOff.text() == "":
            notEnterednumber("قیمت تخفیف")
        elif self.priceOff.text() == "":
            isEmpty("قیمت تخفیف",
                    lambda:Network.post_product_data(
                                    self.title.text(),
                                    self.code.text(),
                                    self.place.text(),
                                    self.number.text(),
                                    self.brand.text(),
                                    self.description.text(),
                                    self.smallDescription.text(),
                                    self.price.text(),
                                    self.priceOff.text(),
                                    self.picDirectory,
                                    self.active.isChecked(),
                                    self.vige.isChecked()
                                    )
                    )
            self.setEmptyProduct()
                


        else:
            Network.post_product_data(
                                    self.title.text(),
                                    self.code.text(),
                                    self.place.text(),
                                    self.number.text(),
                                    self.brand.text(),
                                    self.description.text(),
                                    self.smallDescription.text(),
                                    self.price.text(),
                                    self.priceOff.text(),
                                    self.picDirectory,
                                    self.active.isChecked(),
                                    self.vige.isChecked()
                                    )
            self.setEmptyProduct()

    @property
    def gripSize(self):
        return self._gripSize

    # def setGripSize(self, size):
    #     if size == self._gripSize:
    #         return
    #     self._gripSize = max(2, size)
    #     self.updateGrips()

    def updateGrips(self):
        print("ok")
        # self.setContentsMargins(*[self.gripSize] * 4)
        self.setContentsMargins(3, 3, 3, 3)

        outRect = self.rect()
        # an "inner" rect used for reference to set the geometries of size grips
        inRect = outRect.adjusted(self.gripSize, self.gripSize,
                                  -self.gripSize, -self.gripSize)

        # top left
        self.cornerGrips[0].setGeometry(
            QtCore.QRect(outRect.topLeft(), inRect.topLeft()))

        self.cornerGrips[0].setStyleSheet("""
                background-color: transparent; 
        """)
        # top right
        self.cornerGrips[1].setGeometry(
            QtCore.QRect(outRect.topRight(), inRect.topRight()).normalized())

        self.cornerGrips[1].setStyleSheet("""
                background-color: transparent; 
        """)
        # bottom right
        self.cornerGrips[2].setGeometry(
            QtCore.QRect(inRect.bottomRight(), outRect.bottomRight()))
        self.cornerGrips[2].setStyleSheet("""
                background-color: transparent; 
        """)
        # bottom left
        self.cornerGrips[3].setGeometry(
            QtCore.QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized())
        self.cornerGrips[3].setStyleSheet("""
                background-color: transparent; 
        """)
        # left edge
        self.sideGrips[0].setGeometry(
            0, inRect.top(), self.gripSize, inRect.height())
        # top edge
        self.sideGrips[1].setGeometry(
            inRect.left(), 0, inRect.width(), self.gripSize)
        # right edge
        self.sideGrips[2].setGeometry(
            inRect.left() + inRect.width(),
            inRect.top(), self.gripSize, inRect.height())
        # bottom edge
        self.sideGrips[3].setGeometry(
            self.gripSize, inRect.top() + inRect.height(),
            inRect.width(), self.gripSize)

    def resizeEvent(self, event):
        print("ok")
        QtWidgets.QMainWindow.resizeEvent(self, event)
        self.updateGrips()


    def handleTextEntered(self):
 
        # get the text
        text = self.qrTitle.text()
        # self.qrLabel.setText(text)
                # creating a pix map of qr code
        qr_image = qrcode.make(text, image_factory = Image).pixmap()
 
        # set image to the label
        self.qrLabel.setPixmap(qr_image)
        print(text)

    def qrCodeclicked(self):
        self.frameRight.hide()
        self.frame_8.hide()
        self.frameQrcode.show()

    def addProduct(self):
        self.frameRight.show()
        self.frame_8.show()
        self.frameQrcode.hide()       

class NetworkServer(Main):#Main

    def __init__(self, parent, child):
        super(Main, self).__init__(parent)
        self.parentWindow = parent
        self.child = child
        # self.child.setText("dataGetFromscript")

    def server(self):
        s = socket.socket()        
        # print ("Socket successfully created")
        port = 54321               
        s.bind(('127.0.0.1', port))        
        # print ("socket binded to %s" %(port))
        s.listen(5)    
        # print ("socket is listening")           
        c, addr = s.accept() 
        finalData =''  
        # self.parentWindow.smallDescription.clicked.disconnect()
        # self.parentWindow.description.clicked.disconnect()
        # self.parentWindow.smallDescription.clicked.disconnect()
        while True:
            # print ('Got connection from', addr )
            data =c.recv(8)
            finalData +=str(data, 'UTF-8')#str(data, 'UTF-8')
            # print(data)
            if not data:
                # if data is not received break
                c.close()
                # print("from connected user: " + str(data))
                # print(type(data))
                print(f'finalData = {finalData}')
                # self.parentWindow.description.setText(finalData)
                self.child.setText(finalData)

                # self.parentWindow.description.clicked.connect(lambda: self.desc(self.parentWindow.smallDescription), QtCore.Qt.DirectConnection)
                # self.parentWindow.smallDescription.clicked.connect(lambda: self.desc(self.parentWindow.smallDescription), QtCore.Qt.DirectConnection)
                # self.parentWindow.smallDescription.clicked.connect(lambda: print("oklambda"), QtCore.Qt.DirectConnection)
                # self.parentWindow.description.setText(finalData)
                break
 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # w = QtWidgets.QMainWindow()
    # t2 = threading.Thread(target=server_start)#, args=(10,)
    # t2.start()
    # t2.join()
    stop_threads = False

    # thread = ServerThread()
    # thread.finished.connect(app.exit)
    # thread.start()
    ex = Main()
    # ex.description.setText('every thing ok')

    # network = NetworkServer(ex)
    # threading.Thread(target=network.server).start()
    

    # ex.setupUi(w)
    # w.show()
    sys.exit(app.exec_())
