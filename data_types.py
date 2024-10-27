from abc import ABC, abstractmethod
from typing import List


# Абстрактный класс для всех числовых типов
class DataType(ABC):
    # Абстрактный метод для упрощения объектов
    @abstractmethod
    def simplify(self):
        pass


# Класс натурального числа
class Natural(DataType):
    def __init__(self, numbers):
        # Проверка: элементы массива должны быть цифрами от 0 до 9
        valid = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        if any(number not in valid for number in numbers):
            raise ValueError("Invalid digits in natural number")

        # Натуральное число не должно заканчиваться на 0
        if len(numbers) > 1 and numbers[-1] == 0:
            raise ValueError("Natural number cannot end with 0")

        self.numbers = numbers

    # Строковое представление натурального числа
    def __str__(self):
        pass

    # Метод для упрощения объекта
    def simplify(self):
        pass


# Класс целого числа
class Integer(DataType):
    def __init__(self, natural, is_positive=True):
        # Проверка типа: natural должен быть экземпляром класса Natural
        if not isinstance(natural, Natural):
            raise ValueError("Integer must contain a Natural number")

        self.natural = natural
        self.is_positive = is_positive

    # Строковое представление целого числа
    def __str__(self):
        pass

    # Метод для упрощения объекта
    def simplify(self):
        pass


# Класс рационального числа
class Rational(DataType):
    def __init__(self, numerator, denominator):
        # Проверка: числитель должен быть целым числом, а знаменатель натуральным (и не ноль)
        if not isinstance(numerator, Integer):
            raise ValueError("Numerator must be an Integer")
        if not isinstance(denominator, Natural) or denominator.numbers == [0]:
            raise ValueError("Denominator must be a non-zero Natural number")

        self.numerator = numerator
        self.denominator = denominator

    # Строковое представление рационального числа
    def __str__(self):
        pass

    # Метод для упрощения объекта
    def simplify(self):
        pass


# Класс многочлена с рациональными коэффициентами
class Polynomial(DataType):
    def __init__(self, coefficients):
        # Проверка: каждый коэффициент должен быть рациональным числом
        if not all(isinstance(coef, Rational) for coef in coefficients):
            raise ValueError("All coefficients must be Rational numbers")

        self.coefficients = coefficients

    # Строковое представление многочлена
    def __str__(self):
        pass

    # Метод для упрощения объекта
    def simplify(self):
        pass
