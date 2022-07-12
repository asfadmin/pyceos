from construct import Struct, Terminated

from pyceos.types import F16_7, AsciiInt, ComplexAdapter, Spare

Complex = ComplexAdapter(
    Struct(
        "real" / F16_7,
        "imag" / F16_7
    )
)


def MatrixRow(length: int):
    return Complex[length]


def Matrix(rows: int, cols: int):
    return MatrixRow(rows)[cols]


RadiometricRecord = Struct(
    "sequence_number" / AsciiInt(4),
    "num_fields" / AsciiInt(4),
    "calibration_factor" / F16_7,
    "delta_trans" / Matrix(2, 2),
    "delta_receive" / Matrix(2, 2),
    Spare(9568),
    Terminated
)
