from data_types import *
from core import generic_module as gm


class MUL_ZZ_Z(gm.AbstractModule):
    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes 2 arg")

        if not (isinstance(args[0], Integer) and isinstance(args[1], Integer)):
            raise ValueError("Invalid data type: must be integer")

        multiplier, multiplicand = (args[0], args[1]) if len(args[0].natural.numbers) <= len(args[1].natural.numbers) else (args[1], args[0])

        # Инициализация результата как пустого числа максимально возможной длины
        result = Integer(Natural([0]), is_positive=(multiplier.is_positive == multiplicand.is_positive))
        result.natural.numbers = [0] * (len(multiplier.natural.numbers) + len(multiplicand.natural.numbers))

        # Перемножение "столбиком" каждой цифры множителя на каждую цифру множимого
        for i, multiplier_digit in enumerate(multiplier.natural.numbers):
            carry = 0
            for k, multiplicand_digit in enumerate(multiplicand.natural.numbers):
                product = multiplier_digit * multiplicand_digit + result.natural.numbers[i + k] + carry #Складываем с предыдущим найденным и переносом
                result.natural.numbers[i + k] = product % 10  # Запись текущей цифры результата
                carry = product // 10        # Перенос на следующий разряд

            # Добавление последнего переноса, если он остался, в следующий разряд
            result.natural.numbers[i + len(multiplicand.natural.numbers)] += carry

        result.natural.simplify()
        return [result]

    def reference(self) -> str:
        pass
