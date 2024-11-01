from core import generic_module as gm
from core.ADD_NN_N import ADD_NN_N
from core.SUB_NN_N import SUB_NN_N
from core.POZ_Z_D import POZ_Z_D
from core.COM_NN_D import COM_NN_D
from data_types import *


class ADD_ZZ_Z(gm.AbstractModule):
    def __init__(self):
        self.com_nn_d = COM_NN_D()
        self.add_nn_n = ADD_NN_N()
        self.poz = POZ_Z_D()
        self.sub_nn_n = SUB_NN_N()

    def execute(self, args):
        if not len(args) == 2:
            raise ValueError("Improper arguments: function takes 2 arg")

        if not (isinstance(args[0], Integer) and isinstance(args[1], Integer)):
            raise ValueError("Invalid data type: must be integer")

        addent_1, addent_2 = (args[1], args[0]) if self.com_nn_d.execute([args[0].natural, args[1].natural])[0].numbers == [1] else (args[0], args[1])  # Большее по МОДУЛЮ число берём в первый аргумент

        if self.poz.execute([addent_1])[0].numbers == [1] and self.poz.execute([addent_2])[0].numbers != [1]:
            return [Integer(Natural(self.sub_nn_n.execute([addent_1.natural, addent_2.natural])[0].numbers), is_positive=False)]

        if self.poz.execute([addent_2])[0].numbers == [1] and self.poz.execute([addent_1])[0].numbers != [1]:
            return [Integer(Natural(self.sub_nn_n.execute([addent_1.natural, addent_2.natural])[0].numbers), is_positive=True)]

        return [Integer(Natural(self.add_nn_n.execute([addent_1.natural, addent_2.natural])[0].numbers), is_positive=False if self.poz.execute([addent_1])[0].numbers == [1] else True)]

    def reference(self) -> str:
        pass
