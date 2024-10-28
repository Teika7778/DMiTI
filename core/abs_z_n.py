from data_types import Natural, Integer

def abs_z_n(integer):
    if not isinstance(integer, Integer): #проверка типа
            raise ValueError("Invalid data type: must be integer")
    return [integer.natural] #возвращаем массив
