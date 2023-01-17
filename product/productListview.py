from importerProduct import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import pandas as pd

from numpy.random import randint

# from product.widgets_product import AlignDelegate

# from product.widgets_product import CenterDelegate


def productListView(self):
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

    self.table = QtWidgets.QTableView()

    data_ccontent = [
                    ["sex", 9, 2, 1, 1, 1, 1, 1],
                    [1, "for", -1, 1],
                    [3, 5, "me", 1], 
                    ["sex", 9, 2, 1, 1, 1, 1, 1],
                    [1, "for", -1, 1],
                    [3, 5, "me", 1], 
                    ["sex", 9, 2, 1, 1, 1, 1, 1],
                    [1, "for", -1, 1],
                    [3, 5, "me", 1], 
                    ["sex", 9, 2, 1, 1, 1, 1, 1],
                    [1, "for", -1, 1],
                    [3, 5, "me", 1], 
                    ]

    data_ccontent.append([3, 5, "me", 1])
    data = pd.DataFrame(data_ccontent, columns=['ویژه', 'فعال', 'قیمت تخفیف', 'قیمت', 'تعداد', 'مکان کالا', 'نام', 'کد'])
    data.loc[len(data)]= ["sex", 9, 2, 1, 1, 1, 1, 1]
    self.model = TableModel(data)
    data.loc[len(data)+1]= ["sex", 9, 2, 1, 1, 1, 1, 100]
    self.table.setModel(self.model)

    self.table.verticalHeader().setVisible(False)


    self.setCentralWidget(self.table)
    self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.table.verticalHeader().setDefaultSectionSize(50)
    self.table.horizontalHeader().setFixedHeight(60)

    font = QtGui.QFont()
    font.setPointSize(12)

    delegate = AlignDelegate(self.table)
    self.table.setItemDelegate(delegate)
    self.table.setFont(font)
    self.table.horizontalHeader().setFont(font)
    self.table.setSelectionBehavior(QTableView.SelectRows);
    self.table.doubleClicked.connect(lambda: print("vivio"))
    # self.table.horizontalHeader().setDefaultSectionSize(50)
    # self.tableWidget = QTableWidget(self.productList)
    # self.tableWidget.verticalHeader().setVisible(False)
    # # self.tableWidget.horizontalHeader().setVisible(False)
    # self.tableWidget.setRowCount(5)
    # # set column count
    # self.tableWidget.setColumnCount(8)

    self.verticalLayout_11.addWidget(self.table)
    return self.productList
