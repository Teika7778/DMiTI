from data_types import *
from core import generic_module as gm
from core.MUL_ZZ_Z import MUL_ZZ_Z
import copy

class DIV_QQ_Q(gm.AbstractModule):
    def execute(self, args):
        
        self.mull_zz_z = MUL_ZZ_Z()

        if not len(args) == 2: #проверка на получение двух аргументов
            raise ValueError("Improper arguments: function takes only 2 args")
        
        rational1 = copy.deepcopy(args[0])
        rational2 = copy.deepcopy(args[1])

        if not (isinstance(rational1, Rational) and isinstance(rational2, Rational)):  # проверка типов получаемых аргументов
            raise ValueError("Invalid data type: must be Rational")
        
        denominator1 = Integer(Natural(rational1.denominator.numbers), is_positive = True) # из натурального знамянателя первого числа делаем положительное целое число чтобы воспользоваться модулем умножения целых чисел
        denominator2 = Integer(Natural(rational2.denominator.numbers), is_positive = True) # из натурального знамянателя второго числа делаем положительное целое число чтобы воспользоваться модулем умножения целых чисел

        numerator = self.mull_zz_z.execute([rational1.numerator, denominator2]) # перемножаем числитель первого числа и знамянатель второго
        denominator = self.mull_zz_z.execute([denominator1, rational2.numerator]) # перемножаем числитель второго числа и знамянатель первого
        if ((numerator[0].is_positive is True and denominator[0].is_positive is True) or (numerator[0].is_positive is False and denominator[0].is_positive is False)): # проверяем знак итогового дробного числа
            resSign = True # переменная для знака итогового дробного числа
        else:
            resSign = False 
        resNumerator = Integer(Natural(numerator[0].natural.numbers), resSign) # сохраняем результат числителя в виде целого числа с учетом знака
        resDenominator = Natural(denominator[0].natural.numbers) # сохраняем результат знамянателя

        return [Rational(resNumerator, resDenominator)]

    def reference(self) -> str:
        return ("Division of fractions [RATIONAL. RATIONAL -> RATIONAL]\n"
                "Arguments:\n"
                "\t1: Rational - divisible\n"
                "\t2: Rational - divider\n"
                "Returns:\n"
                "\t1: Rational - product of division\n"
                "Author: Timofey Komarenko\n")
