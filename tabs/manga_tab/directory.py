import os
import time

from tabs import vars


def get_title_name(foldername):
    if foldername == '':
        return ''
    while '(' in foldername and ')' in foldername:
        foldername = foldername.replace(foldername[foldername.index('('):foldername.index(')') + 1], '')
    while '[' in foldername and ']' in foldername:
        foldername = foldername.replace(foldername[foldername.index('['):foldername.index(']') + 1], '')
    return foldername.strip()

class Directory():
    def __init__(self, folderpath = None, serial = None):
        self.folderpath = ''
        self.timestamp = ''
        self.foldername = ''
        self.author = ''
        self.group = ''
        self.__name = ''
        if folderpath != None:
            self.folderpath = folderpath
            self.timestamp = ''
        elif serial != None:
            self.folderpath = serial.folderpath
            self.timestamp = serial.timestamp
        if self.folderpath != '':
            self.foldername = self.folderpath.split(vars.split)[-1:][0]
            self.timestamp = time.ctime(os.path.getmtime(folderpath)) if self.timestamp == '' else self.timestamp
            author_string = self.folderpath[self.folderpath.find('[') + 1:self.folderpath.find(']')]
            self.author = author_string[author_string.find('(') + 1:author_string.find(')')] if '(' in author_string else author_string
            self.group = author_string[:author_string.find('(')] if '(' in author_string else ''
            self.author = self.author.strip(' ')
            self.group = self.group.strip(' ')

    def get_name(self):
        if self.__name == '':
            self.__name = get_title_name(self.foldername)
        return self.__name

    def set_name(self, name):
        self.__name = name

    def del_name(self):
        del self.__name

    @property
    def author_string(self):
        if self.group == '':
            return '[' + self.author + ']'
        else:
            return '[' + self.group + ' (' + self.author + ')]'

    name = property(get_name, set_name, del_name, '')
