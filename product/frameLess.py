from importerProduct import *

def frameLessFrame(self,MainWindow):   
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

        return self.frame_9
