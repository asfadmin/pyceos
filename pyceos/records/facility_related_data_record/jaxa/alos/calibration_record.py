from construct import Const, IfThenElse, Struct, Terminated, this

from pyceos.types import E20_10, AsciiInt, Spare

ORIGINAL_FIELDS = (
    "a_map" / E20_10[10],
    "b_map" / E20_10[10],
    "cal_data_indicator" / AsciiInt(4),
    "start_line_up" / AsciiInt(8),
    "stop_line_up" / AsciiInt(8),
    "start_line_bottom" / AsciiInt(8),
    "stop_line_bottom" / AsciiInt(8),
    "prf_switching_indicator" / AsciiInt(4),
    "line_prf_switching" / AsciiInt(8),
    "sigma_start_line" / AsciiInt(8),
    "number_loss_lines_l0" / AsciiInt(8),
    "number_loss_lines_l1" / AsciiInt(8),
    Spare(312),
    Spare(224),
)


def make_record(record_number: int, *subcons):
    return Struct(
        "sequence_number" / Const(record_number, AsciiInt(4)),
        *subcons,
        Terminated
    )


# From MapReady:
# Old Palsar data, before the larger transformation blocks were
# added, so we do not have as much available for decoding.
def CalibrationRecordShort(record_number: int):
    return make_record(record_number, *ORIGINAL_FIELDS)


def CalibrationRecordFull(record_number: int):
    return make_record(
        record_number,
        *ORIGINAL_FIELDS,
        "a" / E20_10[25],
        "b" / E20_10[25],
        "origin_pixel" / E20_10,
        "origin_line" / E20_10,
        "c" / E20_10[25],
        "d" / E20_10[25],
        "origin_lat" / E20_10,
        "origin_lon" / E20_10,
        Spare(1896)
    )


def CalibrationRecord(record_number: int):
    return IfThenElse(
        this.header.size == 1000,
        CalibrationRecordShort(record_number),
        CalibrationRecordFull(record_number)
    )
