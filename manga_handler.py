from PyQt5 import QtWidgets
import shutil
from source_handler import source_handler

class manga_handler(source_handler):
	def __init__(self, view, dir_util):
		super().__init__(view, dir_util)

	def parse(self, source_path, dest_path, force_parse_source = False, force_parse_dest = False):
		super().parse(source_path, dest_path, force_parse_source, force_parse_dest)
		source_directory = self.dir_util.parse_directory_with_json(source_path, force_parse_source)
		dest_directory = self.dir_util.parse_directory_with_json(dest_path, force_parse_dest)
		self.datasource = self.get_datasource(source_directory, dest_directory)
		self.table_data = self.get_table_data(self.datasource)
		self.view.set_tableWidget_items(self.table_data)

	def on_move_all(self):
		dest_valid_list = \
			self.get_dest_valid_list( \
				self.datasource, \
				self.table_data)
		if len(dest_valid_list) >= 10:
			result = QtWidgets.QMessageBox.question(self, \
													'Warning', \
													'There are over ' + str(len(
														dest_valid_list)) + ' folders to move, are you sure to move all of them?', \
													QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, \
													QtWidgets.QMessageBox.No)

		if result == QtWidgets.QMessageBox.Yes:
			print('Yes.')
		else:
			print('No.')

	def get_dest_valid_list(self, datasource, table_data):
		dest_valid_list = []
		for row_idx in range(len(datasource[0])):
			if not datasource[1][row_idx]:
				continue
			if datasource[1][row_idx].foldername[0] == '[' and \
							datasource[1][row_idx].foldername[-1:][0] == ']' and \
							table_data[2][row_idx] == '':
				dest_valid_list.append([datasource[0][row_idx], datasource[1][row_idx]])
		return dest_valid_list

	def move_to_dest(self):
		idx = self.view.button_mapper[self.view.sender()]
		if not self.datasource[1][idx]:
			dest = self.dest_path
		else:
			dest = self.datasource[1][idx].folderpath
		print(idx)
		print(dest)
		shutil.move(self.datasource[0][idx].folderpath, dest)
		self.parse(self.source_path, self.dest_path, force_parse_source=True)

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
				if (source.author != '' and \
							(source.author == dest.author or source.author == dest.group)) or \
						(source.group != '' and \
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
		result.append( \
			[self.check_folder_is_duplicate( \
				datasource[0][i], datasource[1][i]) for i in range(len(datasource[0]))
			 ])
		return result

	def check_folder_is_duplicate(self, source, dest):
		return 'Yes' if self.dir_util.check_folder_is_duplicate(source, dest) else ''

	def delete(self, target):
		result = QtWidgets.QMessageBox.question(self.view, \
												'Warning', \
												'Are you sure want to delete this folder?\n' + str(
													target.foldername), \
												QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, \
												QtWidgets.QMessageBox.Yes)
		if result == QtWidgets.QMessageBox.Yes:
			try:
				shutil.rmtree(target.folderpath)
			except Exception as e:
				print(str(e))
			self.parse(self.source_path, self.dest_path, force_parse_source=True)