from construct import Struct, Terminated

from pyceos.types import AsciiInt, AsciiString, FixedSized, RepeatUntilEof, Spare

Location = Struct(
    "type" / AsciiString(4),
    "sequence_number" / AsciiInt(8),
    "sequence_number_size" / AsciiInt(4),
)

Descriptor = Struct(
    "num" / AsciiInt(6),
    "size" / AsciiInt(6)
)

LargeDescriptor = Struct(
    "num" / AsciiInt(6),
    "size" / AsciiInt(8)
)

SARLeaderFileDescriptorRecord = Struct(
    "ascii_flag" / AsciiString(2),
    Spare(2),
    "format_doc" / AsciiString(12),
    "format_rev" / AsciiString(2, leftpad=True),
    "design_rev" / AsciiString(2, leftpad=True),
    "software_id" / AsciiString(12),
    "file_num" / AsciiInt(4),
    "product_id" / AsciiString(16),
    "record_sequence" / Location,
    "record_code" / Location,
    "record_length" / Location,
    Spare(68),
    "record_descriptors" / Struct(
        "data_set_summary" / Descriptor,
        "map_projection" / Descriptor,
        "platform_position" / Descriptor,
        "attitude" / Descriptor,
        "radiometric" / Descriptor,
        "radiometric_compensation" / Descriptor,
        "data_quality_summary" / Descriptor,
        "data_histogram" / Descriptor,
        "range_spectra" / Descriptor,
        "dem_descriptor" / Descriptor,
        "radar_parameter_update" / Descriptor,
        "annotation_data" / Descriptor,
        "detail_processing" / Descriptor,
        "calibration" / Descriptor,
        "gcp" / Descriptor,
        Spare(60),
        "facility_related" / FixedSized(
            14 * 11,
            RepeatUntilEof(LargeDescriptor),
            pattern=b" ",
            trim=True
        ),
        Spare(146)
    ),
    Terminated
)
