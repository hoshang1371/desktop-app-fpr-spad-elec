from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
  
  
class Window(QWidget):
    def __init__(self):
        super().__init__()
        print("ok")
        # setting title
        # self.setWindowTitle("Python ")
  
        # setting geometry
        # self.setGeometry(100, 100, 600, 400)
        # self.MainWindow = QMainWindow()
        # self.resize(897, 654)

        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
    # method for widgets
    def UiComponents(self):
        # self.MainWindow.resize(897, 654)
        # creating a push button
        button = QPushButton("CLICK", self)
  
        # setting geometry of button
        button.setGeometry(200, 150, 100, 30)
  
        # adding action to a button
        button.clicked.connect(self.clickme)
  
    # action method
    def clickme(self):
        print("pressed")

    def resizeEvent(self, event):
        print("ok")
        # self.resized.emit()
        # return super(Window, self).resizeEvent(event)
  
# # create pyqt5 app
# App = QApplication(sys.argv)
  
# # create the instance of our Window
# window = Window()
  
# # start the app
# sys.exit(App.exec())


if __name__ == "__main__":
    app =QApplication(sys.argv)
    ex = Window()
    # w = QMainWindow()
    # ex.setupUi(w)
    # w.show()
    sys.exit(app.exec_())