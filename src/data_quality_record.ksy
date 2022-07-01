meta:
  id: data_quality_record
  ks-opaque-types: true
seq:
  - id: sequence_number
    size: 4
    type: ascii_int
  - id: sar_chan
    size: 4
    type: str
    encoding: ascii
  - id: cali_date
    size: 6
    type: str
    encoding: ascii
  - id: nchan
    size: 4
    type: ascii_int
  - id: islr
    size: 16
    type: ascii_float
  - id: pslr
    size: 16
    type: ascii_float
  - id: azi_ambig
    size: 16
    type: ascii_float
  - id: rng_ambig
    size: 16
    type: ascii_float
  - id: snr
    size: 16
    type: ascii_float
  - id: ber
    size: 16
    type: ascii_float
  - id: rng_res
    size: 16
    type: ascii_float
  - id: azi_res
    size: 16
    type: ascii_float
  - id: rad_res
    size: 16
    type: ascii_float
  - id: dyn_rng
    size: 16
    type: ascii_float
  - id: abs_radiometric_uncertainty
    type: db_deg
  - id: rel_radiometric_uncertainty
    type: db_deg
    repeat: expr
    repeat-expr: nchan.as<u4>
  - id: alt_locerr
    size: 16
    type: ascii_float
  - id: crt_locerr
    size: 16
    type: ascii_float
  - id: alt_scale
    size: 16
    type: ascii_float
  - id: crt_scale
    size: 16
    type: ascii_float
  - id: dis_skew
    size: 16
    type: ascii_float
  - id: ori_err
    size: 16
    type: ascii_float
  - id: misregistration_error
    type: alt_crt
    repeat: expr
    repeat-expr: nchan.as<u4>
types:
  db_deg:
    seq:
      - id: decibles
        size: 16
        type: ascii_float
      - id: degrees
        size: 16
        type: ascii_float
  alt_crt:
    seq:
      - id: along_track
        size: 16
        type: ascii_float
      - id: cross_track
        size: 16
        type: ascii_float
