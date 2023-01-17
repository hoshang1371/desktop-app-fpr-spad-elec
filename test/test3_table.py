import sys
from PyQt5 import QtSql
from PyQt5.QtWidgets import (QWidget, QApplication,
                             QGridLayout, QTableView)
from PyQt5.Qt import (QModelIndex, QAbstractProxyModel, QSqlRelationalDelegate)
from PyQt5.QtCore import Qt

class FlippedProxyModel(QAbstractProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)

    def mapFromSource(self, index):
        return self.createIndex(index.column(), index.row())

    def mapToSource(self, index):
        return self.sourceModel().index(index.column(), index.row(), QModelIndex())

    def columnCount(self, parent):
        return self.sourceModel().rowCount(QModelIndex())

    def rowCount(self, parent):
        return self.sourceModel().columnCount(QModelIndex())

    def index(self, row, column, parent):
        return self.createIndex(row, column)

    def parent(self, index):
        return QModelIndex()

    def data(self, index, role):
        return self.sourceModel().data(self.mapToSource(index), role)

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal:
            return self.sourceModel().headerData(section, Qt.Vertical, role)
        if orientation == Qt.Vertical:
            return self.sourceModel().headerData(section, Qt.Horizontal, role)


class FlippedProxyDelegate(QSqlRelationalDelegate):
    def createEditor(self, parent, option, index):
        proxy = index.model()
        base_index = proxy.mapToSource(index)
        return super().createEditor(parent, option, base_index)

    def setEditorData(self, editor, index):
        proxy = index.model()
        base_index = proxy.mapToSource(index)
        return super().setEditorData(editor, base_index)

    def setModelData(self, editor, model, index):
        base_model = model.sourceModel()
        base_index = model.mapToSource(index)
        return super().setModelData(editor, base_model, base_index)


class InvertedTable(QWidget):
    def __init__(self, company):
        super().__init__()
        self.db_file = "test.db"
        self.company = company
        self.create_connection()
        self.fill_table()
        self.create_model()
        self.init_UI()

    def create_connection(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.db_file)
        if not self.db.open():
            print("Cannot establish a database connection to {}!".format(self.db_file))
            return False

    def fill_table(self):
        self.db.transaction()
        q = QtSql.QSqlQuery()
        q.exec_("DROP TABLE IF EXISTS Cars;")
        q.exec_("""CREATE TABLE Cars (Company TEXT, Model TEXT, Cars TEXT)""") 
        q.exec_("INSERT INTO Cars VALUES ('Honda', 'Civic', 5)") 
        q.exec_("INSERT INTO Cars VALUES ('Volkswagen', 'Golf', 3)")
        self.db.commit()

    def create_model(self):
        self.model = QtSql.QSqlTableModel()
        q = QtSql.QSqlQuery()
        query = """SELECT * from cars where company = 'Honda'
         """
        q.exec_(query)
        self.model.setQuery(q)
        self.proxy = FlippedProxyModel() # use flipped proxy model
        self.proxy.setSourceModel(self.model)

    def init_UI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.table = QTableView()
        self.table.setModel(self.proxy)
        self.table.setItemDelegate(FlippedProxyDelegate(self.table)) # use flipped proxy delegate
        self.table.horizontalHeader().hide()

        self.grid.addWidget(self.table, 0, 0)

    def closeEvent(self, e):
        if (self.db.open()):
            self.db.close()

    def check_error(self, q):
        lasterr = q.lastError()
        if lasterr.isValid():
            print(lasterr.text())
            self.db.close()
            exit(1)


def main():
    app = QApplication(sys.argv)
    ex = InvertedTable("Honda")
    ex.show()

    result = app.exec_()
    sys.exit(result)


if __name__ == '__main__':
    main()     