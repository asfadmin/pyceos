import pytest

from pyceos.records.data_set_summary_record.sensor_specific import (
    ImageAnnotation,
    ImageAnnotationPoint,
)

TEST_DATA = [
    {
        "name": "ImageAnnotationPoint empty",
        "struct": ImageAnnotationPoint,
        "attrs": dict(
            line_num=None,
            pixel_num=None,
            text=""
        ),
        "data": b" " * 32
    },
    {
        "name": "ImageAnnotationPoint full",
        "struct": ImageAnnotationPoint,
        "attrs": dict(
            line_num=10,
            pixel_num=12345,
            text="Hello World"
        ),
        "data": b"      10   12345Hello World     "
    },
    {
        "name": "ImageAnnotationPoint partial",
        "struct": ImageAnnotationPoint,
        "attrs": dict(
            line_num=10,
            pixel_num=12345,
            text=""
        ),
        "data": b"      10   12345                "
    },
    {
        "name": "ImageAnnotation empty",
        "struct": ImageAnnotation,
        "attrs": dict(
            annotations=[]
        ),
        "data": b"       0          "
    },
    {
        "name": "ImageAnnotation",
        "struct": ImageAnnotation,
        "attrs": dict(
            annotations=[
                dict(
                    line_num=10,
                    pixel_num=12345,
                    text="Hello World"
                ),
                dict(
                    line_num=20,
                    pixel_num=54321,
                    text="Goodbye"
                )
            ]
        ),
        "data": (
            b"       2        "
            b"      10   12345Hello World     "
            b"      20   54321Goodbye         "
            b"  "
        )
    }
]


@pytest.mark.parametrize(
    "struct,attrs,expected",
    [(item["struct"], item["attrs"], item["data"]) for item in TEST_DATA],
    ids=[item["name"] for item in TEST_DATA]
)
def test_build(struct, attrs, expected):
    data = struct.build(attrs)

    assert data == expected


@pytest.mark.parametrize(
    "struct,data,expected_attrs",
    [(item["struct"], item["data"], item["attrs"]) for item in TEST_DATA],
    ids=[item["name"] for item in TEST_DATA]
)
def test_parse(struct, data, expected_attrs):
    container = struct.parse(data)

    # There may be some extra attributes for spare fields
    assert container.items() >= expected_attrs.items()
