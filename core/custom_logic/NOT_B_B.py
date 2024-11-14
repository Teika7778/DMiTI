from core import generic_module as gm


class NOT_B_B(gm.AbstractModule):
    def execute(self, args):
        if not len(args) == 1:
            raise ValueError("Improper arguments: function takes only 1 arg")
        arg1 = args[0]
        if not isinstance(arg1, bool):  # проверка типа
            raise ValueError("Invalid data type: args must be boolean")
        return [not arg1]

    def reference(self) -> str:
        return ("Logical NOT [BOOLEAN, BOOLEAN -> BOOLEAN]\n"
                "Arguments:\n"
                "\t1: Boolean - bool to be inverted\n"
                "Returns:\n"
                "\t1: Boolean - result\n"
                "Author: Evdokimov Maxim \n")