from core import generic_module as gm


class OR_BB_B(gm.AbstractModule):
    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes only 2 arg")
        arg1 = args[0]
        arg2 = args[1]
        if not isinstance(arg1, bool) or not isinstance(arg2, bool):  # проверка типа
            raise ValueError("Invalid data type: args must be boolean")
        return [arg1 or arg2]

    def reference(self) -> str:
        return ("Logical OR [BOOLEAN, BOOLEAN -> BOOLEAN]\n"
                "Arguments:\n"
                "\t1: Boolean - first term\n"
                "\t2: Boolean - second term\n"
                "Returns:\n"
                "\t1: Boolean - result\n"
                "Author: Evdokimov Maxim \n")