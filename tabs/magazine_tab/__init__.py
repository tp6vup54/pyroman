import os

from tabs.tab import Tab
from tabs.magazine_tab.parser import *

class MagazineTab(Tab):
    def __init__(self, view):
        super().__init__(view)
        self.magazine = None
        self.parsers = [LivedoorParser(), AcgnichieParser()]

    def parse(self, source_path, dest_path, force_parse_source=False, force_parse_dest=False):
        super().parse(source_path, dest_path)
        parser = self._find_proper_parser(source_path)
        if parser == None:
            raise ProperParserNotFoundException(source_path)
        self.magazine = parser.parse(source_path)
        self.view.set_tableWidget_items(self._get_table_data(self.magazine))

    def _get_table_data(self, source):
        return [[_.author_name, _.name] for _ in source.works]

    def _find_proper_parser(self, path):
        for parser in self.parsers:
            if parser.domain in path:
                return parser
        return None

    def on_create_multiple_folders(self, list, dest):
        for idx, checkbox in enumerate(list):
            if checkbox.checkState():
                pass
                # self.on_create_folder(_, dest)

    def on_create_folder(self, name, dest):
        newpath = dest + '/' + name
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    def get_image_url(self, idx):
        if idx > len(self.magazine.works):
            return None
        return self.magazine.works[idx].image_url


class ProperParserNotFoundException(Exception):
    def __init__(self, path):
        self.cause = 'ProperParserNotFoundException'
        self.message = 'There is no proper parser can be established for source %s.' % (path)
        super().__init__(self.cause, self.message)