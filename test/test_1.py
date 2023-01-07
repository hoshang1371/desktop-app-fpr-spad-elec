import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
							QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QPoint

# from PyQt5 import QtCore, QtGui

class FormWidget(QWidget):

    def __init__(self, parent):        
        super(FormWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.button1 = QPushButton("Button 1")
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton("Button 2")
        self.layout.addWidget(self.button2)
		
        self.setLayout(self.layout)
        self.par = parent

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()
        print(self.oldPosition)

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()
        # print(delta)

class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.window_width, self.window_height = 1200, 800
		self.setMinimumSize(self.window_width, self.window_height)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setStyleSheet('''
			QWidget {
				font-size: 60px;
			}
		''')		

		self.lineEdit = QLineEdit(self)
		self.lineEdit.setGeometry(550, 50, 200, 50)


		self.form_widget = FormWidget(self) 
		# self.setCentralWidget(self.form_widget)

		self.btn = QPushButton('Hello', self)
		self.btn.setGeometry(250, 250, 300, 300)
			
	# action #1
	# def mousePressEvent(self, event):
	# 	self.oldPosition = event.globalPos()
	# 	print(self.oldPosition)
        

	# # action #2
	# def mouseMoveEvent(self, event):
	# 	delta = QPoint(event.globalPos() - self.oldPosition)
	# 	self.move(self.x() + delta.x(), self.y() + delta.y())
	# 	self.oldPosition = event.globalPos()
	# 	print(delta)


if __name__ == '__main__':
	# don't auto scale when drag app to a different monitor.
	# QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
	
	app = QApplication(sys.argv)
	
	myApp = MyApp()
	myApp.show()

	try:
		sys.exit(app.exec_())
	except SystemExit:
		print('Closing Window...')

