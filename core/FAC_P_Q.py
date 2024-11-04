from core import generic_module as gm
from data_types import *
from core.ABS_Z_N import ABS_Z_N
from core.TRANS_Z_N import TRANS_Z_N
from core.LCM_NN_N import LCM_NN_N
from core.GCF_NN_N import GCF_NN_N
from core.TRANS_N_Z import TRANS_N_Z
import copy

class FAC_P_Q(gm.AbstractModule):
    def __init__(self):
        self.abs_z_n = ABS_Z_N()  
        self.trans_z_n = TRANS_Z_N()
        self.lcm_nn_n = LCM_NN_N() 
        self.gcf_nn_n = GCF_NN_N() 
        self.trans_n_z = TRANS_N_Z()
    
    def execute(self, args):
        # Проверка на наличие двух аргументов
        if len(args) != 1:
            raise ValueError("Improper arguments: function takes 1 arg")
        # Проверка типа данных
        if not (isinstance(args[0], Polynomial)):
            raise ValueError("Invalid data types: expected Polynomial")
        result = Rational(Integer(Natural([1])), Natural([1])) # 1/1
        for coef in args[0].coefficients:
            result_numerator_copy = self.trans_z_n.execute([result.numerator])[0]
            coef_numerator_copy =  self.abs_z_n.execute([coef.numerator])[0]
            result.numerator = self.lcm_nn_n.execute([result_numerator_copy, coef_numerator_copy])[0]
            result.numerator = self.trans_n_z.execute([result.numerator])[0]
            result.denominator = self.lcm_nn_n.execute([result.denominator, coef.denominator])[0]
        return [result]
    
    def reference(self) -> str:
        pass