# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 844)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 941, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_5.setContentsMargins(13, 13, 13, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_find_source = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_find_source.setObjectName("btn_find_source")
        self.horizontalLayout_2.addWidget(self.btn_find_source)
        self.edit_source = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_source.setObjectName("edit_source")
        self.horizontalLayout_2.addWidget(self.edit_source)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_find_dest = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_find_dest.setObjectName("btn_find_dest")
        self.horizontalLayout_4.addWidget(self.btn_find_dest)
        self.edit_dest = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_dest.setObjectName("edit_dest")
        self.horizontalLayout_4.addWidget(self.edit_dest)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(12, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_parse = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_parse.sizePolicy().hasHeightForWidth())
        self.btn_parse.setSizePolicy(sizePolicy)
        self.btn_parse.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_parse.setObjectName("btn_parse")
        self.verticalLayout_6.addWidget(self.btn_parse)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 110, 941, 691))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_7.setContentsMargins(13, 0, 13, 13)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget_3)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidgetManga = QtWidgets.QTableWidget(self.tab)
        self.tableWidgetManga.setGeometry(QtCore.QRect(0, 0, 911, 651))
        self.tableWidgetManga.setAutoFillBackground(False)
        self.tableWidgetManga.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetManga.setTabKeyNavigation(True)
        self.tableWidgetManga.setProperty("showDropIndicator", False)
        self.tableWidgetManga.setDragDropOverwriteMode(False)
        self.tableWidgetManga.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidgetManga.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidgetManga.setObjectName("tableWidgetManga")
        self.tableWidgetManga.setColumnCount(4)
        self.tableWidgetManga.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidgetManga.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetManga.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetManga.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetManga.setHorizontalHeaderItem(3, item)
        self.tableWidgetManga.horizontalHeader().setVisible(False)
        self.tableWidgetManga.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetManga.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetManga.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetManga.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 911, 651))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidgetImage = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidgetImage.setObjectName("tableWidgetImage")
        self.tableWidgetImage.setColumnCount(3)
        self.tableWidgetImage.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetImage.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetImage.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetImage.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.tableWidgetImage)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_image = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.verticalLayout.addWidget(self.label_image)
        self.pushButtonMove = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonMove.setObjectName("pushButtonMove")
        self.verticalLayout.addWidget(self.pushButtonMove)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 6)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 911, 651))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidgetMagazine = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        self.tableWidgetMagazine.setObjectName("tableWidgetMagazine")
        self.tableWidgetMagazine.setColumnCount(2)
        self.tableWidgetMagazine.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMagazine.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMagazine.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_3.addWidget(self.tableWidgetMagazine)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_work_preview = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_work_preview.setObjectName("label_work_preview")
        self.verticalLayout_2.addWidget(self.label_work_preview)
        self.pushButton_gen = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_gen.setObjectName("pushButton_gen")
        self.verticalLayout_2.addWidget(self.pushButton_gen)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 6)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_7.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_find_source.setText(_translate("MainWindow", "Find"))
        self.label.setText(_translate("MainWindow", "Source:"))
        self.btn_find_dest.setText(_translate("MainWindow", "Find"))
        self.label_2.setText(_translate("MainWindow", "Dest:"))
        self.btn_parse.setText(_translate("MainWindow", "Parse"))
        item = self.tableWidgetManga.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Source Name"))
        item = self.tableWidgetManga.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Dest Name"))
        item = self.tableWidgetManga.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Duplicated"))
        item = self.tableWidgetManga.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Move"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Manga"))
        item = self.tableWidgetImage.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Source"))
        item = self.tableWidgetImage.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Dest"))
        item = self.tableWidgetImage.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Duplicated"))
        self.pushButtonMove.setText(_translate("MainWindow", "Move"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Image"))
        item = self.tableWidgetMagazine.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Author"))
        item = self.tableWidgetMagazine.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Work Name"))
        self.label_work_preview.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_gen.setText(_translate("MainWindow", "Generate folders"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Magazine"))

