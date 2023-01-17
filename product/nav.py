from importerProduct import *

def nav(self):
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 200))
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
        # self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4 = Frame(self.frame_2)
        self.frame_4.setStyleSheet(
            "border-image: url(:/product_list/noun-list-product-3434625.svg);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        # self.frame_4.clicked.connect(lambda: print("frame_4 is ok"))
        self.frame_4.clicked.connect(self.ProductList)

        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet(
            "border-image: url(:/calender/noun-calender-3455260.svg);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        return self.frame_2
  