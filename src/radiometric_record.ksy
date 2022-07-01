meta:
  id: radiometric_record
  ks-opaque-types: true
seq:
  - id: sequence_number
    size: 4
    type: ascii_int
  - id: number_rec
    size: 4
    type: ascii_int
  - id: calibration_factor
    size: 16
    type: ascii_float
  - id: delta_trans
    type: matrix2x2
  - id: delta_receive
    type: matrix2x2
types:
  matrix2x2:
    seq:
      - id: rows
        type: matrix2x2row
        repeat: expr
        repeat-expr: 2
  matrix2x2row:
    seq:
      - id: values
        type: complex
        repeat: expr
        repeat-expr: 2
  complex:
    seq:
      - id: real
        size: 16
        type: ascii_float
      - id: imaginary
        size: 16
        type: ascii_float
