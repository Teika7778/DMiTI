from core.DIV_NN_Dk import DIV_NN_Dk
from core.COM_NN_D import COM_NN_D
from core.MUL_NN_N import MUL_NN_N
from core.SUB_NN_N import SUB_NN_N
from core.ADD_NN_N import ADD_NN_N
from core import generic_module as gm
from data_types import *

class DIV_NN_N(gm.AbstractModule):
    def execute(self, args):
        # выброс исключения, если:
        if not isinstance(args, list):  # args не list
            raise ValueError("Invalid args type: args must be a list")

        if not len(args) == 2:  # в списке аргументов не 2 аргумента
            raise ValueError("Improper arguments: function takes only 2 args")

        if not isinstance(args[0], Natural):  # первый аргумент не Natural
            raise ValueError("Invalid data type: first arg must be natural")

        if not isinstance(args[1], Natural):  # второй аргумент не Natural
            raise ValueError("Invalid data type: second arg must be natural")

        divider = args[1]  # делитель
        if divider.numbers[-1] == 0:  # деление на 0
            raise ValueError("Invalid division: division by zero")

        divisible = args[0]  # делимое
        quotient = Natural([0])  # частное
        while COM_NN_D().execute([divisible, divider])[0].numbers[0] != 1:  # пока делимое больше либо равно делителя
            subquotient = DIV_NN_Dk().execute([divisible, divider])[0]  # первый разряд частного с нужным кол-вом нулей
            quotient = ADD_NN_N().execute([quotient, subquotient])[0]  # увеличиваем частное
            deductible = MUL_NN_N().execute([subquotient, divider])[0]  # произведение "мини-частного" и делителя
            divisible = SUB_NN_N().execute([divisible, deductible])[0]  # вычитаем их делимого произведение

        return [quotient]

    def reference(self) -> str:
        pass
