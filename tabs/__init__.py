import os
from tabs.image_tab.__init__ import ImageTab
from tabs.manga_tab.__init__ import MangaTab
from tabs.magazine_tab.__init__ import MagazineTab


class Pyroman():
    def __init__(self, view):
        self.manga_tab = MangaTab(view)
        self.image_tab = ImageTab(view)
        self.magazine_tab = MagazineTab(view)
        self.view = view

    def on_parse(self, source_path, dest_path, tab_index, force_parse_source=False, force_parse_dest=False):
        if tab_index == 0:
            self.manga_tab.parse(source_path, dest_path, force_parse_source, force_parse_dest)
        elif tab_index == 1:
            self.image_tab.parse(source_path, dest_path, force_parse_source, force_parse_dest)
        elif tab_index == 2:
            self.magazine_tab.parse(source_path, dest_path)

    def on_open_folder(self, x, y):
        import subprocess
        directory = None
        if y <= 1:
            if self.manga_tab.datasource != None:
                directory = self.manga_tab.datasource[y][x]
            try:
                subprocess.check_call(['explorer', directory.folderpath])
            except:
                pass

    def _get_image_list(self, path):
        def is_image(filename):
            return filename.lower().endswith(('.png', '.jpg', '.jpeg'))

        if os.path.isdir(path):
            return [os.path.join(path, f) for f in os.listdir(path) if is_image(f)]

    def on_preview_manga(self, x, y):
        self.view.ui.tableWidgetManga.current_hover_pos = (x, y)
        if y == 0:
            l = self._get_image_list(self.manga_tab.datasource[0][x].folderpath)
            self.view.preview_label.set_image_list(l)
            self.view.preview_label.show()

    def on_preview_mange_terminate(self, x, y):
        self.view.ui.tableWidgetManga.current_hover_pos = (x, y)
        self.view.preview_label.hide()

    def on_show_image(self, x, y):
        self.view.going_to_show_image(self.image_tab.datasource[0][x].full_path)

    def table_key_event(self, event):
        from PyQt5 import QtCore, QtWidgets
        if event.key() == QtCore.Qt.Key_Delete:
            selected = self.view.ui.tableWidgetManga.selectionModel().selectedIndexes()[0]
            if selected.column() == 0:
                self.manga_tab.delete(self.manga_tab.datasource[0][selected.row()])
        return QtWidgets.QTableWidget.keyPressEvent(self.view.ui.tableWidgetManga, event)