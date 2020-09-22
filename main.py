import os
import re
import sys
from functools import partial
import numpy as np
from PyQt5.QtGui import QPalette, QPixmap, QBrush, QFont, QColor, QPainter
from widget import Ui_Form
from ClockProgressBar import PercentProgressBar as cpb
from enum import Enum
import time
import PyQt5
from PyQt5.QtCore import Qt, QRectF, pyqtSignal
from PyQt5 import QtCore, QtWidgets, QtGui
import timer
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QWidget, QHBoxLayout, QLabel, QLineEdit, \
    QListWidgetItem, QComboBox, QPushButton, QFileDialog


def change_time(time_str):
    sobj = re.search(r"(.*)[:|：](.*)", time_str)
    return int(sobj.group(1)) * 60 + int(sobj.group(2))

class timer_clock(cpb):
    TextColor = QColor(255, 255, 255)  # 文字颜色
    BorderColor = QColor(24, 189, 155)  # 边框圆圈颜色
    BackgroundColor = QColor(70, 70, 70)  # 背景颜色

    def _drawArc(self, painter: QPainter, radius: int):
        # 绘制圆弧
        painter.save()
        painter.setBrush(Qt.NoBrush)
        # 修改画笔
        pen = painter.pen()
        pen.setWidthF(self.BorderWidth)
        pen.setCapStyle(Qt.RoundCap)

        arcLength = 360.0 / (self.MaxValue - self.MinValue) * self.Value
        rect = QRectF(-radius, -radius, radius * 2, radius * 2)

        if not self.Clockwise:
            # 逆时针
            arcLength = -arcLength

        # 绘制剩余进度圆弧
        pen.setColor(self.BorderColor)
        painter.setPen(pen)
        #painter.drawArc(rect, (0 - arcLength) * 16, -(360 - arcLength) * 16)
        painter.drawArc(rect, (90 - arcLength) * 16, -(360 - arcLength) * 16)

        # 绘制当前进度圆弧
        acolor = self.BorderColor.toRgb()
        acolor.setAlphaF(0.2)
        pen.setColor(acolor)
        painter.setPen(pen)
        #painter.drawArc(rect, 0, -arcLength * 16)
        painter.drawArc(rect, 90 * 16, -arcLength * 16)

        painter.restore()

    def _drawText(self, painter: QPainter, radius: int):
        # 绘制文字
        painter.save()
        painter.setPen(self.TextColor)
        painter.setFont(QFont('Arial', 16))
        strValue = '{:0=2}:{:0=2}'.format(int(self.Value / 60), int(self.value % 60))
        painter.drawText(QRectF(-radius, -radius, radius * 2,
                                radius * 2), Qt.AlignCenter, strValue)
        painter.restore()

    def setMaxValue(self, maxvalue):
        self.MaxValue = maxvalue

class timer_widget(QWidget, Ui_Form):


    def __init__(self, value_map, time_table):
        super(timer_widget, self).__init__()
        self.setupUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.value_map = value_map
        self.time_table = time_table
        self.init_label()
        self.init_clock()
        self.set_background("background0.jpg")
        self.SetSingaltoSlots()
        self.index = 0
        self.time_item_num = len(self.time_table)

    def init_label(self):
        self.trace_name.setText(self.value_map["trace_name"])
        self.trace_name.setAlignment(Qt.AlignCenter)
        self.trace_name.setFont(QFont("微软雅黑",24,QFont.Bold))
        self.debate_title.setText(self.value_map["debate"])
        self.debate_title.setAlignment(Qt.AlignCenter)
        self.debate_title.setFont(QFont("微软雅黑",36,QFont.Bold))
        self.pros_debate.setText(self.value_map["pros_debate"])
        self.pros_debate.setAlignment(Qt.AlignCenter)
        self.pros_debate.setFont(QFont("微软雅黑",12))
        self.pros_name.setText(self.value_map["pros_name"])
        self.pros_name.setAlignment(Qt.AlignCenter)
        self.pros_name.setFont(QFont("微软雅黑",10))
        self.cons_debate.setText(self.value_map["cons_debate"])
        self.cons_debate.setAlignment(Qt.AlignCenter)
        self.cons_debate.setFont(QFont("微软雅黑",12))
        self.cons_name.setText(self.value_map["cons_name"])
        self.cons_name.setAlignment(Qt.AlignCenter)
        self.cons_name.setFont(QFont("微软雅黑",10))
        self.turn_name.setVisible(False)

    def init_clock(self):
        self.pros_time = timer_clock()
        self.pros_time.setObjectName("pros_time")
        self.pros_time.setVisible(False)
        self.pros_hlayout.addWidget(self.pros_time)
        self.cons_time = timer_clock()
        self.cons_time.setObjectName("cons_time")
        self.cons_time.setVisible(False)
        self.cons_hlayout.addWidget(self.cons_time)
        self.mid_time = timer_clock()
        self.mid_time.setObjectName("mid_time")
        self.mid_vlayout.addWidget(self.mid_time)
        self.mid_time.setVisible(False)

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:  # 左键按下
            self.cut()


    def cut(self):
        if self.index == self.time_item_num:
            self.Signal_Close(True)
        print(self.time_table[self.index])
        self.setwidget(self.time_table[self.index]["item_type"])
        self.index += 1

    class Background_type(Enum):
        MID = 0
        PROS = 1
        CONS = 2

    background = Background_type.MID

    def cut_standpoint(self):
        if self.background == self.Background_type.PROS:
            self.background = self.Background_type.CONS
        else:
            self.background = self.Background_type.PROS

    def setwidget(self, widget_type):
        if widget_type == 0:
            self.turn_name.setText(self.time_table[self.index]["name"])
            if self.time_table[self.index]["standpoint"] == "正方":
                self.mid_time.setVisible(False)
                self.cons_time.setVisible(False)
                self.pros_time.setVisible(True)
                self.pros_time.setMaxValue(change_time(self.time_table[self.index]["time"]))
                self.pros_time.setValue(change_time(self.time_table[self.index]["time"]))
                self.set_background("background_pros.jpg")
                self.background = self.Background_type.PROS
            else:
                self.mid_time.setVisible(False)
                self.pros_time.setVisible(False)
                self.cons_time.setVisible(True)
                self.cons_time.setMaxValue(change_time(self.time_table[self.index]["time"]))
                self.cons_time.setValue(change_time(self.time_table[self.index]["time"]))
                self.set_background("background_cons.jpg")
                self.background = self.Background_type.CONS
        elif widget_type == 1:
            self.turn_name.setText(self.time_table[self.index]["name"])
            if self.time_table[self.index]["standpoint"] == "正方":
                self.mid_time.setVisible(False)
                self.pros_time.setVisible(True)
                self.pros_time.setMaxValue(change_time(self.time_table[self.index]["time1"]))
                self.pros_time.setValue(change_time(self.time_table[self.index]["time1"]))
                self.cons_time.setVisible(True)
                self.cons_time.setMaxValue(change_time(self.time_table[self.index]["time2"]))
                self.cons_time.setValue(change_time(self.time_table[self.index]["time2"]))
                self.set_background("background_pros.jpg")
                self.background = self.Background_type.PROS
            else:
                self.mid_time.setVisible(False)
                self.cons_time.setVisible(True)
                self.cons_time.setMaxValue(change_time(self.time_table[self.index]["time1"]))
                self.cons_time.setValue(change_time(self.time_table[self.index]["time1"]))
                self.pros_time.setVisible(True)
                self.pros_time.setMaxValue(change_time(self.time_table[self.index]["time2"]))
                self.pros_time.setValue(change_time(self.time_table[self.index]["time2"]))
                self.set_background("background_cons.jpg")
                self.background = self.Background_type.CONS
        elif widget_type == 2:
            self.turn_name.setText(self.time_table[self.index]["name"])
            if self.time_table[self.index]["standpoint"] == "正方":
                self.set_background("background_pros.jpg")
                self.background = self.Background_type.PROS
            else:
                self.set_background("background_cons.jpg")
                self.background = self.Background_type.CONS
            self.mid_time.setVisible(True)
            self.mid_time.setMaxValue(change_time(self.time_table[self.index]["time"]))
            self.mid_time.setValue(change_time(self.time_table[self.index]["time"]))
            self.pros_time.setVisible(False)
            self.cons_time.setVisible(False)
        elif widget_type == 3:
            self.turn_name.setText(self.time_table[self.index]["name"])
            if self.time_table[self.index]["standpoint"] == "正方":
                self.set_background("background_pros.jpg")
                self.background = self.Background_type.PROS
            else:
                self.set_background("background_cons.jpg")
                self.background = self.Background_type.CONS
            self.mid_time.setVisible(False)
            self.pros_time.setVisible(True)
            self.pros_time.setMaxValue(change_time(self.time_table[self.index]["time"]))
            self.pros_time.setValue(change_time(self.time_table[self.index]["time"]))
            self.cons_time.setVisible(True)
            self.cons_time.setMaxValue(change_time(self.time_table[self.index]["time"]))
            self.cons_time.setValue(change_time(self.time_table[self.index]["time"]))
        elif widget_type == 4:
            self.turn_name.setText(self.time_table[self.index]["name"])
            if self.time_table[self.index]["standpoint"] == "正方":
                self.set_background("background_pros.jpg")
                self.background = self.Background_type.PROS
            else:
                self.set_background("background_cons.jpg")
                self.background = self.Background_type.CONS
            self.mid_time.setVisible(False)
            self.pros_time.setVisible(True)
            self.pros_time.setMaxValue(change_time(self.time_table[self.index]["time"]))
            self.pros_time.setValue(change_time(self.time_table[self.index]["time"]))
            self.cons_time.setVisible(True)
            self.cons_time.setMaxValue(change_time(self.time_table[self.index]["time"]))
            self.cons_time.setValue(change_time(self.time_table[self.index]["time"]))
        else:
            self.turn_name.setText(self.time_table[self.index]["name"])
            self.mid_time.setVisible(True)
            self.mid_time.setMaxValue(change_time(self.time_table[self.index]["time"]))
            self.mid_time.setValue(change_time(self.time_table[self.index]["time"]))
            self.pros_time.setVisible(False)
            self.cons_time.setVisible(False)


    def SetSingaltoSlots(self):
        self.pushButton.clicked.connect(self.close)

    def set_background(self, img):
        pal = self.palette()
        pal.setBrush(QPalette.Background,QBrush(QPixmap(img).scaled(
                self.size(),
                Qt.IgnoreAspectRatio,
                Qt.SmoothTransformation)))
        self.setPalette(pal)


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
        self.start_button.clicked.connect(self.Start_time)

    def Close_time(self, tag):
        if tag:
            self.tw.close()

    def Start_time(self):
        self.get_allValue()
        self.tw = timer_widget(self.value_map, self.timetable)
        self.tw.setWindowModality(Qt.WindowModal)
        self.tw.setWindowTitle("qu")
        self.tw.setWindowFlag(Qt.Window)
        self.tw.Signal_Close.connect(self.Close_time)
        #self.tw.showFullScreen()
        self.tw.show()

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
        self.value_map = {}
        self.value_map["trace_name"] = self.trace_name_edit.text()
        self.value_map["debate"] = self.debate_edit.text()
        self.value_map["pros_debate"] = self.pros_debate_edit.text()
        self.value_map["pros_name"] = self.pros_name_edit.text()
        self.value_map["pros_players"] = []
        for player_index in range(self.pros_players_list.count()):
            self.value_map["pros_players"].append(
                self.pros_players_list.itemWidget(self.pros_players_list.item(player_index)).findChild(QLineEdit,
                                                                                                       "player_name_edit").text())
        self.value_map["cons_debate"] = self.cons_debate_edit.text()
        self.value_map["cons_name"]= self.cons_name_edit.text()
        self.value_map["cons_players"] = []
        for player_index in range(self.cons_players_list.count()):
            self.value_map["cons_players"].append(
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