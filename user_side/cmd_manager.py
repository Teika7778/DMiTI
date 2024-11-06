from command.cmd import CMD
from command.hlp import HLP
from command.put import PUT


class CmdManager:
    def __init__(self):
        self.commands_dict = {
            "CMD": CMD(),
            "PUT": PUT(),
            "HLP": HLP()
        }

    def process_cmd(self, cmd_string: str, window):
        while "  " in cmd_string or " |" in cmd_string or "| " in cmd_string:
            cmd_string = cmd_string.replace("  ", " ")
            cmd_string = cmd_string.replace(" |", "|")
            cmd_string = cmd_string.replace("| ", "|")
        if '|' in cmd_string:
            args = cmd_string.split('|')
            for i in range(len(args)):
                args[i] = args[i].split(' ')
            if len(args) == 0:
                raise ValueError()
            command_tag = args[0][0]
            args = args[0][1:]
        else:
            args = cmd_string.split(' ')
            if len(args) == 0:
                raise ValueError()
            command_tag = args[0]
            args = args[1:]

        if command_tag not in self.commands_dict:
            raise ValueError()
        self.commands_dict[command_tag].execute(args, window)




m = CmdManager()
m.process_cmd("CMD AAA A A  A AA A  F | FF fF          D               | F", 0)

