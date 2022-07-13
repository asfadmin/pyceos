from construct import GreedyBytes, Switch, this

from pyceos.enums import FileDescriptorSubtype1

from .sar_leader import SARLeaderFileDescriptorRecord

FileDescriptorRecord = Switch(
    this.header.subtype_1,
    {
        FileDescriptorSubtype1.sar_leader_file_descriptor.name: SARLeaderFileDescriptorRecord,
    },
    default=GreedyBytes
)

__all__ = (
    "FileDescriptorRecord",
    "SARLeaderFileDescriptorRecord"
)
