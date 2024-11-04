from core import generic_module as gm
from data_types import *
from core.MUL_ZZ_Z import MUL_ZZ_Z
from core.MUL_NN_N import MUL_NN_N

class MUL_QQ_Q(gm.AbstractModule):
    def __init__(self):
        self.mul_zz_z = MUL_ZZ_Z()
        self.mul_nn_n = MUL_NN_N()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes 2 arg")
        if not (isinstance(args[0], Rational) and isinstance(args[1], Rational)):
            raise ValueError("Invalid data type:  must be rational")
        result = Rational(self.mul_zz_z.execute([args[0].numerator, args[1].numerator])[0], self.mul_nn_n.execute([args[0].denominator, args[1].denominator])[0])
        return [result]

    def reference(self) -> str:
        pass