from construct import Byte, Enum, GreedyRange, Int32ub, Struct, Switch, Terminated, this

from pyceos.enums import FacilityRelatedSubtype3, RecordType
from pyceos.records.data_set_summary_record import DataSetSummaryRecord
from pyceos.types import FixedSized

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

Ceos = Struct(
    "records" / GreedyRange(
        Struct(
            "header" / RecordHeader,
            "body" / FixedSized(
                this.header.size - 12,
                Switch(
                    this.header.type,
                    {
                        RecordType.data_set_summary.name: DataSetSummaryRecord
                    },
                    default=Byte
                ),
                pattern=b" ",
            ),
        )
    ),
    Terminated
)
