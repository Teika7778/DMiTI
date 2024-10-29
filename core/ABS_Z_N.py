from data_types import *
import copy


def ABS_Z_N(args):
    if not len(args) == 1:
        raise ValueError("Improper arguments: function takes only 1 arg")
    integer = args[0]
    if not isinstance(integer, Integer):  # проверка типа
        raise ValueError("Invalid data type: must be integer")
    return [copy.deepcopy(integer.natural)]  # возвращаем массив
