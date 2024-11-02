from core import generic_module as gm
from data_types import *
from core.DEG_P_N import DEG_P_N
from core.MOD_PP_P import MOD_PP_P
import copy

class GCF_PP_P(gm.AbstractModule):
    def __init__(self):
        self.deg_p_n = DEG_P_N()
        self.mod_pp_p = MOD_PP_P()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes 2 arg")
        if not (isinstance(args[0], Polynomial) and isinstance(args[1], Polynomial)):
            raise ValueError("Invalid data type:  must be polynomial")
        arg0_copy = copy.deepcopy(args[0]) # Копии многочленов
        arg1_copy = copy.deepcopy(args[1])
        #Алгоритм Евклида делением
        while( (self.deg_p_n(arg0_copy)[0] != 0) and (self.deg_p_n(arg1_copy)[0] != 0) ): # Пока степени обоих не равны нулю
            if ( (self.deg_p_n(arg0_copy)[0] > self.deg_p_n(arg1_copy)[0])): # если степень первого больше
                arg0_copy = self.mod_pp_p([arg0_copy, arg1_copy])[0] # делим на второй
            else: #иначе
                arg1_copy = self.mod_pp_p([arg1_copy, arg0_copy])[0] # делим на первый
        if (self.deg_p_n(arg0_copy)[0] == 0):  # проверяем, какой не равен нулю
            return [arg1_copy]
        else:
            return [arg0_copy]

    def reference(self) -> str:
        pass