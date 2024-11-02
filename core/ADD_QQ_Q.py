from core import generic_module as gm
from data_types import *
from core.ADD_ZZ_Z import ADD_ZZ_Z
from core.MUL_ZZ_Z import MUL_ZZ_Z
from core.LCM_NN_N import LCM_NN_N
import copy


class ADD_QQ_Q(gm.AbstractModule):
    def __init__(self):
        # Инициализация зависимостей: сложение и умножение целых чисел, НОК натуральных чисел
        self.add_zz_z = ADD_ZZ_Z()
        self.mul_zz_z = MUL_ZZ_Z()
        self.lcm_nn_n = LCM_NN_N()

    def execute(self, args):
        # Проверка: функция должна принимать два аргумента
        if not len(args) == 2:
            raise ValueError("Неправильное количество аргументов: функция принимает 2 аргумента")
        # Проверка типов: аргументы должны быть рациональными числами
        if not (isinstance(args[0], Rational) and isinstance(args[1], Rational)):
            raise ValueError("Неправильный тип данных: аргументы должны быть рациональными числами")

        # Копирование аргументов для избежания мутаций исходных объектов
        rational_1, rational_2 = copy.deepcopy(args[0]), copy.deepcopy(args[1])

        # Шаг 1: Вычисляем наименьшее общее кратное (НОК) знаменателей
        lcm_denom = self.lcm_nn_n.execute([rational_1.denominator, rational_2.denominator])[0]

        # Шаг 2: Приводим каждый числитель к общему знаменателю
        num1_mult = self.mul_zz_z.execute([rational_1.numerator, lcm_denom])[0]
        denom1_mult = self.mul_zz_z.execute([rational_2.numerator, lcm_denom])[0]

        # Шаг 3: Складываем приведенные числители
        numerator_sum = self.add_zz_z.execute([num1_mult, denom1_mult])[0]

        # Шаг 4: Создаем и возвращаем новый объект Rational с суммой числителей и общим знаменателем
        result = Rational(numerator_sum, lcm_denom)
        return [result]

    def reference(self) -> str:
        return "Модуль для сложения рациональных чисел"
