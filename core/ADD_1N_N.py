from core import generic_module as gm
from data_types import *
import copy

class ADD_1N_N(gm.AbstractModule):
    def execute(self, args):
        if not isinstance(args, list):  # аргумент должен быть листом
            raise ValueError("Invalid args type: args must be a list")
        if not len(args) == 1:  # должен быть только 1 аргумент
            raise ValueError("Improper arguments: function takes only 1 arg")
        if not isinstance(args[0], Natural):  # проверка типа
            raise ValueError("Invalid data type: must be natural")

        numbers = copy.deepcopy(args[0].numbers)
        for i in range(len(numbers)):  # бежим по цифрам, начиная с меньшей
            if numbers[i] != 9:  # если натыкаемся не на 9, то просто прибавляем к ней 1 и возвращаем нат. число
                numbers[i] += 1
                return [Natural(numbers)]
            else:
                numbers[i] = 0  # если 9, то +1 переходит на след. разряд
        numbers.append(1)  # если цикл закончился, но не было выхода из функции, то значит, что число состояло из
        return [Natural(numbers)]  # одних лишь 9, поэтому надо сделать еще один разряд

    def reference(self) -> str:
        return ("Add 1 to a natural number [NATURAL -> NATURAL]\n"
                "Arguments:\n"
                "\t1: Natural - number to increase\n"
                "Returns:\n"
                "\t1: Natural - increased number\n"
                "Author: Aleksei Maidurov\n")


