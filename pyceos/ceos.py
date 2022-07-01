# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version("0.9"):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s"
        % (kaitaistruct.__version__)
    )

from . import data_set_summary_record
from . import data_quality_record
from . import radiometric_record
from . import platform_position_record
from . import imagery_options_record
from . import map_projection_record
from . import attitude_record


class Ceos(KaitaiStruct):
    class RecordType(Enum):
        data_set_summary = 10
        scene_header = 18
        map_projection = 20
        platform_position = 30
        map_projection_alos = 36
        attitude = 40
        radiometric = 50
        radiometric_compensation = 51
        data_quality = 60
        data_histogram = 70
        range_spectra = 80
        processing_parameter = 120
        imagery_options = 192
        trailer_file_descriptor = 193
        facility_related = 200
        asf_facility_related = 210
        esa_facility_related = 220
        jaxa_facility_related = 230
        file_descriptor = 300

    class Subtype3(Enum):
        ceos = 10
        unspecified = 18
        ccrs = 36
        esa = 50
        nasa = 60
        jpl = 61
        jaxa = 70
        dfvlr = 80
        rae = 90
        telespazio = 100

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.records = []
        i = 0
        while not self._io.is_eof():
            self.records.append(Ceos.Record(self._io, self, self._root))
            i += 1

    class Record(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header = Ceos.RecordHeader(self._io, self, self._root)
            _on = self.header.type
            if _on == Ceos.RecordType.imagery_options:
                self._raw_body = self._io.read_bytes((self.header.size - 12))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = imagery_options_record.ImageryOptionsRecord(_io__raw_body)
            elif _on == Ceos.RecordType.data_quality:
                self._raw_body = self._io.read_bytes((self.header.size - 12))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = data_quality_record.DataQualityRecord(_io__raw_body)
            elif _on == Ceos.RecordType.data_set_summary:
                self._raw_body = self._io.read_bytes((self.header.size - 12))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = data_set_summary_record.DataSetSummaryRecord(_io__raw_body)
            elif _on == Ceos.RecordType.attitude:
                self._raw_body = self._io.read_bytes((self.header.size - 12))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = attitude_record.AttitudeRecord(_io__raw_body)
            elif _on == Ceos.RecordType.radiometric:
                self._raw_body = self._io.read_bytes((self.header.size - 12))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = radiometric_record.RadiometricRecord(_io__raw_body)
            elif _on == Ceos.RecordType.map_projection:
                self._raw_body = self._io.read_bytes((self.header.size - 12))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = map_projection_record.MapProjectionRecord(_io__raw_body)
            elif _on == Ceos.RecordType.platform_position:
                self._raw_body = self._io.read_bytes((self.header.size - 12))
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = platform_position_record.PlatformPositionRecord(
                    _io__raw_body
                )
            else:
                self.body = self._io.read_bytes((self.header.size - 12))

    class RecordHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sequence_number = self._io.read_u4be()
            self.subtype_1 = self._io.read_u1()
            self.type = KaitaiStream.resolve_enum(Ceos.RecordType, self._io.read_u1())
            self.subtype_2 = self._io.read_u1()
            self.subtype_3 = KaitaiStream.resolve_enum(
                Ceos.Subtype3, self._io.read_u1()
            )
            self.size = self._io.read_u4be()
