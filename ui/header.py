from PyQt5 import QtCore, QtWidgets

class MagazineHeader(QtWidgets.QHeaderView):
    def __init__(self, parent=None):
        QtWidgets.QHeaderView.__init__(self, QtCore.Qt.Horizontal, parent)
        self.is_on = False

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        QtWidgets.QHeaderView.paintSection(self, painter, rect, logicalIndex)
        painter.restore()

        if logicalIndex == 0:
            option = QtWidgets.QStyleOptionButton()
            option.rect = QtCore.QRect(5, 5, 10, 10)
            if self.is_on:
                option.state = QtWidgets.QStyle.State_On
            else:
                option.state = QtWidgets.QStyle.State_Off
            self.style().drawControl(QtWidgets.QStyle.CE_CheckBox, option, painter)

    def mousePressEvent(self, event):
        self.is_on = not self.is_on
        self.updateSection(0)
        QtWidgets.QHeaderView.mousePressEvent(self, event)