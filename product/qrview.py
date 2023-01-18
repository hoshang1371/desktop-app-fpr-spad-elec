from importerProduct import *
 
def qrViewCreator(self):
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
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.qrLabel = QtWidgets.QLabel('This is qrLabel' ,self.frameQrcode)
        self.qrLabel.setAlignment(Qt.AlignCenter)
        self.qrTitle = QtWidgets.QLineEdit(self.frameQrcode)
        self.qrTitle.setGeometry(QtCore.QRect(40, 0, 170, 50))
        self.qrTitle.setStyleSheet("border-radius: 25px;\n" "border: 1px solid black;")
        self.qrTitle.setObjectName("QrTitle")
        self.qrTitle.setAlignment(Qt.AlignCenter)
        self.qrTitle.returnPressed.connect(self.handleTextEntered)
        self.verticalLayout_9.addWidget(self.qrLabel)
        self.verticalLayout_9.addWidget(self.qrTitle)
        return self.frameQrcode

