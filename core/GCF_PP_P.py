from core import generic_module as gm
from data_types import *
from core.MOD_PP_P import MOD_PP_P
from core.RED_Q_Q import RED_Q_Q
import copy


class GCF_PP_P(gm.AbstractModule):
    def __init__(self):
        self.mod_pp_p = MOD_PP_P()
        self.red = RED_Q_Q()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes 2 arg")
        if not (isinstance(args[0], Polynomial) and isinstance(args[1], Polynomial)):
            raise ValueError("Invalid data type:  must be polynomial")
        arg0_copy = copy.deepcopy(args[0])  # Копии многочленов
        arg1_copy = copy.deepcopy(args[1])
        # Алгоритм Евклида делением
        # Пока степени обоих не равны нулю
        c= 0
        while len(arg0_copy.coefficients) > 1 and len(arg1_copy.coefficients) > 1:
            c +=1
            print(c)
            # если степень первого больше
            if len(arg0_copy.coefficients) > len(arg1_copy.coefficients):
                # делим на второй
                arg0_copy = self.mod_pp_p.execute([arg0_copy, arg1_copy])[0]
                for degree_counter in range(len(arg0_copy.coefficients)):
                    arg0_copy.coefficients[degree_counter] = self.red.execute([arg0_copy.coefficients[degree_counter]])[0]
            else:  # иначе
                arg1_copy = self.mod_pp_p.execute([arg1_copy, arg0_copy])[0]  # делим на первый
                for degree_counter in range(len(arg1_copy.coefficients)):
                    arg1_copy.coefficients[degree_counter] = self.red.execute([arg1_copy.coefficients[degree_counter]])[0]

        if len(arg0_copy.coefficients) == 1:  # проверяем, какой не равен нулю
            return [arg1_copy]
        else:
            return [arg0_copy]

    def reference(self) -> str:
        return ("Greatest common divisor of polynomials [POLYNOMIAL. POLYNOMIAL -> POLYNOMIAL]\n"
                "Arguments:\n"
                "\t1: Polynomial - first\n"
                "\t2: Polynomial - second\n"
                "Returns:\n"
                "\t1: Polynomial - greatest common divisor\n"
                "Author: Gleb Khorchev\n")

