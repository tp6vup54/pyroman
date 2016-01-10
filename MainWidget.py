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
		datasource = self.get_datasource(source_directory, dest_direcotry)
		table_data = self.get_table_data(datasource)
		for column_idx, row in enumerate(table_data):
			for row_idx, cell in enumerate(row):
				self.ui.tableWidget.setItem(row_idx, column_idx, QtWidgets.QTableWidgetItem(cell))
		self.ui.tableWidget.update()

	def get_table_data(self, datasource):
		result = []
		result.append([d.foldername for d in datasource[0]])
		result.append([d.foldername if d != None else '' for d in datasource[1]])
		return result

	def get_datasource(self, source_directory, dest_direcotry):
		datasource = []
		datasource.append(self.get_datasource_source(source_directory))
		datasource.append(self.get_datasource_dest(source_directory, dest_direcotry))
		return datasource

	def get_datasource_source(self, source_directory):
		return source_directory

	def get_datasource_dest(self, source_directory, dest_direcotry):
		result = []
		found = False
		for source in source_directory:
			for dest in dest_direcotry:
				if (source.author != '' and\
					dest.author != ''  and\
					source.author == dest.author) or\
					(source.group != '' and\
					dest.group != '' and\
					source.group == dest.group):
					result.append(dest)
					found = True
			if not found:
				result.append(None)
			found = False
		return result