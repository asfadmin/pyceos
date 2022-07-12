import io
import itertools
from typing import Optional

from construct import (
    Adapter,
    Construct,
    GreedyBytes,
    GreedyRange,
    GreedyString,
    ListContainer,
    Padding,
    PaddingError,
    StreamError,
    Subconstruct,
    evaluate,
    stream_read,
    stream_write,
)


class RepeatUntilEof(GreedyRange):
    """
    Like construct.GreedyRange but does not swallow errors.
    """
    def _parse(self, stream, context, path):
        discard = self.discard
        obj = ListContainer()
        try:
            for i in itertools.count():
                context._index = i
                e = self.subcon._parsereport(stream, context, path)
                if not discard:
                    obj.append(e)
        except StreamError:
            pass
        return obj


class FixedSized(Subconstruct):
    """
    Like construct.FixedSized but supports different padding characters and
    padding on the left.
    """

    def __init__(
        self,
        length,
        subcon: Construct,
        pattern: bytes = b"\x00",
        trim: bool = False,
        leftpad=False
    ):
        if not isinstance(pattern, bytes) or len(pattern) != 1:
            raise PaddingError("pattern expected to be bytes of length 1")
        super().__init__(subcon)
        self.length = length
        self.pattern = pattern
        self.trim = trim
        self.leftpad = leftpad

    def _parse(self, stream, context, path):
        length = evaluate(self.length, context)
        if length < 0:
            raise PaddingError("length cannot be negative", path=path)
        leftpad = evaluate(self.leftpad, context)
        data = stream_read(stream, length, path)
        if self.trim:
            if leftpad:
                data = data.lstrip(self.pattern)
            else:
                data = data.rstrip(self.pattern)
        if self.subcon is GreedyBytes:
            return data
        if type(self.subcon) is GreedyString:
            return data.decode(self.subcon.encoding)
        return self.subcon._parsereport(io.BytesIO(data), context, path)

    def _build(self, obj, stream, context, path):
        length = evaluate(self.length, context)
        if length < 0:
            raise PaddingError("length cannot be negative", path=path)
        leftpad = evaluate(self.leftpad, context)
        stream2 = io.BytesIO()
        buildret = self.subcon._build(obj, stream2, context, path)
        data = stream2.getvalue()
        pad = length - len(data)
        if pad < 0:
            raise PaddingError("subcon build %d bytes but was allowed only %d" % (len(data), length), path=path)
        if leftpad:
            stream_write(stream, self.pattern * pad, pad, path)
            stream_write(stream, data, len(data), path)
        else:
            stream_write(stream, data, len(data), path)
            stream_write(stream, self.pattern * pad, pad, path)
        return buildret

    def _sizeof(self, context, path):
        length = evaluate(self.length, context)
        if length < 0:
            raise PaddingError("length cannot be negative", path=path)
        return length


class IntAdapter(Adapter):
    def _decode(self, obj: str, _context, _path) -> Optional[int]:
        if obj:
            return int(obj)
        return None

    def _encode(self, obj: Optional[int], _context, _path) -> str:
        if obj is None:
            return ""
        return str(obj)


class BoolAdapter(Adapter):
    def _decode(self, obj: int, _context, _path) -> Optional[bool]:
        if obj is None:
            return None
        return bool(obj)

    def _encode(self, obj: Optional[bool], _context, _path) -> Optional[int]:
        if obj is None:
            return None
        return int(obj)


class FloatAdapter(Adapter):
    def __init__(self, subcon: Construct, format: str = ".7G"):
        super().__init__(subcon)
        self.format = format

    def _decode(self, obj: str, _context, _path) -> Optional[float]:
        if obj:
            return float(obj)
        return None

    def _encode(self, obj: Optional[float], _context, _path) -> str:
        if obj is None:
            return ""
        return f"{obj:{self.format}}"


def AsciiString(length: int, leftpad: bool = False):
    return FixedSized(
        length,
        GreedyString("ascii"),
        pattern=b" ",
        trim=True,
        leftpad=leftpad
    )


def AsciiInt(length: int) -> IntAdapter:
    return IntAdapter(AsciiString(length, leftpad=True))


def AsciiBool(length: int) -> BoolAdapter:
    return BoolAdapter(AsciiInt(length))


def AsciiFloat(length: int, format: str = ".7G") -> IntAdapter:
    return FloatAdapter(
        AsciiString(length, leftpad=True),
        format=format
    )


def Spare(length: int):
    return Padding(length, b" ")


# ALOS standard float types
F8_3 = AsciiFloat(8, format=".3G")
F16_7 = AsciiFloat(16, format=".7G")
E16_7 = AsciiFloat(16, format=".7E")
E20_10 = AsciiFloat(20, format=".10E")
E20_13 = AsciiFloat(20, format=".13E")
E22_15 = AsciiFloat(22, format=".15E")
