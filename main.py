from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, Qt, QUrl, QTimer, QPoint
from PyQt5.QtGui import QPixmap, QFontDatabase
from PyQt5 import QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QListWidgetItem
from pypinyin import lazy_pinyin, Style
from pydub import AudioSegment
from PyQt5.QtWidgets import QMessageBox

import sqlite3
import os
import sys
import random
import json
import music_tag


from sqlite_lib import UsingSqlite
from Ui_mainwindow import Ui_MainWindow
from songs import Song

import socket
import threading

sharing = 0
VERSION = 'v0.2.0'
third_party_db_path = ""
SPECIAL_FILE_IDENTIFIER = "SPECIAL_FILE_IDENTIFIER"

# p2p sharing function: send_file, broadcast_file, download_file
def send_file(file_path, client_socket):
    with open(file_path, "rb") as file:
        chunk = file.read(1024)
        while chunk:
            client_socket.send(chunk)
            chunk = file.read(1024)
    client_socket.close()


def broadcast_file(file_path, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", port))
    server_socket.listen(5)

    print(f"Broadcasting file: {file_path}")

    client_socket, client_addr = server_socket.accept()
    print(f"Connected to {client_addr}")
    threading.Thread(target=send_file, args=(file_path, client_socket)).start()

    sys.exit()


def download_file(file_path, host, port):
    download_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    download_socket.connect((host, port))

    with open(file_path, "wb") as file:
        chunk = download_socket.recv(1024)
        while chunk:
            file.write(chunk)
            chunk = download_socket.recv(1024)

    download_socket.close()
    print(f"File downloaded: {file_path}")

def download_file_multi(file_path, host1, port1, host2, port2):
    download_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    download_socket1.connect((host1, port1))
    download_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    download_socket2.connect((host2, port2))
    file_data1 = bytearray()
    file_data2 = bytearray()

    chunk1 = download_socket1.recv(1024)
    chunk2 = download_socket2.recv(1024)
    while chunk1:
        file_data1.extend(chunk1)
        chunk1 = download_socket1.recv(1024)
    while chunk2:
        file_data2.extend(chunk2)
        chunk2 = download_socket2.recv(1024)

    download_socket1.close()
    download_socket2.close()

    merged_data = bytearray()
    i, j = 0, 0
    flag = 0
    while i < len(file_data1) and j < len(file_data2):
        if flag==0:
            merged_data.append(file_data1[i])
            flag = 1
        else:
            merged_data.append(file_data2[j])
            flag = 0
        i += 1
        j += 1

    while i < len(file_data1):
        merged_data.append(file_data1[i])
        i += 1

    while j < len(file_data2):
        merged_data.append(file_data2[j])
        j += 1

    with open(file_path, "wb") as file:
        file.write(merged_data)

    print(f"File downloaded: {file_path}")


def download_file_living(file_path, host, port):
    download_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    download_socket.connect((host, port))
    file_data = bytearray()

    chunk = download_socket.recv(1024)

    while chunk:
        file_data.extend(chunk)
        chunk = download_socket.recv(1024)

    download_socket.close()
    merged_data = bytearray()
    i = 0

    while i < len(file_data):
        merged_data.append(file_data[i])
        i += 1
    with open(file_path, "wb") as file:
        file.write(merged_data)
    split_wav_file(file_path, output_dir="output")
    os.remove(file_path)

def split_wav_file(input_file, output_dir, chunk_size=1024):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    
    audio = AudioSegment.from_wav(input_file)
    audio_length = len(audio)
    num_chunks = audio_length // chunk_size + (1 if audio_length % chunk_size != 0 else 0)

    for i in range(num_chunks):
        start_time = i * chunk_size
        end_time = min((i + 1) * chunk_size, audio_length)
        chunk = audio[start_time:end_time]
        chunk.export(os.path.join(output_dir, f"chunk_{i}.wav"), format="wav")
        #print(f"Saved chunk {i + 1} of {num_chunks}")




# make the window draggable
class DraggableWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._is_dragging = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = True
            self._drag_offset = event.pos()

    def mouseMoveEvent(self, event):
        if self._is_dragging:
            self.parent().move(self.parent().pos() + event.pos() - self._drag_offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = False

class PlayerWindow(QtWidgets.QMainWindow):
 
    def __init__(self):
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

        self.ui.widget_top = DraggableWidget(self)
        self.ui.widget_top.setGeometry(0, 0, 200, 30)

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
        self.ui.pushButton_song_find.clicked.connect(self.song_find)
        self.ui.pushButton_save_to_playlist.clicked.connect(self.save_playlist)
        self.ui.listWidget.doubleClicked.connect(self.song_double_clicked)
        self.ui.listWidget_2.doubleClicked.connect(self.lrc_double_clicked)
        self.ui.listWidget_3.doubleClicked.connect(self.info_double_clicked)
        self.ui.lineEdit.textChanged.connect(self.search_song)
        self.ui.pushButton_next.clicked.connect(self.play_next)
        self.ui.pushButton_last.clicked.connect(self.play_last)
        self.ui.horizontalSlider.sliderReleased.connect(self.slider_release)
        self.ui.horizontalSlider.sliderPressed.connect(self.slider_press)
        self.ui.horizontalSlider.sliderMoved.connect(self.slider_move)
        self.ui.pushButton_volume.clicked.connect(self.change_volume)
        self.ui.pushButton_change_sort_mode.clicked.connect(self.change_sort_mode)
        self.ui.pushButton_is_online.clicked.connect(self.p2p_share)
        self.ui.pushButton_random.clicked.connect(self.p2p_share_multi)
        self.ui.pushButton_random_2.clicked.connect(self.set_metadata)
        self.ui.pushButton_path_2.clicked.connect(self.setthirddir)
       
        try:
            self.ui.pushButton_is_trans.clicked.connect(self.change_trans_mode)
            self.ui.pushButton_update.clicked.connect(self.get_update)
        
        except:
            print("not done")


        # Lyric refresh timer
        self.lrc_timer = QTimer(self)
        self.lrc_timer.timeout.connect(self.song_timer)
        # Song Fade Timer
        self.volume_smooth_timer = QTimer(self)
        self.volume_smooth_timer.timeout.connect(self.volume_smooth_timeout)
        self.volume_add_buffer = 0
        self.volume_buffer = 0
        self.volume_smooth_low_mode = True

        self.player = QMediaPlayer(flags=QMediaPlayer.Flags())  
        self.song_selected = Song(None)  # current song
        self.song_path_list = []  # song path list
        self.song_path_playlist = []  # song path play list
        self.local_path_list = []  # local path list
        self.local_songs_count = 0  # songs number count
        self.directory_path = ''  # song directory path
        self.song_now_path = ''  # current song path
        self.is_started = False  # start status default to False
        self.is_sliderPress = False  # slide press status default to False
        self.lrc_time_index = 0  # lyric time index
        self.song_index = 0  # song index
        self.lrc_time_list = []  # lyric time list
        self.play_mode = 0  # play mode
        self.lrc_mode = 0  # lyric mode
        self.is_window_maximized = False  # maximize window
        self.volume_change_mode = 0  # change volume mode
        self.sort_mode = 0  # sort mode

        self.ui.lineEdit.setClearButtonEnabled(True)  # show a clear button
        self.player.setVolume(90)  # default volume
        # self.volume_style_refresh() 

        self.ui.listWidget_2.setWordWrap(True)
        self.ui.listWidget_3.setWordWrap(True)
        self.ui.label_name.setWordWrap(True)

        self.ui.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ui.listWidget.verticalScrollBar().setSingleStep(15)
        self.ui.listWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ui.listWidget_2.verticalScrollBar().setSingleStep(15)

        self.thread_load_songs = Thread()
        self.thread_load_songs.signal_item.connect(self.thread_search_num)
        self.thread_load_songs.signal_stop.connect(self.thread_search_stop)

        self.db_path = UsingSqlite.DB_PATH
        self.setting_path = 'setting.json'

        if os.path.exists(self.db_path):
            self.load_setting()

    def load_setting(self):
        if not os.path.exists(self.setting_path):
            return
        with open('setting.json') as f:
            config = json.load(f)
            self.directory_path = config.get('directory_path')
            if self.directory_path:
                self.update_songs()


            self.lrc_mode = config.get('lrc_mode', 0)
            #self.set_lrc_mode_stylesheet()

            self.player.setVolume(config.get('player_volume', 90))
            self.volume_style_refresh()

            self.sort_mode = config.get('sort_mode', 0)
            self.set_sort_mode_stylesheet()

            if os.path.exists(self.db_path):
                self.select_songs('')
                self.song_path_playlist = self.song_path_list.copy()

            self.play_mode = config.get('play_mode', 0)
            self.set_play_mode()
            self.set_play_mode_stylesheet()

    def save_setting(self):
        config = {
            "directory_path": self.directory_path,
            "play_mode": self.play_mode,
            "lrc_mode": self.lrc_mode,
            "player_volume": self.player.volume(),
            "sort_mode": self.sort_mode
        }
        with open(self.setting_path, 'w') as f:
            json.dump(config, f)
    
    def slider_move(self):
        """Move slider, refresh tab"""
        self.ui.label_time_start.setText(self.ms_to_str(self.ui.horizontalSlider.value()))

    def slider_release(self):
        """Release the slider to adjust the progress"""
        self.player.setPosition(self.ui.horizontalSlider.value())
        self.lrc_time_index = 0
        self.is_sliderPress = False

    def slider_press(self):
        """press the slide bar"""
        self.is_sliderPress = True

    def lrc_double_clicked(self):
        """Double-click the lyrics to jump to the corresponding time"""
        # The timestamp of the lyrics has been obtained
        if len(self.lrc_time_list) != 0:
            print(f'jump to {self.lrc_time_list[self.ui.listWidget_2.currentRow()]}')
            self.player.setPosition(self.lrc_time_list[self.ui.listWidget_2.currentRow()])
            self.lrc_time_index = 0

    @staticmethod
    def ms_to_str(ms):
        """Convert millisecond time to timestamp"""
        s, ms = divmod(ms, 1000)
        m, s = divmod(s, 60)
        # h, m = divmod(m, 60)
        return f'{str(m).zfill(2)}:{str(s).zfill(2)}'

    def song_timer(self):
        """timer，500ms"""
        # time stamp formatting
        if not self.is_sliderPress:
            self.ui.label_time_start.setText(self.ms_to_str(self.player.position()))
            self.ui.label_time_end.setText(self.ms_to_str(self.player.duration()))
        # Lyric Timestamp Positioning
        if len(self.lrc_time_list) != 0:
            while True:
                # Guarantee that the list does not exceed the limit
                if self.lrc_time_index > len(self.lrc_time_list) - 1:
                    break
                # Match Lyric Time
                elif self.lrc_time_list[self.lrc_time_index] < self.player.position():
                    self.lrc_time_index += 1
                else:
                    break
            # Move to the corresponding position and select
            # self.ui.listWidget_2.verticalScrollBar().setSliderPosition(self.lrc_time_index - 1)
            self.ui.listWidget_2.setCurrentRow(self.lrc_time_index - 1)
            item = self.ui.listWidget_2.item(self.lrc_time_index - 1)
            self.ui.listWidget_2.scrollToItem(item, QtWidgets.QAbstractItemView.PositionAtCenter)

        # set slider limits
        self.ui.horizontalSlider.setMaximum(self.player.duration())
        self.ui.horizontalSlider.setMinimum(0)
        # Release the slider to adjust the progress
        if not self.is_sliderPress:
            self.ui.horizontalSlider.setValue(self.player.position())
        # song finished
        if self.player.position() == self.player.duration():
            print('Time over')
            self.play_next()

    def volume_smooth_timeout(self):
        """volume fade"""
        volume = self.volume_buffer  # get the volume
        if volume == 0:  # in case volume = 0
            self.volume_smooth_timer.stop()
        else:
            volume_step = volume/500  # Interrupt once every 1ms, a total of 500ms, that is, enter 500 times
            self.volume_add_buffer += volume_step
            if self.volume_add_buffer > 1:  # Cache floats, pass integers
                self.volume_add_buffer -= 1
                if self.volume_smooth_low_mode:  # parse
                    if self.player.volume() - 1 >= 0:
                        self.player.setVolume(self.player.volume() - 1)
                    else:
                        self.song_pause()
                        self.volume_smooth_timer.stop()
                        self.player.setVolume(volume)
                else:  # play
                    if self.player.volume() + 1 <= volume:
                        self.player.setVolume(self.player.volume() + 1)
                    else:
                        self.volume_smooth_timer.stop()

    def volume_add(self, step=5):
        volume = self.player.volume()
        if volume + step > 100:
            volume = 100
        else:
            volume += step
        self.player.setVolume(volume)
        print(f'Volume adjusted to: {volume}')
        self.volume_style_refresh()

    def volume_sub(self, step=5):
        volume = self.player.volume()
        if volume - step < 0:
            volume = 0
        else:
            volume -= step
        self.player.setVolume(volume)
        print(f'Volume to: {volume}')
        self.volume_style_refresh()

    def volume_style_refresh(self):
        volume = self.player.volume()
        if volume == 100:
            self.ui.pushButton_volume.setText('M')
        else:
            self.ui.pushButton_volume.setText(str(volume))

    def change_volume(self):
        volume = self.player.volume()
        if volume == 0:
            volume_out = 100
        else:
            volume_out = volume - 20
            if volume_out < 0:
                volume_out = 0
        self.player.setVolume(volume_out)
        self.volume_style_refresh()

    def change_sort_mode(self):
        self.sort_mode += 1
        if self.sort_mode > 2:
            self.sort_mode = 0
        self.set_sort_mode_stylesheet()

    def set_sort_mode_stylesheet(self):
        if self.sort_mode == 0:
            text = 'Sort by alphabetical order'
        elif self.sort_mode == 1:
            text = 'Sort by modification time'
        else:
            text = 'Sort by creation time'
        self.ui.pushButton_change_sort_mode.setToolTip(text)
        self.select_songs(self.ui.lineEdit.text())

    def set_play_mode(self):
        if self.play_mode == 0:  # in order
            self.song_path_playlist.sort(key=lambda x: x['index'])
            if self.song_now_path != '':
                for item in self.song_path_playlist:
                    if item['path'] == self.song_now_path:
                        self.song_index = self.song_path_playlist.index(item)
        elif self.play_mode == 1:  # single recycle
            pass
        elif self.play_mode == 2:  # random
            random.shuffle(self.song_path_playlist)

    def set_play_mode_stylesheet(self):
        return



    def close_window(self):
        self.save_setting()
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
            mess_str = 'no proper music file'
            print(mess_str)
            QtWidgets.QMessageBox.information(self, "cannot find music file", mess_str, QtWidgets.QMessageBox.Ok)
        else:
            self.ui.horizontalSlider.setMaximum(self.local_songs_count)
            self.ui.horizontalSlider.setMinimum(0)
            self.thread_load_songs.directory_path = self.directory_path
            self.thread_load_songs.start()

    def get_songs_count(self):
        path_list = []
        for root, dirs, items in os.walk(self.directory_path):
            for item in items:
                file_path = f'{root}/{item}'
                suffix = file_path.split('.')[-1].lower()
                suffix_limit = ['wav', 'wave', 'mp3'] 
                # suffix_limit = ['flac', 'mp3', 'wav', 'wave', 'dsf', 'dff', 'dsdiff', 'ape', 'm4a'] 
                if suffix not in suffix_limit:
                    continue
                path_list.append(file_path)
        self.local_songs_count = len(path_list)
        self.local_path_list = path_list

    def thread_search_num(self, data):
        self.ui.horizontalSlider.setValue(data)

    def thread_search_stop(self):
        self.select_songs('')
        self.song_path_playlist = self.song_path_list.copy()
        self.set_play_mode()
        self.save_setting()

    def search_song(self):
        if os.path.exists(self.db_path):
            self.select_songs(self.ui.lineEdit.text())
    def upload_download(self, path):
        # connect to the database
        conn = sqlite3.connect(path)
        # create a cursor object
        c = conn.cursor()
        sql = f"select * from music_info "
        # execute a SELECT statement to retrieve all songs in the database
        c.execute(sql)
        # search for a specific song by title
        # print the results of the search
        result = c.fetchall()
        for item in result:
            new_path = self.directory_path +"/"+ item[1] + ".wav"
            if not new_path:
                try:
                    with open(new_path, "w") as f:
                        f.write("#")
                        f.close()
                except Exception:
                    continue
        # close the cursor and database connection
        c.close()
        conn.close()

    def setthirddir(self):
        global third_party_db_path
        dir, format=  QFileDialog.getOpenFileName(None, "Open 3rd party DB File", "", "(*.db)")
        if dir == "":
            return
        third_party_db_path = dir
        self.upload_download(third_party_db_path)

        
    def select_songs(self, text):
        with UsingSqlite() as us:
            text = '%{}%'.format(text)
            sql = """
            select * from music_info 
            where title like ? or artist like ? or album like ? or genre like ? or date like ? or file_name like ?
            """
            params = (text, text, text, text, text, text)
            result = us.fetch_all(sql, params)

        for item in result:
            if item['title'] == 'None':
                item['title'] = item['file_name']

        if self.sort_mode == 0:
            # sort by pinyin/alpha beta
            result = sorted(result, key=lambda x: ''.join(lazy_pinyin(x['title'], style=Style.TONE3)).lower())
        elif self.sort_mode == 1:
            # sort by modify time
            result = sorted(result, key=lambda x: x['mtime'], reverse=True)
        elif self.sort_mode == 2:
            # sort by creat time
            result = sorted(result, key=lambda x: x['ctime'], reverse=True)

        self.ui.listWidget.clear()
        self.song_path_list = []
        count = 0
        for item in result:
            self.ui.listWidget.addItem(item['title'] + '\n- ' + item['artist'])
            self.song_path_list.append({
                'index': count,
                'path': item['path']
            })
            count += 1
        self.local_songs_count = count
        self.ui.label_list_name.setText(f'song list({count})')

    def update_songs(self):
        def list_compare(local_list, db_list):
            local_list = set(local_list)
            db_list = set(db_list)
            _updated_list = local_list - db_list
            _removed_list = db_list - local_list
            return _updated_list, _removed_list

        self.get_songs_count()

        with UsingSqlite() as us:
            sql = 'select path from music_info'
            results = us.fetch_all(sql)
            sql_list = []
            for result in results:
                sql_list.append(result['path'])
            updated_list, removed_list = list_compare(self.local_path_list, sql_list)

            if len(updated_list) == 0 and len(removed_list) == 0:
                print('counted fine')
            else:
                # update
                for path in updated_list:
                    song = Song(path)
                    sql = """
                        insert into music_info (file_name, path, title, artist, album, date, genre, mtime, ctime) 
                        values (?,?,?,?,?,?,?,?,?)
                    """
                    file_name = song.path.split('/')[-1]
                    get_mtime = int(os.path.getmtime(song.path))
                    get_ctime = int(os.path.getctime(song.path))
                    params = (file_name, song.path, song.title, song.artist, song.album, song.date, song.genre,
                              get_mtime, get_ctime)
                    us.cursor.execute(sql, params)
                    print(f'inserted{path}')

                # replace
                for path in removed_list:
                    sql = """
                        delete from music_info
                        where path like ?
                    """
                    params = (path,)
                    us.cursor.execute(sql, params)
                    print(f'remove{path}')

                QtWidgets.QMessageBox.information(self, "database updated", QtWidgets.QMessageBox.Ok)

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

    def song_find(self):
        # self.ui.listWidget.verticalScrollBar().setSliderPosition(self.song_index)
        flag = False
        song_index = 0
        for item in self.song_path_list:
            if item['path'] == self.song_now_path:
                song_index = self.song_path_list.index(item)
                flag = True
        if flag:
            self.ui.listWidget.setCurrentRow(song_index)
            item = self.ui.listWidget.item(song_index)
            self.ui.listWidget.scrollToItem(item, QtWidgets.QAbstractItemView.PositionAtTop)

    def save_playlist(self):
        self.song_path_playlist = self.song_path_list.copy()
        self.set_play_mode()
        QtWidgets.QMessageBox.information(self, "save successfully", 'the playlist has been replaced', QtWidgets.QMessageBox.Ok)


    def song_double_clicked(self):
        song_index = self.ui.listWidget.currentRow()
        song_dict: dict = self.song_path_list[song_index]
        self.song_now_path = song_dict['path']
        if self.play_mode == 2:  # random
            random.shuffle(self.song_path_playlist)

        for item in self.song_path_playlist:
            if item['path'] == self.song_now_path:
                self.song_index = self.song_path_playlist.index(item)
        self.play_init()

    def info_double_clicked(self):
        if self.song_now_path:
            text = self.ui.listWidget_3.currentItem().text().split('：')[-1]
            self.ui.lineEdit.setText(text)

    def play_init(self):
        self.player.setMedia(QMediaContent(QUrl(self.song_now_path)))
        self.song_data_init()
        self.song_play()

    def play_next(self):
        print('Next')
        print(self.song_path_playlist)
        if len(self.song_path_playlist) == 0:
            return
        elif self.play_mode != 1 and self.song_now_path != '':
            self.song_index += 1
            if self.song_index > len(self.song_path_playlist) - 1:
                self.song_index = 0
        self.song_now_path = self.song_path_playlist[self.song_index]['path']
        self.play_init()
        self.song_find()

    def play_last(self):
        print('Last')
        if len(self.song_path_playlist) == 0:
            return
        elif self.play_mode != 1 and self.song_now_path != '':
            self.song_index -= 1
            if self.song_index < 0 or (self.song_index > len(self.song_path_playlist) - 1):
                self.song_index = len(self.song_path_playlist) - 1
        self.song_now_path = self.song_path_playlist[self.song_index]['path']
        self.play_init()
        self.song_find()
    
    def is_special_file(self, filename):
        try:
            with open(filename, "r") as f:
                content = f.read()
                if "#" in content:
                    return True
                else:
                    return False
        except Exception:
            print("File do not exist")
            return False

    def song_play(self):
        print(self.song_path_playlist[self.song_index]['path'])
        if self.is_special_file(self.song_path_playlist[self.song_index]['path']) is True:
            QtWidgets.QMessageBox.information(self, "warning", 'please download it online', QtWidgets.QMessageBox.Ok)
        self.player.play()
        self.lrc_timer.start(500)
        self.is_started = True
        print('Play')
        self.ui.pushButton_start.setToolTip('暂停')
        self.ui.pushButton_start.setStyleSheet("QPushButton{\n"
                                               "image: url(./images/pause button2.png);\n}\n"
                                               "QPushButton:hover{\n"
                                               "image: url(./images/pause button2d.png);\n}")

    def song_pause(self):
        self.player.pause()
        self.lrc_timer.stop()
        self.is_started = False
        print('Pause')
        self.ui.pushButton_start.setToolTip('播放')
        self.ui.pushButton_start.setStyleSheet("QPushButton{\n"
                                               "image: url(./images/play button2.png);\n}\n"
                                               "QPushButton:hover{\n"
                                               "image: url(./images/play button2d.png);\n}")
        
    
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

    def song_data_init(self):
        self.song_selected = Song(self.song_now_path)

        self.song_lrc_init()

        self.ui.label_pic.clear()
        pix = QPixmap()
        pix.loadFromData(self.song_selected.cover)
        self.ui.label_pic.setPixmap(pix)
        self.ui.label_pic.setScaledContents(True)

        self.ui.listWidget_3.clear()
        self.ui.label_name.setText(self.song_selected.title)
        self.setWindowTitle(self.song_selected.title + ' - ' + self.song_selected.artist + ' - LrcMusicPlayer')
        self.ui.listWidget_3.addItem(f'Title: {self.song_selected.title}')
        self.ui.listWidget_3.addItem(f'Aritst:{self.song_selected.artist}')
        self.ui.listWidget_3.addItem(f'Album: {self.song_selected.album}')
        self.ui.listWidget_3.addItem(f'Date:  {self.song_selected.date}')
        self.ui.listWidget_3.addItem(f'Genre: {self.song_selected.genre}')

        print(self.song_selected)
        if self.song_selected.bits_per_sample == 0:
            self.ui.label_info.setText(
                f'{round(self.song_selected.sample_rate / 1000, 1)} kHz / '
                f'{self.song_selected.audio_type}'
            )
        else:
            self.ui.label_info.setText(
                f'{round(self.song_selected.sample_rate / 1000, 1)} kHz / '
                f'{self.song_selected.bits_per_sample} bits / '
                f'{self.song_selected.audio_type}'
            )

    def song_lrc_init(self):

        self.lrc_time_index = 0
        self.ui.listWidget_2.clear()
        lrc_dict = self.song_selected.get_lrc_dict()
        self.lrc_time_list = list(lrc_dict.keys())
        
        if len(self.lrc_time_list) != 0:
            for lrc_time in self.lrc_time_list:
                lrc_output = lrc_dict[lrc_time][0]

                item = QListWidgetItem(lrc_output)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.ui.listWidget_2.addItem(item)
        else:
            item = QListWidgetItem('There are no lyrics')
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.listWidget_2.addItem(item)

    def p2p_share(self):
        
        dialog = QtWidgets.QDialog()
        
        items = ["broadcast", "download"]
        # get the sharing mode
        sharing_mode, ok = QtWidgets.QInputDialog.getItem(dialog, "Sharing Mode", "Enter sharing mode:", items, 0, False)
        if not ok:
            return None, None, None, None
        # get the file path
        if sharing_mode == "broadcast":    
            file_path, format=  QFileDialog.getOpenFileName(None, "Open File", "", "(*.*)")
            if file_path == "":
                return None, None, None, None
            
        elif sharing_mode == "download":
            format, ok = QtWidgets.QInputDialog.getText(dialog, "File Format", "Enter file format:")
            if not ok:
                return None, None, None, None
            directory_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory", "", options=QtWidgets.QFileDialog.ShowDirsOnly)
            if directory_path == "":
                return None, None, None, None
            i = 1
            while True:
                file_name = str(i) + '.' + format
                file_path = directory_path + '/'+ file_name
                if not os.path.exists(file_path):
                    break
                i += 1
            
        # get the port number    
        port_number, ok = QtWidgets.QInputDialog.getInt(dialog, "Port Number", "Enter port number:")
        if not ok:
            return None, None, None, None
        
        # get the server ip address        
        if sharing_mode == "download":
            server_ip_address, ok = QtWidgets.QInputDialog.getText(dialog, "Server IP Address", "Enter server IP address:")
            if not ok:
                return None, None, None, None
        
        
        if sharing_mode == "broadcast":
            broadcast_thread = threading.Thread(target=broadcast_file, args=(file_path, port_number))
            broadcast_thread.start()
        elif sharing_mode == "download":
            living, ok = QtWidgets.QInputDialog.getText(dialog, "living?", "Enter Y/N:")
            print(living)
            if living == 'Y':
                download_thread = threading.Thread(target=download_file_living, args=(file_path, server_ip_address, port_number))
            else:
                download_thread = threading.Thread(target=download_file, args=(file_path, server_ip_address, port_number))
            download_thread.start()
        return # sharing_mode, file_path, port_number, server_ip_address
    
    def p2p_share_multi(self):
        dialog = QtWidgets.QDialog()
        
        items = ["broadcast", "download"]
        # get the sharing mode
        sharing_mode, ok = QtWidgets.QInputDialog.getItem(dialog, "Sharing Mode", "Enter sharing mode:", items, 0, False)
        if not ok:
            return None, None, None, None
        # get the file path
        if sharing_mode == "broadcast":    
            file_path, format=  QFileDialog.getOpenFileName(None, "Open File", "", "(*.*)")
            if file_path == "":
                return None, None, None, None
        elif sharing_mode == "download":
            format, ok = QtWidgets.QInputDialog.getText(dialog, "File Format", "Enter file format:")
            if not ok:
                return None, None, None, None
            directory_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory", "", options=QtWidgets.QFileDialog.ShowDirsOnly)
            if directory_path == "":
                return None, None, None, None
            i = 1
            while True:
                file_name = str(i) + '.' + format
                file_path = directory_path + '/'+ file_name
                if not os.path.exists(file_path):
                    break
                i += 1

        if sharing_mode == "broadcast":    
            port_number, ok = QtWidgets.QInputDialog.getInt(dialog, "Port Number", "Enter port number:")
            if not ok:
                return None, None, None, None
        elif sharing_mode == "download":
            server_ip_address1, ok = QtWidgets.QInputDialog.getText(dialog, "Server IP Address1", "Enter server IP address1:")
            if not ok:
                return None, None, None, None
            port_number1, ok = QtWidgets.QInputDialog.getInt(dialog, "Port Number1", "Enter port number1:")
            if not ok:
                return None, None, None, None
            server_ip_address2, ok = QtWidgets.QInputDialog.getText(dialog, "Server IP Address2", "Enter server IP address2:")
            if not ok:
                return None, None, None, None
            port_number2, ok = QtWidgets.QInputDialog.getInt(dialog, "Port Number2", "Enter port number2:")
            if not ok:
                return None, None, None, None
        
        
        if sharing_mode == "broadcast":
            broadcast_thread = threading.Thread(target=broadcast_file, args=(file_path, port_number))
            broadcast_thread.start()
        elif sharing_mode == "download":
            download_thread = threading.Thread(target=download_file_multi, args=(file_path, server_ip_address1, port_number1 , server_ip_address2, port_number2))
            download_thread.start()
        return

    def set_metadata(self):
        dialog = QtWidgets.QDialog()
        mypath = self.song_path_playlist[self.song_index]['path']
        f = music_tag.load_file(mypath)
        print(mypath)
        title = f['title']
        artist = f['artist']
        album = f['album'] 
        #date = f['date']
        genre = f['genre']
        title, ok = QtWidgets.QInputDialog.getText(dialog, "new title", "Enter new title:")
        if ok:
            f['title'] = title
        artist, ok = QtWidgets.QInputDialog.getText(dialog, "new artist", "Enter new artist:")
        if ok:
            f['artist'] = artist
        album, ok = QtWidgets.QInputDialog.getText(dialog, "new album", "Enter new album:")
        if ok:
            f['album'] = album
        #date, ok = QtWidgets.QInputDialog.getText(dialog, "new date", "Enter new date:")
        #if ok:
        #    f['date'] = date
        genre, ok = QtWidgets.QInputDialog.getText(dialog, "new genre", "Enter new genre:")
        if ok:
            f['genre'] = genre

        f.save()

 

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
                    # suffix_limit = ['flac', 'mp3', 'wav', 'wave', 'dsf', 'dff', 'dsdiff', 'ape', 'm4a']
                    suffix_limit = ['wav', 'wave', 'mp3']
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
