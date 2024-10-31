from core import generic_module as gm
from data_types import *
import copy

class MUL_Pxk_P(gm.AbstractModule):
    def execute(self, args):
        if len(args) != 2: #Проверка на неверное число аргументов
            raise ValueError("Improper arguments: function takes only 2 arg")
        if not (isinstance(args[0], Polynomial) and isinstance(args[1], Natural)):
            raise ValueError("Invalid data type: first argument must be polynomial and second must be natural")
        result = copy.deepcopy(args[0]) # Создаём глубокую копию
        counter = 0 # Счётчик, считает на сколько нужно увеличить степень многочлена
        for i in range(0, len(args[1].numbers)):
            counter += (10**i)*args[1].numbers[i] 
        result.coefficients = [Natural([0])]*counter + result.coefficients # Заполняем нулями для увеличения степени
        return [result]

    def reference(self) ->str:
        pass
