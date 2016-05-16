import os
import global_vars
from source_handler import source_handler

class image_handler(source_handler):
	def __init__(self, view, dir_util):
		super().__init__(view, dir_util)

	def parse(self, source_path, dest_path, force_parse_source=False, force_parse_dest=False):
		super().parse(source_path, dest_path, force_parse_source, force_parse_dest)
		images = self.dir_util.parse_image(source_path)
		self.datasource = self.get_datasource(images, dest_path)
		self.table_data = self.get_table_data(self.datasource)

	def get_datasource(self, images, dest_path):
		datasource = [images]
		datasource.append(self.get_datasource_dest(images, dest_path))
		return datasource

	def get_table_data(self, datasource):
		self.table_data = []
		self.table_data.append([image.file_name for image in datasource[0]])
		self.table_data.append([list(_.keys())[0] if _ else '' for _ in datasource[1]])
		self.table_data.append(self.get_duplicated_list(datasource))
		self.view.set_tableWidget_items(self.table_data)

	def get_duplicated_list(self, datasource):
		result = []
		found = False
		for idx, image in enumerate(datasource[0]):
			if datasource[1][idx] == '':
				result.append('')
				continue
			for root, dirs, files in os.walk(list(datasource[1][idx].values())[0]):
				if image.file_name in files:
					result.append('Yes')
					found = True
					break
			if not found: result.append('')
			found = False
		return result

	def get_datasource_dest(self, images, dest_path):
		result = []
		dest_dict = {}
		for _ in os.listdir(dest_path):
			fullpath = dest_path + global_vars.split + _
			if os.path.isdir(fullpath):
				dest_dict.update({os.path.basename(_): fullpath})
		for i in images:
			found = False
			if not i.tags:
				result.append('')
				continue
			for t in i.tags:
				if t in dest_dict:
					result.append({t: dest_dict[t]})
					found = True
					break
			if not found:
				result.append('')
		return result