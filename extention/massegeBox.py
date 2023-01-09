import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import functools

# msgOfIsEmpty =''
def addProductSuccesMessege():
   msgBox = QMessageBox()
   msgBox.setIcon(QMessageBox.Information)
   msgBox.setText("محصول مورد نظر اضافه شد")
   msgBox.setWindowTitle("اضافه کردن محصول")
   msgBox.setStandardButtons(QMessageBox.Ok)# | QMessageBox.Cancel
#    msgBox.buttonClicked.connect(msgButtonClick)

   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok:
      print('OK clicked')


def notEnteredMessege(value):
   msgBox = QMessageBox()
   msgBox.setIcon(QMessageBox.Warning)
   msgBox.setText(f"{value} را وارد کنید")
   msgBox.setWindowTitle("خطا")
   msgBox.setStandardButtons(QMessageBox.Ok)# | QMessageBox.Cancel
#    msgBox.buttonClicked.connect(msgButtonClick)

   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok:
      print('OK clicked')


def notEnterednumber(value):
   msgBox = QMessageBox()
   msgBox.setIcon(QMessageBox.Warning)
   msgBox.setText(f"{value} به صورت عددی می باشد")
   msgBox.setWindowTitle("خطا")
   msgBox.setStandardButtons(QMessageBox.Ok)# | QMessageBox.Cancel
#    msgBox.buttonClicked.connect(msgButtonClick)

   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok:
      print('OK clicked')
   

def isEmpty(value,function):
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Question)
   msg.setText(f"آیا از مقدار {value} صرف نظر می کنید")
#    msg.setInformativeText("This is additional information")
   msg.setWindowTitle("اخطار")
   msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

#    msg.buttonClicked.connect(lambda: msgbtn(msg.result(),function))

   msg.buttonClicked.connect(lambda button, arg=function: msgbtn(button, arg))

   retval = msg.exec_()
   
#    msg.buttonClicked.connect(fu
# ;nctools.partial(msgbtn,file_path))

#OK
#Cancel
def msgbtn(i,func):
    # print(i)
    if i.text() == 'OK':
        print("ok hojjat")
        func()
    elif i.text() == 'Cancel':
        print("Cancel hojjat")

    # return i.text()
#    print ("Button pressed is:",i.text())
# def msgButtonClick(i):
#    print("Button clicked is:",i.text())