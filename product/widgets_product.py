from PyQt5.QtWidgets import (
                            QLineEdit,
                            QWidget,
                            QFrame,
                            )
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtCore import QPoint
from PyQt5 import QtCore, QtGui, QtWidgets


class MyLineEdit(QLineEdit):

    def __init__(self, parent):

        super(MyLineEdit, self).__init__(parent)
        self.parentWindow = parent
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        # print('forwarding to the main window')
        if event.button() == Qt.LeftButton: 
            self.clicked.emit()
            # print('left')
        self.parentWindow.mousePressEvent(event)

 

class FormWidget(QWidget):
    def __init__(self, parent, MainWindow):
        super(FormWidget, self).__init__(parent)
    #   #*push button
        self.mainWindow = MainWindow

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.mainWindow.move(self.mainWindow.x() + delta.x(),
                             self.mainWindow.y() + delta.y())
        self.oldPosition = event.globalPos()




class SideGrip(QtWidgets.QWidget):
    def __init__(self, parent, edge):
        super(SideGrip, self).__init__(parent)
        if edge == QtCore.Qt.LeftEdge:
            self.setCursor(QtCore.Qt.SizeHorCursor)
            self.resizeFunc = self.resizeLeft
        elif edge == QtCore.Qt.TopEdge:
            self.setCursor(QtCore.Qt.SizeVerCursor)
            self.resizeFunc = self.resizeTop
        elif edge == QtCore.Qt.RightEdge:
            self.setCursor(QtCore.Qt.SizeHorCursor)
            self.resizeFunc = self.resizeRight
        else:
            self.setCursor(QtCore.Qt.SizeVerCursor)
            self.resizeFunc = self.resizeBottom
        self.mousePos = None

    def resizeLeft(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() - delta.x())
        geo = window.geometry()
        geo.setLeft(geo.right() - width)
        window.setGeometry(geo)

    def resizeTop(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() - delta.y())
        geo = window.geometry()
        geo.setTop(geo.bottom() - height)
        window.setGeometry(geo)

    def resizeRight(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() + delta.x())
        window.resize(width, window.height())

    def resizeBottom(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() + delta.y())
        window.resize(window.width(), height)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.mousePos = event.pos()

    def mouseMoveEvent(self, event):
        if self.mousePos is not None:
            delta = event.pos() - self.mousePos
            self.resizeFunc(delta)

    def mouseReleaseEvent(self, event):
        self.mousePos = None

class Frame(QFrame):

    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton: 
            self.clicked.emit()



