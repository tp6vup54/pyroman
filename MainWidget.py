from PyQt5 import QtCore, QtGui, QtWidgets, uic
from mainwindow import Ui_MainWindow
from model import Model
import global_vars

class MainWidget(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWidget, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.initialize()
		self.event_connect()
		self.model = Model()

	def initialize(self):
		self.ui.edit_source.setText(global_vars.default_source_path)
		self.ui.edit_dest.setText(global_vars.default_dest_path)

	def event_connect(self):
		self.ui.btn_parse.clicked.connect(lambda: self.on_parse(self.ui.edit_source.text(), self.ui.edit_dest.text()))

	def on_parse(self, source_path, dest_path):
		source_directory, dest_direcotry = self.model.parse_dir(source_path, dest_path)
		self.set_table_widget_items(source_directory)

	def set_table_widget_items(self, source_directory):
		self.ui.tableWidget.setRowCount(len(source_directory))
		for idx, d in enumerate(source_directory):
			self.ui.tableWidget.setItem(idx, 0, QtWidgets.QTableWidgetItem(d.foldername))
		self.ui.tableWidget.update()

	