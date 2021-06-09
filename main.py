import sys
import re
from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView
from PyQt5 import uic
from MyWeb import MyWeb
from bs4 import BeautifulSoup
from NewDiv import newDiv
from CollapsibleBox import CollapsibleBox

global html
html = "<html>\n<body style='margin:0;padding:0;'>\n"


class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		uic.loadUi("mainwindow.ui", self)
		self.installEventFilter(self)
		self.setMouseTracking(True)
		self.setStyle(QStyleFactory.create('Fusion'))
		global html
		#self.html = "<html>\n<body style='margin:0;padding:0;'>\n"
		self.browser = self.findChild(MyWeb, "Browser")
		self.browserw = self.browser.frameGeometry().width()
		self.browserh = self.browser.frameGeometry().height()
		print(self.browserw)
		print(self.browserh)
		self.widget = self.browser.findChild(QWidget, "centralwidget")
		self.items = self.findChild(custom_list_items, "QWidget")
		self.dock2 = self.findChild(QDockWidget, "dockWidget2")
		self.itemHolder = self.findChild(listWidget,"QListWidget")
		self.itemHolder.setWidget(self.items)
		self.topbar = self.findChild(QPushButton, "Top")
		self.topbar.clicked.connect(self.topclick)
		self.sidebar = self.findChild(QPushButton, "Side")
		self.sidebar.clicked.connect(self.sideclick)
		self.Main = self.findChild(QPushButton, "Main")
		self.Main.clicked.connect(self.mainclick)
		self.footer = self.findChild(QPushButton, "Foot")
		self.footer.clicked.connect(self.footclick)
		self.editor = self.findChild(QTextEdit, "textbox")
		self.editor.setTabStopDistance(50)
		self.editor.textChanged.connect(self.update)
		self.element = self.findChild(QLabel, "element")
		self.coords = self.findChild(QLabel, "cordinates")
		self.test = self.findChild(QWidget, "test")
		self.position = self.findChild(QLineEdit, "Positionvalue")
		self.position.textChanged.connect(self.pos)
		self.width = self.findChild(QLineEdit, "widthvalue")
		#self.width.textChanged.connect(self.wid)
		self.heightval = self.findChild(QLineEdit, "Heightvalue")
		self.heightval.textChanged.connect(self.heigh)
		self.hightval = self.findChild(QLineEdit, "highval")
		self.hightval.textChanged.connect(self.heighv)
		self.bgcolor = self.findChild(QLineEdit, "Bgcolorvalue")
		#self.bgcolor.textChanged.connect(self.bg)
		self.color = self.findChild(QLineEdit, "Colorvalue")
		#self.color.textChanged.connect(self.colr)
		self.border = self.findChild(QLineEdit, "Bordervalue")
		#self.border.textChanged.connect(self.brdr)
		self.borderradius = self.findChild(QLineEdit, "Borderradiusvalue")
		#self.borderradius.textChanged.connect(self.bradius)
		self.zindex = self.findChild(QLineEdit, "ZIndexvalue")
		#self.zindex.textChanged.connect(self.zind)
		self.classv = self.findChild(QLineEdit, "Classvalue")
		#self.classv.textChanged.connect(self.clsv)
		self.id = self.findChild(QLineEdit, "IDvalue")
		#self.id.textChanged.connect(self.idv)
		self.childof = self.findChild(QLineEdit, "ChildOfvalue")
		#self.childof.textChanged.connect(self.chldof)
		self.left = self.findChild(QLineEdit, "Leftvalue")
		#self.Left.textChanged.connect(self.leftv)
		self.top = self.findChild(QLineEdit, "Topvalue")
		#self.top.textChanged.connect(self.topv)
		global brow
		brow = self.browser
		self.list_of_div = []
		self.showMaximized()
		self.show()
		self.browser.setHtml("<html></html>")
		self.browser._onCmd(self.onclick_browser)


	def topclick(self):
		global html, brow
		topbar = "<div class='top' style='position:absolute;width:100%;height:54px;background:red;color:White;left:0;top:0'>\ni can make html\n</div>\n"
		html = html + topbar
		brow.setHtml(html)
		self.editor.setPlainText(html)
		posval, widthval, highval, bgval, colval, leftval, topval, classval = self.parseHtml(topbar)
		mydiv = newDiv(posval, widthval, highval, bgval, colval, leftval, topval, classval)
		self.update_property_from_myDiv(mydiv)
		self.list_of_div.append(mydiv)
		self.update_code_from_property(mydiv)


	def sideclick(self):
		global html, brow
		sidebar = "<div class='side' style='position:absolute;width:200px;height:calc(100% - 54px);background:blue;color:white;left:0;top:54;'>\ni m a sidebar\n</div>\n"
		html = html + sidebar
		brow.setHtml(html)
		self.editor.setPlainText(html)
		posval, widthval, highval, bgval, colval, leftval, topval, classval = self.parseHtml(sidebar)
		mydiv = newDiv(posval, widthval, highval, bgval, colval, leftval, topval, classval)
		self.update_property_from_myDiv(mydiv)
		self.list_of_div.append(mydiv)

	def mainclick(self):
		global html, brow
		maincont = "<div class='main' style='position:absolute;width:calc(100% - 200px);height:calc(100% - 109px);background:green;color:White;left:200;top:54;'>\ni m a boss\n</div>\n"
		html = html + maincont
		brow.setHtml(html)
		self.editor.setPlainText(html)
		posval, widthval, highval, bgval, colval, leftval, topval, classval = self.parseHtml(maincont)
		mydiv = newDiv(posval, widthval, highval, bgval, colval, leftval, topval, classval)
		self.update_property_from_myDiv(mydiv)
		self.list_of_div.append(mydiv)

	def footclick(self):
		global html, brow
		foot = "<div class='foot' style='position:absolute;width:calc(100% - 200px);height:55px;background:orange;color:White;left:200;top:616;'>\ni m a foot\n</div>\n</body>\n</html>\n"
		html = html + foot
		brow.setHtml(html)
		soup = BeautifulSoup(html, 'html.parser')
		self.editor.setPlainText(soup.prettify())
		posval, widthval, highval, bgval, colval, leftval, topval, classval = self.parseHtml(foot)
		mydiv = newDiv(posval, widthval, highval, bgval, colval, leftval, topval, classval)
		self.update_property_from_myDiv(mydiv)
		self.list_of_div.append(mydiv), classval
		self.print_list_divs()

	def print_list_divs(self):
		#print("print from list")
		for mydiv in self.list_of_div:
			print(mydiv.getproperties())

	def parseHtml(self, html):
		soup = BeautifulSoup(html, 'html.parser')
		#print(soup.prettify())
		soup.prettify()
		style = soup.find("div")["style"]
		clas = soup.find("div")["class"]
		classval = clas[0]
		result = re.split(';|:', style)
		#print(result)
		posi = result[0]
		posval = result[1]
		widt = result[2]
		widthval = result[3]
		high = result[4]
		highval = result[5]
		bg = result[6]
		bgval = result[7]
		col = result[8]
		colval = result[9]
		lft = result[10]
		leftval = result[11]
		top = result[12]
		topval = result[13]
		return posval, widthval, highval, bgval, colval, leftval, topval, classval;

	def heigh(self, height):
		#global html
		string = self.editor.toPlainText()
		for mydiv in self.list_of_div:
			old_height = mydiv.getHeight()
			print("old_height = {}".format(old_height))
			new_height = self.heightval.text()
			print("new_height = {}".format(new_height))
			if "class='{}'".format(mydiv.getClass()) and "height:{}".format(mydiv.getHeight()) in string:
				v = string.replace(old_height, new_height, 1)
				self.editor.setPlainText(v)
				#html = v


	def heighv(self):
		for mydiv in self.list_of_div:
			val1 = self.hightval.text()
			high = mydiv.getproperties()[2]
			#print(high, val1)
			result = self.editor.toPlainText()
			if high in result:
				result.replace(high, val1)
				#print("changed result{}".format(high, val1))
			val2 = result.find("54px")
			print("val2 is {}".format(val2))
			res = self.editor.setText(result)
			print("res is {}".format(res))



	def update_code_from_property(self, mydiv):
		global html
		height = self.heightval.setText(mydiv.getHeight())
		edit = self.editor.toPlainText()
		for mydiv in self.list_of_div:
			high = mydiv.getproperties()[2]

		qny = html.replace("height:{}px".format(high), "height:{}".format(self.heigh(high)))
		self.editor.setPlainText(qny)
		print(qny)


	def update(self):
		global html, brow
		html = self.editor.toPlainText()#self
		brow.setHtml(html)

		#print(reap)
		#out = self.parseHtml(html)

		#posval, widthval, highval, bgval, colval = self.parseHtml(html)
		#self.update_to_property_panel(posval, widthval, highval, bgval, colval)

	def update_to_property_panel(self, posval, widthval, highval, bgval, colval, leftval, topval, classval):
		self.position.setText(posval)
		self.width.setText(widthval)
		self.heightval.setText(highval)
		self.bgcolor.setText(bgval)
		self.color.setText(colval)
		self.left.setText(leftval)
		self.top.setText(topval)

	def update_property_from_myDiv(self, mydiv):
		self.position.setText(mydiv.getPosition())
		self.width.setText(mydiv.getWidth())
		self.heightval.setText(mydiv.getHeight())
		self.bgcolor.setText(mydiv.getBackground())
		self.color.setText(mydiv.getColor())
		self.left.setText(mydiv.getLeft())
		self.top.setText(mydiv.getTop())
		self.classv.setText(mydiv.getClass())

	def getvalue_from_string(self, value, maxvalue):
		if "px" in value:
			value = value.replace("px", "")

		if "%" in value:
			value1 = re.findall('\d*%', value)[0]
			value2 = value1.replace("%", "")
			value2 = int(value2) // 100
			value2 = value2 * maxvalue
			value = value.replace(value1, str(value2))

		if "calc(" and ")" in value:
			value = value.replace("calc", "")

		valueint = eval(value)
		return valueint


	def onclick_browser(self, event):
		print('UI: mouseMoveEvent: x=%d, y=%d' % (event.x(), event.y()))
		self.coords.setText('x=%d, y=%d' % (event.x(), event.y()))

		for mydiv in self.list_of_div:
			wid = mydiv.getproperties()[1]
			high = mydiv.getproperties()[2]#
			left = mydiv.getproperties()[5]
			top = mydiv.getproperties()[6]
			wid = self.getvalue_from_string(wid, self.browserw)
			high = self.getvalue_from_string(high, self.browserh)
			startX = int(left)
			startY = int(top)
			endX = startX + int(wid)
			endY = startY + int(high)

			if event.x() >= startX and event.x() <= endX and event.y() >= startY and event.y() <= endY:
				self.element.setText(mydiv.getBackground())
				self.update_property_from_myDiv(mydiv)
			#else:
			#	self.element.setText("outbound")






app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
