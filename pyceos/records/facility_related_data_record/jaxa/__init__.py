from construct import Select, Switch, this

from . import alos

FacilityRelatedDataRecordJAXA = Switch(
    this._root.mission_id,
    {
        "ALOS": Select(
            alos.CalibrationRecord(11),
            alos.GenericRecord
        ),
        "ALOS2": Select(
            alos.CalibrationRecord(5),
            alos.GenericRecord
        )
    }
)

__all__ = (
    "FacilityRelatedDataRecordJAXA",
)
