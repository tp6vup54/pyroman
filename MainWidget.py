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
		self.set_table_widget_items(source_directory, dest_direcotry)

	def set_table_widget_items(self, source_directory, dest_direcotry):
		self.ui.tableWidget.setRowCount(len(source_directory))
		datasource = self.get_table_datasource(source_directory, dest_direcotry)
		for column_idx, row in enumerate(datasource):
			for row_idx, cell in enumerate(row):
				self.ui.tableWidget.setItem(row_idx, column_idx, QtWidgets.QTableWidgetItem(cell))
		self.ui.tableWidget.update()

	def get_table_datasource(self, source_directory, dest_direcotry):
		datasource = []
		datasource.append(self.get_datasource_column_1(source_directory))
		return datasource

	def get_datasource_column_1(self, source_directory):
		return [d.foldername for d in source_directory]

	def get_datasource_column_2(self, source_directory, dest_direcotry):
		