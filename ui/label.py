from PyQt5 import QtCore, QtGui, QtWidgets
import os

class MangaPreviewLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(0, 0, 960, 1080))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setScaledContents(True)
        # self.setAutoFillBackground(False)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


    def set_image_path(self, path):
        if os.path.isfile(path):
            img = QtGui.QImage(path)
            p = QtGui.QPainter()
            p.begin(img)
            p.setCompositionMode(QtGui.QPainter.CompositionMode_DestinationIn)
            p.fillRect(img.rect(), QtGui.QColor(0, 0, 0, 100))
            p.end()
            pixmap = QtGui.QPixmap.fromImage(img)
            scaledPix = pixmap.scaled(self.size(), QtCore.Qt.KeepAspectRatio)

            self.setMaximumSize(scaledPix.size())
            self.setPixmap(scaledPix)