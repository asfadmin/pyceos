meta:
  id: attitude_record
  ks-opaque-types: true
seq:
  - id: npoints
    size: 4
    type: ascii_int
  - id: attitude_data_points
    type: attitude_point
    repeat: expr
    repeat-expr: npoints.as<u4>
types:
  attitude_point:
    seq:
      - id: gmt_day
        size: 4
        type: ascii_int
      - id: gmt_millis
        size: 8
        type: ascii_int
      - id: pitch_flag
        size: 4
        type: ascii_int
      - id: roll_flag
        size: 4
        type: ascii_int
      - id: yaw_flag
        size: 4
        type: ascii_int
      - id: pitch
        size: 14
        type: ascii_float
      - id: roll
        size: 14
        type: ascii_float
      - id: yaw
        size: 14
        type: ascii_float
      - id: pitch_rate_flag
        size: 4
        type: ascii_int
      - id: roll_rate_flag
        size: 4
        type: ascii_int
      - id: yaw_rate_flag
        size: 4
        type: ascii_int
      - id: pitch_rate
        size: 14
        type: ascii_float
      - id: roll_rate
        size: 14
        type: ascii_float
      - id: yaw_rate
        size: 14
        type: ascii_float
