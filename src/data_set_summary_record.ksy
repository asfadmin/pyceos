meta:
  id: data_set_summary_record
  ks-opaque-types: true
  imports:
    - data_set_summary_record_sensor_specific_alos
seq:
  - id: sequence_number
    size: 4
    type: ascii_int
  - id: sar_chan
    size: 4
    type: ascii_int
  - id: product_id
    size: 32
    type: str
    encoding: ascii
  - id: scene_des
    size: 16
    type: str
    encoding: ascii
  - id: inp_sctim
    size: 32
    type: str
    encoding: ascii
  - id: asc_des
    size: 16
    type: str
    encoding: ascii
  - id: pro_lat
    size: 16
    type: ascii_float
  - id: pro_long
    size: 16
    type: ascii_float
  - id: pro_head
    size: 16
    type: ascii_float
  - id: ellip_des
    size: 16
    type: str
    encoding: ascii
  - id: ellip_maj
    size: 16
    type: ascii_float
  - id: ellip_min
    size: 16
    type: ascii_float
  - id: earth_mass
    size: 16
    type: ascii_float
  - id: grav_const
    size: 16
    type: ascii_float
  - id: ellip_j
    size: 16
    type: ascii_float
    repeat: expr
    repeat-expr: 3
  # In mapready the following 48 bytes can also be partitioned differently
  # ----------
  - id: spare_1
    size: 16
  - id: terrain_h
    size: 16
    type: ascii_float
  - id: sc_lin
    size: 8
    type: ascii_float
  - id: sc_pix
    size: 8
    type: ascii_float
  # ----------
  - id: scene_len
    size: 16
    type: ascii_float
  - id: scene_wid
    size: 16
    type: ascii_float
  - id: spare_2
    size: 16
  - id: nchn
    size: 4
    type: ascii_int
  - id: spare_3
    size: 4
  - id: mission_id
    size: 16
    type: str
    encoding: ascii
  - id: sensor_id
    size: 32
    type: str
    encoding: ascii
  - id: revolution
    size: 8
    type: ascii_int
  - id: plat_lat
    size: 8
    type: ascii_float
  - id: plat_long
    size: 8
    type: ascii_float
  - id: plat_head_scene
    size: 8
    type: ascii_float
  - id: clock_ang
    size: 8
    type: ascii_float
  - id: incident_ang
    size: 8
    type: ascii_float
  - id: frequency
    size: 8
    type: ascii_float
  - id: wave_length
    size: 16
    type: ascii_float
  - id: motion_comp
    size: 2
    type: str
    encoding: ascii
  - id: pulse_code
    size: 16
    type: str
    encoding: ascii
  - id: ampl_coef
    size: 16
    type: ascii_float
    repeat: expr
    repeat-expr: 5
  - id: phase_coef
    size: 16
    type: ascii_float
    repeat: expr
    repeat-expr: 5
  - id: chirp_ext_ind
    size: 8
    type: ascii_int
  - id: spare_4
    size: 8
  - id: rng_samp_rate
    size: 16
    type: ascii_float
  - id: rng_gate
    size: 16
    type: ascii_float
  - id: rng_length
    size: 16
    type: ascii_float
  - id: baseband_f
    size: 4
    type: str
    encoding: ascii
  - id: rngcmp_f
    size: 4
    type: str
    encoding: ascii
  - id: gn_polar
    size: 16
    type: ascii_float
  - id: gn_cross
    size: 16
    type: ascii_float
  - id: chn_bits
    size: 8
    type: ascii_int
  - id: quant_desc
    size: 12
    type: str
    encoding: ascii
  - id: i_bias
    size: 16
    type: ascii_float
  - id: q_bias
    size: 16
    type: ascii_float
  - id: iq_ratio
    size: 16
    type: ascii_float
  - id: spare_dss_7
    size: 16
    type: ascii_float
  - id: spare_dss_8
    size: 16
    type: ascii_float
  - id: ele_sight
    size: 16
    type: ascii_float
  - id: mech_sight
    size: 16
    type: ascii_float
  - id: echo_track
    size: 4
    type: str
    encoding: ascii
  - id: prf
    size: 16
    type: ascii_float
  - id: elev_beam
    size: 16
    type: ascii_float
  - id: azi_beam
    size: 16
    type: ascii_float
  - id: sat_bintim
    size: 16
    type: ascii_int
  - id: sat_clktim
    size: 32
    type: str
    encoding: ascii
  - id: sat_clkinc
    size: 16
    type: ascii_int
  - id: fac_id
    size: 16
    type: str
    encoding: ascii
  - id: sys_id
    size: 8
    type: str
    encoding: ascii
  - id: ver_id
    size: 8
    type: str
    encoding: ascii
  - id: fac_code
    size: 16
    type: str
    encoding: ascii
  - id: lev_code
    size: 16
    type: str
    encoding: ascii
  - id: product_type
    size: 32
    type: str
    encoding: ascii
  - id: algor_id
    size: 32
    type: str
    encoding: ascii
  - id: n_azilok
    size: 16
    type: ascii_float
  - id: n_rnglok
    size: 16
    type: ascii_float
  - id: bnd_azilok
    size: 16
    type: ascii_float
  - id: bnd_rnglok
    size: 16
    type: ascii_float
  - id: bnd_azi
    size: 16
    type: ascii_float
  - id: bnd_rng
    size: 16
    type: ascii_float
  - id: azi_weight
    size: 32
    type: str
    encoding: ascii
  - id: rng_weight
    size: 32
    type: str
    encoding: ascii
  - id: data_inpsrc
    size: 16
    type: str
    encoding: ascii
  - id: rng_res
    size: 16
    type: ascii_float
  - id: azi_res
    size: 16
    type: ascii_float
  - id: radi_stretch
    size: 16
    type: ascii_float
    repeat: expr
    repeat-expr: 2
  - id: alt_dopcen
    size: 16
    type: ascii_float
    repeat: expr
    repeat-expr: 3
  - id: spare_5
    size: 16
  - id: crt_dopcen
    size: 16
    type: ascii_float
    repeat: expr
    repeat-expr: 3
  - id: time_dir_pix
    size: 8
    type: str
    encoding: ascii
  - id: time_dir_lin
    size: 8
    type: str
    encoding: ascii
  - id: alt_rate
    size: 16
    type: ascii_float
    repeat: expr
    repeat-expr: 3
  - id: spare_6
    size: 16
  - id: crt_rate
    size: 16
    type: ascii_float
    repeat: expr
    repeat-expr: 3
  - id: spare_7
    size: 16
  - id: line_cont
    size: 8
    type: str
    encoding: ascii
  - id: clutterlock_flg
    size: 4
    type: str
    encoding: ascii
  - id: auto_focus
    size: 4
    type: str
    encoding: ascii
  - id: line_spacing
    size: 16
    type: ascii_float
  - id: pixel_spacing
    size: 16
    type: ascii_float
  - id: rngcmp_desg
    size: 16
    type: str
    encoding: ascii
  - id: dopcen_const
    size: 16
    type: ascii_float
  - id: dopcen_lin
    size: 16
    type: ascii_float
  - id: sensor_specific
    size-eos: true
    type:
      switch-on: sensor_id.substring(0, 4)
      cases:
        '"ALOS"': data_set_summary_record_sensor_specific_alos
