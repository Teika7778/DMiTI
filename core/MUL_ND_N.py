from core import generic_module as gm
from data_types import *



class MUL_ND_N(gm.AbstractModule):
    def execute(self, args):
        if len(args) != 2:
            raise ValueError("Improper arguments: function takes only 2 arg")
        if not (isinstance(args[0], Natural) and isinstance(args[1], Natural)):
            raise ValueError("Invalid data type: must be natural")
        if len(args[1].numbers) != 1:
            raise ValueError("Improper arguments: the second argument must be a "
                             "natural number storing a single digit")
        if args[1].numbers[0] == 0:
            return [Natural([0])]
        transfer = 0  # Переменная, хронящая перенос в следующий разряд при умножении
        result = []  # Список, хранящий результат умножения
        for i in args[0].numbers:
            mul = i * args[1].numbers[0] + transfer  # Подсчитываем результат умножения для текущего разряда
            result.append(mul % 10)  # Добавляем в список результата цифру для текущего разряда
            transfer = mul // 10  # Убираем в переменную цифру, переходяшую в следующий разряд
        if transfer != 0:
            result.append(transfer)
        return [Natural(result)]

    def reference(self) -> str:
        pass
