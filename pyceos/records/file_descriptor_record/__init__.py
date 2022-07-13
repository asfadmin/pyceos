from construct import GreedyBytes, Switch, this

from pyceos.enums import FileDescriptorSubtype1

from .sar_leader import SARLeaderFileDescriptorRecord
from .volume_descriptor import VolumeDescriptorRecord

FileDescriptorRecord = Switch(
    this.header.subtype_1,
    {
        FileDescriptorSubtype1.sar_leader_file_descriptor.name: SARLeaderFileDescriptorRecord,
        FileDescriptorSubtype1.volume_descriptor.name: VolumeDescriptorRecord,
    },
    default=GreedyBytes
)

__all__ = (
    "FileDescriptorRecord",
    "SARLeaderFileDescriptorRecord",
    "VolumeDescriptorRecord",
)
