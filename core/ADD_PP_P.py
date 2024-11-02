from core import generic_module as gm
from data_types import *
from core.ADD_QQ_Q import ADD_QQ_Q  # Импортируем модуль сложения рациональных чисел


class ADD_PP_P(gm.AbstractModule):
    def __init__(self):
        # Инициализация модуля сложения рациональных чисел
        self.add_qq_q = ADD_QQ_Q()

    def execute(self, args):
        # Проверка: функция должна принимать два аргумента
        if len(args) != 2:
            raise ValueError("Неправильное количество аргументов: функция принимает 2 полинома")

        # Проверка типов аргументов
        poly1, poly2 = args
        if not (isinstance(poly1, Polynomial) and isinstance(poly2, Polynomial)):
            raise ValueError("Неправильный тип данных: оба аргумента должны быть полиномами")

        # Определяем максимальную степень результирующего многочлена
        max_degree = max(len(poly1.coefficients), len(poly2.coefficients))

        # Создаем массив для хранения коэффициентов результирующего многочлена
        result_coefficients = []

        for i in range(max_degree):
            # Получаем коэффициенты из каждого полинома, если они существуют; иначе используем Rational(0/1)
            coeff1 = poly1.coefficients[i] if i < len(poly1.coefficients) else Rational(Integer(Natural([0])),
                                                                                        Natural([1]))
            coeff2 = poly2.coefficients[i] if i < len(poly2.coefficients) else Rational(Integer(Natural([0])),
                                                                                        Natural([1]))

            # Складываем коэффициенты с использованием модуля ADD_QQ_Q
            result_coeff = self.add_qq_q.execute([coeff1, coeff2])[0]
            result_coefficients.append(result_coeff)

        # Создаем и возвращаем результирующий полином
        result_polynomial = Polynomial(result_coefficients)
        return [result_polynomial]

    def reference(self):
        return "Модуль для сложения многочленов"
