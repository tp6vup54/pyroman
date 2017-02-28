from PyQt5 import QtCore, QtGui, QtWidgets
import os

class MangaPreviewLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._max_size = QtCore.QSize(960, 1080)
        self.setGeometry(QtCore.QRect(0, 0, 960, 1080))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setScaledContents(True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self._image_list = []
        self.current_image_index = -1

    def set_image_list(self, l):
        self._image_list = l
        self.set_image_path(self._image_list[0])
        self.current_image_index = 0

    def set_image_path(self, path):
        if os.path.isfile(path):
            img = QtGui.QImage(path)
            img = img.scaled(self._max_size, QtCore.Qt.KeepAspectRatio)
            img = img.convertToFormat(QtGui.QImage.Format_ARGB32)
            p = QtGui.QPainter()
            p.begin(img)
            p.setCompositionMode(QtGui.QPainter.CompositionMode_DestinationIn)
            p.fillRect(img.rect(), QtGui.QColor(0, 0, 0, 100))
            p.end()
            pixmap = QtGui.QPixmap.fromImage(img)

            self.setMaximumSize(pixmap.size())
            self.setPixmap(pixmap)

    def scroll_preview(self, offset):
        if offset.y() < 0 and self.current_image_index < len(self._image_list):
            self.current_image_index += 1
        elif offset.y() > 0 and self.current_image_index > 0:
            self.current_image_index -= 1
        self.set_image_path(self._image_list[self.current_image_index])