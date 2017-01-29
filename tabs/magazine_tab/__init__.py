from tabs.tab import Tab
from tabs.magazine_tab.parser import *

class MagazineTab(Tab):
    def __init__(self, view):
        super().__init__(view)
        self.parsers = [LivedoorParser(), AcgnichieParser()]

    def parse(self, source_path, dest_path, force_parse_source=False, force_parse_dest=False):
        super().parse(source_path, dest_path)
        parser = self._find_proper_parser(source_path)
        if parser == None:
            raise ProperParserNotFoundException(source_path)
        magazine = parser.parse(source_path)
        self.view.set_tableWidget_items(self._get_table_data(magazine))

    def _get_table_data(self, source):
        return [[_.author_name, _.name] for _ in source.works]

    def _find_proper_parser(self, path):
        for parser in self.parsers:
            if parser.domain in path:
                return parser
        return None


class ProperParserNotFoundException(Exception):
    def __init__(self, path):
        self.cause = 'ProperParserNotFoundException'
        self.message = 'There is no proper parser can be established for source %s.' % (path)
        super().__init__(self.cause, self.message)