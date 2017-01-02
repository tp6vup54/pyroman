from directory_util import directory_util
from manga_handler import manga_handler
from image_handler import image_handler

class Controller():
    def __init__(self, view):
        self.dir_util = directory_util()
        self.manga_page_handler = manga_handler(view, self.dir_util)
        self.image_page_handler = image_handler(view, self.dir_util)
        self.view = view

    def on_parse(self, source_path, dest_path, tab_index, force_parse_source = False, force_parse_dest = False):
        if tab_index == 0:
            self.manga_page_handler.parse(source_path, dest_path, force_parse_source, force_parse_dest)
        elif tab_index == 1:
            self.image_page_handler.parse(source_path, dest_path, force_parse_source, force_parse_dest)

    def on_open_folder(self, x, y):
        import subprocess
        if y <= 1:
            if self.manga_page_handler.datasource != None:
                directory = self.manga_page_handler.datasource[y][x]
            try:
                subprocess.check_call(['explorer', directory.folderpath])
            except:
                pass

    def on_show_image(self, x, y):
        self.view.going_to_show_image(self.image_page_handler.datasource[0][x].full_path)

    def table_key_event(self, event):
        from PyQt5 import QtCore, QtWidgets
        if event.key() == QtCore.Qt.Key_Delete:
            selected = self.view.ui.tableWidgetManga.selectionModel().selectedIndexes()[0]
            if selected.column() == 0:
                self.manga_page_handler.delete(self.manga_page_handler.datasource[0][selected.row()])
        return QtWidgets.QTableWidget.keyPressEvent(self.view.ui.tableWidgetManga, event)