import json

import pytest
from construct import ConstructError

from pyceos import Ceos, CeosRaw


def test_parse_empty_string():
    assert Ceos.parse(b"") == {"records": []}


def test_parse_raw_empty_string():
    assert CeosRaw.parse(b"") == {"records": []}


def test_parse_zeros():
    with pytest.raises(ConstructError):
        Ceos.parse(bytes(12))


def test_parse_empty_header():
    empty_header_data = bytes(8) + b"\x0c\x00\x00\x00"
    empty_record = {
        "header": {
            "sequence_number": 0,
            "subtype_1": 0,
            "type": 0,
            "subtype_2": 0,
            "subtype_3": 0,
            "size": 0
        },
        "body": b""
    }

    Ceos.parse(empty_header_data) == {"records": [empty_record]}
    Ceos.parse(empty_header_data * 5) == {"records": [empty_record] * 5}
