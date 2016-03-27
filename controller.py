from PyQt5 import QtCore, QtWidgets
from model import Model
import shutil

class Controller():
	def __init__(self, view):
		self.model = Model()
		self.view = view
		self.datasource = None
		self.table_data = None
		self.source_path = ''
		self.dest_path = ''

	def on_parse(self, source_path, dest_path, force_parse_source = False, force_parse_dest = False):
		self.source_path = source_path
		self.dest_path = dest_path
		source_directory = self.model.parse_directory(source_path, force_parse_source)
		dest_directory = self.model.parse_directory(dest_path, force_parse_dest)
		self.datasource = self.get_datasource(source_directory, dest_directory)
		self.table_data = self.get_table_data(self.datasource)
		self.view.set_table_widget_items(self.table_data)

	def on_move_all(self):
		dest_valid_list =\
			self.get_dest_valid_list(\
				self.datasource,\
				self.table_data)
		if len(dest_valid_list) >= 10:
			result = QtWidgets.QMessageBox.question(self,\
				'Warning',\
				'There are over ' + str(len(dest_valid_list)) + ' folders to move, are you sure to move all of them?',\
				QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,\
				QtWidgets.QMessageBox.No)
 
		if result == QtWidgets.QMessageBox.Yes:
			print('Yes.')
		else:
			print('No.')

	def on_open_folder(self, x, y):
		import subprocess
		if y <= 1:
			if self.datasource != None:
				directory = self.datasource[y][x]
			try:
				subprocess.check_call(['explorer', directory.folderpath])
			except:
				pass

	def move_to_dest(self):
		idx = self.view.button_mapper[self.view.sender()]
		if not self.datasource[1][idx]:
			dest = self.dest_path
		else:
			dest = self.datasource[1][idx].folderpath
		print(idx)
		print(dest)
		shutil.move(self.datasource[0][idx].folderpath, dest)
		self.on_parse(self.source_path, self.dest_path, force_parse_source = True)

	def get_dest_valid_list(self, datasource, table_data):
		dest_valid_list = []
		for row_idx in range(len(datasource[0])):
			if not datasource[1][row_idx]:
				continue
			if datasource[1][row_idx].foldername[0] == '[' and\
				datasource[1][row_idx].foldername[-1:][0] == ']' and\
				table_data[2][row_idx] == '':
				dest_valid_list.append([datasource[0][row_idx], datasource[1][row_idx]])
		return dest_valid_list

	def table_key_event(self, event):
		if event.key() == QtCore.Qt.Key_Delete:
			selected = self.view.ui.tableWidget.selectionModel().selectedIndexes()[0]
			if selected.column() == 0:
				self.delete_source_folder(self.datasource[0][selected.row()])
		return QtWidgets.QTableWidget.keyPressEvent(self.view.ui.tableWidget, event)

	def delete_source_folder(self, directory):
		result = QtWidgets.QMessageBox.question(self.view,\
			'Warning',\
			'Are you sure want to delete this folder?\n' + str(directory.foldername),\
			QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,\
			QtWidgets.QMessageBox.Yes)
		if result == QtWidgets.QMessageBox.Yes:
			shutil.rmtree(directory.folderpath)
			self.on_parse(self.source_path, self.dest_path, force_parse_source = True)

	def get_datasource(self, source_directory, dest_directory):
		datasource = []
		datasource.append(self.get_datasource_source(source_directory))
		datasource.append(self.get_datasource_dest(source_directory, dest_directory))
		return datasource

	def get_datasource_source(self, source_directory):
		return source_directory

	def get_datasource_dest(self, source_directory, dest_directory):
		result = []
		found = False
		for source in source_directory:
			for dest in dest_directory:
				if (source.author != '' and\
					(source.author == dest.author or source.author == dest.group)) or\
					(source.group != '' and\
					source.group in dest.foldername):
					result.append(dest)
					found = True
					break
			if not found:
				result.append(None)
			found = False
		return result

	def get_table_data(self, datasource):
		result = []
		result.append([d.foldername for d in datasource[0]])
		result.append([d.foldername if d != None else '' for d in datasource[1]])
		result.append(\
			[self.check_folder_is_duplicate(\
				datasource[0][i], datasource[1][i]) for i in range(len(datasource[0]))
			])
		return result

	def check_folder_is_duplicate(self, source, dest):
		return 'Yes' if self.model.check_folder_is_duplicate(source, dest) else ''