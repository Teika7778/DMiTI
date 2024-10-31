from core.COM_NN_D import COM_NN_D
from core.MUL_Nk_N import MUL_Nk_N
from core.ADD_NN_N import ADD_NN_N
from core import generic_module as gm
from data_types import *
import copy

class DIV_NN_Dk(gm.AbstractModule):
    def execute(self, args):
        # выброс исключения, если:
        if not isinstance(args, list):  # args не list
            raise ValueError("Invalid args type: args must be a list")

        if not len(args) == 2:  # в списке аргументов не 2 аргумента
            raise ValueError("Improper arguments: function takes only 2 args")

        if not isinstance(args[0], Natural):  # первый аргумент не Natural
            raise ValueError("Invalid data type: first arg must be natural")

        if not isinstance(args[1], Natural):  # второй аргумент не Natural
            raise ValueError("Invalid data type: second arg must be natural")

        divider = args[1]  # делитель
        if divider.numbers[-1] == 0:  # деление на 0
            raise ValueError("Invalid division: division by zero")

        divisible = args[0]  # делимое
        compare = COM_NN_D().execute([divisible, divider])[0] # результат сравнения
        if compare.numbers[0] == 1: # если второе строго больше первого
            raise ValueError("Invalid division: divider must be less than divisible")

        # Что вообще тут происходит? По сути нас просят реализовать шаг алгоритма деления в столбик
        # Сразу пример: 2233 надо поделить на 37. Как бы мы это делали в рил лайф?
        # Смотрим на делимое 2 - слишком мало, 22 - все еще мало, 223 - уже нормально
        # Осталось только подобрать цифру - по сколько надо взять делитель, чтобы при вычитании из делимого
        # получился остаток меньше делителя. В данном случае 223 - 6 * 37 = 1, т.е. берем по 6
        # Дальше надо вычислить k - по сути сколько еще раз надо будет выполнить шаг деления в столбик до полного деления
        # Это ровно количество оставшихся разрядов. Брали 223, значит осталось только 3 - один разряд => k = 1
        # Ответ: 6 * 10^1 = 60
        # Вот еще пример, но уже без пояснений: (666, 10) -> 60
        # Что будет происходить в алгоритме:
        # 1) вместо первого перебора можно сразу взять k старших разрядов делимого(k - длина делителя) - если их мало,
        # то брем еще один разряд - этого точно хватит, потому что теперь этих разрядов больше, чем разрядов делителя =>
        # они точно больше. Эти разряды обозначаются за nepon
        # 2) подбор цифры: заводим счетчик, который равен {текущая цифра} * делитель. Если счетчик стал больше nepon, то
        # значит, что текущая цифра не подходит, поэтому берем предыдущую

        k = len(divider.numbers)  # длина делителя
        m = len(divisible.numbers)  # длина делимого
        nepon = Natural(divisible.numbers[m-k:]) # k старших разрядов делимого
        if COM_NN_D().execute([nepon, divider])[0].numbers[0] == 1:  # если nepon меньше, чем делитель
            nepon.numbers.insert(0, divisible.numbers[m - k - 1])  # добавляем еще 1 разряд

        accum = divider  # счетчик
        for i in range(2, 11):  # пробегаем все цифры, но т.к. будет отслеживаться переполнение, то берем на 1 больше
            accum = ADD_NN_N().execute([accum, divider])[0] # на каждой итерации прибавляем к счетчику делитель
            if COM_NN_D().execute([nepon, accum])[0].numbers[0] == 1: # если переполнение
                return MUL_Nk_N().execute([Natural([i - 1]), Natural([m - len(nepon.numbers)])])   # пред. цифра
                # не забываем домножить на 10^{сдвиг между nepon и делимым}

    def reference(self) -> str:
        pass


