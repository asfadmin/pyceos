import json

import pytest
from construct import ConstructError, Container
from pytest_assert_utils import assert_dict_is_subset

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


# Parsing single record files #
@pytest.mark.parametrize(
    "name",
    (
        "data_quality_summary",
        "data_set_summary",
        "facility_related_jaxa_calibration",
        "platform_position",
        "sar_leader_file_descriptor",
    )
)
def test_parse_data_quality_summary(data_path, name):
    records_path = data_path / "records"
    parsed = Ceos.parse_file(
        records_path / f"{name}.dat",
        _root=Container(mission_id="ALOS2")
    )

    with open(records_path / f"{name}.json") as f:
        expected = json.load(f)

    assert_dict_is_subset(expected, parsed)
