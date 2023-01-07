# from PyQt5.QtWidgets import QWidget
# from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import Qt

x = "hhh"

class myTextBox(QTextEdit):
    def persian(self):
        self.setFixedSize(640, 480)

        self.setLayoutDirection(Qt.RightToLeft)
        self.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        # set text alignment to AlignRight
        self.setAlignment(Qt.AlignRight)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        self.titleBar = MyBar(self)
        self.setContentsMargins(0, self.titleBar.height(), 0, 0)

        self.resize(640, self.titleBar.height() + 480)


        self.layout = QVBoxLayout(self)
        # widget = QTextEdit()
        self.widget = myTextBox()
        self.layout.addWidget(self.widget)

        # self.mytext = self.widget.toPlainText()

        self.button = QPushButton("OK", self)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.send)

    def send(self):
        mytext = self.widget.toPlainText()
        print(mytext)
        self.window().close()
    def changeEvent(self, event):
        if event.type() == event.WindowStateChange:
            self.titleBar.windowStateChanged(self.windowState())

    def resizeEvent(self, event):
        self.titleBar.resize(self.width(), self.titleBar.height())

# from PyQt5.QtGui import QPalette
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
# 							QHBoxLayout, QVBoxLayout

class MyBar(QWidget):
    clickPos = None
    def __init__(self, parent):
        super(MyBar, self).__init__(parent)
        self.setAutoFillBackground(True)
        
        self.setBackgroundRole(QPalette.Shadow)
        # alternatively:
        # palette = self.palette()
        # palette.setColor(palette.Window, Qt.black)
        # palette.setColor(palette.WindowText, Qt.white)
        # self.setPalette(palette)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.addStretch()

        self.title = QLabel("My Own Bar", self, alignment=Qt.AlignCenter)
        # if setPalette() was used above, this is not required
        self.title.setForegroundRole(QPalette.Light)

        style = self.style()
        ref_size = self.fontMetrics().height()
        ref_size += style.pixelMetric(style.PM_ButtonMargin) * 2
        self.setMaximumHeight(ref_size + 2)

        btn_size = QSize(ref_size, ref_size)
        for target in ('min', 'normal', 'max', 'close'):
            btn = QToolButton(self, focusPolicy=Qt.NoFocus)
            layout.addWidget(btn)
            btn.setFixedSize(btn_size)

            iconType = getattr(style, 
                'SP_TitleBar{}Button'.format(target.capitalize()))
            btn.setIcon(style.standardIcon(iconType))

            if target == 'close':
                colorNormal = 'red'
                colorHover = 'orangered'
            else:
                colorNormal = 'palette(mid)'
                colorHover = 'palette(light)'
            btn.setStyleSheet('''
                QToolButton {{
                    background-color: {};
                }}
                QToolButton:hover {{
                    background-color: {}
                }}
            '''.format(colorNormal, colorHover))

            signal = getattr(self, target + 'Clicked')
            btn.clicked.connect(signal)

            setattr(self, target + 'Button', btn)

        self.normalButton.hide()

        self.updateTitle(parent.windowTitle())
        parent.windowTitleChanged.connect(self.updateTitle)

    def updateTitle(self, title=None):
        if title is None:
            title = self.window().windowTitle()
        width = self.title.width()
        width -= self.style().pixelMetric(QStyle.PM_LayoutHorizontalSpacing) * 2
        self.title.setText(self.fontMetrics().elidedText(
            title, Qt.ElideRight, width))

    def windowStateChanged(self, state):
        self.normalButton.setVisible(state == Qt.WindowMaximized)
        self.maxButton.setVisible(state != Qt.WindowMaximized)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clickPos = event.windowPos().toPoint()

    def mouseMoveEvent(self, event):
        if self.clickPos is not None:
            self.window().move(event.globalPos() - self.clickPos)

    def mouseReleaseEvent(self, QMouseEvent):
        self.clickPos = None

    def closeClicked(self):
        print("exit")
        self.window().close()

    def maxClicked(self):
        self.window().showMaximized()

    def normalClicked(self):
        self.window().showNormal()

    def minClicked(self):
        self.window().showMinimized()

    def resizeEvent(self, event):
        self.title.resize(self.minButton.x(), self.height())
        self.updateTitle()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    # layout = QVBoxLayout(mw)
    # # widget = QTextEdit()
    # widget = myTextBox()
    # layout.addWidget(widget)
    print(sys.argv[0])
    print(sys.argv[1])
    print(len(sys.argv))
    mw.show()
    mw.setWindowTitle(sys.argv[1])
    # mytext = widget.toPlainText()
    sys.exit(app.exec_())
