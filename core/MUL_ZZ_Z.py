from data_types import *
from core import generic_module as gm
from core.POZ_Z_D import POZ_Z_D
from core.MUL_NN_N import MUL_NN_N
from core.MUL_ZM_Z import MUL_ZM_Z


class MUL_ZZ_Z(gm.AbstractModule):
    def __init__(self):
        self.poz = POZ_Z_D()
        self.mul_nn_n = MUL_NN_N()
        self.mul_zm_z = MUL_ZM_Z()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes 2 arg")

        if not (isinstance(args[0], Integer) and isinstance(args[1], Integer)):
            raise ValueError("Invalid data type: must be integer")

        if args[0].natural.numbers == [1] and args[0].is_positive is False:  # Применяем модуль умножения на -1
            return self.mul_zm_z.execute([args[1]])

        if args[1].natural.numbers == [1] and args[1].is_positive is False:
            return self.mul_zm_z.execute([args[0]])

        is_positive = False if self.poz.execute([args[0]])[0].numbers != self.poz.execute([args[1]])[0].numbers else True # Если знаки не совпадают = "-"
        abs_result = self.mul_nn_n.execute([args[0].natural, args[1].natural])[0]
        if abs_result.numbers == [0]: is_positive = True
        result = Integer(abs_result, is_positive=is_positive)

        return [result]

    def reference(self) -> str:
        return ("Multiplication of a integer by a integer [INTEGER. INTEGER -> INTEGER]\n"
                "Arguments:\n"
                "\t1: Integer - multiplier\n"
                "\t2: Integer - multiplicand\n"
                "Returns:\n"
                "\t1: Integer - product of multiplication\n"
                "Author: Sofia Skryabina\n")
