from core import generic_module as gm
from data_types import Natural

class COM_NN_D(gm.AbstractModule):  #сравнение натуральных чисел
    def execute(self, args):  
        if len(args) != 2:  #проверка на количество аргументов
            raise ValueError("Необходимы два массива для сравнения.")  
        if not (isinstance(args[0], Natural) and isinstance(args[1], Natural)):#проверка на тип данных
            raise ValueError()
        
        if len(args[0].numbers) > len(args[1].numbers):
            return [2]  # Первое число больше 
        elif len(args[0].numbers) < len(args[1].numbers):  
            return [1]  # Первое число меньше  

        # Если длины одинаковы, сравниваем элементы по индексам  
        for i in range(len(args[0].numbers)-1,-1,-1):
            if args[0].numbers[i] > args[1].numbers[i]:  
                return [2]  # Первое число больше  
            elif args[0].numbers[i] < args[1].numbers[i]:
                return [1]  # Первое число меньше  
        
        return [0]  # Числа равны  
    
    def reference(self) -> str:
        pass