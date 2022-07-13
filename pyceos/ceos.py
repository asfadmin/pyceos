from construct import (
    Byte,
    Computed,
    Enum,
    GreedyBytes,
    Int32ub,
    Struct,
    Switch,
    Terminated,
    this,
)

from pyceos.enums import FacilityRelatedSubtype3, FileDescriptorSubtype1, RecordType
from pyceos.records.attitude_record import AttitudeRecord
from pyceos.records.data_quality_summary_record import DataQualitySummaryRecord
from pyceos.records.data_set_summary_record import DataSetSummaryRecord
from pyceos.records.facility_related_data_record import (
    FacilityRelatedDataRecord,
    FacilityRelatedDataRecordJAXA,
)
from pyceos.records.file_descriptor_record import FileDescriptorRecord
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


class ComputeSubtype():
    def __init__(self, field: str, mapping: dict):
        self.field = field
        self.mapping = mapping

    def __call__(self, ctx):
        enum = self.mapping.get(ctx.type)
        value = ctx[self.field]
        if not enum:
            return value
        return enum(value).name


RecordHeader = Struct(
    "sequence_number" / Int32ub,
    "_subtype_1" / Byte,
    "type" / Enum(Byte, RecordType),
    # Subtype1 depends on type, and it's logical for it to come after
    "subtype_1" / Computed(ComputeSubtype("_subtype_1", {
        RecordType.file_descriptor.name: FileDescriptorSubtype1
    })),
    "_subtype_2" / Byte,
    "subtype_2" / Computed(ComputeSubtype("_subtype_2", {})),
    "_subtype_3" / Byte,
    "subtype_3" / Computed(ComputeSubtype("_subtype_3", {
        RecordType.facility_related.name: FacilityRelatedSubtype3
    })),
    "size" / Int32ub,
)

RecordBody = FixedSized(
    this.header.size - 12,
    Switch(
        this.header.type,
        {
            RecordType.file_descriptor.name: FileDescriptorRecord,
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
