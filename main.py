from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt, QUrl, QTimer, QPoint
from PyQt5.QtGui import QPixmap, QFontDatabase
from PyQt5 import QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QListWidgetItem
from pypinyin import lazy_pinyin, Style

import os
import sys

from Ui_mainwindow import Ui_MainWindow


VERSION = 'v0.0.1'


class PlayerWindow(QtWidgets.QMainWindow):
    """主窗体类"""

    def __init__(self):
        # 继承父类
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # maybe for chinese, can be deleted if don't need
        if os.path.exists("fonts/霞鹜文楷.ttf"):
            QFontDatabase.addApplicationFont("fonts/霞鹜文楷.ttf")

        # window
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_update.setText(VERSION)

        # mouse
        self.setMouseTracking(True)
        self.ui.centralwidget.setMouseTracking(True)
        self.ui.widget.setMouseTracking(True)
        self.ui.widget_bottom.setMouseTracking(True)

        # window's vairable
        self.move_drag = False
        self.move_DragPosition = 0
        self.right_bottom_corner_drag = False
        self.left_bottom_corner_drag = False
        self.left_drag = False
        self.right_drag = False
        self.bottom_drag = False
        self.left_rect = []
        self.right_rect = []
        self.bottom_rect = []
        self.right_bottom_corner_rect = []
        self.left_bottom_corner_rect = []

        # bind buttons
        self.ui.pushButton_red.clicked.connect(self.close_window)
        self.ui.pushButton_green.clicked.connect(self.showMinimized)
        self.ui.pushButton_yellow.clicked.connect(self.maximize_window)
        self.ui.pushButton_start.clicked.connect(self.song_start_switch)
        self.ui.pushButton_path.clicked.connect(self.get_songs_from_directory)
        try:
            self.ui.listWidget.doubleClicked.connect(self.song_double_clicked)
            self.ui.listWidget_2.doubleClicked.connect(self.lrc_double_clicked)
            self.ui.listWidget_3.doubleClicked.connect(self.info_double_clicked)
            self.ui.horizontalSlider.sliderReleased.connect(self.slider_release)
            self.ui.horizontalSlider.sliderPressed.connect(self.slider_press)
            self.ui.horizontalSlider.sliderMoved.connect(self.slider_move)
            self.ui.pushButton_next.clicked.connect(self.play_next)
            self.ui.pushButton_last.clicked.connect(self.play_last)
            self.ui.pushButton_song_find.clicked.connect(self.song_find)
            self.ui.pushButton_save_to_playlist.clicked.connect(self.save_playlist)
            self.ui.pushButton_random.clicked.connect(self.change_play_mode)
            self.ui.pushButton_is_online.clicked.connect(self.change_lrc_mode)
            self.ui.lineEdit.textChanged.connect(self.search_song)
            self.ui.pushButton_is_trans.clicked.connect(self.change_trans_mode)
            self.ui.pushButton_update.clicked.connect(self.get_update)
            self.ui.pushButton_volume.clicked.connect(self.change_volume)
            self.ui.pushButton_change_sort_mode.clicked.connect(self.change_sort_mode)


            # 歌词刷新计时器
            self.lrc_timer = QTimer(self)
            self.lrc_timer.timeout.connect(self.song_timer)
            # 歌曲淡入淡出计时器
            self.volume_smooth_timer = QTimer(self)
            self.volume_smooth_timer.timeout.connect(self.volume_smooth_timeout)
            self.volume_add_buffer = 0
            self.volume_buffer = 0
            self.volume_smooth_low_mode = True
        
        except:
            print("not done")


        self.player = QMediaPlayer(flags=QMediaPlayer.Flags())  # 无参数也行，但是会有提示
        # self.song_selected = Song(None)  # 当前音乐对象
        self.song_path_list = []  # 歌曲路径列表
        self.song_path_playlist = []  # 歌曲路径播放列表
        self.local_path_list = []  # 本地歌曲路径列表
        self.local_songs_count = 0  # 歌曲计数
        self.directory_path = ''  # 歌曲文件夹路径
        self.song_now_path = ''  # 当前歌曲路径
        self.is_started = False  # 播放按钮状态
        self.is_sliderPress = False  # 进度条按压状态
        self.lrc_trans_mode = 1  # 歌词翻译模式
        self.lrc_time_index = 0  # 歌词时间戳标记
        self.song_index = 0  # 歌曲标记
        self.lrc_time_list = []  # 歌词时间戳列表
        self.play_mode = 0  # 播放模式
        self.lrc_mode = 0  # 歌词模式
        self.is_window_maximized = False  # 窗口最大化状态
        self.volume_change_mode = 0  # 点击的音量档位
        self.sort_mode = 0  # 排序方式

        self.ui.label_pic_hires.setVisible(False)  # 是否显示小金标
        self.ui.lineEdit.setClearButtonEnabled(True)  # 显示一个清空按钮
        self.player.setVolume(90)  # 默认音量
        # self.volume_style_refresh() 

        self.thread_load_songs = Thread()
        # self.thread_load_songs.signal_item.connect(self.thread_search_num)
        # self.thread_load_songs.signal_stop.connect(self.thread_search_stop)



    def close_window(self):
        # self.save_setting() # do it in the future
        QCoreApplication.quit()

    def maximize_window(self):
        if self.is_window_maximized:
            self.showNormal()
            self.is_window_maximized = False
        else:
            self.showMaximized()
            self.is_window_maximized = True

    def get_songs_from_directory(self):
        # self.song_pause()
        self.directory_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'choose path', '',
                                                                         options=QtWidgets.QFileDialog.ShowDirsOnly)
        if not self.directory_path:
            print('cancelled')
            return
        self.song_index = 0
        self.ui.listWidget.clear()
        self.get_songs_count()
        if self.local_songs_count == 0:
            mess_str = 'no wav file'
            print(mess_str)
            QtWidgets.QMessageBox.information(self, "cannot find wav file", mess_str, QtWidgets.QMessageBox.Ok)
        else:
            self.ui.horizontalSlider.setMaximum(self.local_songs_count)
            self.ui.horizontalSlider.setMinimum(0)
            self.thread_load_songs.directory_path = self.directory_path
            self.thread_load_songs.start()  # 开始线程，将音乐数据存入数据库

    def get_songs_count(self):
        path_list = []
        for root, dirs, items in os.walk(self.directory_path):
            for item in items:
                file_path = f'{root}/{item}'
                suffix = file_path.split('.')[-1].lower()
                suffix_limit = ['wav'] 
                # suffix_limit = ['flac', 'mp3', 'wav', 'wave', 'dsf', 'dff', 'dsdiff', 'ape', 'm4a'] 
                if suffix not in suffix_limit:
                    continue
                path_list.append(file_path)
        self.local_songs_count = len(path_list)
        self.local_path_list = path_list

    def song_start_switch(self):
        if self.song_now_path == '' and self.local_songs_count != 0:
            self.play_next()
            return
        elif self.song_now_path == '':
            return

        self.volume_buffer = self.player.volume()
        self.volume_add_buffer = 0
        if self.is_started is True:
            # self.song_pause()
            self.volume_smooth_low_mode = True
            self.volume_smooth_timer.start(1)
        else:
            self.volume_smooth_low_mode = False
            self.player.setVolume(0)
            self.song_play()
            self.volume_smooth_timer.start(1)

class Thread(QtCore.QThread):
    signal_stop = QtCore.pyqtSignal()
    signal_item = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.directory_path = ''

    def run(self):
        self.creat_song_table()

    def creat_song_table(self):
        with UsingSqlite() as us:
            us.cursor.execute("drop table if exists music_info")
            us.cursor.execute("""
            create table if not exists music_info (
            id integer primary key autoincrement, 
            file_name text, path text, title text, artist text, album text, date text, genre text,
            mtime int, ctime int
            )""")

            file_num = 0
            for root, dirs, items in os.walk(self.directory_path):
                for item in items:
                    file_path = f'{root}/{item}'
                    file_name = os.path.splitext(item)[0]
                    suffix = file_path.split('.')[-1].lower()
                    suffix_limit = ['flac', 'mp3', 'wav', 'wave', 'dsf', 'dff', 'dsdiff', 'ape', 'm4a']  # 格式限定
                    if suffix not in suffix_limit:
                        continue
                    song = Song(file_path)
                    sql = """
                    insert into music_info (file_name, path, title, artist, album, date, genre, mtime, ctime) 
                    values (?,?,?,?,?,?,?,?,?)
                    """
                    get_mtime = int(os.path.getmtime(file_path))
                    get_ctime = int(os.path.getctime(file_path))
                    params = (file_name, song.path, song.title, song.artist, song.album, song.date, song.genre,
                              get_mtime, get_ctime)
                    us.cursor.execute(sql, params)
                    file_num += 1
                    self.signal_item.emit(file_num)
        self.signal_stop.emit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) 
    player_window = PlayerWindow() 
    player_window.show()
    sys.exit(app.exec_())
