import os
import time

class Model():

	def parse_dir_json(self, source_path, dest_path):
		print('fsdf')
		latest_folder = self.get_latest_folder(source_path)
		print(time.ctime(os.path.getmtime(latest_folder)))
		

	def parse_directory(self, path):
		pathes = [path + '\\' + f for f in os.listdir(path) if os.path.isdir(path + '\\' + f)]
		d = [DirForSerial(folderpath = p) for p in pathes]
		serialization.dump(d, 'test')
		d = serialization.load('test')
		dirs = [Directory(serial = dd) for dd in d]
		for dd in dirs:
			test_data(dd)

	def get_latest_folder(self, path):
		all_subdirs = [path + '\\' + d for d in os.listdir(path) if os.path.isdir(path + '\\' + d)]
		return max(all_subdirs, key=os.path.getmtime)


