from construct import Check, GreedyBytes, Peek, Switch, this

from pyceos.enums import RecordType
from pyceos.types import AsciiInt, KeepLast

from . import alos

AlosRecord = Switch(
    this.record_sequence_number,
    {
        11: alos.CalibrationRecord
    },
    default=alos.GenericRecord
)
Alos2Record = Switch(
    this.record_sequence_number,
    {
        5: alos.CalibrationRecord
    },
    default=alos.GenericRecord
)

FacilityRelatedDataRecordJAXA = KeepLast(
    Check(this.header.type == RecordType.facility_related.name),
    "record_sequence_number" / Peek(AsciiInt(4)),
    Switch(
        this._root.mission_id,
        {
            "ALOS": AlosRecord,
            "ALOS2": Alos2Record
        }
    )
)

__all__ = (
    "FacilityRelatedDataRecordJAXA",
)
