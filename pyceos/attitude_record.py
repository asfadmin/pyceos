# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version("0.9"):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s"
        % (kaitaistruct.__version__)
    )

from . import ascii_int
from . import ascii_float


class AttitudeRecord(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw_npoints = self._io.read_bytes(4)
        _io__raw_npoints = KaitaiStream(BytesIO(self._raw_npoints))
        self.npoints = ascii_int.AsciiInt(_io__raw_npoints)
        self.attitude_data_points = [None] * (self.npoints)
        for i in range(self.npoints):
            self.attitude_data_points[i] = AttitudeRecord.AttitudePoint(
                self._io, self, self._root
            )

    class AttitudePoint(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_gmt_day = self._io.read_bytes(4)
            _io__raw_gmt_day = KaitaiStream(BytesIO(self._raw_gmt_day))
            self.gmt_day = ascii_int.AsciiInt(_io__raw_gmt_day)
            self._raw_gmt_millis = self._io.read_bytes(8)
            _io__raw_gmt_millis = KaitaiStream(BytesIO(self._raw_gmt_millis))
            self.gmt_millis = ascii_int.AsciiInt(_io__raw_gmt_millis)
            self._raw_pitch_flag = self._io.read_bytes(4)
            _io__raw_pitch_flag = KaitaiStream(BytesIO(self._raw_pitch_flag))
            self.pitch_flag = ascii_int.AsciiInt(_io__raw_pitch_flag)
            self._raw_roll_flag = self._io.read_bytes(4)
            _io__raw_roll_flag = KaitaiStream(BytesIO(self._raw_roll_flag))
            self.roll_flag = ascii_int.AsciiInt(_io__raw_roll_flag)
            self._raw_yaw_flag = self._io.read_bytes(4)
            _io__raw_yaw_flag = KaitaiStream(BytesIO(self._raw_yaw_flag))
            self.yaw_flag = ascii_int.AsciiInt(_io__raw_yaw_flag)
            self._raw_pitch = self._io.read_bytes(14)
            _io__raw_pitch = KaitaiStream(BytesIO(self._raw_pitch))
            self.pitch = ascii_float.AsciiFloat(_io__raw_pitch)
            self._raw_roll = self._io.read_bytes(14)
            _io__raw_roll = KaitaiStream(BytesIO(self._raw_roll))
            self.roll = ascii_float.AsciiFloat(_io__raw_roll)
            self._raw_yaw = self._io.read_bytes(14)
            _io__raw_yaw = KaitaiStream(BytesIO(self._raw_yaw))
            self.yaw = ascii_float.AsciiFloat(_io__raw_yaw)
            self._raw_pitch_rate_flag = self._io.read_bytes(4)
            _io__raw_pitch_rate_flag = KaitaiStream(BytesIO(self._raw_pitch_rate_flag))
            self.pitch_rate_flag = ascii_int.AsciiInt(_io__raw_pitch_rate_flag)
            self._raw_roll_rate_flag = self._io.read_bytes(4)
            _io__raw_roll_rate_flag = KaitaiStream(BytesIO(self._raw_roll_rate_flag))
            self.roll_rate_flag = ascii_int.AsciiInt(_io__raw_roll_rate_flag)
            self._raw_yaw_rate_flag = self._io.read_bytes(4)
            _io__raw_yaw_rate_flag = KaitaiStream(BytesIO(self._raw_yaw_rate_flag))
            self.yaw_rate_flag = ascii_int.AsciiInt(_io__raw_yaw_rate_flag)
            self._raw_pitch_rate = self._io.read_bytes(14)
            _io__raw_pitch_rate = KaitaiStream(BytesIO(self._raw_pitch_rate))
            self.pitch_rate = ascii_float.AsciiFloat(_io__raw_pitch_rate)
            self._raw_roll_rate = self._io.read_bytes(14)
            _io__raw_roll_rate = KaitaiStream(BytesIO(self._raw_roll_rate))
            self.roll_rate = ascii_float.AsciiFloat(_io__raw_roll_rate)
            self._raw_yaw_rate = self._io.read_bytes(14)
            _io__raw_yaw_rate = KaitaiStream(BytesIO(self._raw_yaw_rate))
            self.yaw_rate = ascii_float.AsciiFloat(_io__raw_yaw_rate)
