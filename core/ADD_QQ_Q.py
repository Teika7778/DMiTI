from core import generic_module as gm
from data_types import *
from core.ADD_ZZ_Z import ADD_ZZ_Z
from core.MUL_ZZ_Z import MUL_ZZ_Z
from core.LCM_NN_N import LCM_NN_N
from core.TRANS_N_Z import TRANS_N_Z  # Импортируем модуль для преобразования
from core.DIV_NN_N import DIV_NN_N  # Импортируем модуль деления
import copy


class ADD_QQ_Q(gm.AbstractModule):
    def __init__(self):
        self.add_zz_z = ADD_ZZ_Z()  # Сложение целых чисел
        self.mul_zz_z = MUL_ZZ_Z()  # Умножение целых чисел
        self.lcm_nn_n = LCM_NN_N()  # НОК натуральных чисел
        self.trans_n_z = TRANS_N_Z()  # Преобразование из натурального в целое
        self.div_nn_n = DIV_NN_N()  # Деление натуральных чисел

    def execute(self, args):
        if len(args) != 2:
            raise ValueError("Неправильное количество аргументов: функция принимает 2 аргумента")
        if not (isinstance(args[0], Rational) and isinstance(args[1], Rational)):
            raise ValueError("Неправильный тип данных: аргументы должны быть рациональными числами")

        rational_1, rational_2 = copy.deepcopy(args[0]), copy.deepcopy(args[1])  # Избегаем мутаций

        # 1. Вычисляем наименьшее общее кратное (НОК) знаменателей
        lcm_denom = self.lcm_nn_n.execute([rational_1.denominator, rational_2.denominator])[0]

        # 2. НОК делим на каждый знаменатель, получаем множители
        denom_mult_1 = self.trans_n_z.execute([self.div_nn_n.execute([lcm_denom, rational_1.denominator])[0]])[0]
        denom_mult_2 = self.trans_n_z.execute([self.div_nn_n.execute([lcm_denom, rational_2.denominator])[0]])[0]

        # 3. Умножаем числители на соответствующие множители
        # Преобразуем НОК в целое число

        num1_mult = self.mul_zz_z.execute([rational_1.numerator, denom_mult_1])[0]  # Числитель 1
        num2_mult = self.mul_zz_z.execute([rational_2.numerator, denom_mult_2])[0]  # Числитель 2

        # 4. Складываем приведённые числители
        numerator_sum = self.add_zz_z.execute([num1_mult, num2_mult])[0]

        # 5. Возвращаем новый объект Rational с суммой числителей и общим знаменателем
        return [Rational(numerator_sum, lcm_denom)]

    def reference(self) -> str:
        return "Модуль для сложения рациональных чисел"

