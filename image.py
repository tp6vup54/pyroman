import global_vars
from pixiv_util import pixiv_util

class image():
	def __init__(self, full_path):
		self.full_path = full_path
		self.file_name = full_path.split(global_vars.split)[-1]
		self.tags = pixiv_util().get_file_tag(self.file_name)

	is_pixiv = property(lambda self: self.tags != None)