import requests
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from extention.base64 import image_to_data_url

uriImportant = "http://192.168.1.52:8000";
Tok = {}
class Network:
    url_email_login = f"{uriImportant}/api/api_token_auth/";
    url_add_product = f"{uriImportant}/api/addProduct/";

    myToken = "Token 0703e9e4e6a24cfce15b26a7fa0544de3c8101ea"   
    # head = {'Authorization': ''.format(myToken)}
    # head = {'Authorization': "Token 0703e9e4e6a24cfce15b26a7fa0544de3c8101ea" }
    head = {'Authorization': f"{myToken}" }

    # def __init__(self,title,code,place,brand,picDir):
    # def __init__(self):
    #     # self.title = title
    #     # self.code = code
    #     # self.place = place
    #     # self.brand =brand
    #     # self.picDir = picDir
    #     self.myToken = "Token 0703e9e4e6a24cfce15b26a7fa0544de3c8101ea"
    #     self.head = {'Authorization': ''.format(self.myToken)}


    # self.myToken = '<token>'
    # print(url_email_login)
    

    # def post_login():
    #     print(Network.url_email_login)

    def post_login(email,password):
        print(email)
        print(password)
        r = requests.post(Network.url_email_login, json={
        "email": email,
        "password": password
        # "email": "hoshang.1371@yahoo.com",
        # "password": "Ho741jj555at963"
        })
        # print(f"Status Code: {r.status_code}, Response: {r.json()}")
        if r.status_code == 200:
            Tok = r.json()
            # print("ok")
            # print(Tok['token'])


    def post_product_data(title,code,place,number,
                          brand,description,smallDescription,price,
                          priceOff,picDir,active,vige):
    # def post_product_data(self):
        # print(title)
        # print(code)
        # print(place)
        # print(description)
        # print(brand)
        # o = int(price)
        # print(o)
        # print(picDir)
        picName = picDir.split('.')[-2]
        picName = picName.split('/')[-1]
        print('+++++++++++++++++++++++++++++++++')
        print(picName)
        img = image_to_data_url(picDir)
        # print(dir)
        print('+++++++++++++++++++++++++++++++++')
        r = requests.post(Network.url_add_product, 
            headers =Network.head,
            json={
                "title": title,
                "code": code,
                "place": place,
                "number": number,
                "brand":brand,
                "description": description,
                "smallDescription":  smallDescription,
                "price": int(price),
                "priceOff": int(priceOff),
                "active": active,
                "vige": vige,
                "image":{
                    "filename": "picName",
                    "contents": img
            }        
    })

        print(r.status_code) 
        
        
        # print(r.headers) 
        # print(r.content) 
        print(r.text) 
        print(r.reason) 
        if r.status_code == 200:
            addProductSucces()


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# def window():
#    app = QApplication(sys.argv)
#    win = QWidget()
#    button1 = QPushButton(win)
#    button1.setText("Show dialog!")
#    button1.move(50,50)
#    button1.clicked.connect(showDialog)
#    win.setWindowTitle("Click button")
#    win.show()
#    sys.exit(app.exec_())
	
def addProductSucces():
   msgBox = QMessageBox()
   msgBox.setIcon(QMessageBox.Information)
   msgBox.setText("محصول مورد نظر اضافه شد")
   msgBox.setWindowTitle("اضافه کردن محصول")
   msgBox.setStandardButtons(QMessageBox.Ok)# | QMessageBox.Cancel
   msgBox.buttonClicked.connect(msgButtonClick)

   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok:
      print('OK clicked')
   
def msgButtonClick(i):
   print("Button clicked is:",i.text())
	
# if __name__ == '__main__': 
#    window()
