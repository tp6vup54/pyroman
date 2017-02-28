from PyQt5 import QtCore, QtGui, QtWidgets

class tableWidgetManga(QtWidgets.QTableWidget):
    cellExited = QtCore.pyqtSignal(int, int)
    itemExited = QtCore.pyqtSignal(QtWidgets.QTableWidgetItem)

    def __init__(self, parent):
        super().__init__(parent)
        self.initialize()

    def initialize(self):
        self.setGeometry(QtCore.QRect(0, 0, 911, 651))
        self.setAutoFillBackground(False)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setTabKeyNavigation(True)
        self.setProperty("showDropIndicator", False)
        self.setDragDropOverwriteMode(False)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.setGridStyle(QtCore.Qt.DashLine)
        self.setObjectName("tableWidgetManga")
        self.setColumnCount(4)
        self.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(3, item)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalHeader().setSortIndicatorShown(False)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setStretchLastSection(False)
        self.setMouseTracking(True)
        self._last_index = QtCore.QPersistentModelIndex()
        self.viewport().installEventFilter(self)
        self.set_colunm_width()

    def set_colunm_width(self):
        w = self.width()
        self.setColumnWidth(0, w * 3 / 10)
        self.setColumnWidth(1, w * 3 / 10)
        self.setColumnWidth(2, w * 1.5 / 10)
        self.setColumnWidth(3, w * 1.5 / 10)

    def eventFilter(self, widget, event):
        if widget is self.viewport():
            index = self._last_index
            if event.type() == QtCore.QEvent.MouseMove:
                index = self.indexAt(event.pos())
            elif event.type() == QtCore.QEvent.Leave:
                index = QtCore.QModelIndex()
            if index != self._last_index:
                row = self._last_index.row()
                column = self._last_index.column()
                item = self.item(row, column)
                if item is not None:
                    self.itemExited.emit(item)
                self.cellExited.emit(row, column)
                self._last_index = QtCore.QPersistentModelIndex(index)
        return QtWidgets.QTableWidget.eventFilter(self, widget, event)