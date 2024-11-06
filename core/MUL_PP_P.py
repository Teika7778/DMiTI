from core import generic_module as gm
from data_types import *
from core.MUL_PQ_P import MUL_PQ_P
from core.MUL_Pxk_P import MUL_Pxk_P
from core.ADD_PP_P import ADD_PP_P
import copy

class MUL_PP_P(gm.AbstractModule):
    def __init__(self):
        self.mul_pq_p = MUL_PQ_P()
        self.mul_pxk_p = MUL_Pxk_P()
        self.add_pp_p = ADD_PP_P()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes 2 arg")
        if not (isinstance(args[0], Polynomial) and isinstance(args[1], Polynomial)):
            raise ValueError("Invalid data type:  must be polynomial")
        result = Polynomial([Rational(Integer(Natural([0])), Natural([1]))]) # Нулевой многочлен
        for degree in range(len(args[1].coefficients)): # Цикл по элементам второго многочлен
            temp_result = self.mul_pq_p.execute([args[0], args[1].coefficients[degree]])[0]  # промежуточный результат - результат умножения
            degree_num = list(map(int, list(str(degree))[::-1]))
            temp_result = self.mul_pxk_p.execute([temp_result, Natural(degree_num)])[0] # всего P(x) на i-ый коэф Q(x) и умноженный на x^i
            result = self.add_pp_p.execute([result, temp_result])[0] # Ответ - сумма таких промежуточных результатов
        return [result]

    def reference(self) -> str:
        pass

