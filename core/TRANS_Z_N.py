from core import generic_module as gm
from data_types import *
import copy


# Преобразование целого неотрицательного в натуральное
class TRANS_Z_N(gm.AbstractModule):
    def execute(self, args):
        if len(args) != 1:  # проверка на количество аргументов
            raise ValueError("Invalid number of arguments")
        if not (isinstance(args[0], Integer)):  # проверка на тип данных
            raise ValueError("The number isn`t integer")
        if not args[0].is_positive:  # проверяем знак полученного целого числа
            raise ValueError("The integer must be positive")  # если число отрицательное, выбрасываем ошибку

        return [copy.deepcopy(args[0].natural)]  # возвращаем копию натурального числа

    def reference(self) -> str:
        return ("Convert positive integer to natural number [INTEGER -> NATURAL]\n"
                "Arguments:\n"
                "\t1: Integer (positive) - number to convert\n"
                "Returns:\n"
                "\t1: Natural - converted number\n"
                "Author: Dmitry Kashutin\n")
