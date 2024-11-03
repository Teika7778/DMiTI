from core.ADD_QQ_Q import ADD_QQ_Q
import copy


class ADD_PP_P(gm.AbstractModule):
    def __init__(self):
        self.add_qq_q = ADD_QQ_Q()  # Модуль для сложения рациональных чисел

    def execute(self, args):
        if len(args) != 2:
            raise ValueError("Неправильное количество аргументов: функция принимает 2 аргумента")
        if not (isinstance(args[0], Polynomial) and isinstance(args[1], Polynomial)):
            raise ValueError("Неправильный тип данных: аргументы должны быть многочленами")

        poly1, poly2 = copy.deepcopy(args[0]), copy.deepcopy(args[1])  # Копируем многочлены для избежания мутаций
        result_poly = Polynomial([])  # Инициализируем результат пустым многочленом

        # Определяем максимальную степень многочленов
        max_degree = max(poly1.degree(), poly2.degree())

        # Складываем коэффициенты одночленов с одинаковыми степенями
        for degree in range(max_degree + 1):
            term1 = poly1.coefficient(degree) if poly1.degree() >= degree else Rational(0, 1)
            term2 = poly2.coefficient(degree) if poly2.degree() >= degree else Rational(0, 1)

            # Используем ADD_QQ_Q для сложения коэффициентов
            sum_of_terms = self.add_qq_q.execute([term1, term2])[0]

            # Добавляем результат к многочлену, если коэффициент не равен нулю
            if sum_of_terms.numerator != 0:
                result_poly.add_term(sum_of_terms, degree)

        return result_poly

    def reference(self) -> str:
        return "Модуль для сложения многочленов"
