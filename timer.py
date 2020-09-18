# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1272, 858)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 7, 11, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 11, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 9, 2, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 0, 10, 12, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 9, 1, 1)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setObjectName("delete_button")
        self.gridLayout.addWidget(self.delete_button, 10, 1, 2, 1)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 0, 11, 1, 3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 4, 13, 2, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setMaximumSize(QtCore.QSize(80, 16777215))
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 7, 13, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 4, 11, 2, 1)
        self.output_button = QtWidgets.QPushButton(self.centralwidget)
        self.output_button.setObjectName("output_button")
        self.gridLayout.addWidget(self.output_button, 10, 3, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 9, 2, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 4, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 2, 0, 1, 7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 5, 4, 2, 1)
        self.cons_name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.cons_name_edit.setObjectName("cons_name_edit")
        self.gridLayout_4.addWidget(self.cons_name_edit, 4, 5, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 4, 4, 1, 1)
        self.trace_name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.trace_name_edit.setObjectName("trace_name_edit")
        self.gridLayout_4.addWidget(self.trace_name_edit, 0, 1, 1, 6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 5, 0, 2, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 7, 0, 1, 7)
        self.cons_players_list = QtWidgets.QListWidget(self.centralwidget)
        self.cons_players_list.setMinimumSize(QtCore.QSize(0, 205))
        self.cons_players_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.cons_players_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.cons_players_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.cons_players_list.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.cons_players_list.setObjectName("cons_players_list")
        self.gridLayout_4.addWidget(self.cons_players_list, 5, 5, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 3, 3, 4, 1)
        self.debate_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.debate_edit.setObjectName("debate_edit")
        self.gridLayout_4.addWidget(self.debate_edit, 1, 1, 1, 6)
        self.pros_name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pros_name_edit.setObjectName("pros_name_edit")
        self.gridLayout_4.addWidget(self.pros_name_edit, 4, 1, 1, 2)
        self.cons_debate_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.cons_debate_edit.setObjectName("cons_debate_edit")
        self.gridLayout_4.addWidget(self.cons_debate_edit, 3, 5, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 3, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)
        self.pros_debate_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.pros_debate_edit.setObjectName("pros_debate_edit")
        self.gridLayout_4.addWidget(self.pros_debate_edit, 3, 1, 1, 2)
        self.pros_players_list = QtWidgets.QListWidget(self.centralwidget)
        self.pros_players_list.setMinimumSize(QtCore.QSize(0, 200))
        self.pros_players_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.pros_players_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pros_players_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.pros_players_list.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.pros_players_list.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.pros_players_list.setObjectName("pros_players_list")
        self.gridLayout_4.addWidget(self.pros_players_list, 5, 1, 2, 2)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 2, 4)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 4, 12, 2, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 7, 12, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 1, 11, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 7, 9, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 11, 1, 3)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 9, 11, 3, 3)
        self.number_label = QtWidgets.QLabel(self.centralwidget)
        self.number_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.number_label.setObjectName("number_label")
        self.gridLayout.addWidget(self.number_label, 2, 11, 1, 1)
        self.input_button = QtWidgets.QPushButton(self.centralwidget)
        self.input_button.setObjectName("input_button")
        self.gridLayout.addWidget(self.input_button, 10, 2, 2, 1)
        self.number_slider = QtWidgets.QSlider(self.centralwidget)
        self.number_slider.setMaximumSize(QtCore.QSize(160, 16777215))
        self.number_slider.setMinimum(1)
        self.number_slider.setMaximum(10)
        self.number_slider.setProperty("value", 4)
        self.number_slider.setOrientation(QtCore.Qt.Horizontal)
        self.number_slider.setObjectName("number_slider")
        self.gridLayout.addWidget(self.number_slider, 2, 12, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 10, 9, 2, 1)
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 10, 0, 2, 1)
        self.timetable_list = QtWidgets.QListWidget(self.centralwidget)
        self.timetable_list.setMinimumSize(QtCore.QSize(950, 0))
        self.timetable_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.timetable_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.timetable_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.timetable_list.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.timetable_list.setObjectName("timetable_list")
        self.gridLayout.addWidget(self.timetable_list, 2, 0, 8, 4)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1272, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.label_9.setText(_translate("MainWindow", "配色:"))
        self.delete_button.setText(_translate("MainWindow", "删除"))
        self.logo.setText(_translate("MainWindow", "TextLabel"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_6.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.output_button.setText(_translate("MainWindow", "导出"))
        self.label_4.setText(_translate("MainWindow", "正方队名："))
        self.label_8.setText(_translate("MainWindow", "反方队员："))
        self.label_6.setText(_translate("MainWindow", "反方队名："))
        self.label_7.setText(_translate("MainWindow", "正方队员："))
        self.label_2.setText(_translate("MainWindow", "辩题："))
        self.label.setText(_translate("MainWindow", "比赛名称："))
        self.label_5.setText(_translate("MainWindow", "反方："))
        self.label_3.setText(_translate("MainWindow", "正方："))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox"))
        self.label_10.setText(_translate("MainWindow", "切换方式："))
        self.start_button.setText(_translate("MainWindow", "开始计时"))
        self.number_label.setText(_translate("MainWindow", "每队人数:4"))
        self.input_button.setText(_translate("MainWindow", "导入"))
        self.add_button.setText(_translate("MainWindow", "添加"))