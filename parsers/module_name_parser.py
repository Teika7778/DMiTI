"""
Данный класс должен сопоставлять строке, содержащей название модуля объект класса этого модуля
Пример: "ADD_ZZ_Z" -> объект класса ADD_Z_Z
Таким образом каждой строке с названием модуля должен быть сопоставлен объект класса
"""
from core.ABS_Z_N import ABS_Z_N
from core.ADD_1N_N import ADD_1N_N
from core.ADD_NN_N import ADD_NN_N
from core.ADD_PP_P import ADD_PP_P
from core.ADD_QQ_Q import ADD_QQ_Q


class ModuleNameParser:
    def __init__(self):
        self.names = dict()
        self.names["ABS_Z_N"] = ABS_Z_N()
        self.names["ADD_NN_N"] = ADD_NN_N()
        self.names["ADD_1N_N"] = ADD_1N_N()
        self.names["ADD_PP_P"] = ADD_PP_P()
        self.names["ADD_QQ_Q"] = ADD_QQ_Q()

    def parse(self, string):
        print(string)
        if string not in self.names:
            raise ValueError()
        return self.names[string]
