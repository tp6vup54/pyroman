class source_handler():
    def __init__(self, view, dir_util):
        self.dir_util = dir_util
        self.view = view
        self.datasource = None
        self.table_data = None
        self.source_path = ''
        self.dest_path = ''

    def parse(self, source_path, dest_path, force_parse_source=False, force_parse_dest=False):
        self.source_path = source_path
        self.dest_path = dest_path

    def move_to_dest(self):
        pass

    def delete(self, target):
        pass