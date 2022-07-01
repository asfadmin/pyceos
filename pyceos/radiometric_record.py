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


class RadiometricRecord(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw_sequence_number = self._io.read_bytes(4)
        _io__raw_sequence_number = KaitaiStream(BytesIO(self._raw_sequence_number))
        self.sequence_number = ascii_int.AsciiInt(_io__raw_sequence_number)
        self._raw_number_rec = self._io.read_bytes(4)
        _io__raw_number_rec = KaitaiStream(BytesIO(self._raw_number_rec))
        self.number_rec = ascii_int.AsciiInt(_io__raw_number_rec)
        self._raw_calibration_factor = self._io.read_bytes(16)
        _io__raw_calibration_factor = KaitaiStream(
            BytesIO(self._raw_calibration_factor)
        )
        self.calibration_factor = ascii_float.AsciiFloat(_io__raw_calibration_factor)
        self.delta_trans = RadiometricRecord.Matrix2x2(self._io, self, self._root)
        self.delta_receive = RadiometricRecord.Matrix2x2(self._io, self, self._root)

    class Matrix2x2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.rows = [None] * (2)
            for i in range(2):
                self.rows[i] = RadiometricRecord.Matrix2x2row(
                    self._io, self, self._root
                )

    class Matrix2x2row(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.values = [None] * (2)
            for i in range(2):
                self.values[i] = RadiometricRecord.Complex(self._io, self, self._root)

    class Complex(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_real = self._io.read_bytes(16)
            _io__raw_real = KaitaiStream(BytesIO(self._raw_real))
            self.real = ascii_float.AsciiFloat(_io__raw_real)
            self._raw_imaginary = self._io.read_bytes(16)
            _io__raw_imaginary = KaitaiStream(BytesIO(self._raw_imaginary))
            self.imaginary = ascii_float.AsciiFloat(_io__raw_imaginary)
