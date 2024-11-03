from core import generic_module as gm
from data_types import *
from core.LCM_NN_N import LCM_NN_N  # Наименьшее общее кратное для натуральных чисел
from core.MUL_ZZ_Z import MUL_ZZ_Z  # Умножение целых чисел
from core.SUB_ZZ_Z import SUB_ZZ_Z  # Вычитание целых чисел
import copy

class SUB_QQ_Q(gm.AbstractModule):
    def __init__(self):
        # Инициализация зависимостей: НОК натуральных чисел, умножение и вычитание целых чисел
        self.lcm_nn_n = LCM_NN_N()
        self.mul_zz_z = MUL_ZZ_Z()
        self.sub_zz_z = SUB_ZZ_Z()

    def execute(self, args):
        # Проверка на наличие двух аргументов
        if len(args) != 2:
            raise ValueError("Improper arguments: function takes exactly 2 arguments")
        # Проверка типов аргументов
        if not (isinstance(args[0], Rational) and isinstance(args[1], Rational)):
            raise ValueError("Invalid data type: arguments must be Rational")


        # Копирование аргументов для предотвращения изменения исходных данных
        rational_1, rational_2 = copy.deepcopy(args[0]), copy.deepcopy(args[1])

        # Шаг 1: Вычисляем НОК знаменателей
        lcm_denom = self.lcm_nn_n.execute([rational_1.denominator, rational_2.denominator])[0]
        
        # Шаг 2: Приводим числители обеих дробей к общему знаменателю
        if(rational_1.denominator.numbers ==  lcm_denom.numbers and rational_2.denominator.numbers ==  lcm_denom.numbers):    
            num2_mult = copy.deepcopy(rational_2.numerator)
            num1_mult = copy.deepcopy(rational_1.numerator)
            newDen = Integer(lcm_denom, is_positive=True)
        else:
            num1_mult = self.mul_zz_z.execute([rational_1.numerator, Integer(rational_2.denominator, is_positive=True)])[0]
            num2_mult = self.mul_zz_z.execute([rational_2.numerator, Integer(rational_1.denominator, is_positive=True)])[0]
            newDen = self.mul_zz_z.execute([Integer(rational_2.denominator, is_positive=True), Integer(rational_1.denominator, is_positive=True)])[0]

        # Шаг 3: Вычитаем приведенные числители
        numerator_diff = self.sub_zz_z.execute([num1_mult, num2_mult])[0]
        # Шаг 4: Создаем и возвращаем результат в виде рационального числа с вычитанием числителей и общим знаменателем
        result = Rational(numerator_diff, newDen.natural)
        return [result]

    def reference(self) -> str:
        pass
