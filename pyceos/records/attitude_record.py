from construct import Rebuild, Struct, len_, this

from pyceos.types import E14_6, AsciiInt, FixedSized

AttitudePoint = Struct(
    "gmt_day" / AsciiInt(4),
    "gmt_msec" / AsciiInt(8),
    "pitch_flag" / AsciiInt(4),
    "roll_flag" / AsciiInt(4),
    "yaw_flag" / AsciiInt(4),
    "pitch" / E14_6,
    "roll" / E14_6,
    "yaw" / E14_6,
    "pitch_rate_flag" / AsciiInt(4),
    "roll_rate_flag" / AsciiInt(4),
    "yaw_rate_flag" / AsciiInt(4),
    "pitch_rate" / E14_6,
    "roll_rate" / E14_6,
    "yaw_rate" / E14_6,
)

AttitudeRecord = FixedSized(
    16384 - 12,
    Struct(
        "num_points" / Rebuild(AsciiInt(4), len_(this.points)),
        "points" / AttitudePoint[this.num_points]
    ),
    pattern=b" "
)
