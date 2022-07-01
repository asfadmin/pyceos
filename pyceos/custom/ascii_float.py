from typing import Optional

from kaitaistruct import KaitaiStream


def AsciiFloat(stream: KaitaiStream) -> Optional[float]:
    data = stream.read_bytes_full().decode("ascii").strip()
    if data:
        return float(data)
    return None
