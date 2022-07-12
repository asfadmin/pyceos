from construct import Struct, Terminated, this

from pyceos.types import F16_7, AsciiInt, AsciiString, FixedSized, Spare

DeciblesDegrees = Struct(
    "decibles" / F16_7,
    "degrees" / F16_7
)

AlongTrackCrossTrack = Struct(
    "along_track" / F16_7,
    "cross_track" / F16_7
)

DataQualitySummaryRecord = Struct(
    "sequence_number" / AsciiInt(4),
    "sar_chan" / AsciiString(4),
    "cali_date" / AsciiString(6),
    "num_channels" / AsciiInt(4),
    "islr" / F16_7,
    "pslr" / F16_7,
    "azi_ambig" / F16_7,
    "rng_ambig" / F16_7,
    "snr" / F16_7,
    "ber" / F16_7,
    "rng_res" / F16_7,
    "azi_res" / F16_7,
    "rad_res" / F16_7,
    "dyn_rng" / F16_7,
    "abs_radiometric_uncertainty" / DeciblesDegrees,
    "rel_radiometric_uncertainty" / FixedSized(
        256,
        DeciblesDegrees[this.num_channels]
    ),
    Spare(256),
    "alt_locerr" / F16_7,
    "crt_locerr" / F16_7,
    "alt_scale" / F16_7,
    "crt_scale" / F16_7,
    "dis_skew" / F16_7,
    "ori_err" / F16_7,
    "misregistration_error" / FixedSized(
        256,
        DeciblesDegrees[this.num_channels]
    ),
    Spare(534),
    Terminated
)
