from core import generic_module as gm
from data_types import *

from core.DIV_ZZ_Z import DIV_ZZ_Z  # Частное от деления целого на целое (делитель отличен от нуля)
from core.MUL_ZZ_Z import MUL_ZZ_Z  # Умножение целых чисел
from core.SUB_ZZ_Z import SUB_ZZ_Z  # Вычитание целых чисел

#  остаток от деления целого на целое(делитель отличен от нуля)
class MOD_ZZ_Z(gm.AbstractModule):

    def __init__(self):
        self.div_zz_z = DIV_ZZ_Z()
        self.mull_zz_z = MUL_ZZ_Z()
        self.sub_zz_z = SUB_ZZ_Z()

    def execute(self, args):
        if len(args) != 2:  # проверка на количество аргументов
            raise ValueError("Invalid number of arguments")
        if not (isinstance(args[0], Integer) and isinstance(args[1], Integer)):  # проверка на тип данных
            raise ValueError("The number isn`t integer")
        if len(args[1].natural.numbers) == 1 and args[1].natural.numbers[-1] == 0:  # проверка делителя на ноль
            raise ValueError("The divisor cannot be zero")

        # a/b => a=b*q+r => r=a-b*q
        quotient = self.div_zz_z.execute([args[0], args[1]])  # получаем частное от деления
        multiplication = self.mull_zz_z.execute([quotient[0], args[1]])  # умножаем частное на делитель
        result = self.sub_zz_z.execute([args[0], multiplication[0]])  # вычитаем из делимого и получаем остаток

        return [result]

    def reference(self) -> str:
        pass