# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version("0.9"):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s"
        % (kaitaistruct.__version__)
    )

from . import ascii_float
from . import ascii_int


class PlatformPositionRecord(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.orbit_ele_desg = (self._io.read_bytes(32)).decode("ascii")
        self._raw_orbit_ele = [None] * (6)
        self.orbit_ele = [None] * (6)
        for i in range(6):
            self._raw_orbit_ele[i] = self._io.read_bytes(16)
            _io__raw_orbit_ele = KaitaiStream(BytesIO(self._raw_orbit_ele[i]))
            self.orbit_ele[i] = ascii_float.AsciiFloat(_io__raw_orbit_ele)

        self._raw_npoints = self._io.read_bytes(4)
        _io__raw_npoints = KaitaiStream(BytesIO(self._raw_npoints))
        self.npoints = ascii_int.AsciiInt(_io__raw_npoints)
        self._raw_year = self._io.read_bytes(4)
        _io__raw_year = KaitaiStream(BytesIO(self._raw_year))
        self.year = ascii_int.AsciiInt(_io__raw_year)
        self._raw_month = self._io.read_bytes(4)
        _io__raw_month = KaitaiStream(BytesIO(self._raw_month))
        self.month = ascii_int.AsciiInt(_io__raw_month)
        self._raw_day = self._io.read_bytes(4)
        _io__raw_day = KaitaiStream(BytesIO(self._raw_day))
        self.day = ascii_int.AsciiInt(_io__raw_day)
        self._raw_gmt_day = self._io.read_bytes(4)
        _io__raw_gmt_day = KaitaiStream(BytesIO(self._raw_gmt_day))
        self.gmt_day = ascii_int.AsciiInt(_io__raw_gmt_day)
        self._raw_gmt_sec = self._io.read_bytes(22)
        _io__raw_gmt_sec = KaitaiStream(BytesIO(self._raw_gmt_sec))
        self.gmt_sec = ascii_float.AsciiFloat(_io__raw_gmt_sec)
        self._raw_data_int = self._io.read_bytes(22)
        _io__raw_data_int = KaitaiStream(BytesIO(self._raw_data_int))
        self.data_int = ascii_float.AsciiFloat(_io__raw_data_int)
        self.ref_coord = (self._io.read_bytes(64)).decode("ascii")
        self._raw_hr_angle = self._io.read_bytes(22)
        _io__raw_hr_angle = KaitaiStream(BytesIO(self._raw_hr_angle))
        self.hr_angle = ascii_float.AsciiFloat(_io__raw_hr_angle)
        self._raw_alt_poserr = self._io.read_bytes(16)
        _io__raw_alt_poserr = KaitaiStream(BytesIO(self._raw_alt_poserr))
        self.alt_poserr = ascii_float.AsciiFloat(_io__raw_alt_poserr)
        self._raw_crt_poserr = self._io.read_bytes(16)
        _io__raw_crt_poserr = KaitaiStream(BytesIO(self._raw_crt_poserr))
        self.crt_poserr = ascii_float.AsciiFloat(_io__raw_crt_poserr)
        self._raw_rad_poserr = self._io.read_bytes(16)
        _io__raw_rad_poserr = KaitaiStream(BytesIO(self._raw_rad_poserr))
        self.rad_poserr = ascii_float.AsciiFloat(_io__raw_rad_poserr)
        self._raw_alt_velerr = self._io.read_bytes(16)
        _io__raw_alt_velerr = KaitaiStream(BytesIO(self._raw_alt_velerr))
        self.alt_velerr = ascii_float.AsciiFloat(_io__raw_alt_velerr)
        self._raw_crt_velerr = self._io.read_bytes(16)
        _io__raw_crt_velerr = KaitaiStream(BytesIO(self._raw_crt_velerr))
        self.crt_velerr = ascii_float.AsciiFloat(_io__raw_crt_velerr)
        self._raw_rad_velerr = self._io.read_bytes(16)
        _io__raw_rad_velerr = KaitaiStream(BytesIO(self._raw_rad_velerr))
        self.rad_velerr = ascii_float.AsciiFloat(_io__raw_rad_velerr)
        self.positional_data_points = [None] * (self.npoints)
        for i in range(self.npoints):
            self.positional_data_points[
                i
            ] = PlatformPositionRecord.PlatformPositionPoint(self._io, self, self._root)

    class PlatformPositionPoint(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_position = [None] * (3)
            self.position = [None] * (3)
            for i in range(3):
                self._raw_position[i] = self._io.read_bytes(22)
                _io__raw_position = KaitaiStream(BytesIO(self._raw_position[i]))
                self.position[i] = ascii_float.AsciiFloat(_io__raw_position)

            self._raw_velocity = [None] * (3)
            self.velocity = [None] * (3)
            for i in range(3):
                self._raw_velocity[i] = self._io.read_bytes(22)
                _io__raw_velocity = KaitaiStream(BytesIO(self._raw_velocity[i]))
                self.velocity[i] = ascii_float.AsciiFloat(_io__raw_velocity)
