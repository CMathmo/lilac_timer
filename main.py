import os
import sys
from functools import partial
import numpy as np

import PyQt5
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets, QtGui
import timer
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QWidget, QHBoxLayout, QLabel, QLineEdit, \
    QListWidgetItem, QComboBox, QPushButton, QFileDialog


class timer_designer_mainwindow(QMainWindow, timer.Ui_MainWindow):
    def __init__(self):
        super(timer_designer_mainwindow, self).__init__()
        self.setupUi(self)
        self.SetSingaltoSlots()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.player_num = 4
        self.players_list_refresh(self.pros_players_list)
        self.players_list_refresh(self.cons_players_list)
        zz_jpg = QtGui.QPixmap("D:/File/Picture/zz.jpg")
        self.logo.setPixmap(zz_jpg)
        self.logo.setAlignment(Qt.AlignCenter)

    def SetSingaltoSlots(self):
        self.number_slider.valueChanged.connect(self.show_number)
        self.add_button.clicked.connect(self.list_add)
        self.delete_button.clicked.connect(self.list_delete)
        self.output_button.clicked.connect(self.export_data)
        self.input_button.clicked.connect(self.import_data)

    def show_number(self):
        self.player_num = self.number_slider.value()
        self.number_label.setText("每队人数:" + str(self.player_num))
        self.players_list_refresh(self.pros_players_list)
        self.players_list_refresh(self.cons_players_list)

    def players_list_refresh(self, list):
        length = list.count()
        if length < self.player_num:
            for i in range(self.player_num - length):
                self.players_list_add(list)
        elif length > self.player_num:
            for i in range(length - self.player_num):
                list.takeItem(list.count() - 1)

    def players_list_add(self, list):
        item = QListWidgetItem()
        widget = self.get_players_item_widget(list.count() + 1)
        list.addItem(item)
        item.setSizeHint(widget.sizeHint())  # 一定要这样设置，否则显示不出来
        list.setItemWidget(item, widget)

    def get_players_item_widget(self, num):
        widget = QWidget()
        layout = QHBoxLayout()
        title = self.player_title[num]
        label = QtWidgets.QLabel(self.centralwidget)
        label.setObjectName("label")
        label.setText(title)
        layout.addWidget(label)
        player_name_edit = QLineEdit()
        player_name_edit.setObjectName("player_name_edit")
        layout.addWidget(player_name_edit)
        widget.setLayout(layout)
        return widget

    player_title = {
        1: "一辩",
        2: "二辩",
        3: "三辩",
        4: "四辩",
        5: "五辩",
        6: "六辩",
        7: "七辩",
        8: "八辩",
        9: "九辩",
        10: "十辩"
    }

    def list_add(self):
        item = QListWidgetItem()
        items = self.timetable_list.selectedIndexes()
        if len(items) == 0:
            self.timetable_list.addItem(item)
        else:
            max_row = 0
            for i in items:
                if i.row() > max_row:
                    max_row = i.row()
            self.timetable_list.insertItem(max_row + 1, item)
        widget = QWidget()
        layout = QHBoxLayout()
        number_label = QLabel()
        number_label.setObjectName("number_label")
        number_label.setMinimumWidth(20)
        layout.addWidget(number_label)
        combox = self.get_type_combox()
        combox.currentIndexChanged.connect(partial(self.set_item_widget, widget, combox))
        layout.addWidget(combox)
        son_widget = self.get_item_1_widget()
        layout.addWidget(son_widget)
        widget.setLayout(layout)
        item.setSizeHint(widget.sizeHint())  # 一定要这样设置，否则显示不出来
        self.timetable_list.setItemWidget(item, widget)
        self.list_refresh()

    def list_delete(self):
        items = self.timetable_list.selectedIndexes()
        delete_list = []
        for item in items:
            delete_list.append(item.row())
        delete_list.sort(reverse=True)
        for i in delete_list:
            self.timetable_list.takeItem(i)
        self.list_refresh()

    def list_refresh(self):
        length = self.timetable_list.count()
        for index in range(length):
            self.timetable_list.itemWidget(self.timetable_list.item(index)).findChild(QLabel, "number_label").setText(
                str(index + 1))

    def set_item_widget(self, widget, combox):
        layout = widget.layout()
        widget.findChild(QWidget, "item_widget").deleteLater()
        layout.addWidget(self.item_widget[combox.currentIndex() + 1](self))

    def get_item_1_widget(self):
        widget = QWidget()
        widget.setObjectName("item_widget")
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft)
        name_label = QLabel("名称：")
        name_label.setMaximumWidth(40)
        layout.addWidget(name_label)
        name_edit = QLineEdit()
        name_edit.setObjectName("name_edit")
        name_edit.setMaximumWidth(100)
        layout.addWidget(name_edit)
        button = QPushButton()
        button.setObjectName("standpoint_button")
        button.setMaximumWidth(50)
        button.setText("正方")
        button.clicked.connect(partial(self.cut_button, button))
        layout.addWidget(button)
        layout.addWidget(self.get_player_combox())
        time_label = QLabel("时长：")
        time_label.setMaximumWidth(40)
        layout.addWidget(time_label)
        time_edit = QLineEdit()
        time_edit.setObjectName("time_edit")
        time_edit.setMaximumWidth(50)
        layout.addWidget(time_edit)
        widget.setLayout(layout)
        return widget

    def get_item_2_widget(self):
        widget = QWidget()
        widget.setObjectName("item_widget")
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft)
        name_label = QLabel("名称：")
        name_label.setMaximumWidth(40)
        layout.addWidget(name_label)
        name_edit = QLineEdit()
        name_edit.setObjectName("name_edit")
        name_edit.setMaximumWidth(100)
        layout.addWidget(name_edit)
        button1 = QPushButton()
        button1.setObjectName("standpoint_button")
        button1.setMaximumWidth(50)
        button1.setText("正方")
        button2 = QPushButton()
        button2.setMaximumWidth(50)
        button2.setText("反方")
        button2.setObjectName("ob_standpoint_button")
        button1.clicked.connect(partial(self.cut_button_group, button1, button2))
        button2.clicked.connect(partial(self.cut_button_group, button1, button2))
        layout.addWidget(button1)
        player1_combox = self.get_player_combox()
        player1_combox.setObjectName("player1_combox")
        layout.addWidget(player1_combox)
        time1_label = QLabel("时长：")
        time1_label.setMaximumWidth(40)
        layout.addWidget(time1_label)
        time1_edit = QLineEdit()
        time1_edit.setObjectName("time1_edit")
        time1_edit.setMaximumWidth(60)
        layout.addWidget(time1_edit)
        layout.addWidget(button2)
        player2_combox = self.get_player_combox()
        player2_combox.setObjectName("player2_combox")
        layout.addWidget(player2_combox)
        time2_label = QLabel("时长：")
        time2_label.setMaximumWidth(40)
        layout.addWidget(time2_label)
        time2_edit = QLineEdit()
        time2_edit.setObjectName("time2_edit")
        time2_edit.setMaximumWidth(60)
        layout.addWidget(time2_edit)
        widget.setLayout(layout)
        return widget

    def get_item_3_widget(self):
        widget = QWidget()
        widget.setObjectName("item_widget")
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft)
        name_label = QLabel("名称：")
        name_label.setMaximumWidth(40)
        layout.addWidget(name_label)
        name_edit = QLineEdit()
        name_edit.setObjectName("name_edit")
        name_edit.setMaximumWidth(100)
        layout.addWidget(name_edit)
        button1 = QPushButton()
        button1.setObjectName("standpoint_button")
        button1.setMaximumWidth(50)
        button1.setText("正方")
        button2 = QPushButton()
        button2.setMaximumWidth(50)
        button2.setText("反方")
        button2.setObjectName("ob_standpoint_button")
        button1.clicked.connect(partial(self.cut_button_group, button1, button2))
        button2.clicked.connect(partial(self.cut_button_group, button1, button2))
        layout.addWidget(button1)
        combox1 = self.get_player_combox()
        combox1.setObjectName("player1_combox")
        layout.addWidget(combox1)
        layout.addWidget(button2)
        combox2 = self.get_player_combox()
        combox2.setObjectName("player2_combox")
        layout.addWidget(combox2)
        time_label = QLabel("总时长：")
        time_label.setMaximumWidth(60)
        layout.addWidget(time_label)
        time_edit = QLineEdit()
        time_edit.setObjectName("time_edit")
        time_edit.setMaximumWidth(60)
        layout.addWidget(time_edit)
        widget.setLayout(layout)
        return widget

    def get_item_4_widget(self):
        widget = QWidget()
        widget.setObjectName("item_widget")
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft)
        name_label = QLabel("名称：")
        name_label.setMaximumWidth(40)
        layout.addWidget(name_label)
        name_edit = QLineEdit()
        name_edit.setObjectName("name_edit")
        name_edit.setMaximumWidth(100)
        layout.addWidget(name_edit)
        button1 = QPushButton()
        button1.setObjectName("standpoint_button")
        button1.setMaximumWidth(50)
        button1.setText("正方")
        button2 = QPushButton()
        button2.setMaximumWidth(50)
        button2.setText("反方")
        button2.setObjectName("ob_standpoint_button")
        button1.clicked.connect(partial(self.cut_button_group, button1, button2))
        button2.clicked.connect(partial(self.cut_button_group, button1, button2))
        first_label = QLabel("先手：")
        first_label.setMaximumWidth(40)
        layout.addWidget(first_label)
        layout.addWidget(button1)
        combox1 = self.get_player_combox()
        combox1.setObjectName("player1_combox")
        layout.addWidget(combox1)
        last_label = QLabel("后手：")
        last_label.setMaximumWidth(40)
        layout.addWidget(last_label)
        layout.addWidget(button2)
        combox2 = self.get_player_combox()
        combox2.setObjectName("player2_combox")
        layout.addWidget(combox2)
        time_label = QLabel("时长：")
        time_label.setMaximumWidth(40)
        layout.addWidget(time_label)
        time_edit = QLineEdit()
        time_edit.setObjectName("time_edit")
        time_edit.setMaximumWidth(60)
        layout.addWidget(time_edit)
        widget.setLayout(layout)
        return widget

    def get_item_5_widget(self):
        widget = QWidget()
        widget.setObjectName("item_widget")
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft)
        name_label = QLabel("名称：")
        name_label.setMaximumWidth(40)
        layout.addWidget(name_label)
        name_edit = QLineEdit()
        name_edit.setObjectName("name_edit")
        name_edit.setMaximumWidth(100)
        layout.addWidget(name_edit)
        first_label = QLabel("先手：")
        first_label.setMaximumWidth(40)
        layout.addWidget(first_label)
        button = QPushButton()
        button.setObjectName("standpoint_button")
        button.setMaximumWidth(50)
        button.setText("正方")
        button.clicked.connect(partial(self.cut_button, button))
        layout.addWidget(button)
        time_label = QLabel("时长：")
        time_label.setMaximumWidth(40)
        layout.addWidget(time_label)
        time_edit = QLineEdit()
        time_edit.setObjectName("time_edit")
        time_edit.setMaximumWidth(60)
        layout.addWidget(time_edit)
        widget.setLayout(layout)
        return widget

    def get_item_6_widget(self):
        widget = QWidget()
        widget.setObjectName("item_widget")
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignLeft)
        name_label = QLabel("名称：")
        name_label.setMaximumWidth(40)
        layout.addWidget(name_label)
        name_edit = QLineEdit()
        name_edit.setObjectName("name_edit")
        name_edit.setMaximumWidth(100)
        layout.addWidget(name_edit)
        time_label = QLabel("时长：")
        time_label.setMaximumWidth(40)
        layout.addWidget(time_label)
        time_edit = QLineEdit()
        time_edit.setObjectName("time_edit")
        time_edit.setMaximumWidth(60)
        layout.addWidget(time_edit)
        widget.setLayout(layout)
        return widget

    def get_type_combox(self):
        combox = QComboBox()
        combox.setObjectName("type_combox")
        combox.addItem("一个人逼逼赖赖")
        combox.addItem("阴阳怪气对面")
        combox.addItem("阴阳怪气对面全家")
        combox.addItem("两个人撕逼")
        combox.addItem("一群人开团")
        combox.addItem("其他")
        return combox

    def get_player_combox(self):
        combox = QComboBox()
        combox.setObjectName("player_combox")
        edit = QLineEdit()
        edit.setReadOnly(True)
        combox.setLineEdit(edit)
        combox.setMaximumWidth(100)
        for i in range(self.player_num):
            combox.addItem(self.player_title[i + 1])
        combox.addItem("任意辩手")
        combox.addItem("全部辩手")
        return combox

    def cut_button(self, button):
        if button.text() == "正方":
            button.setText("反方")
        else:
            button.setText("正方")

    def cut_button_group(self, button1, button2):
        self.cut_button(button1)
        self.cut_button(button2)

    item_widget = {
        1: get_item_1_widget,
        2: get_item_2_widget,
        3: get_item_3_widget,
        4: get_item_4_widget,
        5: get_item_5_widget,
        6: get_item_6_widget
    }

    def export_data(self):
        self.get_allValue()
        fileName, filetype = QFileDialog.getSaveFileName(self,
                                                         "文件保存",
                                                         os.getcwd(),  # 起始路径
                                                         "Ltim Files (*.ltim)")
        if fileName != "":
            with open(fileName, 'w') as f:
                f.write(str(self.player_num) + "\n")
                for item_map in self.timetable:
                    if item_map["item_type"] == 0:
                        f.write(
                            str(item_map["item_type"]) + ";" + item_map["name"] + ";" + item_map["standpoint"] + ";" +
                            item_map["player"] + ";" +
                            item_map["time"] + "\n")
                    elif item_map["item_type"] == 1:
                        f.write(
                            str(item_map["item_type"]) + ";" + item_map["name"] + ";" + item_map["standpoint"] + ";" +
                            item_map["player1"] + ";" +
                            item_map["time1"] + ";" + item_map["player2"] + ";" + item_map["time2"] + "\n")
                    elif item_map["item_type"] == 2:
                        f.write(
                            str(item_map["item_type"]) + ";" + item_map["name"] + ";" + item_map["standpoint"] + ";" +
                            item_map["player1"] + ";" + item_map["player2"] + ";" + item_map[
                                "time"] + "\n")
                    elif item_map["item_type"] == 3:
                        f.write(
                            str(item_map["item_type"]) + ";" + item_map["name"] + ";" + item_map["standpoint"] + ";" +
                            item_map["player1"] + ";" + item_map["player2"] + ";" + item_map[
                                "time"] + "\n")
                    elif item_map["item_type"] == 4:
                        f.write(
                            str(item_map["item_type"]) + ";" + item_map["name"] + ";" + item_map["standpoint"] + ";" +
                            item_map["time"] + "\n")
                    else:
                        f.write(str(item_map["item_type"]) + ";" + item_map["name"] + ";" +
                                item_map["time"] + "\n")

    def import_data(self):
        fileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "选取文件",
                                                         os.getcwd(),  # 起始路径
                                                         "Ltim Files (*.ltim)")  # 设置文件扩展名过滤,用双分号间隔
        if fileName != "":
            with open(fileName) as f:
                lines = f.readlines()  # 读取文本中所有内容，并保存在一个列表中，列表中每一个元素对应一行数据
            self.number_slider.setValue(int(lines[0]))
            length = self.timetable_list.count()
            for i in range(length):
                self.timetable_list.takeItem(self.timetable_list.count() - 1)
            for line_index in range(1, len(lines)):
                item_list = lines[line_index].rstrip().split(";")
                self.list_add()
                item_type = int(item_list[0])
                self.timetable_list.itemWidget(self.timetable_list.item(line_index - 1)).findChild(QComboBox,
                                                                                                   "type_combox").setCurrentIndex(
                    item_type)

                if item_type == 0:
                    item_widget = self.timetable_list.itemWidget(self.timetable_list.item(line_index - 1)).findChild(
                        QWidget, "item_widget")
                    item_widget.findChild(QLineEdit, "name_edit").setText(item_list[1])
                    if item_list[2] != "正方":
                        item_widget.findChild(QPushButton, "standpoint_button").setText("反方")
                    item_widget.findChild(QComboBox, "player_combox").setCurrentText(item_list[3])
                    item_widget.findChild(QLineEdit, "time_edit").setText(item_list[4])
                elif item_type == 1:
                    item_widget = self.timetable_list.itemWidget(self.timetable_list.item(line_index - 1)).findChild(
                        QWidget, "item_widget")
                    item_widget.findChild(QLineEdit, "name_edit").setText(item_list[1])
                    if item_list[2] != "正方":
                        item_widget.findChild(QPushButton, "standpoint_button").setText("反方")
                        item_widget.findChild(QPushButton, "ob_standpoint_button").setText("正方")
                    item_widget.findChild(QComboBox, "player1_combox").setCurrentText(item_list[3])
                    item_widget.findChild(QLineEdit, "time1_edit").setText(item_list[4])
                    item_widget.findChild(QComboBox, "player2_combox").setCurrentText(item_list[5])
                    item_widget.findChild(QLineEdit, "time2_edit").setText(item_list[6])
                elif item_type == 2:
                    item_widget = self.timetable_list.itemWidget(self.timetable_list.item(line_index - 1)).findChild(
                        QWidget, "item_widget")
                    item_widget.findChild(QLineEdit, "name_edit").setText(item_list[1])
                    if item_list[2] != "正方":
                        item_widget.findChild(QPushButton, "standpoint_button").setText("反方")
                        item_widget.findChild(QPushButton, "ob_standpoint_button").setText("正方")
                    item_widget.findChild(QComboBox, "player1_combox").setCurrentText(item_list[3])
                    item_widget.findChild(QComboBox, "player2_combox").setCurrentText(item_list[4])
                    item_widget.findChild(QLineEdit, "time_edit").setText(item_list[5])
                elif item_type == 3:
                    item_widget = self.timetable_list.itemWidget(self.timetable_list.item(line_index - 1)).findChild(
                        QWidget, "item_widget")
                    item_widget.findChild(QLineEdit, "name_edit").setText(item_list[1])
                    if item_list[2] != "正方":
                        item_widget.findChild(QPushButton, "standpoint_button").setText("反方")
                        item_widget.findChild(QPushButton, "ob_standpoint_button").setText("正方")
                    item_widget.findChild(QComboBox, "player1_combox").setCurrentText(item_list[3])
                    item_widget.findChild(QComboBox, "player2_combox").setCurrentText(item_list[4])
                    item_widget.findChild(QLineEdit, "time_edit").setText(item_list[5])
                elif item_type == 4:
                    item_widget = self.timetable_list.itemWidget(self.timetable_list.item(line_index - 1)).findChild(
                        QWidget, "item_widget")
                    item_widget.findChild(QLineEdit, "name_edit").setText(item_list[1])
                    if item_list[2] != "正方":
                        item_widget.findChild(QPushButton, "standpoint_button").setText("反方")
                        item_widget.findChild(QPushButton, "ob_standpoint_button").setText("正方")
                    item_widget.findChild(QLineEdit, "time_edit").setText(item_list[3])
                elif item_type == 5:
                    item_widget = self.timetable_list.itemWidget(self.timetable_list.item(line_index - 1)).findChild(
                        QWidget, "item_widget")
                    item_widget.findChild(QLineEdit, "name_edit").setText(item_list[1])
                    item_widget.findChild(QLineEdit, "time_edit").setText(item_list[2])

    def get_allValue(self):
        self.trace_name = self.trace_name_edit.text()
        self.debate = self.debate_edit.text()
        self.pros_debate = self.pros_debate_edit.text()
        self.pros_name = self.pros_name_edit.text()
        self.pros_players = []
        for player_index in range(self.pros_players_list.count()):
            self.pros_players.append(
                self.pros_players_list.itemWidget(self.pros_players_list.item(player_index)).findChild(QLineEdit,
                                                                                                       "player_name_edit").text())
        self.cons_debate = self.cons_debate_edit.text()
        self.cons_name = self.cons_name_edit.text()
        self.cons_players = []
        for player_index in range(self.cons_players_list.count()):
            self.cons_players.append(
                self.cons_players_list.itemWidget(self.cons_players_list.item(player_index)).findChild(QLineEdit,
                                                                                                       "player_name_edit").text())
        self.timetable = []
        for index in range(self.timetable_list.count()):
            item_type = self.timetable_list.itemWidget(self.timetable_list.item(index)).findChild(QComboBox,
                                                                                                  "type_combox").currentIndex()
            widget = self.timetable_list.itemWidget(self.timetable_list.item(index)).findChild(QWidget, "item_widget")
            if item_type == 0:
                item_map = {
                    "item_type": item_type,
                    "name": widget.findChild(QLineEdit, "name_edit").text(),
                    "standpoint": widget.findChild(QPushButton, "standpoint_button").text(),
                    "player": widget.findChild(QComboBox, "player_combox").currentText(),
                    "time": widget.findChild(QLineEdit, "time_edit").text()
                }
            elif item_type == 1:
                item_map = {
                    "item_type": item_type,
                    "name": widget.findChild(QLineEdit, "name_edit").text(),
                    "standpoint": widget.findChild(QPushButton, "standpoint_button").text(),
                    "player1": widget.findChild(QComboBox, "player1_combox").currentText(),
                    "time1": widget.findChild(QLineEdit, "time1_edit").text(),
                    "player2": widget.findChild(QComboBox, "player2_combox").currentText(),
                    "time2": widget.findChild(QLineEdit, "time2_edit").text()
                }
            elif item_type == 2:
                item_map = {
                    "item_type": item_type,
                    "name": widget.findChild(QLineEdit, "name_edit").text(),
                    "standpoint": widget.findChild(QPushButton, "standpoint_button").text(),
                    "player1": widget.findChild(QComboBox, "player1_combox").currentText(),
                    "player2": widget.findChild(QComboBox, "player2_combox").currentText(),
                    "time": widget.findChild(QLineEdit, "time_edit").text()
                }
            elif item_type == 3:
                item_map = {
                    "item_type": item_type,
                    "name": widget.findChild(QLineEdit, "name_edit").text(),
                    "standpoint": widget.findChild(QPushButton, "standpoint_button").text(),
                    "player1": widget.findChild(QComboBox, "player1_combox").currentText(),
                    "player2": widget.findChild(QComboBox, "player2_combox").currentText(),
                    "time": widget.findChild(QLineEdit, "time_edit").text()
                }
            elif item_type == 4:
                item_map = {
                    "item_type": item_type,
                    "name": widget.findChild(QLineEdit, "name_edit").text(),
                    "standpoint": widget.findChild(QPushButton, "standpoint_button").text(),
                    "time": widget.findChild(QLineEdit, "time_edit").text()
                }
            elif item_type == 5:
                item_map = {
                    "item_type": item_type,
                    "name": widget.findChild(QLineEdit, "name_edit").text(),
                    "time": widget.findChild(QLineEdit, "time_edit").text()
                }
            self.timetable.append(item_map)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = timer_designer_mainwindow()
    MainWindow.setWindowTitle("计时器设计器")
    MainWindow.show()
    sys.exit(app.exec_())
