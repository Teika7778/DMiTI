from core import generic_module as gm
from core.custom_logic.AND_BB_B import AND_BB_B
from core.custom_logic.OR_BB_B import OR_BB_B
from core.custom_logic.NOT_B_B import NOT_B_B


class XOR_BB_B(gm.AbstractModule):
    def __init__(self):
        self.or_m = OR_BB_B()
        self.and_m = AND_BB_B()
        self.not_m = NOT_B_B()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes only 2 arg")
        arg1 = args[0]
        arg2 = args[1]
        if not isinstance(arg1, bool) or not isinstance(arg2, bool):  # проверка типа
            raise ValueError("Invalid data type: args must be boolean")
        return self.and_m.execute(
            [self.or_m.execute([arg1, arg2])[0], self.not_m.execute([self.and_m.execute([arg1, arg2])[0]])[0]])

    def reference(self) -> str:
        return ("Logical XOR [BOOLEAN, BOOLEAN -> BOOLEAN]\n"
                "Arguments:\n"
                "\t1: Boolean - first term\n"
                "\t2: Boolean - second term\n"
                "Returns:\n"
                "\t1: Boolean - result\n"
                "Author: Evdokimov Maxim \n")
