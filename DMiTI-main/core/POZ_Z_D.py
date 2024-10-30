from core import generic_module as gm
from data_types import *
import copy

# Определение положительности числа(2 - положительное, 0 — равное нулю, 1 - отрицательное)
class POZ_Z_D(gm.AbstractModule):
    def execute(self, args):
        if len(args) != 1:  # проверка на количество аргументов
            raise ValueError("Invalid number of arguments")
        if not (isinstance(args[0], Integer)):  # проверка на тип данных
            raise ValueError("The number isn`t integer")

        if len(args[0].natural.numbers) and args[0].natural.numbers[-1] == 0: # проверяем длину натурального числа и значение
            return [Natural([0])]                                  # последней цифры, если натуральное число равно 0, возвращаем 0
        else:                                            # если натуральное число не равно 0:
            return [Natural([2])] if args[0].is_positive else [Natural([1])]   # если знак положительный, возвращаем 2, иначе 1

    def reference(self) -> str:
        pass
