from PyQt5 import QtCore, QtGui, QtWidgets, uic
from mainwindow import Ui_MainWindow
from controller import Controller
import global_vars

class MainWidget(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWidget, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.initialize()
		self.controller = Controller(self)
		self.event_connect()
		self.button_mapper = {}

	def initialize(self):
		self.ui.edit_source.setText(global_vars.default_source_path)
		self.ui.edit_dest.setText(global_vars.default_dest_path)
		w = self.ui.tableWidget.width()
		self.ui.tableWidget.setColumnWidth(0, w * 3 / 10)
		self.ui.tableWidget.setColumnWidth(1, w * 3 / 10)
		self.ui.tableWidget.setColumnWidth(2, w * 1.5 / 10)
		self.ui.tableWidget.setColumnWidth(3, w * 1.5 / 10)

	def event_connect(self):
		self.ui.btn_parse.clicked.connect(lambda: self.controller.on_parse(self.ui.edit_source.text(), self.ui.edit_dest.text()))
		self.ui.btn_move_all.clicked.connect(self.controller.on_move_all)
		self.ui.tableWidget.cellDoubleClicked.connect(self.controller.on_open_folder)
		self.ui.tableWidget.keyPressEvent = self.controller.table_key_event

	def set_table_widget_items(self, table_data):
		self.ui.tableWidget.setRowCount(len(table_data[0]))
		for column_idx, row in enumerate(table_data):
			for row_idx, cell in enumerate(row):
				self.ui.tableWidget.setItem(row_idx, column_idx, QtWidgets.QTableWidgetItem(cell))
		for row_idx, duplicated in enumerate(table_data[2]):
			if not duplicated:
				button = QtWidgets.QPushButton(self.ui.tableWidget)
				button.setText('Move')
				self.button_mapper[button] = row_idx
				button.clicked.connect(self.controller.move_to_dest)
				self.ui.tableWidget.setCellWidget(row_idx, 3, button)
		self.ui.tableWidget.update()