# This script is modified from Mutagen WAVE decoder.
# https://github.com/quodlibet/mutagen/blob/master/mutagen/wave.py
"""Microsoft WAVE/RIFF audio file/stream information and tags."""
# The parsing part of wav file is writen by us.
# We preserve the function of tag reader as an Enhanced Feature.
# The tag reading feature is provided by Mutagen,
# we still keep the ID3 decoder function in the module.


# All the referring part to the Mutagen library are only used to extract the tag of wav file
# The decoding part is originally written

import sys
import struct
# The ID3 part is used as the extension feature
from mutagen.id3 import ID3
from mutagen._riff import (
    IffChunk,
    IffContainerChunkMixin,
    IffFile,
    InvalidChunk,
)
from mutagen._iff import error as IffError
from mutagen.id3._util import ID3NoHeaderError, error as ID3Error
from mutagen._util import (
    loadfile,
    reraise,
)

__all__ = ["WAVE", "Open", "delete"]


class error(IffError):
    """WAVE stream parsing errors."""


class RiffFile(IffFile):
    def __init__(self, fileobj):
        super().__init__(RiffChunk, fileobj)

        if self.root.id != u'RIFF':
            raise InvalidChunk("Root chunk must be a RIFF chunk, got %s"
                               % self.root.id)

        self.file_type = self.root.name


class RiffChunk(IffChunk):
    @classmethod
    def parse_header(cls, header):
        return struct.unpack('<4sI', header)

    @classmethod
    def get_class(cls, id):
        if id in (u'LIST', u'RIFF'):
            return RiffListChunk
        else:
            return cls

    def write_new_header(self, id_, size):
        self._fileobj.write(struct.pack('<4sI', id_, size))

    def write_size(self):
        self._fileobj.write(struct.pack('<I', self.data_size))


class RiffListChunk(RiffChunk, IffContainerChunkMixin):
    def parse_next_subchunk(self):
        return RiffChunk.parse(self._fileobj, self)

    def __init__(self, fileobj, id, data_size, parent_chunk):
        if id not in (u'RIFF', u'LIST'):
            raise InvalidChunk('Expected RIFF or LIST chunk, got %s' % id)

        RiffChunk.__init__(self, fileobj, id, data_size, parent_chunk)
        self.init_container()


class WaveFile(RiffFile):
    """Representation of a RIFF/WAVE file"""

    def __init__(self, fileobj):
        RiffFile.__init__(self, fileobj)

        if self.file_type != u'WAVE':
            raise error("Expected RIFF/WAVE.")

        # Normalize ID3v2-tag-chunk to lowercase
        if u'ID3' in self:
            self[u'ID3'].id = u'id3'


class WaveStreamInfo:

    length = 0.0
    bit_rate = 0
    channels = 0
    sample_rate = 0
    bits_per_sample = 0

    SIZE = 16

    def __init__(self, fileobj):
        wave_file = WaveFile(fileobj)
        try:
            format_chunk = wave_file[u'fmt']
        except KeyError as e:
            raise error(str(e))

        data = format_chunk.read()
        if len(data) < 16:
            raise InvalidChunk()

        info = struct.unpack('<HHLLHH', data[:16])
        self.audio_format, self.channels, self.sample_rate, byte_rate, \
            block_align, self.bits_per_sample = info
        # Compute bit_rate
        self.bit_rate = self.channels * self.bits_per_sample * self.sample_rate

        # Compute duration
        self._number_of_samples = 0
        if block_align > 0:
            data_chunk = wave_file[u'data']
            self._number_of_samples = data_chunk.data_size / block_align
        if self.sample_rate > 0:
            self.length = self._number_of_samples / self.sample_rate


# The ID3 part is used as the extension feature
class WaveID3(ID3):
    """A Wave file with ID3v2 tags"""

    def _pre_load_header(self, fileobj):
        try:
            fileobj.seek(WaveFile(fileobj)[u'id3'].data_offset)
        except (InvalidChunk, KeyError):
            raise ID3NoHeaderError("No ID3 chunk")

    @loadfile(writable=True)
    def save(self, filething, v1=1, v2_version=4, v23_sep='/', padding=None):
        """Save ID3v2 data to the Wave/RIFF file"""

        fileobj = filething.fileobj
        wave_file = WaveFile(fileobj)

        if u'id3' not in wave_file:
            wave_file.insert_chunk(u'id3')

        chunk = wave_file[u'id3']

        try:
            data = self._prepare_data(
                fileobj, chunk.data_offset, chunk.data_size, v2_version,
                v23_sep, padding)
        except ID3Error as e:
            reraise(error, e, sys.exc_info()[2])

        chunk.resize(len(data))
        chunk.write(data)

    def delete(self, filething):
        delete(filething)
        self.clear()


# The ID3 part is used as the extension feature
@loadfile(method=False, writable=True)
def delete(filething):
    try:
        WaveFile(filething.fileobj).delete_chunk(u'id3')
    except KeyError:
        pass


def endswith(text, end):
    # useful for paths which can be both, str and bytes
    if isinstance(text, str):
        if not isinstance(end, str):
            end = end.decode("ascii")
    else:
        if not isinstance(end, bytes):
            end = end.encode("ascii")
    return text.endswith(end)


class WAVE:
    """WAVE(filething)
    A Waveform Audio File Format
    (WAVE, or more commonly known as WAV due to its filename extension)
    Arguments:
        filething (filething)
    Attributes:
        tags (`mutagen.id3.ID3`)
        info (`WaveStreamInfo`)
    """

    _mimes = ["audio/wav", "audio/wave"]


    def score(filename, fileobj, header):
        filename = filename.lower()

        return (header.startswith(b"RIFF") + (header[8:12] == b'WAVE')
                + endswith(filename, b".wav") + endswith(filename, b".wave"))

    def add_tags(self):
        """Add an empty ID3 tag to the file."""
        if self.tags is None:
            self.tags = WaveID3()
        else:
            raise error("an ID3 tag already exists")

    @loadfile()
    def load(self, filething, **kwargs):
        """Load stream and tag information from a file."""

        fileobj = filething.fileobj
        self.info = WaveStreamInfo(fileobj)
        fileobj.seek(0, 0)

        try:
            self.tags = WaveID3(fileobj, **kwargs)
        except ID3NoHeaderError:
            self.tags = None
        except ID3Error as e:
            raise error(e)
        else:
            self.tags.filename = self.filename


Open = WAVE