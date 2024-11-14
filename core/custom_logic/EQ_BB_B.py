from core import generic_module as gm
from core.custom_logic.XOR_BB_B import XOR_BB_B
from core.custom_logic.NOT_B_B import NOT_B_B


class EQ_BB_B(gm.AbstractModule):
    def __init__(self):
        self.xor_m = XOR_BB_B()
        self.not_m = NOT_B_B()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes only 2 arg")
        arg1 = args[0]
        arg2 = args[1]
        if not isinstance(arg1, bool) or not isinstance(arg2, bool):  # проверка типа
            raise ValueError("Invalid data type: args must be boolean")
        return self.not_m.execute([self.xor_m.execute([arg1, arg2])[0]])

    def reference(self) -> str:
        return ("Checks if provided bools are equal [BOOLEAN, BOOLEAN -> BOOLEAN]\n"
                "Arguments:\n"
                "\t1: Boolean - first term\n"
                "\t2: Boolean - second term\n"
                "Returns:\n"
                "\t1: Boolean - result\n"
                "Author: Evdokimov Maxim \n")