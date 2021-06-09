from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets


class CollapsibleBox(QtWidgets.QWidget):
    def __init__(self, title="", parent=None):
        super(CollapsibleBox, self).__init__(parent)

        self.toggle_button = QtWidgets.QToolButton(
            text=title, checkable=True, checked=False
        )
        self.toggle_button.setStyleSheet("QToolButton { border: none;}")
        self.toggle_button.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        self.toggle_button.setToolButtonStyle(
            QtCore.Qt.ToolButtonTextBesideIcon
        )
        self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)

        self.toggle_animation = QtCore.QParallelAnimationGroup(self)

        self.content_area = QtWidgets.QScrollArea(
            maximumHeight=0, minimumHeight=0
        )
        self.content_area.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        self.content_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content_area.setStyleSheet("QWidget { background:white;margin:0;}")#border: 1px solid #000; 

        lay = QtWidgets.QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.toggle_button)
        lay.addWidget(self.content_area)

        self.toggle_animation.addAnimation(
            QtCore.QPropertyAnimation(self, b"minimumHeight")
        )
        self.toggle_animation.addAnimation(
            QtCore.QPropertyAnimation(self, b"maximumHeight")
        )
        self.toggle_animation.addAnimation(
            QtCore.QPropertyAnimation(self.content_area, b"maximumHeight")
        )

    @QtCore.pyqtSlot()
    def on_pressed(self):
        checked = self.toggle_button.isChecked()
        self.toggle_button.setArrowType(
            QtCore.Qt.DownArrow if not checked else QtCore.Qt.RightArrow
        )
        self.toggle_animation.setDirection(
            QtCore.QAbstractAnimation.Forward
            if not checked
            else QtCore.QAbstractAnimation.Backward
        )
        self.toggle_animation.start()

    def setContentLayout(self, layout):
        lay = self.content_area.layout()
        del lay
        self.content_area.setLayout(layout)
        collapsed_height = (
            self.sizeHint().height() - self.content_area.maximumHeight()
        )
        content_height = layout.sizeHint().height()
        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(0)#500
            animation.setStartValue(collapsed_height)
            animation.setEndValue(collapsed_height + content_height)

        content_animation = self.toggle_animation.animationAt(
            self.toggle_animation.animationCount() - 1
        )
        content_animation.setDuration(0)#500
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)


if __name__ == "__main__":
    import sys
    import random

    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QMainWindow()
    w.setCentralWidget(QtWidgets.QWidget())
    dock = QtWidgets.QDockWidget("Collapsible Demo")
    w.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
    w.setContentsMargins(0, 0, 0, 0)
    scroll = QtWidgets.QScrollArea()
    dock.setWidget(scroll)
    content = QtWidgets.QWidget()
    content.setContentsMargins(0, 0, 0, 0)
    scroll.setWidget(content)
    scroll.setWidgetResizable(True)
    vlay = QtWidgets.QVBoxLayout(content)
    vlay.setContentsMargins(0, 0, 0, 0)
    for i in range(10):
        box = CollapsibleBox("Collapsible Box Header-{}".format(i))
        vlay.addWidget(box)
        lay = QtWidgets.QVBoxLayout()
        for j in range(8):
            label = QtWidgets.QLabel("{}".format(j))
            label.setContentsMargins(0, 0, 0, 0)
            color = QtGui.QColor(*[random.randint(0, 255) for _ in range(3)])

            label.setStyleSheet(
                "background-color:{}; margin:0px; color:white;height:12px;".format(color.name())
            )
            label.setAlignment(QtCore.Qt.AlignCenter)
            lay.addWidget(label)
            lay.setContentsMargins(0, 0, 0, 0)


        box.setContentLayout(lay)
       
    vlay.addStretch()
    vlay.setContentsMargins(0, 0, 0, 0)
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())