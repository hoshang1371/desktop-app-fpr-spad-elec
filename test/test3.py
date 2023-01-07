from PyQt5 import QtCore
# import pyautogui
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
# import pyautogui
from pynput.mouse import Button, Controller

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
							QHBoxLayout, QVBoxLayout, QMainWindow, QSizeGrip

class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.gripSize = 16
        self.grips = []
        for i in range(4):
            grip = QSizeGrip(self)
            grip.resize(self.gripSize, self.gripSize)
            self.grips.append(grip)

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        rect = self.rect()
        # top left grip doesn't need to be moved...
        # top right
        self.grips[1].move(rect.right() - self.gripSize, 0)
        # bottom right
        self.grips[2].move(
            rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        # bottom left
        self.grips[3].move(0, rect.bottom() - self.gripSize)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Main()
    w = QtWidgets.QMainWindow()
    # ex.setupUi(w)
    w.show()
    
    sys.exit(app.exec_())
