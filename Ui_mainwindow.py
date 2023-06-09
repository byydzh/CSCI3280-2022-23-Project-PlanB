# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(971, 610)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.widget.setStyleSheet("QWidget#widget{\n"
"    background:rgb(255, 250, 232);\n"
"    border-top-right-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QListWidget{\n"
"    font: 9pt \"霞鹜文楷\";\n"
"    background:rgb(255, 250, 232);\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"    width:8px;\n"
"    border:none;\n"
"    background:rgba(0,0,0,0%);\n"
"    margin:0px,0px,0px,0px;\n"
"    padding-top:9px;\n"
"    padding-bottom:9px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    width:8px;\n"
"    background:rgba(0,0,0,25%);\n"
"    border-radius:4px;\n"
"    min-height:20;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover\n"
"{\n"
"    width:8px;\n"
"    background:rgba(0,0,0,50%);\n"
"    border-radius:4px;\n"
"    min-height:20;\n"
"}\n"
"QScrollBar::add-page:vertical{\n"
"    background-color:rgb(255, 250, 232);\n"
"    height: 0px;\n"
"}\n"
"QScrollBar::sub-page:vertical{\n"
"    background-color:rgb(255, 250, 232);\n"
"}\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    height:9px;width:8px;\n"
"    image: url(:/icon/images/arrow-down-bold.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    height:9px;width:8px;\n"
"    image: url(:/icon/images/arrow-up-bold.png);\n"
"    subcontrol-position:top;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_top = QtWidgets.QWidget(self.widget)
        self.widget_top.setMinimumSize(QtCore.QSize(0, 35))
        self.widget_top.setMaximumSize(QtCore.QSize(16777215, 35))
        self.widget_top.setMouseTracking(False)
        self.widget_top.setStyleSheet("QWidget#widget_top{\n"
"    background:rgb(255, 255, 255);\n"
"    border-top-right-radius:10px;\n"
"    border-top-left-radius:10px;\n"
"}")
        self.widget_top.setObjectName("widget_top")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_top)
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_update = QtWidgets.QPushButton(self.widget_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_update.sizePolicy().hasHeightForWidth())
        self.pushButton_update.setSizePolicy(sizePolicy)
        self.pushButton_update.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton_update.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_update.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_update.setStyleSheet("QPushButton{\n"
"    background:rgb(0, 255, 72);\n"
"    border-radius:10px;\n"
"    font: 9pt \"微软雅黑\";\n"
"    color: #ff7043;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#24f5f2;\n"
"}\n"
"")
        self.pushButton_update.setObjectName("pushButton_update")
        self.horizontalLayout_3.addWidget(self.pushButton_update)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_lights_btn = QtWidgets.QHBoxLayout()
        self.horizontalLayout_lights_btn.setSpacing(6)
        self.horizontalLayout_lights_btn.setObjectName("horizontalLayout_lights_btn")
        self.pushButton_green = QtWidgets.QPushButton(self.widget_top)
        self.pushButton_green.setMinimumSize(QtCore.QSize(15, 15))
        self.pushButton_green.setMaximumSize(QtCore.QSize(15, 15))
        self.pushButton_green.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_green.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_green.setStyleSheet("QPushButton{background:#6DDF6D;border-radius:7px;}QPushButton:hover{background:green;}")
        self.pushButton_green.setText("")
        self.pushButton_green.setObjectName("pushButton_green")
        self.horizontalLayout_lights_btn.addWidget(self.pushButton_green)
        self.pushButton_yellow = QtWidgets.QPushButton(self.widget_top)
        self.pushButton_yellow.setMinimumSize(QtCore.QSize(15, 15))
        self.pushButton_yellow.setMaximumSize(QtCore.QSize(15, 15))
        self.pushButton_yellow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_yellow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_yellow.setStyleSheet("QPushButton{background:#F7D674;border-radius:7px;}\n"
"QPushButton:hover{background:yellow;}")
        self.pushButton_yellow.setText("")
        self.pushButton_yellow.setObjectName("pushButton_yellow")
        self.horizontalLayout_lights_btn.addWidget(self.pushButton_yellow)
        self.pushButton_red = QtWidgets.QPushButton(self.widget_top)
        self.pushButton_red.setMinimumSize(QtCore.QSize(15, 15))
        self.pushButton_red.setMaximumSize(QtCore.QSize(15, 15))
        self.pushButton_red.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_red.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_red.setStyleSheet("QPushButton{background:#F76677;border-radius:7px;}QPushButton:hover{background:red;}")
        self.pushButton_red.setText("")
        self.pushButton_red.setObjectName("pushButton_red")
        self.horizontalLayout_lights_btn.addWidget(self.pushButton_red)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_lights_btn)
        self.verticalLayout_5.addWidget(self.widget_top)
        self.horizontalLayout_body = QtWidgets.QHBoxLayout()
        self.horizontalLayout_body.setContentsMargins(15, 10, 15, 10)
        self.horizontalLayout_body.setSpacing(15)
        self.horizontalLayout_body.setObjectName("horizontalLayout_body")
        self.verticalLayout_musiclist = QtWidgets.QVBoxLayout()
        self.verticalLayout_musiclist.setSpacing(4)
        self.verticalLayout_musiclist.setObjectName("verticalLayout_musiclist")
        self.horizontalLayout_save_btn = QtWidgets.QHBoxLayout()
        self.horizontalLayout_save_btn.setObjectName("horizontalLayout_save_btn")
        self.label_list_name = QtWidgets.QLabel(self.widget)
        self.label_list_name.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_list_name.sizePolicy().hasHeightForWidth())
        self.label_list_name.setSizePolicy(sizePolicy)
        self.label_list_name.setStyleSheet("font: 10pt \"霞鹜文楷\";")
        self.label_list_name.setObjectName("label_list_name")
        self.horizontalLayout_save_btn.addWidget(self.label_list_name)
        self.pushButton_save_to_playlist = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save_to_playlist.sizePolicy().hasHeightForWidth())
        self.pushButton_save_to_playlist.setSizePolicy(sizePolicy)
        self.pushButton_save_to_playlist.setMinimumSize(QtCore.QSize(45, 0))
        self.pushButton_save_to_playlist.setMaximumSize(QtCore.QSize(45, 17))
        self.pushButton_save_to_playlist.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_save_to_playlist.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_save_to_playlist.setStyleSheet("QPushButton{\n"
"    background:#ffe7ba;\n"
"    border-radius:0px;\n"
"    font: 9pt \"微软雅黑\";\n"
"    color: rgb(255, 250, 232);\n"
"}\n"
"QPushButton:hover{\n"
"    background:#ffa940;\n"
"}\n"
"")
        self.pushButton_save_to_playlist.setObjectName("pushButton_save_to_playlist")
        self.horizontalLayout_save_btn.addWidget(self.pushButton_save_to_playlist)
        self.horizontalLayout_save_btn.setStretch(0, 8)
        self.horizontalLayout_save_btn.setStretch(1, 4)
        self.verticalLayout_musiclist.addLayout(self.horizontalLayout_save_btn)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border:1px groove lightgray;\n"
"    border-radius:2px;\n"
"    font: 9pt \"霞鹜文楷\";\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_musiclist.addWidget(self.lineEdit)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget.setStyleSheet("QListView::item:hover {\n"
"    background-color: #fff7e6;\n"
"    border-left: 3px solid #ff441a;\n"
"}\n"
"QListView::item:selected {\n"
"    background-color: #fff3e0;\n"
"    border-left: 3px solid #c92a2a;\n"
"}\n"
"QListView::item {\n"
"    border-bottom: 1px solid #e4e4e4;\n"
"}")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_musiclist.addWidget(self.listWidget)
        self.pushButton_song_find = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_song_find.sizePolicy().hasHeightForWidth())
        self.pushButton_song_find.setSizePolicy(sizePolicy)
        self.pushButton_song_find.setMaximumSize(QtCore.QSize(16777215, 15))
        self.pushButton_song_find.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_song_find.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_song_find.setStyleSheet("QPushButton{\n"
"    image: url(:/icon/images/arrow-up-bold.png);\n"
"}")
        self.pushButton_song_find.setText("")
        self.pushButton_song_find.setFlat(True)
        self.pushButton_song_find.setObjectName("pushButton_song_find")
        self.verticalLayout_musiclist.addWidget(self.pushButton_song_find)
        self.verticalLayout_musiclist.setStretch(0, 1)
        self.verticalLayout_musiclist.setStretch(1, 1)
        self.verticalLayout_musiclist.setStretch(2, 10)
        self.verticalLayout_musiclist.setStretch(3, 1)
        self.horizontalLayout_body.addLayout(self.verticalLayout_musiclist)
        self.verticalLayout_lrc = QtWidgets.QVBoxLayout()
        self.verticalLayout_lrc.setObjectName("verticalLayout_lrc")
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setStyleSheet("font: 13pt \"微软雅黑\";")
        self.label_name.setObjectName("label_name")
        self.verticalLayout_lrc.addWidget(self.label_name)
        self.listWidget_2 = QtWidgets.QListWidget(self.widget)
        self.listWidget_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.listWidget_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget_2.setStyleSheet("QListView::item:hover {\n"
"    background-color: #fff7e6;\n"
"}\n"
"QListView::item:selected {\n"
"    background-color: #fff3e0;\n"
"}")
        self.listWidget_2.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.HongKong))
        self.listWidget_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(False)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.verticalLayout_lrc.addWidget(self.listWidget_2)
        self.horizontalLayout_body.addLayout(self.verticalLayout_lrc)
        self.widget_info = QtWidgets.QWidget(self.widget)
        self.widget_info.setObjectName("widget_info")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_info)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_pic = QtWidgets.QHBoxLayout()
        self.horizontalLayout_pic.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_pic.setObjectName("horizontalLayout_pic")
        self.widget_pic = QtWidgets.QWidget(self.widget_info)
        self.widget_pic.setMinimumSize(QtCore.QSize(170, 170))
        self.widget_pic.setMaximumSize(QtCore.QSize(170, 170))
        self.widget_pic.setObjectName("widget_pic")
        self.label_pic_under = QtWidgets.QLabel(self.widget_pic)
        self.label_pic_under.setGeometry(QtCore.QRect(0, 0, 170, 170))
        self.label_pic_under.setMinimumSize(QtCore.QSize(170, 170))
        self.label_pic_under.setMaximumSize(QtCore.QSize(170, 170))
        self.label_pic_under.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_pic_under.setText("")
        self.label_pic_under.setPixmap(QtGui.QPixmap(":/images/images/skadi.jpg"))
        self.label_pic_under.setScaledContents(True)
        self.label_pic_under.setObjectName("label_pic_under")
        self.label_pic = QtWidgets.QLabel(self.widget_pic)
        self.label_pic.setGeometry(QtCore.QRect(0, 0, 170, 170))
        self.label_pic.setMinimumSize(QtCore.QSize(170, 170))
        self.label_pic.setMaximumSize(QtCore.QSize(170, 170))
        self.label_pic.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_pic.setText("")
        self.label_pic.setPixmap(QtGui.QPixmap(":/images/images/skadi.jpg"))
        self.label_pic.setScaledContents(True)
        self.label_pic.setObjectName("label_pic")
        self.horizontalLayout_pic.addWidget(self.widget_pic)
        self.verticalLayout_4.addLayout(self.horizontalLayout_pic)
        self.label_info = QtWidgets.QLabel(self.widget_info)
        self.label_info.setStyleSheet("font: 8pt \"微软雅黑\";")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.verticalLayout_4.addWidget(self.label_info)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget_3 = QtWidgets.QListWidget(self.widget_info)
        self.listWidget_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget_3.setStyleSheet("QListView::item:hover {\n"
"    background-color: transparent;\n"
"    border-left: 3px solid #ff441a;\n"
"}\n"
"QListView::item:selected {\n"
"    background-color: transparent;\n"
"}")
        self.listWidget_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_body.addWidget(self.widget_info, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_body.setStretch(1, 4)
        self.horizontalLayout_body.setStretch(2, 2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_body)
        self.widget_bottom = QtWidgets.QWidget(self.widget)
        self.widget_bottom.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_bottom.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_bottom.setStyleSheet("QWidget#widget_bottom{\n"
"        background:rgb(255, 255, 255);\n"
"        border-bottom-right-radius:10px;\n"
"        border-bottom-left-radius:10px;\n"
"    }")
        self.widget_bottom.setObjectName("widget_bottom")
        self.widget1 = QtWidgets.QWidget(self.widget_bottom)
        self.widget1.setGeometry(QtCore.QRect(11, 10, 931, 42))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_path_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_path_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_path_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_path_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_path_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_path_2.setStyleSheet("QPushButton{\n"
"    image: url(:/icon/images/翻译.png);\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(:/icon/images/翻译 深色.png);\n"
"}\n"
"")
        self.pushButton_path_2.setText("")
        self.pushButton_path_2.setFlat(True)
        self.pushButton_path_2.setObjectName("pushButton_path_2")
        self.horizontalLayout_2.addWidget(self.pushButton_path_2)
        self.pushButton_path = QtWidgets.QPushButton(self.widget1)
        self.pushButton_path.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_path.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_path.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_path.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_path.setStyleSheet("QPushButton{\n"
"    image: url(:/icon/images/folder_add.png);\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(:/icon/images/folder_add 深色.png);\n"
"}\n"
"")
        self.pushButton_path.setText("")
        self.pushButton_path.setFlat(True)
        self.pushButton_path.setObjectName("pushButton_path")
        self.horizontalLayout_2.addWidget(self.pushButton_path)
        self.pushButton_last = QtWidgets.QPushButton(self.widget1)
        self.pushButton_last.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_last.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_last.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_last.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_last.setStyleSheet("QPushButton{\n"
"    image: url(./images/last.png);\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(./images/lastd.png);\n"
"}\n"
"")
        self.pushButton_last.setText("")
        self.pushButton_last.setFlat(True)
        self.pushButton_last.setObjectName("pushButton_last")
        self.horizontalLayout_2.addWidget(self.pushButton_last)
        self.pushButton_start = QtWidgets.QPushButton(self.widget1)
        self.pushButton_start.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_start.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_start.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_start.setStyleSheet("QPushButton{\n"
"    image: url(./images/play button2.png);\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(./images/play button2d.png);\n"
"}")
        self.pushButton_start.setText("")
        self.pushButton_start.setFlat(True)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_2.addWidget(self.pushButton_start)
        self.pushButton_next = QtWidgets.QPushButton(self.widget1)
        self.pushButton_next.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_next.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_next.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_next.setStyleSheet("QPushButton{\n"
"    image: url(./images/next.png);\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(./images/nextd.png);\n"
"}\n"
"")
        self.pushButton_next.setText("")
        self.pushButton_next.setFlat(True)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout_2.addWidget(self.pushButton_next)
        self.pushButton_change_sort_mode = QtWidgets.QPushButton(self.widget1)
        self.pushButton_change_sort_mode.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_change_sort_mode.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_change_sort_mode.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_change_sort_mode.setStyleSheet("QPushButton{\n"
"    image: url(./images/随机播放.png);\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(./images/随机播放 深色.png);\n"
"}")
        self.pushButton_change_sort_mode.setText("")
        self.pushButton_change_sort_mode.setFlat(True)
        self.pushButton_change_sort_mode.setObjectName("pushButton_change_sort_mode")
        self.horizontalLayout_2.addWidget(self.pushButton_change_sort_mode)
        self.label_time_start = QtWidgets.QLabel(self.widget1)
        self.label_time_start.setMinimumSize(QtCore.QSize(0, 0))
        self.label_time_start.setStyleSheet("font: 9pt \"霞鹜文楷\";\n"
"color: #616161;")
        self.label_time_start.setObjectName("label_time_start")
        self.horizontalLayout_2.addWidget(self.label_time_start)
        self.horizontalSlider = QtWidgets.QSlider(self.widget1)
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
" \n"
"border: 0px solid #bbb;\n"
" \n"
"}\n"
" \n"
"QSlider::sub-page:horizontal {\n"
" \n"
"background: #f03e3e;\n"
" \n"
"border-radius: 0px;\n"
" \n"
"margin-top:8px;\n"
" \n"
"margin-bottom:8px;\n"
" \n"
"}\n"
" \n"
"QSlider::add-page:horizontal {\n"
" \n"
"background: #e4e4e4;\n"
" \n"
"border: 0px solid #777;\n"
" \n"
"border-radius: 2px;\n"
" \n"
"margin-top:8px;\n"
" \n"
"margin-bottom:8px;\n"
" \n"
"}\n"
" \n"
"QSlider::handle:horizontal {\n"
" \n"
"background: #f03e3e;\n"
" \n"
"border: 1px solid #f03e3e;\n"
" \n"
"width: 14px;\n"
" \n"
"height:14px;\n"
" \n"
"border-radius: 8px;\n"
" \n"
"margin-top:2px;\n"
" \n"
"margin-bottom:2px;\n"
" \n"
"}\n"
" \n"
"QSlider::handle:horizontal:hover {\n"
" \n"
"background: #c92a2a;\n"
" \n"
"border: 1px solid #c92a2a;\n"
" \n"
"border-radius: 8px;\n"
" \n"
"}\n"
" \n"
"QSlider::sub-page:horizontal:disabled {\n"
" \n"
"background: #bbb;\n"
" \n"
"border-color: #999;\n"
" \n"
"}\n"
" \n"
"QSlider::add-page:horizontal:disabled {\n"
" \n"
"background: #eee;\n"
" \n"
"border-color: #999;\n"
" \n"
"}\n"
" \n"
"QSlider::handle:horizontal:disabled {\n"
" \n"
"background: #eee;\n"
" \n"
"border: 1px solid #aaa;\n"
" \n"
"border-radius: 4px;\n"
" \n"
"}\n"
" ")
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.label_time_end = QtWidgets.QLabel(self.widget1)
        self.label_time_end.setMinimumSize(QtCore.QSize(0, 0))
        self.label_time_end.setStyleSheet("font: 9pt \"霞鹜文楷\";\n"
"color: #616161;")
        self.label_time_end.setObjectName("label_time_end")
        self.horizontalLayout_2.addWidget(self.label_time_end)
        self.pushButton_volume = QtWidgets.QPushButton(self.widget1)
        self.pushButton_volume.setMinimumSize(QtCore.QSize(25, 20))
        self.pushButton_volume.setMaximumSize(QtCore.QSize(25, 20))
        self.pushButton_volume.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_volume.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_volume.setStyleSheet("QPushButton{\n"
"    font: 7pt \"微软雅黑\";\n"
"    color: #f03e3e;\n"
"    border:2px solid #f03e3e;\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: #c92a2a;\n"
"    border:2px solid #c92a2a;\n"
"}")
        self.pushButton_volume.setFlat(True)
        self.pushButton_volume.setObjectName("pushButton_volume")
        self.horizontalLayout_2.addWidget(self.pushButton_volume)
        self.pushButton_is_online = QtWidgets.QPushButton(self.widget1)
        self.pushButton_is_online.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_is_online.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_is_online.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_is_online.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_is_online.setStyleSheet("QPushButton{\n"
"    image: url(:/icon/images/cloud_off.png);\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(:/icon/images/cloud_off 深色.png);\n"
"}")
        self.pushButton_is_online.setText("")
        self.pushButton_is_online.setFlat(True)
        self.pushButton_is_online.setObjectName("pushButton_is_online")
        self.horizontalLayout_2.addWidget(self.pushButton_is_online)
        self.pushButton_random = QtWidgets.QPushButton(self.widget1)
        self.pushButton_random.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_random.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_random.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_random.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_random.setStyleSheet("QPushButton{\n"
"    image: url(:/icon/images/列表循环.png);\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(:/icon/images/列表循环 深色.png);\n"
"}")
        self.pushButton_random.setText("")
        self.pushButton_random.setFlat(True)
        self.pushButton_random.setObjectName("pushButton_random")
        self.horizontalLayout_2.addWidget(self.pushButton_random)
        self.pushButton_random_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_random_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_random_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_random_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_random_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_random_2.setStyleSheet("QPushButton{\n"
"    image: url(./images/info.png);\n"
"}\n"
"QPushButton:hover{\n"
"    image: url(./images/info2.png);\n"
"}")
        self.pushButton_random_2.setText("")
        self.pushButton_random_2.setFlat(True)
        self.pushButton_random_2.setObjectName("pushButton_random_2")
        self.horizontalLayout_2.addWidget(self.pushButton_random_2)
        self.verticalLayout_5.addWidget(self.widget_bottom)
        self.horizontalLayout_9.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The New Musicplayer"))
        self.pushButton_update.setText(_translate("MainWindow", "v0.0.0"))
        self.label_list_name.setText(_translate("MainWindow", "Song list"))
        self.pushButton_save_to_playlist.setText(_translate("MainWindow", "Save"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "search"))
        self.label_name.setText(_translate("MainWindow", "Title"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(5)
        item.setText(_translate("MainWindow", "The New Musicplayer"))
        item = self.listWidget_2.item(6)
        item.setText(_translate("MainWindow", "2023-03-28"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_info.setText(_translate("MainWindow", "MUSIC INFO"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.label_time_start.setText(_translate("MainWindow", "00:00"))
        self.label_time_end.setText(_translate("MainWindow", "00:00"))
        self.pushButton_volume.setText(_translate("MainWindow", "66"))
import resource_rc
