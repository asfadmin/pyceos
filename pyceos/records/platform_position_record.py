from construct import Rebuild, Struct, Terminated, len_, this

from pyceos.types import E22_15, F16_7, AsciiBool, AsciiInt, AsciiString, Spare

PlatformPositionPoint = Struct(
    "position" / E22_15[3],
    "velocity" / E22_15[3]
)

PlatformPositionRecord = Struct(
    "orbit_ele_desg" / AsciiString(32),
    "orbit_ele" / F16_7[6],
    "num_points" / Rebuild(AsciiInt(4), len_(this.positional_data_points)),
    "year" / AsciiInt(4),
    "month" / AsciiInt(4),
    "day" / AsciiInt(4),
    "gmt_day" / AsciiInt(4),
    "gmt_sec" / E22_15,
    "data_int" / E22_15,
    "ref_coord" / AsciiString(64),
    "hr_angle" / E22_15,
    "alt_poserr" / F16_7,
    "crt_poserr" / F16_7,
    "rad_poserr" / F16_7,
    "alt_velerr" / F16_7,
    "crt_velerr" / F16_7,
    "rad_velerr" / F16_7,
    "positional_data_points" / PlatformPositionPoint[this.num_points],
    Spare(18),
    "has_leap_second" / AsciiBool(1),
    Spare(579),
    Terminated
)
