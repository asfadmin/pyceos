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


class DataSetSummaryRecordSensorSpecificAlos(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw_cal_data_indicator = self._io.read_bytes(4)
        _io__raw_cal_data_indicator = KaitaiStream(
            BytesIO(self._raw_cal_data_indicator)
        )
        self.cal_data_indicator = ascii_int.AsciiInt(_io__raw_cal_data_indicator)
        self._raw_start_cal_up = self._io.read_bytes(8)
        _io__raw_start_cal_up = KaitaiStream(BytesIO(self._raw_start_cal_up))
        self.start_cal_up = ascii_int.AsciiInt(_io__raw_start_cal_up)
        self._raw_stop_cal_up = self._io.read_bytes(8)
        _io__raw_stop_cal_up = KaitaiStream(BytesIO(self._raw_stop_cal_up))
        self.stop_cal_up = ascii_int.AsciiInt(_io__raw_stop_cal_up)
        self._raw_start_cal_bottom = self._io.read_bytes(8)
        _io__raw_start_cal_bottom = KaitaiStream(BytesIO(self._raw_start_cal_bottom))
        self.start_cal_bottom = ascii_int.AsciiInt(_io__raw_start_cal_bottom)
        self._raw_stop_cal_bottom = self._io.read_bytes(8)
        _io__raw_stop_cal_bottom = KaitaiStream(BytesIO(self._raw_stop_cal_bottom))
        self.stop_cal_bottom = ascii_int.AsciiInt(_io__raw_stop_cal_bottom)
        self._raw_prf_switch = self._io.read_bytes(4)
        _io__raw_prf_switch = KaitaiStream(BytesIO(self._raw_prf_switch))
        self.prf_switch = ascii_int.AsciiInt(_io__raw_prf_switch)
        self._raw_line_prf_switch = self._io.read_bytes(8)
        _io__raw_line_prf_switch = KaitaiStream(BytesIO(self._raw_line_prf_switch))
        self.line_prf_switch = ascii_int.AsciiInt(_io__raw_line_prf_switch)
        self._raw_beam_center_dir = self._io.read_bytes(16)
        _io__raw_beam_center_dir = KaitaiStream(BytesIO(self._raw_beam_center_dir))
        self.beam_center_dir = ascii_float.AsciiFloat(_io__raw_beam_center_dir)
        self._raw_yew_steering = self._io.read_bytes(4)
        _io__raw_yew_steering = KaitaiStream(BytesIO(self._raw_yew_steering))
        self.yew_steering = ascii_int.AsciiInt(_io__raw_yew_steering)
        self._raw_param_table = self._io.read_bytes(4)
        _io__raw_param_table = KaitaiStream(BytesIO(self._raw_param_table))
        self.param_table = ascii_int.AsciiInt(_io__raw_param_table)
        self._raw_off_nadir_angle = self._io.read_bytes(16)
        _io__raw_off_nadir_angle = KaitaiStream(BytesIO(self._raw_off_nadir_angle))
        self.off_nadir_angle = ascii_float.AsciiFloat(_io__raw_off_nadir_angle)
        self._raw_ant_beam_num = self._io.read_bytes(4)
        _io__raw_ant_beam_num = KaitaiStream(BytesIO(self._raw_ant_beam_num))
        self.ant_beam_num = ascii_int.AsciiInt(_io__raw_ant_beam_num)
        self.spare_1 = self._io.read_bytes(28)
        self._raw_incid_a = [None] * (6)
        self.incid_a = [None] * (6)
        for i in range(6):
            self._raw_incid_a[i] = self._io.read_bytes(20)
            _io__raw_incid_a = KaitaiStream(BytesIO(self._raw_incid_a[i]))
            self.incid_a[i] = ascii_float.AsciiFloat(_io__raw_incid_a)

        self.image_annotation = DataSetSummaryRecordSensorSpecificAlos.ImageAnnotation(
            self._io, self, self._root
        )

    class ImageAnnotation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_num_points = self._io.read_bytes(8)
            _io__raw_num_points = KaitaiStream(BytesIO(self._raw_num_points))
            self.num_points = ascii_int.AsciiInt(_io__raw_num_points)
            self.spare_1 = self._io.read_bytes(8)
            self.annotations = [None] * (64)
            for i in range(64):
                self.annotations[
                    i
                ] = DataSetSummaryRecordSensorSpecificAlos.ImageAnnotationPoint(
                    self._io, self, self._root
                )

            self.spare_2 = self._io.read_bytes(2)

    class ImageAnnotationPoint(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_line_num = self._io.read_bytes(8)
            _io__raw_line_num = KaitaiStream(BytesIO(self._raw_line_num))
            self.line_num = ascii_int.AsciiInt(_io__raw_line_num)
            self._raw_pixel_num = self._io.read_bytes(8)
            _io__raw_pixel_num = KaitaiStream(BytesIO(self._raw_pixel_num))
            self.pixel_num = ascii_int.AsciiInt(_io__raw_pixel_num)
            self.text = (self._io.read_bytes(16)).decode("ascii")
