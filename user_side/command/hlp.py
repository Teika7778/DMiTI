"""
Принимает 1 или 0 аргументов, в случае если принимает 0 аргументов, то выводит справку о программе в целом
если принимает 1 аргумент, то это должно быть название модуля, и нужно вывести reference этого модуля или команды
"""

from user_side.command.generic import AbstractCommand


class HLP(AbstractCommand):
    def execute(self, args, window):
        pass

    def reference(self) -> str:
        pass
