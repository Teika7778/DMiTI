from core import generic_module as gm
from data_types import *
from core.NZER_N_B import NZER_N_B
from core.COM_NN_D import COM_NN_D
from core.MOD_NN_N import MOD_NN_N

class GCF_NN_N(gm.AbstractModule):
    def __init__(self):
        self.nzer_n = NZER_N_B()
        self.com_nn = COM_NN_D()
        self.mod_nn = MOD_NN_N()


    def execute(self, args):
        if len(args) != 2:
            raise ValueError("Improper arguments: function takes only 2 arg")
        if not (isinstance(args[0], Natural) and isinstance(args[1], Natural)):
            raise ValueError("Invalid data type: must be natural")
        result_a = Natural(args[0].numbers)
        result_b = Natural(args[1].numbers)   # создаем новые переменные, чтобы не изменить старые
        while self.nzer_n.execute([result_b])[0]:  # пока result_b не нулевое
            result_a, result_b = result_b, self.mod_nn.execute([result_a, result_b])[0]  # Меняем значение местами,
            # заменяя b делением с остатком a на b
        return [result_a]

    def reference(self) -> str:
        return ("Greatest common divisor of natural numbers [NATURAL. NATURAL -> NATURAL]\n"
                "Arguments:\n"
                "\t1: Natural - first\n"
                "\t2: Natural - second\n"
                "Returns:\n"
                "\t1: Natural - greatest common divisor\n"
                "Author: Artyom Grebenshchikov\n")
