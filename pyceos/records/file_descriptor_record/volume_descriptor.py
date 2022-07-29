from construct import Struct, Terminated

from pyceos.types import AsciiInt, AsciiString, Spare

VolumeDescriptorRecord = Struct(
    "ascii_flag" / AsciiString(2),
    Spare(2),
    "format_doc" / AsciiString(12),
    "format_rev" / AsciiString(2, leftpad=True),
    "design_rev" / AsciiString(2, leftpad=True),
    "software_id" / AsciiString(12),
    "physical_volume_id" / AsciiString(16),
    "logical_volume_id" / AsciiString(16),
    "volume_set_id" / AsciiString(16),
    "num_physical_volumes" / AsciiInt(2),
    "sequence_number_first" / AsciiInt(2),
    "sequence_number_last" / AsciiInt(2),
    "sequence_number_current" / AsciiInt(2),
    "file_number" / AsciiInt(4),
    "set_number" / AsciiInt(4),
    "physical_number" / AsciiInt(4),
    "creation_date" / AsciiString(8),
    "creation_time" / AsciiString(8),
    "generation_country" / AsciiString(12),
    "generating_agency" / AsciiString(8),
    "generating_facility" / AsciiString(12),
    "num_file_pointer_records" / AsciiInt(4),
    "num_text_records" / AsciiInt(4),
    Spare(92),
    Spare(100),  # Local use segment
    Terminated
)
