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
		self.tab_list = ['Manga', 'Image']
		self.current_tab = self.tab_list[0]
		self.button_mapper = {}

	def initialize(self):
		self.ui.edit_source.setText(global_vars.default_source_path)
		self.ui.edit_dest.setText(global_vars.default_manga_dest_path)
		w = self.ui.tableWidgetManga.width()
		self.ui.tableWidgetManga.setColumnWidth(0, w * 3 / 10)
		self.ui.tableWidgetManga.setColumnWidth(1, w * 3 / 10)
		self.ui.tableWidgetManga.setColumnWidth(2, w * 1.5 / 10)
		self.ui.tableWidgetManga.setColumnWidth(3, w * 1.5 / 10)

	def event_connect(self):
		self.ui.btn_parse.clicked.connect(lambda: self.controller.on_parse(self.ui.edit_source.text(), self.ui.edit_dest.text(), self.ui.tabWidget.currentIndex()))
		#self.ui.btn_move_all.clicked.connect(self.controller.on_move_all)
		self.ui.tableWidgetManga.cellDoubleClicked.connect(self.controller.on_open_folder)
		self.ui.tableWidgetManga.keyPressEvent = self.controller.table_key_event
		self.ui.tableWidgetImage.cellPressed.connect(self.controller.on_show_image)
		self.ui.tabWidget.currentChanged.connect(self.on_change_tab)

	def set_tableWidget_items(self, table_data):
		current_table = {
			self.tab_list[0]: self.ui.tableWidgetManga,
			self.tab_list[1]: self.ui.tableWidgetImage}.get(self.current_tab)
		if not current_table:
			return
		self.__set_table_value(current_table, table_data)
		if self.current_tab == self.tab_list[0]:
			self.__set_manga_table(current_table, table_data)
		elif self.current_tab == self.tab_list[1]:
			self.__set_image_table(current_table, table_data)
		current_table.update()

	def __set_table_value(self, current_table, table_data):
		current_table.setRowCount(len(table_data[0]))
		for column_idx, row in enumerate(table_data):
			for row_idx, cell in enumerate(row):
				current_table.setItem(row_idx, column_idx, QtWidgets.QTableWidgetItem(cell))

	def __set_manga_table(self, current_table, table_data):
		for row_idx, duplicated in enumerate(table_data[2]):
			if not duplicated:
				button = QtWidgets.QPushButton(current_table)
				button.setText('Move')
				self.button_mapper[button] = row_idx
				button.clicked.connect(self.controller.manga_page_handler.move_to_dest)
				current_table.setCellWidget(row_idx, 3, button)

	def __set_image_table(self, current_table, table_data):
		pass

	def on_change_tab(self, idx):
		self.ui.edit_dest.setText(global_vars.tab_path_dict[idx])
		self.current_tab = self.tab_list[idx]

	def going_to_show_image(self, image_path):
		pixmap = QtGui.QPixmap(image_path)
		scaled_pixmap = pixmap.scaled(self.ui.label_image.size(), QtCore.Qt.KeepAspectRatio)
		self.ui.label_image.setPixmap(scaled_pixmap)