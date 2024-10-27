from core import generic_module as gm
from data_types import *
import copy

class Module(gm.AbstractModule):
    def execute(self, args):
        if len(args) != 2:
            raise ValueError()
        if not (isinstance(args[0], Natural) and isinstance(args[1], Natural)):
            raise ValueError()
        if args[0].numbers[0] > args[1].numbers[0]:
            return [copy.deepcopy(args[0])]
        else:
            return [copy.deepcopy(args[1])]

    def reference(self) -> str:
        pass
