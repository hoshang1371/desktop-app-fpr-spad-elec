# import sys
# from PyQt5.QtWidgets import * 
                    
   
# #Main Window
# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 - QTableWidget'
#         self.left = 0
#         self.top = 0
#         self.width = 300
#         self.height = 200
   
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
   
#         self.createTable()
   
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.tableWidget)
#         self.setLayout(self.layout)
   
#         #Show window
#         self.show()
   
#     #Create table
#     def createTable(self):
#         self.tableWidget = QTableWidget()
  
#         #Row count
#         self.tableWidget.setRowCount(4) 
  
#         #Column count
#         self.tableWidget.setColumnCount(3)  
  
#         self.tableWidget.setItem(0,0, QTableWidgetItem("Name"))
#         self.tableWidget.setItem(0,1, QTableWidgetItem("City"))
#         self.tableWidget.setItem(1,0, QTableWidgetItem("Aloysius"))
#         self.tableWidget.setItem(1,1, QTableWidgetItem("Indore"))
#         self.tableWidget.setItem(2,0, QTableWidgetItem("Alan"))
#         self.tableWidget.setItem(2,1, QTableWidgetItem("Bhopal"))
#         self.tableWidget.setItem(3,0, QTableWidgetItem("Arnavi"))
#         self.tableWidget.setItem(3,1, QTableWidgetItem("Mandsaur"))
   
#         #Table will fit the screen horizontally
#         self.tableWidget.horizontalHeader().setStretchLastSection(True)
#         self.tableWidget.horizontalHeader().setSectionResizeMode(
#             QHeaderView.Stretch)
   
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())

#!====================================================================================
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot

# class App(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 table - pythonspot.com'
#         self.left = 0
#         self.top = 0
#         self.width = 300
#         self.height = 200
#         self.initUI()
        
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
        
#         self.createTable()

#         # Add box layout, add table to box layout and add box layout to widget
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.tableWidget) 
#         self.setLayout(self.layout) 

#         # Show widget
#         self.show()

#     def createTable(self):
#        # Create table
#         self.tableWidget = QTableWidget()
#         self.tableWidget.setRowCount(4)
#         self.tableWidget.setColumnCount(2)
#         self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
#         self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
#         self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
#         self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
#         self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
#         self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
#         self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
#         self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
#         self.tableWidget.move(0,0)

#         # table selection change
#         self.tableWidget.doubleClicked.connect(self.on_click)

#     @pyqtSlot()
#     def on_click(self):
#         print("\n")
#         for currentQTableWidgetItem in self.tableWidget.selectedItems():
#             print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_()) 
#!============================================
# from PyQt5 import QtCore, QtWidgets


# class Widget(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super(Widget, self).__init__(parent)
#         self.table_widget = QtWidgets.QTableWidget(4, 6)
#         self.spinbox = QtWidgets.QSpinBox()
#         self.le = QtWidgets.QLineEdit()
#         self.le.textChanged.connect(self.on_textChanged)
#         button = QtWidgets.QPushButton("Change")
#         button.clicked.connect(self.on_clicked)

#         lay = QtWidgets.QVBoxLayout(self)
#         hlay = QtWidgets.QHBoxLayout()
#         hlay.addWidget(self.spinbox)
#         hlay.addWidget(self.le)
#         hlay.addWidget(button)
#         lay.addWidget(self.table_widget)
#         lay.addLayout(hlay)

#     @QtCore.pyqtSlot(str)
#     def on_textChanged(self, text):
#         words = text.split(",")
#         n_words = len(words)
#         self.spinbox.setValue(n_words)

#     @QtCore.pyqtSlot()
#     def on_clicked(self):
#         words = self.le.text().split(",")
#         n_words = len(words)
#         if n_words > self.table_widget.columnCount():
#             self.table_widget.setColumnCount(n_words)
#         self.table_widget.setHorizontalHeaderLabels(words)


# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     w = Widget()
#     w.show()
#     sys.exit(app.exec_())

import sys
from math import sqrt, sin, acos, hypot, degrees, radians
from PyQt5 import QtCore, QtGui, QtWidgets

class AngledHeader(QtWidgets.QHeaderView):
    borderPen = QtGui.QColor(0, 190, 255)
    labelBrush = QtGui.QColor(255, 212, 0)
    def __init__(self, parent=None):
        QtWidgets.QHeaderView.__init__(self, QtCore.Qt.Horizontal, parent)
        self.setSectionResizeMode(self.Fixed)
        self.setDefaultSectionSize(int(sqrt((self.fontMetrics().height() + 4)** 2 *2)))
        self.setSectionsClickable(True)
        self.setDefaultSectionSize(int(sqrt((self.fontMetrics().height() + 4)** 2 *2)))
        self.setMaximumHeight(100)
        # compute the ellipsis size according to the angle; remember that:
        # 1. if the angle is not 45 degrees, you'll need to compute this value 
        #   using trigonometric functions according to the angle;
        # 2. we assume ellipsis is done with three period characters, so we can 
        #   "half" its size as (usually) they're painted on the bottom line and 
        #   they are large enough, allowing us to show as much as text is possible
        self.fontEllipsisSize = int(hypot(*[self.fontMetrics().height()] * 2) * .5)
        self.setSectionsClickable(True)

    def sizeHint(self):
        # compute the minimum height using the maximum header label "hypotenuse"'s
        hint = QtWidgets.QHeaderView.sizeHint(self)
        count = self.count()
        if not count:
            return hint
        fm = self.fontMetrics()
        width = minSize = self.defaultSectionSize()
        # set the minimum width to ("hypotenuse" * sectionCount) + minimumHeight
        # at least, ensuring minimal horizontal scroll bar interaction
        hint.setWidth(width * count + self.minimumHeight())
        maxDiag = maxWidth = maxHeight = 1
        for s in range(count):
            if self.isSectionHidden(s):
                continue
            # compute the diagonal of the text's bounding rect, 
            # shift its angle by 45° to get the minimum required 
            # height
            rect = fm.boundingRect(
                str(self.model().headerData(s, QtCore.Qt.Horizontal)) + '    ')
            # avoid math domain errors for empty header labels
            diag = max(1, hypot(rect.width(), rect.height()))
            if diag > maxDiag:
                maxDiag = diag
                maxWidth = max(1, rect.width())
                maxHeight = max(1, rect.height())
        # get the angle of the largest boundingRect using the "Law of cosines":
        # https://en.wikipedia.org/wiki/Law_of_cosines
        angle = degrees(acos(
                (maxDiag ** 2 + maxWidth ** 2 - maxHeight ** 2) / 
                (2. * maxDiag * maxWidth)
            ))
        # compute the minimum required height using the angle found above
        minSize = max(minSize, sin(radians(angle + 45)) * maxDiag)
        hint.setHeight(min(self.maximumHeight(), minSize))
        return hint

    def mousePressEvent(self, event):
        width = self.defaultSectionSize()
        start = self.sectionViewportPosition(0)
        rect = QtCore.QRect(0, 0, width, -self.height())
        transform = QtGui.QTransform().translate(0, self.height()).shear(-1, 0)
        for s in range(self.count()):
            if self.isSectionHidden(s):
                continue
            if transform.mapToPolygon(
                rect.translated(s * width + start, 0)).containsPoint(
                    event.pos(), QtCore.Qt.WindingFill):
                        self.sectionPressed.emit(s)
                        return

    def paintEvent(self, event):
        qp = QtGui.QPainter(self.viewport())
        qp.setRenderHints(qp.Antialiasing)
        width = self.defaultSectionSize()
        delta = self.height()
        # add offset if the view is horizontally scrolled
        qp.translate(self.sectionViewportPosition(0) - .5, -.5)
        fmDelta = (self.fontMetrics().height() - self.fontMetrics().descent()) * .5
        # create a reference rectangle (note that the negative height)
        rect = QtCore.QRectF(0, 0, width, -delta)
        diagonal = hypot(delta, delta)
        for s in range(self.count()):
            if self.isSectionHidden(s):
                continue
            qp.save()
            qp.save()
            qp.setPen(self.borderPen)
            # apply a "shear" transform making the rectangle a parallelogram;
            # since the transformation is applied top to bottom
            # we translate vertically to the bottom of the view
            # and draw the "negative height" rectangle
            qp.setTransform(qp.transform().translate(s * width, delta).shear(-1, 0))
            qp.drawRect(rect)
            qp.setPen(QtCore.Qt.NoPen)
            qp.setBrush(self.labelBrush)
            qp.drawRect(rect.adjusted(2, -2, -2, 2))
            qp.restore()

            qp.translate(s * width + width, delta)
            qp.rotate(-45)
            label = str(self.model().headerData(s, QtCore.Qt.Horizontal))
            elidedLabel = self.fontMetrics().elidedText(
                label, QtCore.Qt.ElideRight, int(diagonal - self.fontEllipsisSize))
            qp.drawText(0, -int(fmDelta), elidedLabel)
            qp.restore()


class AngledTable(QtWidgets.QTableView):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTableView.__init__(self, *args, **kwargs)
        self.setHorizontalHeader(AngledHeader(self))
        self.verticalScrollBarSpacer = QtWidgets.QWidget()
        self.addScrollBarWidget(self.verticalScrollBarSpacer, QtCore.Qt.AlignTop)
        self.fixLock = False

    def setModel(self, model):
        if self.model():
            self.model().headerDataChanged.disconnect(self.fixViewport)
        QtWidgets.QTableView.setModel(self, model)
        model.headerDataChanged.connect(self.fixViewport)

    def fixViewport(self):
        if self.fixLock:
            return
        self.fixLock = True
        # delay the viewport/scrollbar states since the view has to process its 
        # new header data first
        QtCore.QTimer.singleShot(0, self.delayedFixViewport)

    def delayedFixViewport(self):
        # add a right margin through the horizontal scrollbar range
        QtWidgets.QApplication.processEvents()
        header = self.horizontalHeader()
        if not header.isVisible():
            self.verticalScrollBarSpacer.setFixedHeight(0)
            self.updateGeometries()
            return
        self.verticalScrollBarSpacer.setFixedHeight(header.sizeHint().height())
        bar = self.horizontalScrollBar()
        bar.blockSignals(True)
        step = bar.singleStep() * (header.height() / header.defaultSectionSize())
        bar.setMaximum(int(bar.maximum() + step))
        bar.blockSignals(False)
        self.fixLock = False

    def resizeEvent(self, event):
        # ensure that the viewport and scrollbars are updated whenever 
        # the table size change
        QtWidgets.QTableView.resizeEvent(self, event)
        self.fixViewport()


class TestWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        l = QtWidgets.QGridLayout()
        self.setLayout(l)
        self.table = AngledTable()
        l.addWidget(self.table)
        model = QtGui.QStandardItemModel(4, 5)
        self.table.setModel(model)
        self.table.setHorizontalScrollMode(self.table.ScrollPerPixel)
        model.setVerticalHeaderLabels(['Location {}'.format(l + 1) for l in range(8)])
        columns = ['Column {}'.format(c + 1) for c in range(8)]
        columns[3] += ' very, very, very, very, very, very, long'
        model.setHorizontalHeaderLabels(columns)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = TestWidget()
    w.show()
    sys.exit(app.exec_())