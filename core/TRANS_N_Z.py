from core import generic_module as gm
from data_types import *
import copy


# Преобразование натурального в целое
class TRANS_N_Z(gm.AbstractModule):
    def execute(self, args):
        if len(args) != 1:  # проверка на количество аргументов
            raise ValueError("Invalid number of arguments")
        if not (isinstance(args[0], Natural)):  # проверка на тип данных
            raise ValueError("The number isn`t natural")

        result = copy.deepcopy(args[0])  # копируем натуральное число
        return [Integer(result)]  # вызываем конструктор целого числа

    def reference(self) -> str:
        return ("Convert natural to integer number [NATURAL -> INTEGER]\n"
                "Arguments:\n"
                "\t1: Natural - number to convert\n"
                "Returns:\n"
                "\t1: Integer - converted number\n"
                "Author: Dmitry Kashutin\n")
