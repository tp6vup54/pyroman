import os
import time
from dirForSerial import DirForSerial

class Directory():
	def __init__(self, folderpath = None, serial = None):
		self.folderpath = ''
		if folderpath != None:
			self.folderpath = folderpath
			self.timestamp = ''
		elif serial != None:
			self.folderpath = serial.folderpath
			self.timestamp = serial.timestamp
		if self.folderpath != '':
			self.foldername = self.folderpath.split('\\')[-1:][0]
			self.timestamp = time.ctime(os.path.getmtime(folderpath)) if self.timestamp == '' else self.timestamp
			author_string = self.folderpath[self.folderpath.find('[') + 1:self.folderpath.find(']')]
			self.author = author_string[author_string.find('(') + 1:author_string.find(')')] if '(' in author_string else author_string
			self.group = author_string[:author_string.find('(')] if '(' in author_string else ''
			self.author = self.author.replace(' ', '')
			self.group = self.group.replace(' ', '')