from importerProduct import *
import defProduct
from internalNetwork import *
from qrview import qrViewCreator  
from frameLess import frameLessFrame
from nav import nav
from theme import productTheme
from picturetheme import picAdder
from productListview import productListView

class Main(QMainWindow):
    _gripSize = 8
    closButtonClicked_exit = defProduct.closButtonClicked_exit
    changeWindow = defProduct.changeWindow
    browsImage = defProduct.browsImage
    setEmptyProduct = defProduct.setEmptyProduct
    sendProduct = defProduct.sendProduct
    gripSize = defProduct.gripSize
    updateGrips = defProduct.updateGrips
    resizeEvent = defProduct.resizeEvent
    handleTextEntered = defProduct.handleTextEntered
    qrCodeclicked = defProduct.qrCodeclicked
    addProduct = defProduct.addProduct
    retranslateUi =defProduct.retranslateUi
    ProductList =defProduct.ProductList
    # desc = defProduct.desc
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.picDirectory =""
        self.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 700)
        MainWindow.setMinimumSize(QtCore.QSize(897, 0))
        MainWindow.setStyleSheet("background-color: rgb(255, 85, 0);")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_NoSystemBackground)
        MainWindow.setMouseTracking(True)
        MainWindow.setContentsMargins(0, 0, 0, 0)
        self.sideGrips = [
            SideGrip(self, QtCore.Qt.LeftEdge),
            SideGrip(self, QtCore.Qt.TopEdge),
            SideGrip(self, QtCore.Qt.RightEdge),
            SideGrip(self, QtCore.Qt.BottomEdge),
        ]

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame_9 = frameLessFrame(self,MainWindow)
        self.verticalLayout.addWidget(self.frame_9)
        #!=====================================================
        self.frame_2 = nav(self)
        self.verticalLayout.addWidget(self.frame_2)
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # self.horizontalLayout_4.hide()
#?========================================================

        self.frame_8 =productTheme(self)
        self.horizontalLayout_4.addWidget(self.frame_8)
#!=============================================================
#*=========================================================================
        self.frameQrcode = qrViewCreator(self)
#*=========================================================================
        self.frameRight = picAdder(self)
#*=========================================================================
        self.productList = productListView(self)
#*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.horizontalLayout_4.addWidget(self.frameRight)
        self.horizontalLayout_4.addWidget(self.frameQrcode)
        self.horizontalLayout_4.addWidget(self.productList)
#*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def desc(self ,child):
        network = NetworkServer(self,child)
        threading.Thread(target=network.server).start()
        print("endof thread")
        print(child.objectName())
        if child.objectName() == 'description':
            os.system('python product\descript.py توضیحات')
        elif child.objectName() == 'smallDescription':
            os.system('python product\descript.py توضیحات کوتاه ')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    stop_threads = False
    ex = Main()
    sys.exit(app.exec_())
