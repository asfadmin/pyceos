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


class DataQualityRecord(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw_sequence_number = self._io.read_bytes(4)
        _io__raw_sequence_number = KaitaiStream(BytesIO(self._raw_sequence_number))
        self.sequence_number = ascii_int.AsciiInt(_io__raw_sequence_number)
        self.sar_chan = (self._io.read_bytes(4)).decode("ascii")
        self.cali_date = (self._io.read_bytes(6)).decode("ascii")
        self._raw_nchan = self._io.read_bytes(4)
        _io__raw_nchan = KaitaiStream(BytesIO(self._raw_nchan))
        self.nchan = ascii_int.AsciiInt(_io__raw_nchan)
        self._raw_islr = self._io.read_bytes(16)
        _io__raw_islr = KaitaiStream(BytesIO(self._raw_islr))
        self.islr = ascii_float.AsciiFloat(_io__raw_islr)
        self._raw_pslr = self._io.read_bytes(16)
        _io__raw_pslr = KaitaiStream(BytesIO(self._raw_pslr))
        self.pslr = ascii_float.AsciiFloat(_io__raw_pslr)
        self._raw_azi_ambig = self._io.read_bytes(16)
        _io__raw_azi_ambig = KaitaiStream(BytesIO(self._raw_azi_ambig))
        self.azi_ambig = ascii_float.AsciiFloat(_io__raw_azi_ambig)
        self._raw_rng_ambig = self._io.read_bytes(16)
        _io__raw_rng_ambig = KaitaiStream(BytesIO(self._raw_rng_ambig))
        self.rng_ambig = ascii_float.AsciiFloat(_io__raw_rng_ambig)
        self._raw_snr = self._io.read_bytes(16)
        _io__raw_snr = KaitaiStream(BytesIO(self._raw_snr))
        self.snr = ascii_float.AsciiFloat(_io__raw_snr)
        self._raw_ber = self._io.read_bytes(16)
        _io__raw_ber = KaitaiStream(BytesIO(self._raw_ber))
        self.ber = ascii_float.AsciiFloat(_io__raw_ber)
        self._raw_rng_res = self._io.read_bytes(16)
        _io__raw_rng_res = KaitaiStream(BytesIO(self._raw_rng_res))
        self.rng_res = ascii_float.AsciiFloat(_io__raw_rng_res)
        self._raw_azi_res = self._io.read_bytes(16)
        _io__raw_azi_res = KaitaiStream(BytesIO(self._raw_azi_res))
        self.azi_res = ascii_float.AsciiFloat(_io__raw_azi_res)
        self._raw_rad_res = self._io.read_bytes(16)
        _io__raw_rad_res = KaitaiStream(BytesIO(self._raw_rad_res))
        self.rad_res = ascii_float.AsciiFloat(_io__raw_rad_res)
        self._raw_dyn_rng = self._io.read_bytes(16)
        _io__raw_dyn_rng = KaitaiStream(BytesIO(self._raw_dyn_rng))
        self.dyn_rng = ascii_float.AsciiFloat(_io__raw_dyn_rng)
        self.abs_radiometric_uncertainty = DataQualityRecord.DbDeg(
            self._io, self, self._root
        )
        self.rel_radiometric_uncertainty = [None] * (self.nchan)
        for i in range(self.nchan):
            self.rel_radiometric_uncertainty[i] = DataQualityRecord.DbDeg(
                self._io, self, self._root
            )

        self._raw_alt_locerr = self._io.read_bytes(16)
        _io__raw_alt_locerr = KaitaiStream(BytesIO(self._raw_alt_locerr))
        self.alt_locerr = ascii_float.AsciiFloat(_io__raw_alt_locerr)
        self._raw_crt_locerr = self._io.read_bytes(16)
        _io__raw_crt_locerr = KaitaiStream(BytesIO(self._raw_crt_locerr))
        self.crt_locerr = ascii_float.AsciiFloat(_io__raw_crt_locerr)
        self._raw_alt_scale = self._io.read_bytes(16)
        _io__raw_alt_scale = KaitaiStream(BytesIO(self._raw_alt_scale))
        self.alt_scale = ascii_float.AsciiFloat(_io__raw_alt_scale)
        self._raw_crt_scale = self._io.read_bytes(16)
        _io__raw_crt_scale = KaitaiStream(BytesIO(self._raw_crt_scale))
        self.crt_scale = ascii_float.AsciiFloat(_io__raw_crt_scale)
        self._raw_dis_skew = self._io.read_bytes(16)
        _io__raw_dis_skew = KaitaiStream(BytesIO(self._raw_dis_skew))
        self.dis_skew = ascii_float.AsciiFloat(_io__raw_dis_skew)
        self._raw_ori_err = self._io.read_bytes(16)
        _io__raw_ori_err = KaitaiStream(BytesIO(self._raw_ori_err))
        self.ori_err = ascii_float.AsciiFloat(_io__raw_ori_err)
        self.misregistration_error = [None] * (self.nchan)
        for i in range(self.nchan):
            self.misregistration_error[i] = DataQualityRecord.AltCrt(
                self._io, self, self._root
            )

    class DbDeg(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_decibles = self._io.read_bytes(16)
            _io__raw_decibles = KaitaiStream(BytesIO(self._raw_decibles))
            self.decibles = ascii_float.AsciiFloat(_io__raw_decibles)
            self._raw_degrees = self._io.read_bytes(16)
            _io__raw_degrees = KaitaiStream(BytesIO(self._raw_degrees))
            self.degrees = ascii_float.AsciiFloat(_io__raw_degrees)

    class AltCrt(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_along_track = self._io.read_bytes(16)
            _io__raw_along_track = KaitaiStream(BytesIO(self._raw_along_track))
            self.along_track = ascii_float.AsciiFloat(_io__raw_along_track)
            self._raw_cross_track = self._io.read_bytes(16)
            _io__raw_cross_track = KaitaiStream(BytesIO(self._raw_cross_track))
            self.cross_track = ascii_float.AsciiFloat(_io__raw_cross_track)
