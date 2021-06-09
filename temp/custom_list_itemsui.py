from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import uic

class CustomListItems(QWidget):
	def __init__(self, parent=None):
		super(CustomListItems, self).__init__()
		uic.loadUi("custom_list_itemsui.ui", self)
		self.installEventFilter(self)
		self.setMouseTracking(True)
		self.setStyle(QStyleFactory.create('Fusion'))
		self.show()

app = QApplication(sys.argv)
UIWindow = CustomListItems()
app.exec_()