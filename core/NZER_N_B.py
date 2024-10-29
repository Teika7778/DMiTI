from core import generic_module as gm
from data_types import *

class NZER_N_B(gm.AbstractModule):
    def execute(self, args):
        if len(args) != 1:  # проверка на количество аргументов
            raise ValueError("Необходим один массив.")
        if not (isinstance(args[0], Natural)):  # проверка на тип данных
            raise ValueError()
        if (len(args[0].numbers)==1) and (args[0].numbers == [0]): # если одна цифра и она равна 0
            return False
        return True

    def reference(self) -> str:
        pass