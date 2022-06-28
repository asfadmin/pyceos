import dataclasses
import io
import struct
from dataclasses import dataclass
from typing import Callable, Type, TypeVar

from pyceos import codes


def fmt(code: str):
    """Set the struct format code to use for deserialization"""
    return dataclasses.field(metadata={"struct_format": code})


T = TypeVar("T")


def deserialize(endian: str = "") -> Callable[[T], T]:
    def decorator(cls: T) -> T:
        format_str = "".join(
            field.metadata["struct_format"] for field in dataclasses.fields(cls)
        )
        format_str = endian + format_str
        print("format_str:", endian + format_str)
        cls._struct = struct.Struct(format_str)
        return cls
    return decorator


Self = TypeVar("Self", bound="_DeserializeMixin")


class _DeserializeMixin:
    """Used with the `deserialize` decorator to play nicer with type checkers"""
    @classmethod
    def unpack(cls: Type[Self], data: bytes) -> Self:
        return cls(*cls._struct.unpack(data))

    @classmethod
    def read(cls: Type[Self], f: io.BytesIO) -> Self:
        return cls.unpack(f.read(cls._struct.size))


HeaderStruct = struct.Struct(">LBBBBL")


@deserialize(endian=">")
@dataclass
class Header(_DeserializeMixin):
    sequence_number: int = fmt("L")
    subtype_1: int = fmt("B")
    type: int = fmt("B")
    subtype_2: int = fmt("B")
    subtype_3: int = fmt("B")
    size: int = fmt("L")


class Record(_DeserializeMixin):
    def __init__(self):
        raise RuntimeError(f"Can't instantiate {self.__class__.__name__} directly")

    def __init_subclass__(cls, /, code: int, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._code = code


ImageryOptionsRecordStruct = struct.Struct("LL25slll5s7l5s5l5s9s9s9s9s9s5s29s9s9s9s9s29s5s3l")


@deserialize(endian="<")
@dataclass
class ImageryOptionsRecord(
    Record,
    code=codes.RecordType.IMAGERY_OPTIONS.value
):
    ascii_flag: bytes = fmt("2s")
    spare_1: bytes = fmt("2s")
    format_doc: bytes = fmt("12s")
    format_rev: bytes = fmt("2s")
    design_rev: bytes = fmt("2s")
    software_id: bytes = fmt("12s")
    file_num: int = fmt("l")
    product_id: bytes = fmt("16s")
    rec_seq_flag: bytes = fmt("4s")
    seq_loc: int = fmt("q")
    seq_len: int = fmt("l")
    rec_code: bytes = fmt("4s")
    code_loc: int = fmt("q")
    code_len: int = fmt("l")
    rec_len: bytes = fmt("4s")
    rlen_loc: int = fmt("q")
    rlen_len: int = fmt("l")
    spare_2: bytes = fmt("4s")
    spare_3: bytes = fmt("64s")
    numofrec: int
    reclen: int
    spare_4: bytes
    bitssamp: int
    sampdata: int
    bytgroup: int
    justific: bytes
    sarchan: int
    linedata: int
    lbrdrpxl: int
    datgroup: int
    rbrdrpxl: int
    topbrdr: int
    botbrdr: int
    interlv: bytes
    recline: int
    mrecline: int
    predata: int
    sardata: int
    sufdata: int
    repflag: bytes
    lin_loc: bytes
    chn_loc: bytes
    time_loc: bytes
    left_loc: bytes
    right_loc: bytes
    pad_ind: bytes
    spare_6: bytes
    qual_loc: bytes
    cali_loc: bytes
    gain_loc: bytes
    bais_loc: bytes
    formatid: bytes
    formcode: bytes
    leftfill: int
    rigtfill: int
    maxidata: int
