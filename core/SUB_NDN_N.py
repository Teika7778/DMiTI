from core.SUB_NN_N import SUB_NN_N
from core.COM_NN_D import COM_NN_D
from core.MUL_ND_N import MUL_ND_N
from core import generic_module as gm
from data_types import *
import copy

class SUB_NDN_N(gm.AbstractModule):
    def execute(self, args):
        # выброс исключения, если:
        if not isinstance(args, list):  # args не list
            raise ValueError("Invalid args type: args must be a list")

        if not len(args) == 3:  # в списке аргументов не 3 аргумента
            raise ValueError("Improper arguments: function takes only 3 args")

        if not isinstance(args[0], Natural):  # первый аргумент не Natural
            raise ValueError("Invalid data type: first arg must be natural")

        if not isinstance(args[1], Natural):  # второй аргумент не Natural
            raise ValueError("Invalid data type: second arg must be natural")

        if not len(args[1].numbers) == 1:  # второй аргумент не является цифрой
            raise ValueError("Invalid second arg: second arg must be a digit")

        if not isinstance(args[2], Natural):  # третий аргумент не Natural
            raise ValueError("Invalid data type: third arg must be natural")

        diminutive  = args[0]  # уменьшаемое
        deductible = MUL_ND_N().execute([args[2], args[1]])[0]  # вычитаемое - произведение второго натурального и цифры
        compare = COM_NN_D().execute([diminutive, deductible])[0]  # результат сравнения
        if compare.numbers[0] == 1:  # если второе СТРОГО БОЛЬШЕ первого
            raise ValueError("Was expected non-negative result, negative one have been gotten")

        return SUB_NN_N().execute([diminutive, deductible])  # упрощение и копия не прописаны здесь,
        # т.к. прописаны в логике вычитания

    def reference(self) -> str:
        return (
            "Subtracting a natural number multiplied by a natural in the range [0,9] from a natural [NATURAL, NATURAL (DIGIT) -> NATURAL]\n"
            "Arguments:\n"
            "\t1: Natural - minuend number\n"
            "\t2: Digit - multiplier\n"
            "Returns:\n"
            "\t1: Natural - difference\n"
            "Author: Alexey Maidurov\n")