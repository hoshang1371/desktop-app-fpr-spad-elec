from importerProduct import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import pandas as pd

from numpy.random import randint

# from product.widgets_product import AlignDelegate

# from product.widgets_product import CenterDelegate


def productListView(self):
    font = QtGui.QFont()
    font.setPointSize(14)

    self.productList = QtWidgets.QFrame(self.frame)
    self.productList.setLayoutDirection(QtCore.Qt.LeftToRight)
    self.productList.setStyleSheet("border: 1px solid black;")
    self.productList.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.productList.setFrameShadow(QtWidgets.QFrame.Raised)
    self.productList.setObjectName("productList")

    self.scrollArea_List = QtWidgets.QScrollArea(self.productList)
    self.scrollArea_List.setWidgetResizable(True)
    self.scrollArea_List.setObjectName("scrollArea_List")
    self.productList.hide()
    self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.productList)
    self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
    self.verticalLayout_10.setSpacing(0)
    self.verticalLayout_10.setObjectName("verticalLayout_10")
    self.verticalLayout_10.addWidget(self.scrollArea_List)

    self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.scrollArea_List)
    self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
    self.verticalLayout_11.setSpacing(0)
    self.verticalLayout_11.setObjectName("verticalLayout_11")


    self.searchTitle = QtWidgets.QLineEdit(self.frameQrcode)
    self.searchTitle.setGeometry(QtCore.QRect(40, 0, 170, 50))
    self.searchTitle.setPlaceholderText("search")
    self.searchTitle.setFixedHeight(60)
    self.searchTitle.setContentsMargins(5, 5, 5, 5)
    self.searchTitle.setFont(font)
    self.searchTitle.setStyleSheet("border-radius: 25px;\n"                                  "border: 1px solid black;")
    self.searchTitle.setObjectName("searchTitle")
    self.searchTitle.setAlignment(Qt.AlignCenter)
    font.setPointSize(12)
    self.verticalLayout_11.addWidget(self.searchTitle)

    # self.table = QtWidgets.QTableWidget()
    self.table = QtWidgets.QTableView()
    data_ccontent = [
                    ]
    global data
    data = pd.DataFrame(data_ccontent, columns=['ویژه', 'فعال', 'قیمت تخفیف', 'قیمت', 'تعداد', 'مکان کالا', 'نام', 'کد'])
    # data.loc[len(data)]= ["sex", 9, 2, 1, 1, 1, 1, 1]
    # data.loc[len(data)+1]= [False, 9, 2, 1, 1, 1, 1, 2]
    self.model = TableModel(data)
    
    self.table.setModel(self.model)

#*=====================================================
    # self.table.setRowCount(3)
    # self.table.setColumnCount(3)
    # self.table.setHorizontalHeaderLabels(['Product', 'Description', 'Likes/UnLikes'])
    # self.setCentralWidget(self.tableWidget)

#*=====================================================
    self.table.verticalHeader().setVisible(False)


    self.setCentralWidget(self.table)
    self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.table.verticalHeader().setDefaultSectionSize(50)
    self.table.horizontalHeader().setFixedHeight(60)



    delegate = AlignDelegate(self.table)

    self.table.setItemDelegate(delegate)

    delegate1 = IconDelegate(self.table)  # <--- 
    self.table.setItemDelegate(delegate1)

    self.table.setFont(font)
    self.table.horizontalHeader().setFont(font)
    self.table.setSelectionBehavior(QTableView.SelectRows)




    self.table.doubleClicked.connect(lambda: print("vivio"))

    # self.table.horizontalHeader().setDefaultSectionSize(50)
    # self.tableWidget = QTableWidget(self.productList)
    # self.tableWidget.verticalHeader().setVisible(False)
    # # self.tableWidget.horizontalHeader().setVisible(False)
    # self.tableWidget.setRowCount(5)
    # # set column count
    # self.tableWidget.setColumnCount(8)
    #! how to add row after add widget
    # data.loc[len(data)+1]= [False, 9, 2, True, 1, "1010", 1, 7]
    # data_ccontent.append([3, 5, "me1", 1])
    self.verticalLayout_11.addWidget(self.table)
    # data.loc[len(data)]= ["sex", 9, 2, 1, 1, 1, 1, 1]
    # self.layoutChanged.emit()
    # self.model.setDataRow(value= [False, True, 2, True, 1, "koskesh", 1, 8])
    

   

    return self.productList
