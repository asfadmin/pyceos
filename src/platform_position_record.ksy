meta:
  id: platform_position_record
  ks-opaque-types: true
seq:
  - id: orbit_ele_desg
    size: 32
    type: str
    encoding: ascii
  - id: orbit_ele
    size: 16
    type: ascii_float
    repeat: expr
    repeat-expr: 6
  - id: npoints
    size: 4
    type: ascii_int
  - id: year
    size: 4
    type: ascii_int
  - id: month
    size: 4
    type: ascii_int
  - id: day
    size: 4
    type: ascii_int
  - id: gmt_day
    size: 4
    type: ascii_int
  - id: gmt_sec
    size: 22
    type: ascii_float
  - id: data_int
    size: 22
    type: ascii_float
  - id: ref_coord
    size: 64
    type: str
    encoding: ascii
  - id: hr_angle
    size: 22
    type: ascii_float
  - id: alt_poserr
    size: 16
    type: ascii_float
  - id: crt_poserr
    size: 16
    type: ascii_float
  - id: rad_poserr
    size: 16
    type: ascii_float
  - id: alt_velerr
    size: 16
    type: ascii_float
  - id: crt_velerr
    size: 16
    type: ascii_float
  - id: rad_velerr
    size: 16
    type: ascii_float
  - id: positional_data_points
    type: platform_position_point
    repeat: expr
    repeat-expr: npoints.as<u4>
types:
  platform_position_point:
    seq:
      - id: position
        size: 22
        type: ascii_float
        repeat: expr
        repeat-expr: 3
      - id: velocity
        size: 22
        type: ascii_float
        repeat: expr
        repeat-expr: 3
