import os
import time


class DirectoryJsonAdapter():
    def __init__(self, directory = None, folderpath = None):
        if directory != None:
            self.folderpath = directory.folderpath
            self.timestamp = directory.timestamp
        elif folderpath != None:
            self.folderpath = folderpath
            self.timestamp = time.ctime(os.path.getmtime(folderpath))
        else:
            self.folderpath = ''
            self.timestamp = ''