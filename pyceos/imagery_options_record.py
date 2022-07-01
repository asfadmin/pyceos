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


class ImageryOptionsRecord(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.ascii_flag = (self._io.read_bytes(2)).decode("ascii")
        self.spare_1 = self._io.read_bytes(2)
        self.format_doc = (self._io.read_bytes(12)).decode("ascii")
        self.format_rev = (self._io.read_bytes(2)).decode("ascii")
        self.design_rev = (self._io.read_bytes(2)).decode("ascii")
        self.software_id = (self._io.read_bytes(12)).decode("ascii")
        self._raw_file_num = self._io.read_bytes(4)
        _io__raw_file_num = KaitaiStream(BytesIO(self._raw_file_num))
        self.file_num = ascii_int.AsciiInt(_io__raw_file_num)
        self.product_id = (self._io.read_bytes(16)).decode("ascii")
        self.rec_seq_flag = (self._io.read_bytes(4)).decode("ascii")
        self._raw_seq_loc = self._io.read_bytes(8)
        _io__raw_seq_loc = KaitaiStream(BytesIO(self._raw_seq_loc))
        self.seq_loc = ascii_int.AsciiInt(_io__raw_seq_loc)
        self._raw_seq_len = self._io.read_bytes(4)
        _io__raw_seq_len = KaitaiStream(BytesIO(self._raw_seq_len))
        self.seq_len = ascii_int.AsciiInt(_io__raw_seq_len)
        self.rec_code = (self._io.read_bytes(4)).decode("ascii")
        self._raw_code_loc = self._io.read_bytes(8)
        _io__raw_code_loc = KaitaiStream(BytesIO(self._raw_code_loc))
        self.code_loc = ascii_int.AsciiInt(_io__raw_code_loc)
        self._raw_code_len = self._io.read_bytes(4)
        _io__raw_code_len = KaitaiStream(BytesIO(self._raw_code_len))
        self.code_len = ascii_int.AsciiInt(_io__raw_code_len)
        self.rec_len = (self._io.read_bytes(4)).decode("ascii")
        self._raw_rlen_loc = self._io.read_bytes(8)
        _io__raw_rlen_loc = KaitaiStream(BytesIO(self._raw_rlen_loc))
        self.rlen_loc = ascii_int.AsciiInt(_io__raw_rlen_loc)
        self._raw_rlen_len = self._io.read_bytes(4)
        _io__raw_rlen_len = KaitaiStream(BytesIO(self._raw_rlen_len))
        self.rlen_len = ascii_int.AsciiInt(_io__raw_rlen_len)
        self.spare_2 = self._io.read_bytes(4)
        self.spare_3 = self._io.read_bytes(64)
        self._raw_num_of_rec = self._io.read_bytes(6)
        _io__raw_num_of_rec = KaitaiStream(BytesIO(self._raw_num_of_rec))
        self.num_of_rec = ascii_int.AsciiInt(_io__raw_num_of_rec)
        self._raw_reclen = self._io.read_bytes(6)
        _io__raw_reclen = KaitaiStream(BytesIO(self._raw_reclen))
        self.reclen = ascii_int.AsciiInt(_io__raw_reclen)
        self.spare_4 = self._io.read_bytes(24)
