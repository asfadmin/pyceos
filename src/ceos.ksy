meta:
  id: ceos
  file-extension: ceos
  ks-opaque-types: true
  imports:
    - data_set_summary_record
    - map_projection_record
    - platform_position_record
    - attitude_record
    - radiometric_record
    - data_quality_record
    - imagery_options_record
seq:
  - id: records
    type: record
    repeat: eos
types:
  record:
    seq:
      - id: header
        type: record_header
      - id: body
        size: header.size - 12
        type:
          switch-on: header.type
          cases:
            'record_type::data_set_summary': data_set_summary_record
            'record_type::map_projection': map_projection_record
            'record_type::platform_position': platform_position_record
            'record_type::attitude': attitude_record
            'record_type::radiometric': radiometric_record
            'record_type::data_quality': data_quality_record
            'record_type::imagery_options': imagery_options_record
  record_header:
    seq:
      - id: sequence_number
        type: u4be
      - id: subtype_1
        type: u1
      - id: type
        type: u1
        enum: record_type
      - id: subtype_2
        type: u1
      - id: subtype_3
        type: u1
        enum: subtype_3
      - id: size
        type: u4be
enums:
  record_type:
    10: data_set_summary
    18: scene_header
    20: map_projection
    30: platform_position
    36: map_projection_alos
    40: attitude
    50: radiometric
    51: radiometric_compensation
    60: data_quality
    70: data_histogram
    80: range_spectra
    120: processing_parameter
    192: imagery_options
    193: trailer_file_descriptor
    200: facility_related
    210: asf_facility_related
    220: esa_facility_related
    230: jaxa_facility_related
    300: file_descriptor
  subtype_3:
    10: ceos
    18: unspecified
    36: ccrs
    50: esa
    60: nasa
    61: jpl
    70: jaxa
    80: dfvlr
    90: rae
    100: telespazio
