from core import generic_module as gm
from core.COM_NN_D import COM_NN_D
from data_types import *


class ADD_NN_N(gm.AbstractModule):
    def __init__(self):
        self.module = COM_NN_D()
    def execute(self, args):  
        # args должны быть списками, содержащими цифры, записанные в обратном порядке
        # проверка данных не проводится, так как будет вызываться метод сравнения чисел, который включает проверку
        carry = 0  #перенос
        result = []
        if self.module.execute(args)[0].numbers == [2]: #первое больше второго
            max_length = len(args[0].numbers)
        else:
            max_length = len(args[1].numbers)
        for i in range(max_length):
            digit1 = args[0].numbers[i] if i < len(args[0].numbers) else 0
            digit2 = args[1].numbers[i] if i < len(args[1].numbers) else 0
            
            total = digit1 + digit2 + carry  
            result.append(total % 10)  # добавляем последнюю цифру к результату  
            carry = total // 10  # вычисляем переноса  

        if carry:
            result.append(carry)  # добавляем переноса, если есть  

        return [Natural(result)]
    def reference(self) -> str:
        return ("Addition of natural numbers [NATURAL, NATURAL -> NATURAL]\n"
                "Arguments:\n"
                "\t1: Natural - first term\n"
                "\t2: Natural - second term\n"
                "Returns:\n"
                "\t1: Natural - their sum\n"
                "Author: Artem Grebenshikov\n")