from importerProduct import *
# import productListview

def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.label_41.setText(_translate("MainWindow", "عنوان"))
    self.label_46.setText(_translate("MainWindow", "کد"))
    self.label_45.setText(_translate("MainWindow", "مکان کالا"))
    self.label_44.setText(_translate("MainWindow", "تعداد"))
    self.label_43.setText(_translate("MainWindow", "برند"))
    self.label_42.setText(_translate("MainWindow", "توضیحات"))
    self.label_40.setText(_translate("MainWindow", "توضیحات کوتاه"))
    self.label_47.setText(_translate("MainWindow", "قیمت"))
    self.label_48.setText(_translate("MainWindow", "قیمت تخفیف"))
    self.label_49.setText(_translate("MainWindow", "فعال"))
    self.label_50.setText(_translate("MainWindow", "ویژه"))
    self.addPic.setText(_translate("MainWindow", "افزودن عکس"))
    self.send.setText(_translate("MainWindow", "ارسال"))


def closButtonClicked_exit(self):
    global stop_threads
    stop_threads =True
    if os.path.exists("examplePickle"):
        os.remove("examplePickle")
    print("exit")
    sys.exit()

def changeWindow(self):
    if self.isMaximized():
        self.showNormal()
    else:
        self.showMaximized()


def browsImage(self):
    print("every tink is Ok")
    fname = QFileDialog.getOpenFileName(
        self, 'open File', 'c\\', 'Image files (*.jpg *.gif)')
    imagePath = fname[0]
    self.picDirectory = imagePath
    # print(fname)
    # with open(imagePath, 'rb') as f:
    #     img = f.read()
    # print(img)
    pixmap = QPixmap(imagePath)
    pixmap = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
    # self.resize(pixmap.width(), pixmap.height())
    self.pic.setPixmap(QPixmap(pixmap))

def setEmptyProduct(self):
    self.title.setText("")
    self.code.setText(""),
    self.place.setText(""),
    self.number.setText(""),
    self.brand.setText(""),
    self.description.setText(""),
    self.smallDescription.setText(""),
    self.price.setText(""),
    self.priceOff.setText(""),#
    self.active.setChecked(False)
    self.vige.setChecked(False)
    self.pic.setPixmap(QtGui.QPixmap())


def sendProduct(self):

    if self.title.text() == "":
        notEnteredMessege("عنوان")
    elif self.code.text() == "":
        notEnteredMessege("کد")
    elif self.place.text() == "":
        notEnteredMessege("مکان کالا")
    elif self.number.text() == "":
        notEnteredMessege("تعداد")
    elif not self.number.text().isnumeric():
        notEnterednumber("تعداد")
    elif self.brand.text() == "":
        notEnteredMessege("برند")
    elif self.description.text() == "":
        notEnteredMessege("توضیحات")
    elif self.smallDescription.text() == "":
        notEnteredMessege("توضیحات کوتاه")
    elif self.price.text() == "":
        notEnteredMessege("قیمت")
    elif not self.price.text().isnumeric():
        notEnterednumber("قیمت")
    elif self.picDirectory == "":
        notEnteredMessege("عکس")
    elif not self.priceOff.text().isnumeric() and not self.priceOff.text() == "":
        notEnterednumber("قیمت تخفیف")
    elif self.priceOff.text() == "":
        isEmpty("قیمت تخفیف",
                lambda:Network.post_product_data(
                                self.title.text(),
                                self.code.text(),
                                self.place.text(),
                                self.number.text(),
                                self.brand.text(),
                                self.description.text(),
                                self.smallDescription.text(),
                                self.price.text(),
                                self.priceOff.text(),
                                self.picDirectory,
                                self.active.isChecked(),
                                self.vige.isChecked()
                                )
                )
        self.setEmptyProduct()
            


    else:
        Network.post_product_data(
                                self.title.text(),
                                self.code.text(),
                                self.place.text(),
                                self.number.text(),
                                self.brand.text(),
                                self.description.text(),
                                self.smallDescription.text(),
                                self.price.text(),
                                self.priceOff.text(),
                                self.picDirectory,
                                self.active.isChecked(),
                                self.vige.isChecked()
                                )
        self.setEmptyProduct()




@property
def gripSize(self):
    return self._gripSize



def updateGrips(self):
    print("ok")
    # self.setContentsMargins(*[self.gripSize] * 4)
    self.setContentsMargins(3, 3, 3, 3)

    outRect = self.rect()
    # an "inner" rect used for reference to set the geometries of size grips
    inRect = outRect.adjusted(self.gripSize, self.gripSize,
                                -self.gripSize, -self.gripSize)

    # top left
    self.cornerGrips[0].setGeometry(
        QtCore.QRect(outRect.topLeft(), inRect.topLeft()))

    self.cornerGrips[0].setStyleSheet("""
            background-color: transparent; 
    """)
    # top right
    self.cornerGrips[1].setGeometry(
        QtCore.QRect(outRect.topRight(), inRect.topRight()).normalized())

    self.cornerGrips[1].setStyleSheet("""
            background-color: transparent; 
    """)
    # bottom right
    self.cornerGrips[2].setGeometry(
        QtCore.QRect(inRect.bottomRight(), outRect.bottomRight()))
    self.cornerGrips[2].setStyleSheet("""
            background-color: transparent; 
    """)
    # bottom left
    self.cornerGrips[3].setGeometry(
        QtCore.QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized())
    self.cornerGrips[3].setStyleSheet("""
            background-color: transparent; 
    """)
    # left edge
    self.sideGrips[0].setGeometry(
        0, inRect.top(), self.gripSize, inRect.height())
    # top edge
    self.sideGrips[1].setGeometry(
        inRect.left(), 0, inRect.width(), self.gripSize)
    # right edge
    self.sideGrips[2].setGeometry(
        inRect.left() + inRect.width(),
        inRect.top(), self.gripSize, inRect.height())
    # bottom edge
    self.sideGrips[3].setGeometry(
        self.gripSize, inRect.top() + inRect.height(),
        inRect.width(), self.gripSize)



def resizeEvent(self, event):
    print("ok")
    QtWidgets.QMainWindow.resizeEvent(self, event)
    self.updateGrips()


def handleTextEntered(self):

    # get the text
    text = self.qrTitle.text()
    # self.qrLabel.setText(text)
            # creating a pix map of qr code
    qr_image = qrcode.make(text, image_factory = Image).pixmap()

    # set image to the label
    self.qrLabel.setPixmap(qr_image)
    print(text)

def qrCodeclicked(self):
    self.frameRight.hide()
    self.frame_8.hide()
    self.frameQrcode.show()
    self.productList.hide()

def addProduct(self):
    self.frameRight.show()
    self.frame_8.show()
    self.frameQrcode.hide()   
    self.productList.hide()

import json 

def ProductList(self):
    self.frameRight.hide()
    self.frame_8.hide()
    self.frameQrcode.hide()   
    self.productList.show()
    r= Network.getProductList()
    products = json.loads(r) 
    # print(products)
    # print("r[0]=",products[0])
    # print("ls[0]['vige']=",products[0]['vige'])
    # print("ls[0]['active']=",products[0]['active'])
    # print("len ls=",len(products))
    # print("type r0=",type(products[0]))


    for product in products:
        self.model.setDataRow(value= [
        product['vige'],
        product['active'],
        product['priceOff'],
        product['price'],
        product['number'],
        product['place'],
        product['title'],
        product['code'],
        ]
        )

def deletAllProductList(self):
    self.model.deletAllDataRow()

def searchProduct(self,textSearch):
    print("search Product=",textSearch)
    result =Network.searchProduct(textSearch)
    print(result)
    products = json.loads(result) 
    
    self.model.deletAllDataRow()
    for product in products:
        self.model.setDataRow(value= [
        product['vige'],
        product['active'],
        product['priceOff'],
        product['price'],
        product['number'],
        product['place'],
        product['title'],
        product['code'],
        ]
        )

    # df.drop(df.index[:], inplace=True)

    # self.model.setDataRow(value= [
    # products[0]['vige'],
    # products[0]['active'],
    # products[0]['priceOff'],
    # products[0]['price'],
    # products[0]['number'],
    # products[0]['place'],
    # products[0]['title'],
    # products[0]['code'],
    # ]
    # )
    # productListview.data.loc[len(productListview.data)+1]= [False, 9, 2, True, 1, False, "gfgf", 6]

    # print("productListview.data")
    # print(productListview.data)
    # data.loc[len(data)+1]= [False, 9, 2, 1, 1, 1, 1, QtGui.QIcon("G:/python/logIn_spad/product/tick.png")]

    # print(r)




