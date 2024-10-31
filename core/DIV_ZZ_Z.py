from core import generic_module as gm
from data_types import *
import copy
from core.ABS_Z_N import ABS_Z_N  # Абсолютная величина числа, результат - натуральное
from core.POZ_Z_D import POZ_Z_D  # Определение положительности числа
### раскоменьтить from core.DIV_NN_N import DIV_NN_N #  Неполное частное от деления первого натурального числа на второе с остатком
from core.ADD_1N_N import ADD_1N_N  # Добавление 1 к натуральному числу
### from core.MOD_NN_N import MOD_NN_N


#  Частное от деления целого на целое (делитель отличен от нуля)
class DIV_ZZ_Z(gm.AbstractModule):

    def __init__(self):
        self.abs_z_n = ABS_Z_N()
        self.poz_z_d = POZ_Z_D()
### раскоменьтить       self.div_nn_n = DIV_NN_N()
        self.add_1n_n = ADD_1N_N()
###     self.mod_nn_n = MOD_NN_N()

    def execute(self, args):
        if len(args) != 2:  # проверка на количество аргументов
            raise ValueError("Invalid number of arguments")
        if not (isinstance(args[0], Integer) and isinstance(args[1], Integer)):  # проверка на тип данных
            raise ValueError("The number isn`t integer")
        if len(args[1].natural.numbers) == 1 and args[1].natural.numbers[-1] == 0:  # проверка делителя на ноль
            raise ValueError("The divisor cannot be zero")

        num1 = self.abs_z_n.execute([args[0]])  # получаем абсолютную величину делимого
        num2 = self.abs_z_n.execute([args[1]])  # получаем абсолютную величину делителя
### раскоменьтить       num3 = self.div_nn_n.execute([num1[0], num2[0]])  # получаем неполное частное от деления двух натуральных чисел

#/// удалить, когда будет DIV_NN_N
        test1 = ''
        test2 = ''
        remainder = False
        for item in num1[0].numbers:
            test1 += str(item)
        for item in num2[0].numbers:
            test2 += str(item)
        if int(test1[::-1]) % int(test2[::-1]) != 0:
            remainder = True
        num3 = int(test1[::-1]) // int(test2[::-1])
        num3 = [int(x) for x in str(num3)]
        num3 = Natural(num3[::-1])
        result = copy.deepcopy(Integer(num3))

#/// удалить, когда будет DIV_NN_N


### раскоменьтить       result = copy.deepcopy(Integer(num3[0]))  # Создаем число типа Integer, равное частному
        # если делимое отрицательное, а делитель положительный -> остаток отрицательный
        # если делимое и делитель отрицательные -> остаток отрицательный
        # => если делимое отрицательное, то остаток отрицательный, нужно прибавить 1
        # частному, чтобы избежать отрицательного остатка
###        if not (len(self.mod_nn_n([num1, num2])[0].numbers) == 0 and self.mod_nn_n([num1, num2])[0].numbers[-1] == 0):
###            if not args[0].is_positive:
###                result.natural = self.add_1n_n.execute([result.natural])[0]

        if remainder:
            if not args[0].is_positive:
                result.natural = self.add_1n_n.execute([result.natural])[0]


        if not (len(result.natural.numbers) == 1 and result.natural.numbers[-1] == 0):  # если частное не равно нулю
            # если делимое положительное, а делитель отрицательный
            if self.poz_z_d.execute([args[0]])[0].numbers == Natural([2]).numbers and\
                    self.poz_z_d.execute([args[1]])[0].numbers == Natural([1]).numbers:
                result.is_positive = not result.is_positive  # меняем знак на противоположный
            # если делимое отрицательное, а делитель положительный
            if self.poz_z_d.execute([args[0]])[0].numbers == Natural([1]).numbers and\
                    self.poz_z_d.execute([args[1]])[0].numbers == Natural([2]).numbers:
                result.is_positive = not result.is_positive  # меняем знак на противоположный
        # Случаи, когда делимое и делитель имеют один знак, можно не рассматривать, тк смены знака не произойдет
        return [result]

    def reference(self) -> str:
        pass
