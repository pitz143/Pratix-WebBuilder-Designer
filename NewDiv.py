import sys

#global high

class newDiv:
	def __init__(self, position, width, height, background, color, left, top, classval):
		self.position = position
		self.background = background
		self.width = width
		self.height = height
		self.color = color
		self.left = left
		self.top = top
		self.classval = classval
         

	def getPosition(self):
		return self.position

	def getBackground(self):
		return self.background
	
	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height
	
	def getColor(self):
		return self.color

	def getLeft(self):
		return self.left

	def getTop(self):
		return self.top

	def getClass(self):
		return self.classval

	def getproperties(self):
		return self.position, self.width, self.height, self.background, self.color, self.left, self.top, self.classval

	def setHeight(self, height):
		self.height = height