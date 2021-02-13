from enum import Enum


class InputType(Enum):
    """
    Defines the naming for input
    readers i.e. file and url
    """

    NONE = 0
    FILE = 1
    URL = 2
