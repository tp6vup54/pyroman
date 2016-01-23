import os
import time
import serialization
import global_vars
import directory

class Model():
	def parse_directory(self, path, force = False):
		json_path = path + global_vars.split + global_vars.json_name
		need_dump = False
		if not os.path.isfile(json_path):
			print(path + ' not found.')
			need_dump = True
		elif force:
			print('Force parse.')
			need_dump = True
		elif self.get_newer_file(self.get_latest_folder(path), json_path) != 2:
			print('A file newer than json is found.')
			need_dump = True
		if need_dump:
			print('Serialize json.')
			serialization.dump_path(path)
		else:
			print('json exist.')
		directories = serialization.load_path(path)
		return directories

	def get_newer_file(self, file1, file2):
		time1 = time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime(os.path.getmtime(file1)))
		time2 = time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime(os.path.getmtime(file2)))
		return self.get_newer_time(self.get_splitted_time(time1), self.get_splitted_time(time2))

	# 0 is same, 1 is time1, 2 is time2
	def get_newer_time(self, time1, time2):
		result = 0
		for i in range(6):
			if time1[i] > time2[i]:
				result = 1
				break
			elif time1[i] < time2[i]:
				result = 2
				break
			else:
				result = 0
		return result

	def get_splitted_time(self, time_string):
		temp = time_string.split(' ')
		return temp[0].split('/') + temp[1].split(':')

	def get_latest_folder(self, path):
		all_subdirs = [path + global_vars.split + d for d in os.listdir(path) if os.path.isdir(path + global_vars.split + d)]
		return max(all_subdirs, key=os.path.getmtime)

	def check_folder_is_duplicate(self, source, dest):
		if not dest:
			return False
		dest_dir = [f for f in os.listdir(dest.folderpath)]
		for d in dest_dir:
			if source.name == directory.get_title_name(d):
				return True
		return False