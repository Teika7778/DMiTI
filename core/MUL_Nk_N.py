from core import generic_module as gm
from data_types import *
import copy


class MUL_Nk_N(gm.AbstractModule):
    def execute(self, args):
        if len(args) != 2:
            raise ValueError("Improper arguments: function takes only 2 arg")
        if not (isinstance(args[0], Natural) and isinstance(args[1], Natural)):
            raise ValueError("Invalid data type: must be natural")
        result = copy.deepcopy(args[0])
        for i in range(len(args[1].numbers)):  # проходит по списку цифр натурального числа k
            result.numbers = args[1].numbers[i] * 10**i * [0] + result.numbers  # Дописывается число нулей в соответсвии
            # с разрядом и цифрой данного разряда
        return [result]

    def reference(self) -> str:
        pass