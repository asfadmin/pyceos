from construct import Struct, Terminated

from pyceos.types import AsciiString, Spare

TextRecord = Struct(
    "ascii_flag" / AsciiString(2),
    Spare(2),
    "product_id" / AsciiString(40),
    "product_creation" / AsciiString(60),
    "tape_id" / AsciiString(40),
    "scene_id" / AsciiString(40),
    "scene_location" / AsciiString(40),
    Spare(124),
    Terminated
)
