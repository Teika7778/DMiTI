from core import generic_module as gm
from data_types import *
import copy


# Умножение целого на (-1)
class MUL_ZM_Z(gm.AbstractModule):
    def execute(self, args):
        if len(args) != 1:  # проверка на количество аргументов
            raise ValueError("Invalid number of arguments")
        if not (isinstance(args[0], Integer)):  # проверка на тип данных
            raise ValueError("The number isn`t integer")

        result = copy.deepcopy(args[0])

        if not(len(result.natural.numbers) == 1 and result.natural.numbers[-1] == 0): # если значение натурального числа не 0:
            result.is_positive = not result.is_positive   # меняем значение знака на противоположное
        return [result]                                   # возвращаем копию целого числа с новым знаком

    def reference(self) -> str:
        pass
