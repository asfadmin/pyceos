from construct import Rebuild, Struct, len_, this

from pyceos.types import E20_13, F16_7, AsciiInt, AsciiString, Spare

ImageAnnotationPoint = Struct(
    "line_num" / AsciiInt(8),
    "pixel_num" / AsciiInt(8),
    "text" / AsciiString(16)
)

ImageAnnotation = Struct(
    "num_points" / Rebuild(AsciiInt(8), len_(this.annotations)),
    Spare(8),
    "annotations" / ImageAnnotationPoint[this.num_points],
    Spare(2)
)

DataSetSummaryRecordSensorSpecificAlos = Struct(
    "cal_data_indicator" / AsciiInt(4),
    "start_cal_up" / AsciiInt(8),
    "stop_cal_up" / AsciiInt(8),
    "start_cal_bottom" / AsciiInt(8),
    "stop_cal_bottom" / AsciiInt(8),
    "prf_switch" / AsciiInt(4),
    "line_prf_switch" / AsciiInt(8),
    "beam_center_dir" / F16_7,
    "yew_steering" / AsciiInt(4),
    "param_table" / AsciiInt(4),
    "off_nadir_angle" / F16_7,
    "ant_beam_num" / AsciiInt(4),
    Spare(28),
    "incid_a" / E20_13[6],
    "image_annotation" / ImageAnnotation
)
