from core import generic_module as gm
from core.ABS_Z_N import ABS_Z_N  # Абсолютная величина числа, результат - натуральное.
from core.GCF_NN_N import GCF_NN_N  # НОД натуральных чисел
from core.DIV_ZZ_Z import DIV_ZZ_Z # Частное от деления целого на целое (делитель отличен от нуля)
from data_types import *
import copy


class RED_Q_Q(gm.AbstractModule):
    def __init__(self):
        self.abs_z_n = ABS_Z_N()
        self.gcf_nn_n = GCF_NN_N()
        self.div_zz_z = DIV_ZZ_Z()
        

    def execute(self, args):

        if not len(args) == 1: #проверка на получение одного аргумента
            raise ValueError("Improper arguments: function takes only 1 args")
        
        rational = copy.deepcopy(args[0])

        if not (isinstance(rational, Rational)):  # проверка типов получаемых аргументов
            raise ValueError("Invalid data type: must be Rational")

        gcf = self.gcf_nn_n.execute([rational.numerator.natural, rational.denominator])[0] # получаем НОД числителя и знамянателя


        numerator = self.div_zz_z.execute([rational.numerator, Integer(gcf, is_positive=True)])[0] # делим числитель на НОД
        denomirator = self.div_zz_z.execute([Integer(rational.denominator, is_positive = True), Integer(gcf, is_positive=True)])[0]# делим знамянатель на НОД

        resDenominator = Natural(denomirator.natural.numbers) # делаем из знамянателя натуральное число
        
        result = Rational(numerator, resDenominator)

        return [result]
                
        
    def reference(self) -> str:
        return ("Reduction of fractional number [RATIONAL -> RATIONAL]\n"
                "Arguments:\n"
                "\t1: Rational - number to reduce\n"
                "Returns:\n"
                "\t1: Rational - reduced number\n"
                "Author: Timofey Komarenko\n")