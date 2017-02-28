from PyQt5 import QtCore, QtGui, QtWidgets
from urllib.request import urlopen

from mainwindow import Ui_MainWindow
from tabs import vars
from tabs.__init__ import Pyroman
import ui.header, ui.tableWidget, ui.label


class MainWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialize()
        self.controller = Pyroman(self)
        self.event_connect()
        self.tab_list = ['Manga', 'Image', 'Magazine']
        self.current_tab = self.tab_list[0]
        self.button_mapper = {}
        self._magazine_checkboxes = []
        self.preview_label = ui.label.MangaPreviewLabel()

    def initialize(self):
        self.ui.edit_source.setText(vars.default_source_path)
        self.ui.edit_dest.setText(vars.default_manga_dest_path)
        self.ui.tableWidgetManga = ui.tableWidget.tableWidgetManga(self.ui.tab)
        self.ui.tableWidgetMagazine.verticalHeader().hide()
        self.ui.tableWidgetMagazine.horizontalHeader().hide()
        self.ui.label_work_preview.setAlignment(QtCore.Qt.AlignCenter)

    def event_connect(self):
        self.ui.btn_parse.clicked.connect(lambda: self.controller.on_parse(
            self.ui.edit_source.text(), self.ui.edit_dest.text(), self.ui.tabWidget.currentIndex()
        ))
        #self.ui.btn_move_all.clicked.connect(self.controller.on_move_all)
        self.ui.pushButton_gen.clicked.connect(lambda: self.controller.magazine_tab.on_create_multiple_folders(
            self._magazine_checkboxes, self.ui.edit_dest.text()
        ))
        self.ui.tableWidgetManga.cellDoubleClicked.connect(self.controller.on_open_folder)
        self.ui.tableWidgetManga.cellEntered.connect(self.controller.on_preview_manga)
        self.ui.tableWidgetManga.cellExited.connect(self.controller.on_preview_mange_terminate)
        self.ui.tableWidgetManga.keyPressEvent = self.controller.table_key_event
        self.ui.tableWidgetImage.cellPressed.connect(self.controller.on_show_image)
        self.ui.tabWidget.currentChanged.connect(self.on_change_tab)
        self.ui.tableWidgetMagazine.itemSelectionChanged.connect(self.on_work_selected_in_magazine)

    def set_tableWidget_items(self, table_data):
        (current_table, func) = {
            self.tab_list[0]: (self.ui.tableWidgetManga,
                               lambda self, table_data: self._set_manga_table(self.ui.tableWidgetManga, table_data)),
            self.tab_list[1]: (self.ui.tableWidgetImage,
                               lambda self, table_data: self._set_image_table(self.ui.tableWidgetImage, table_data)),
            self.tab_list[2]: (self.ui.tableWidgetMagazine,
                               lambda self, table_data: self._set_magazine_table(self.ui.tableWidgetMagazine, table_data))
        }.get(self.current_tab)
        if not current_table:
            return
        current_table.setRowCount(len(table_data))
        func(self, table_data)
        current_table.update()

    def _set_manga_table(self, current_table, table_data):
        def create_move_button():
            button = QtWidgets.QPushButton(current_table)
            button.setText('Move')
            self.button_mapper[button] = row_idx
            button.clicked.connect(self.controller.manga_tab.move_to_dest)
            return button

        self.button_mapper = {}
        for row_idx, row in enumerate(table_data):
            for column_idx, cell in enumerate(row):
                current_table.setItem(row_idx, column_idx, QtWidgets.QTableWidgetItem(cell))
            duplicated = row[2]
            if not duplicated:
                button = create_move_button()
                current_table.setCellWidget(row_idx, 3, button)

    def _set_image_table(self, current_table, table_data):
        pass

    def _set_magazine_table(self, current_table, table_data):
        def create_checkbox_item(text):
            cb = QtWidgets.QCheckBox(text)
            self._magazine_checkboxes.append(cb)
            cb.stateChanged.connect(self.on_magazine_checked_state_changed)
            return cb

        self._magazine_checkboxes = []
        for row_idx, row in enumerate(table_data):
            for column_idx, cell in enumerate(row):
                if column_idx == 0:
                    current_table.setCellWidget(row_idx, column_idx, create_checkbox_item(cell))
                else:
                    current_table.setItem(row_idx, column_idx, QtWidgets.QTableWidgetItem(cell))
        header = ui.header.MagazineHeader(self.ui.tableWidgetMagazine)
        header.check_all_delegate = self.on_check_all_magazine
        self.ui.tableWidgetMagazine.setHorizontalHeader(header)
        self.ui.tableWidgetMagazine.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        w = self.ui.tableWidgetMagazine.width()
        self.ui.tableWidgetMagazine.setColumnWidth(0, w * 4 / 10)
        self.ui.tableWidgetMagazine.setColumnWidth(1, w * 5 / 10)

    def on_change_tab(self, idx):
        self.ui.edit_dest.setText(vars.dest_path_dict[idx])
        self.ui.edit_source.setText(vars.source_path_dict[idx])
        self.current_tab = self.tab_list[idx]

    def on_check_all_magazine(self, state):
        for cb in self._magazine_checkboxes:
            cb.setCheckState(state)

    def on_magazine_checked_state_changed(self, state):
        if state == 0:
            self.ui.tableWidgetMagazine.horizontalHeader().is_on = False
        self.ui.tableWidgetMagazine.horizontalHeader().updateSection(0)

    def on_work_selected_in_magazine(self):
        row_idx = self.ui.tableWidgetMagazine.selectedItems()[0].row()
        image_url = self.controller.magazine_tab.get_image_url(row_idx)
        data = urlopen(image_url).read()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(data)
        self.ui.label_work_preview.setPixmap(pixmap)

    def going_to_show_image(self, image_path):
        pixmap = QtGui.QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(self.ui.label_image.size(), QtCore.Qt.KeepAspectRatio)
        self.ui.label_image.setPixmap(scaled_pixmap)