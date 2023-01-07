from PyQt5.QtWidgets import (
                            QApplication,
                            # QMainWindow,
                            QDialog,
                            QPushButton, 
                            QLabel,
                            QFileDialog,
                            QVBoxLayout, 
                            QWidget,
                            # QWizard
                            )
# from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = " PyWt5 QFileDialog "
        self.left  = 500
        self.top   = 200
        self.width = 300
        self.hight = 250
        # self.iconName = "home.png"

        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        # self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width,self.hight)
        vbox = QVBoxLayout()
        self.btn = QPushButton("Browse Image")
        self.btn.clicked.connect(self.browsImage) 
        vbox.addWidget(self.btn)

        self.label = QLabel("Hello")
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.show()

    def browsImage(self):
        fname = QFileDialog.getOpenFileName(self, 'open File', 'c\\', 'Image files (*.jpg *.gif)')

        imagePath = fname[0]
        print(fname)
        # with open(imagePath, 'rb') as f:
        #     img = f.read()
        # print(img)
        pixmap = QPixmap(imagePath)
        # self.scaledToWidth(64)
        # self.scaled(100, 100)
        pixmap = pixmap.scaled(64, 64, QtCore.Qt.KeepAspectRatio)
        self.resize(pixmap.width(), pixmap.height())
        self.label.setPixmap(QPixmap(pixmap))
        # self.resize(10, 10)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
