meta:
  id: imagery_options_record
  ks-opaque-types: true
seq:
  - id: ascii_flag
    size: 2
    type: str
    encoding: ascii
  - id: spare_1
    size: 2
  - id: format_doc
    size: 12
    type: str
    encoding: ascii
  - id: format_rev
    size: 2
    type: str
    encoding: ascii
  - id: design_rev
    size: 2
    type: str
    encoding: ascii
  - id: software_id
    size: 12
    type: str
    encoding: ascii
  - id: file_num
    size: 4
    type: ascii_int
  - id: product_id
    size: 16
    type: str
    encoding: ascii
  - id: rec_seq_flag
    size: 4
    type: str
    encoding: ascii
  - id: seq_loc
    size: 8
    type: ascii_int
  - id: seq_len
    size: 4
    type: ascii_int
  - id: rec_code
    size: 4
    type: str
    encoding: ascii
  - id: code_loc
    size: 8
    type: ascii_int
  - id: code_len
    size: 4
    type: ascii_int
  - id: rec_len
    size: 4
    type: str
    encoding: ascii
  - id: rlen_loc
    size: 8
    type: ascii_int
  - id: rlen_len
    size: 4
    type: ascii_int
  - id: spare_2
    size: 4
  - id: spare_3
    size: 64
  - id: num_of_rec
    size: 6
    type: ascii_int
  - id: reclen
    size: 6
    type: ascii_int
  - id: spare_4
    size: 24
    doc: "TODO: There appear to be 4 fields here now"
  # Data seems to no longer match mapready implementation after this point
