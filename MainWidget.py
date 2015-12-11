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

	def event_connect(self):
		self.ui.btn_parse.clicked.connect(lambda: self.on_parse(self.ui.edit_source.text(), ''))

	def on_parse(self, source_path, dest_path):
		self.model.parse_dir_json(source_path, dest_path)