from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import icons
from widgets_product import MyLineEdit, FormWidget, SideGrip, Frame, Image,TableModel\
                            ,CenterDelegate,AlignDelegate,IconDelegate
import os
from PyQt5.QtGui import QPixmap, QImage, QPainter
from PyQt5.QtWidgets import (
    QLineEdit,
    QMainWindow,
    QFileDialog,
    QWidget,
    QTableWidget,
    QHeaderView,
    QTableView,
    QTableWidgetItem,
)
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal, Qt)
import threading
import socket
import qrcode

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from network.network import Network
from extention.massegeBox import addProductSuccesMessege,notEnteredMessege,\
                                 isEmpty,notEnterednumber

# from extention import storeData

# from internalNetwork import *

stop_threads =False
dataGetFromscript =""
dataGetProductList =""

# keyToken = b'chz4UshV2y2R3oCf_nWpX_PsqArGPy0WRrqE72krxbI='

