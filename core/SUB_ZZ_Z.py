from core import generic_module as gm
from core.COM_NN_D import COM_NN_D #Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе.
from core.POZ_Z_D import POZ_Z_D # Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)
from core.ABS_Z_N import ABS_Z_N # Абсолютная величина числа, результат - натуральное
from core.ADD_NN_N import ADD_NN_N # Сложение натуральных чисел
from core.SUB_NN_N import SUB_NN_N # Вычитание из первого большего натурального числа второго меньшего или равного
from core.MUL_ZM_Z import MUL_ZM_Z # Умножение целого на (-1)
from data_types import *
import copy


class SUB_ZZ_Z(gm.AbstractModule):
    def __init__(self):
        self.com_nn_d = COM_NN_D()
        self.poz = POZ_Z_D()
        self.abs_z_n = ABS_Z_N()
        self.add_nn_n = ADD_NN_N()
        self.sub_nn_n = SUB_NN_N()
        self.mul_zm_z = MUL_ZM_Z()

    def execute(self, args):

        if not len(args) == 2: #проверка на получение двух аргументов
            raise ValueError("Improper arguments: function takes only 2 args")
        
        integer1 = copy.deepcopy(args[0])
        integer2 = copy.deepcopy(args[1])

        if not (isinstance(integer1, Integer) and isinstance(integer2, Integer)):  # проверка типов получаемых аргументов
            raise ValueError("Invalid data type: must be Ineger")
        
        natural1 = self.abs_z_n.execute([integer1])[0] # получаем абсолютное значение
        natural2 = self.abs_z_n.execute([integer2])[0] # получаем абсолютное значение

        sign1 = self.poz.execute([integer1])[0].numbers[0] # получаем знак 
        sign2 = self.poz.execute([integer2])[0].numbers[0] # получаем зак

        if(sign1 != 1 and sign2 != 1): # если оба числа не отрицательные
            if(self.com_nn_d.execute([natural1,natural2])[0].numbers[0] != 1): #  если первое больше или равно второму
                result = Integer(self.sub_nn_n.execute([natural1, natural2])[0], is_positive = True)
            else:
                result = Integer(self.sub_nn_n.execute([natural2, natural1])[0], is_positive = False)
        elif(sign1 != 2 and sign2 != 1):  # -(x+y)
            
            result = Integer(self.add_nn_n.execute([natural1, natural2])[0], is_positive = False)
        elif(sign1 != 1 and sign2 != 2): # (x+y)
            result = Integer(self.add_nn_n.execute([natural1, natural2])[0], is_positive = True)
        elif(sign1 != 2 and sign2 != 2): # если оба числа не положительные
            if(self.com_nn_d.execute([natural1,natural2])[0].numbers[0] != 1): #  если первое больше или равно второму
                result = Integer(self.sub_nn_n.execute([natural1,natural2])[0], is_positive = False)
            else:
                result = Integer(self.sub_nn_n.execute([natural2,natural1])[0], is_positive = True) 
        
        return [result]
                
        
    def reference(self) -> str:
        return ("Subtracting an integer from an integer [INTEGER, INTEGER -> INTEGER]\n"
                "Arguments:\n"
                "\t1: Integer - minuend number\n"
                "\t2: Integer - subtrahend number\n"
                "Returns:\n"
                "\t1: Integer - difference\n"
                "Author: Timofey Komarenko\n")