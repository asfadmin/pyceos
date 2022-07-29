from enum import Enum, unique


@unique
class RecordType(Enum):
    data_set_summary = 10
    scene_header = 18
    map_projection = 20
    platform_position = 30
    map_projection_alos = 36
    attitude = 40
    radiometric = 50
    radiometric_compensation = 51
    data_quality_summary = 60
    data_histogram = 70
    range_spectra = 80
    processing_parameter = 120
    file_descriptor = 192
    trailer_file_descriptor = 193
    facility_related = 200
    facility_related_asf = 210
    facility_related_esa = 220
    facility_related_jaxa = 230


@unique
class FileDescriptorSubtype1(Enum):
    sar_leader_file_descriptor = 11
    text = 18
    sar_data_file_descriptor = 50
    sar_trailer_file_descriptor = 63
    volume_descriptor = 192
    file_pointer = 219


@unique
class FacilityRelatedSubtype3(Enum):
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
