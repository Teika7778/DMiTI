from user_side.command.generic import AbstractCommand

"""
Помещает в var_stack переменную
принимает 3 аргумента:
имя переменной
тип переменной (INT, NAT, RAT, POL)
значение
"""


class PUT(AbstractCommand):
    def execute(self, args, window):
        pass

    def reference(self) -> str:
        pass
