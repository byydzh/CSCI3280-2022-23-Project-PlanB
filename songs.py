import os
import re

from mutagen.wave import WAVE   # need replaced in the future
from mutagen.mp3 import MP3
from mutagen import File        # don't need


class Song:
    def __init__(self, path):
        self.path: str = path
        
        self.title = 'None'
        self.artist = 'None'
        self.album = 'None'
        self.date = 'None'
        self.genre = 'None'
        self.lyrics = ''
        self.cover = b''
        
        self.sample_rate = 0 
        self.bits_per_sample = 0
        self.bitrate = 0
        self.channels = 0
        self.length = 0
        self.audio_type = ''

        try:
            self.load_metadata()
        except Exception as e:
            print(e)

    def load_metadata(self):
        if not self.path:
            return
        filetype = self.path.split('.')[-1].lower()


        if filetype in ['wav', 'wave']:
            self.audio_type = 'WAV'
            audio = WAVE(self.path)
            # print(self.path)
            self.parse_audio_info(audio.info)
            self.parse_id3_tag(audio)
            if self.title == 'None':
                self.title = self.path.split('/')[-1].split('.')[0]

        elif filetype == 'mp3':
            self.audio_type = 'MP3'
            audio = MP3(self.path)
            self.parse_audio_info(audio.info)
            self.parse_id3_tag(audio)

        else:
            self.audio_type = 'UNKNOWN'
            audio = File(self.path)
            #self.parse_audio_info(audio.info)
            #self.parse_id3_tag(audio)

        # load the lyrics file
        if self.lyrics == '' and os.path.exists(os.path.splitext(self.path)[0] + '.lrc'):
            with open(os.path.splitext(self.path)[0] + '.lrc', "r", encoding='utf-8', errors='ignore') as f:
                self.lyrics = f.read()

    def get_lrc_dict(self):
        if not self.lyrics:
            return {}
        lrc_list = self.lyrics.splitlines()
        
        func = re.compile("\\[.*?]")
        lrc_dict = {}
        for item in lrc_list:
            searched = func.search(item)
            if not searched:
                continue
            lrc_time = searched.group()
            time_str_list = lrc_time[1:-1].split(":")
            if not time_str_list[0].isdigit():
                continue
            lrc_time_int = int(time_str_list[0]) * 60000 + int(float(time_str_list[1]) * 1000)
            lrc_text = func.sub('', item)
            lrc_text = ' '.join(lrc_text.split())
            if lrc_dict.get(lrc_time_int):
                lrc_dict[lrc_time_int].append(lrc_text)
            else:
                lrc_dict[lrc_time_int] = [lrc_text]

        return lrc_dict
    

    def parse_audio_info(self, audio_info):
        self.sample_rate = audio_info.sample_rate
        self.channels = audio_info.channels
        self.length = audio_info.length

        if self.audio_type != 'APE':
            self.bitrate = audio_info.bitrate

        if self.audio_type != 'MP3':
            self.bits_per_sample = audio_info.bits_per_sample
            if self.audio_type in ['DSF', 'DFF'] and self.bits_per_sample == 1:
                self.is_hr = True
            elif self.bits_per_sample > 16 and self.sample_rate > 44100:
                self.is_hr = True
                

    def parse_id3_tag(self, audio):
        for item in audio:
            if 'APIC' in item:
                self.cover = audio.get(item).data
            if 'USLT' in item:
                self.lyrics = str(audio.get(item))

        if audio.get('TIT2'):
            self.title = str(audio.get('TIT2'))
        if audio.get('TPE1'):
            self.artist = str(audio.get('TPE1'))
        if audio.get('TALB'):
            self.album = str(audio.get('TALB'))
        if audio.get('TDRC'):
            self.date = str(audio.get('TDRC'))
        if audio.get('TCON'):
            self.genre = str(audio.get('TCON'))