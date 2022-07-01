meta:
  id: data_set_summary_record_sensor_specific_alos
  ks-opaque-types: true
seq:
  - id: cal_data_indicator
    size: 4
    type: ascii_int
  - id: start_cal_up
    size: 8
    type: ascii_int
  - id: stop_cal_up
    size: 8
    type: ascii_int
  - id: start_cal_bottom
    size: 8
    type: ascii_int
  - id: stop_cal_bottom
    size: 8
    type: ascii_int
  - id: prf_switch
    size: 4
    type: ascii_int
  - id: line_prf_switch
    size: 8
    type: ascii_int
  - id: beam_center_dir
    size: 16
    type: ascii_float
  - id: yew_steering
    size: 4
    type: ascii_int
  - id: param_table
    size: 4
    type: ascii_int
  - id: off_nadir_angle
    size: 16
    type: ascii_float
  - id: ant_beam_num
    size: 4
    type: ascii_int
  - id: spare_1
    size: 28
  - id: incid_a
    size: 20
    type: ascii_float
    repeat: expr
    repeat-expr: 6
  - id: image_annotation
    type: image_annotation
types:
  image_annotation:
    seq:
      - id: num_points
        size: 8
        type: ascii_int
      - id: spare_1
        size: 8
      - id: annotations
        type: image_annotation_point
        repeat: expr
        repeat-expr: 64
      - id: spare_2
        size: 2
  image_annotation_point:
    seq:
      - id: line_num
        size: 8
        type: ascii_int
      - id: pixel_num
        size: 8
        type: ascii_int
      - id: text
        size: 16
        type: str
        encoding: ascii
