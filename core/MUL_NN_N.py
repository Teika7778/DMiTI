from data_types import *
from core import generic_module as gm
from core.ADD_NN_N import ADD_NN_N
from core.MUL_ND_N import MUL_ND_N
from core.MUL_Nk_N import MUL_Nk_N



class MUL_NN_N(gm.AbstractModule):
    def __init__(self):
        self.add_nn = ADD_NN_N()
        self.mul_nd = MUL_ND_N()
        self.mul_nk = MUL_Nk_N()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes 2 arg")

        if not (isinstance(args[0], Natural) and isinstance(args[1], Natural)):
            raise ValueError("Invalid data type: must be natural")

        multiplier, multiplicand = (args[0], args[1]) if len(args[0].numbers) <= len(args[1].numbers) else (args[1], args[0])
        result = Natural([])

        # Перемножение "столбиком" каждой цифры множителя на каждую цифру множимого
        for i in range(len(multiplier.numbers)):
            product = self.mul_nd.execute([multiplicand, Natural([multiplier.numbers[i]])])[0]  # Произведение множимого на i-тую цифру множителя
            product_nums = list(map(int, list(str(i))[::-1]))
            product = self.mul_nk.execute([product, Natural(product_nums)])[0]
            result = self.add_nn.execute([result, product])[0]

        result.simplify()
        return [result]

    def reference(self) -> str:
        return ("Multiplication of a natural by a natural [NATURAL. NATURAL -> NATURAL]\n"
                "Arguments:\n"
                "\t1: Natural - multiplier\n"
                "\t2: Natural - multiplicand\n"
                "Returns:\n"
                "\t1: Natural - product of multiplication\n"
                "Author: Artyom Grebenshchikov\n")
