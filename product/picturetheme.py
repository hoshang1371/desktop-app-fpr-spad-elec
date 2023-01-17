from importerProduct import *

def picAdder(self):
        self.frameRight = QtWidgets.QFrame(self.frame)
        self.frameRight.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frameRight.setStyleSheet("border: 1px solid black;")
        self.frameRight.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRight.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameRight.setObjectName("frameRight")
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

        return self.frameRight
