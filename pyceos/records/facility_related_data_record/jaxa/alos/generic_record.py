from construct import GreedyBytes, Struct

from pyceos.types import AsciiInt, Spare

GenericRecord = Struct(
    "sequence_number" / AsciiInt(4),
    Spare(50),
    "file" / GreedyBytes
)
