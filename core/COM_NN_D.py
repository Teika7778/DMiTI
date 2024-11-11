from core import generic_module as gm
from data_types import *

class COM_NN_D(gm.AbstractModule):  #сравнение натуральных чисел
    def execute(self, args):  
        if len(args) != 2:  #проверка на количество аргументов
            raise ValueError("Two natural numbers are needed for comparison.")
        if not (isinstance(args[0], Natural) and isinstance(args[1], Natural)):#проверка на тип данных
            raise ValueError("Two natural numbers are needed for comparison.")
        
        if len(args[0].numbers) > len(args[1].numbers):
            return [Natural([2])]  # Первое число больше
        elif len(args[0].numbers) < len(args[1].numbers):  
            return [Natural([1])]  # Первое число меньше

        # Если длины одинаковы, сравниваем элементы по индексам  
        for i in range(len(args[0].numbers)-1,-1,-1):  
            if args[0].numbers[i] > args[1].numbers[i]:  
                return [Natural([2])]  # Первое число больше
            elif args[0].numbers[i] < args[1].numbers[i]:
                return [Natural([1])]  # Первое число меньше
        
        return [Natural([0])]  # Числа равны
    
    def reference(self) -> str:
        return ("Comparison of natural numbers [NATURAL, NATURAL -> DIGIT]\n"
                "Arguments:\n"
                "\t1: Natural - first term\n"
                "\t2: Natural - second term\n"
                "Returns:\n"
                "\t1: Digit - 0 if terms are equal, 1 if second term is greater, 2 otherwise\n"
                "Author: Artem Grebenshikov\n")