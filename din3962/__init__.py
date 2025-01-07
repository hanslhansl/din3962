"""Implementation of DIN 3962 - Tolerances for Cylindrical Gear Teeth.

See https://github.com/hanslhansl/din3962."""

from enum import IntEnum

class GearToothQuality(IntEnum):
    DIN1 = 1
    DIN2 = 2
    DIN3 = 3
    DIN4 = 4
    DIN5 = 5
    DIN6 = 6
    DIN7 = 7
    DIN8 = 8
    DIN9 = 9
    DIN10 = 10
    DIN11 = 11
    DIN12 = 12

from . import din3962_1, din3962_2