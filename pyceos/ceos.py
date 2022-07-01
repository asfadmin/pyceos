from construct import Byte, Bytes, Enum, GreedyRange, Int32ub, Struct, Switch, this

from pyceos.enums import FacilityRelatedSubtype3, RecordType

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

Ceos = GreedyRange(
    Struct(
        "header" / RecordHeader,
        "body" / Switch(
            this.header.type,
            {},
            default=Bytes(this.header.size - 12)
        )
    )
)
