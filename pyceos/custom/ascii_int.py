from typing import Optional

from kaitaistruct import KaitaiStream


def AsciiInt(stream: KaitaiStream) -> Optional[int]:
    data = stream.read_bytes_full().decode("ascii").strip()
    if data:
        return int(data)
    return None
