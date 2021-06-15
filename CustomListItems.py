from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import uic
#QApplication,QMainWindow, 

class CustomListItems(QWidget):
	def __init__(self, parent=None):
		super(CustomListItems, self).__init__()
		uic.loadUi("custom_list_itemsui.ui", self)
		#self.setStyle(QStyleFactory.create('Fusion'))
		self.itembtns = self.findChild(QToolButton, "itemBtn")
		self.icon = self.findChild(QGraphicsView ,"icon")#, ""
		self.itemname = self.findChild(QLabel, "itemname")
		self.show()

#app = QApplication(sys.argv)
#UIWindow = CustomListItems()
#app.exec_()