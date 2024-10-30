from core import generic_module as gm
from core.COM_NN_D import COM_NN_D
from data_types import *

class SUB_NN_N(gm.AbstractModule):
    def __init__(self):
        self.module = COM_NN_D()

    def execute(self, args):
        # проверка данных не проводится, так как будет вызываться метод сравнения чисел, который включает проверку
        # Убедимся, что первый аргумент больше или равен второму
        comparison_result = self.module.execute(args)
        if comparison_result[0].numbers == [1]:  # первое больше второго
            raise ValueError("Первое число должно быть больше или равно.")

        # Результат вычитания
        result = Natural([])
        borrow = 0  # Переменная для учета займа

        for i in range(len(args[0].numbers)):
            digit = args[1].numbers[i] if i < len(args[1].numbers) else 0

            # Вычитаем, учитывая заем
            if args[0].numbers[i] < digit + borrow:
                args[0].numbers[i] += 10  # Берем заем
                result.numbers.append(args[0].numbers[i] - digit - borrow)
                borrow = 1
            else:
                result.numbers.append(args[0].numbers[i] - digit - borrow)
                borrow = 0



        # Удаляем ведущие нули из результата, если он не ноль
        result.simplify()
        return [result]

    def reference(self) -> str:
        pass