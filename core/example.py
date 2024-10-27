from core import generic_module as gm
from data_types import *


class Module(gm.AbstractModule):
    def execute(self, args):
        if len(args) != 2:
            raise ValueError()
        if not (isinstance(args[0], Natural) and isinstance(args[1], Natural)):
            raise ValueError()

        if args[0].numbers[0] > args[1].numbers[0]:
            return [Natural(args[0].numbers)]
        else:
            return [Natural(args[1].numbers)]

    def reference(self) -> str:
        pass
