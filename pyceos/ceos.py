from construct import Byte, Enum, GreedyBytes, Int32ub, Struct, Switch, Terminated, this

from pyceos.enums import FacilityRelatedSubtype3, RecordType
from pyceos.records.data_set_summary_record import DataSetSummaryRecord
from pyceos.records.facility_related_data_record import (
    FacilityRelatedDataRecord,
    FacilityRelatedDataRecordJAXA,
)
from pyceos.types import FixedSized, RepeatUntilEof


def process_record(obj, ctx):
    """
    Set global internal state that's needed in later records.
    """
    header = obj.header
    if header.type == RecordType.data_set_summary.name:
        # Needed to determine some record types
        ctx._root.mission_id = obj.body.mission_id


RecordHeader = Struct(
    "sequence_number" / Int32ub,
    "subtype_1" / Byte,
    "type" / Enum(Byte, RecordType),
    "subtype_2" / Byte,
    "subtype_3" / Switch(
        this.type,
        {
            RecordType.facility_related.name: Enum(Byte, FacilityRelatedSubtype3)
        },
        default=Byte
    ),
    "size" / Int32ub
)

RecordBody = FixedSized(
    this.header.size - 12,
    Switch(
        this.header.type,
        {
            RecordType.data_set_summary.name: DataSetSummaryRecord,
            RecordType.facility_related.name: FacilityRelatedDataRecord,
            RecordType.facility_related_jaxa.name: FacilityRelatedDataRecordJAXA
        },
        default=GreedyBytes
    ),
    pattern=b" ",
)

Ceos = Struct(
    "records" / RepeatUntilEof(
        Struct(
            "header" / RecordHeader,
            "body" / RecordBody,
        ) * process_record
    ),
    Terminated
)
