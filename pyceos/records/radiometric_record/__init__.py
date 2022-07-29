from construct import Switch, this

from . import alos

RadiometricRecord = Switch(
    this._root.mission_id,
    {
        "ALOS": alos.RadiometricRecord,
        "ALOS2": alos.RadiometricRecord
    }
)

__all__ = (
    "RadiometricRecord",
)
