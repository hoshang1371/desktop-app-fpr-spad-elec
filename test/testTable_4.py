import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant

class TableModel(QAbstractTableModel):
    def __init__(self, parent, datain, headerdata):
        QAbstractTableModel.__init__(self, parent)

        self.arraydata=datain
        self.headerdata=headerdata

    def rowCount(self,p):
        return len(self.arraydata)

    def columnCount(self,p):
        if len(self.arraydata)>0:
            return len(self.arraydata[0])
        return 0

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        if orientation==Qt.Horizontal and role==Qt.DisplayRole:
            return self.headerdata[col]
        return None

class MyHeaderView(QtWidgets.QHeaderView):
    def __init__(self,parent):
        QtWidgets.QHeaderView.__init__(self,Qt.Horizontal,parent)
        self.sectionResized.connect(self.myresize)

    def myresize(self, *args):
        '''Resize while keep total width constant'''

        # keep a copy of column widths
        ws=[]
        for c in range(self.count()):
            wii=self.sectionSize(c)
            ws.append(wii)

        if args[0]>0 or args[0]<self.count():
            for ii in range(args[0],self.count()):
                if ii==args[0]:
                    # resize present column
                    self.resizeSection(ii,args[2])
                elif ii==args[0]+1:
                    # if present column expands, shrink the one to the right
                    self.resizeSection(ii,ws[ii]-(args[2]-args[1]))
                else:
                    # keep all others as they were
                    self.resizeSection(ii,ws[ii])

    def resizeEvent(self, event):
        """Resize table as a whole, need this to enable resizing"""

        super(QtWidgets.QHeaderView, self).resizeEvent(event)
        self.setSectionResizeMode(1,QtWidgets.QHeaderView.Stretch)
        for column in range(self.count()):
            self.setSectionResizeMode(column, QtWidgets.QHeaderView.Stretch)
            width = self.sectionSize(column)
            self.setSectionResizeMode(column, QtWidgets.QHeaderView.Interactive)
            self.resizeSection(column, width)

        return

class MainFrame(QtWidgets.QWidget):

    def __init__(self):
        super(MainFrame,self).__init__()
        self.initUI()

    def initUI(self):

        self.doc_table=self.createTable()
        dummy_box=QtWidgets.QLineEdit()

        hlayout=QtWidgets.QHBoxLayout()
        h_split=QtWidgets.QSplitter(Qt.Horizontal)
        h_split.addWidget(self.doc_table)
        h_split.addWidget(dummy_box)
        hlayout.addWidget(h_split)
        self.setLayout(hlayout)
        self.show()

    def createTable(self):
        # create some dummy data
        self.tabledata=[['aaa' ,' title1', True, 1999,5],
                    ['bbb' ,' title2', True, 2000,5],
                    ['ccc' ,' title3', False, 2001,555]
                    ]
        header=['author', 'title', 'read', 'year','55']

        tablemodel=TableModel(self,self.tabledata,header)
        tv=QtWidgets.QTableView(self)
        hh=MyHeaderView(self)
        tv.setHorizontalHeader(hh)
        tv.setModel(tablemodel)
        tv.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        tv.setShowGrid(True)

        hh.setSectionsMovable(True)
        hh.setStretchLastSection(False)
        # this may be optional:
        #hh.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        return tv


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()

        self.main_frame=MainFrame()
        self.setCentralWidget(self.main_frame)
        self.setGeometry(100,100,800,600)
        self.show()


if __name__=='__main__':

    app=QtWidgets.QApplication(sys.argv)
    mainwindow=MainWindow()
    sys.exit(app.exec_())