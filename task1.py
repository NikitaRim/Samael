"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""
from enum import Enum

class SimplifiedEnum(type(Enum)):
    def __new__(cls, name, bases, attrs):
        keys = attrs.pop('__keys')
        enum_class = super().__new__(cls, name, bases, attrs)
        for key in keys:
            enum_class.__members__[key] = enum_class(key)
        return enum_class


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ["RED", "BLUE", "ORANGE", "BLACK"]

class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
