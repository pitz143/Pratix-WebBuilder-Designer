import sys
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView
from PyQt5 import QtCore
from PyQt5.QtGui import QPainterPath, QPainter

class MyWeb(QWebEngineView):
	def __init__(self, parent=None):
		super().__init__(parent)
		painter = QPainter()
		path = QPainterPath()

	def _onCmd(self, onclick_callback):
		self.focusProxy().installEventFilter(self)
		self.setMouseTracking(True)
		self.onclick_callback = onclick_callback

	def load(self, url):
		self.setUrl(QUrl(url))

	def adjustTitle(self):
		self.setWindowTitle(self.title())

	def disableJS(self):
		settings = QWebEngineSettings.globalSettings()
		settings.setAttribute(QWebEngineSettings.JavascriptEnabled, False)

	def setMouseTracking(self, flag):
		def recursive_set(parent):
			for child in parent.findChildren(MyWeb):
				try:
					child.setMouseTracking(flag)
				except:
					pass
				recursive_set(child)
		recursive_set(self)

	def eventFilter(self, source, event):
		if (self.focusProxy() is source and event.type() == QtCore.QEvent.MouseButtonPress):
			self.onclick_callback(event)
		return super().eventFilter(source, event)

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.setPen(QPen(Qt.black,10,Qt.SolidLine))
		painter.drawRect(40, 40, 400, 200)