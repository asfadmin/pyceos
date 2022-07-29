from pyceos.types import AsciiBool, AsciiFloat, AsciiInt, AsciiString


# AsciiString #
def test_parse_string():
    st = AsciiString(8)
    assert st.parse(b"        ") == ""
    assert st.parse(b"ALOS    ") == "ALOS"


def test_build_string_pad():
    st = AsciiString(4)
    assert st.build("") == b"    "
    assert st.build("Foo") == b"Foo "


def test_build_string_leftpad():
    st = AsciiString(4, leftpad=True)
    assert st.build("") == b"    "
    assert st.build("Foo") == b" Foo"


# AsciiInt #
def test_parse_int():
    st = AsciiInt(8)
    assert st.parse(b"        ") is None
    assert st.parse(b"       0") == 0
    assert st.parse(b"    1234") == 1234


def test_build_int():
    st = AsciiInt(4)
    assert st.build(None) == b"    "
    assert st.build(0) == b"   0"
    assert st.build(20) == b"  20"


# AsciiBool
def test_parse_bool():
    st = AsciiBool(1)
    assert st.parse(b" ") is None
    assert st.parse(b"0") is False
    assert st.parse(b"1") is True


def test_build_bool():
    st = AsciiBool(2)
    assert st.build(None) == b"  "
    assert st.build(False) == b" 0"
    assert st.build(True) == b" 1"


# AsciiFloat #
def test_parse_float():
    st = AsciiFloat(8)
    assert st.parse(b"        ") is None
    assert st.parse(b"       0") == 0.0
    assert st.parse(b"     0.0") == 0.0
    assert st.parse(b"  12.345") == 12.345
    assert st.parse(b"  12.3E2") == 1230.0
    assert st.parse(b"12.345E2") == 1234.5


def test_build_float_generic():
    st = AsciiFloat(10)
    assert st.build(None) == b"          "
    assert st.build(0.0) == b"         0"
    assert st.build(1.23456789123) == b"  1.234568"


def test_build_float_exp():
    st = AsciiFloat(10, format=".4E")
    assert st.build(None) == b"          "
    assert st.build(0.0) == b"0.0000E+00"
    assert st.build(1.23456789123) == b"1.2346E+00"
    assert st.build(0.23456789123) == b"2.3457E-01"
