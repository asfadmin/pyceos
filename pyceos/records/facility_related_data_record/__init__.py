from construct import GreedyBytes, Switch, this

from pyceos.enums import FacilityRelatedSubtype3

from .jaxa import FacilityRelatedDataRecordJAXA

FacilityRelatedDataRecord = Switch(
    this.header.subtype_3,
    {
        FacilityRelatedSubtype3.jaxa.name: FacilityRelatedDataRecordJAXA
    },
    default=GreedyBytes
)

__all__ = (
    "FacilityRelatedDataRecord",
    "FacilityRelatedDataRecordJAXA",
)
