from data_types import *
import copy

def abs_z_n(integer):
    if not isinstance(integer, Integer): #проверка типа
            raise ValueError("Invalid data type: must be integer")
    return [copy.deepcopy(integer.natural)] #возвращаем массив
