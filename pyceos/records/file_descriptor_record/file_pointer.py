from construct import Struct, Terminated

from pyceos.types import AsciiInt, AsciiString, Spare

FilePointerRecord = Struct(
    "ascii_flag" / AsciiString(2),
    Spare(2),
    "number" / AsciiInt(4),
    "name_id" / AsciiString(16),
    "class" / AsciiString(28),
    "class_code" / AsciiString(4),
    "data_type" / AsciiString(28),
    "data_type_code" / AsciiString(4),
    "num_records" / AsciiInt(8),
    "first_record_size" / AsciiInt(8),
    "max_record_size" / AsciiInt(8),
    "record_length_type" / AsciiString(12),
    "record_length_type_code" / AsciiString(4),
    "physical_volume_set_first" / AsciiInt(2),
    "physical_volume_set_last" / AsciiInt(2),
    "record_first" / AsciiInt(8),
    "record_last" / AsciiInt(8),
    Spare(100),
    Spare(100),  # Local use segment
    Terminated
)
