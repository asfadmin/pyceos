from construct import Check, GreedyBytes, Switch, this

from pyceos.enums import FacilityRelatedSubtype3, RecordType
from pyceos.types import KeepLast

from .jaxa import FacilityRelatedDataRecordJAXA

FacilityRelatedDataRecord = KeepLast(
    Check(this.header.type == RecordType.facility_related.name),
    Switch(
        this.header.subtype_3,
        {
            FacilityRelatedSubtype3.jaxa.name: FacilityRelatedDataRecordJAXA
        },
        default=GreedyBytes
    )
)

__all__ = (
    "FacilityRelatedDataRecord",
    "FacilityRelatedDataRecordJAXA",
)
