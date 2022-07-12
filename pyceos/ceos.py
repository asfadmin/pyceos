from construct import Byte, Enum, GreedyBytes, Int32ub, Struct, Switch, Terminated, this

from pyceos.enums import FacilityRelatedSubtype3, RecordType
from pyceos.records.attitude_record import AttitudeRecord
from pyceos.records.data_quality_summary_record import DataQualitySummaryRecord
from pyceos.records.data_set_summary_record import DataSetSummaryRecord
from pyceos.records.facility_related_data_record import (
    FacilityRelatedDataRecord,
    FacilityRelatedDataRecordJAXA,
)
from pyceos.records.platform_position_record import PlatformPositionRecord
from pyceos.records.radiometric_record import RadiometricRecord
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
            RecordType.platform_position.name: PlatformPositionRecord,
            RecordType.attitude.name: AttitudeRecord,
            RecordType.radiometric.name: RadiometricRecord,
            RecordType.data_quality_summary.name: DataQualitySummaryRecord,
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
