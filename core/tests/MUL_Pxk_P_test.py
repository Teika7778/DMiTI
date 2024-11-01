import unittest
from data_types import *
from core.MUL_Pxk_P import MUL_Pxk_P

class MUL_Pxk_P_test(unittest.TestCase):
    def setUp(self):
        self.mul_module = MUL_Pxk_P()
    
    def test_multiplication(self):
        # Умножение ( 1/3 + 10x + 3/9x^2 + 65/7x^3) * x^3 = 1/3x^3 + 10x^4 + 3/9x^5 + 65/7x^6
        zero_coef = Rational(Integer(Natural([1])), Natural([3])) # 1/3
        first_coef = Rational(Integer(Natural([0, 1])), Natural([1])) # 10
        second_coef = Rational(Integer(Natural([3])), Natural([9])) # 3/9
        third_coef = Rational(Integer(Natural([5, 6])), Natural([7])) #65/7
        multiplier = Polynomial([zero_coef, first_coef, second_coef, third_coef])
        multiplicand = Natural([3]) # 3
        result = self.mul_module.execute([multiplier, multiplicand]) # Умножение ( 1/3 + 10x + 3/9x^2 + 65/7x^3) * x^3
        for result_elem, source_elem in zip(result[0].coefficients[3::], multiplier.coefficients): #сдвиг на 3 степени
            self.assertEqual(str(result_elem), str(source_elem))

    def test_zero_multiplication(self):
        # Умножение ( 2/5 + x ) * x^0 = 2/5 + x
        zero_coef = Rational(Integer(Natural([2])), Natural([5])) # 2/5
        first_coef = Rational(Integer(Natural([1])), Natural([1])) # 1
        multiplier = Polynomial([zero_coef, first_coef])
        multiplicand = Natural([0]) # 1
        result = self.mul_module.execute([multiplier, multiplicand]) # Умножение (2/5 + x) * x^0
        for result_elem, source_elem in zip(result[0].coefficients, multiplier.coefficients): # Cдвига нет
            self.assertEqual(str(result_elem), str(source_elem))

    def test_million_multiplication(self):
        # Умножение ( 15x - 3x^2 + 15/2x^3 ) * x^1000000 = 15x^1000001 - 3x^1000002 + 15x^1000003
        zero_coef = Rational(Integer(Natural([0])), Natural([1])) # 0
        first_coef = Rational(Integer(Natural([3]), False), Natural([2])) # 3/2
        third_coef = Rational(Integer(Natural([5,1])), Natural([2])) #15/2
        multiplier = Polynomial([zero_coef, first_coef, third_coef])
        multiplicand = Natural([0, 0, 0, 0, 0, 0, 1]) #1000000
        result = self.mul_module.execute([multiplier, multiplicand]) #Умножение ( 15x - 3x^2 + 15/2x^3 ) * x^1000000 = 15x^1000001 - 3x^1000002 + 15x^1000003
        for result_elem, source_elem in zip(result[0].coefficients[1000000::], multiplier.coefficients): # Cдвига на миллион
            self.assertEqual(str(result_elem), str(source_elem))

    def test_invalid_argument_count(self):
        # Проверка на неправильное число аргументов
        zero_coef = Rational(Integer(Natural([2])), Natural([5])) # 2/5
        first_coef = Rational(Integer(Natural([0])), Natural([1])) # 0
        third_coef = Rational(Integer(Natural([1])), Natural([2])) #1/2
        multiplier = Polynomial([zero_coef, first_coef, third_coef])
        with self.assertRaises(ValueError):
            self.mul_module.execute([multiplier]) # Передаем только один аргумент
        
    def test_invalid_argument_type(self):
        # Проверка на неправильный тип аргументов
        zero_coef = Rational(Integer(Natural([7, 1])), Natural([0, 1])) # 17/10
        first_coef = Rational(Integer(Natural([0])), Natural([1])) # 0
        third_coef = Rational(Integer(Natural([3])), Natural([1])) #3
        multiplier = Polynomial([zero_coef, first_coef, third_coef])
        invalid_argument = "Hellow Sergey Pozdkov"
        with self.assertRaises(ValueError):
            self.mul_module.execute([multiplier, invalid_argument]) # Передаем незпрааильынй аргумент

if __name__ == "__main__":
    unittest.main()

    