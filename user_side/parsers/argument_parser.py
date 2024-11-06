"""
на вход получает строку в которой либо содержится число либо название переменной, которая хранится в var_stack
вернуть тип данных, либо полученный из парсинга строки, либо извлечением из стэка переменных
"""
# для получения значения, то перед ней нужно поставить *
from data_types_parser import DataTypeParser


class ArgumentParser:
    def parse(self, string, var_stack):
        if len(string) == 0:
            raise ValueError()
        if string[0] == '*':
            string = string[1:]
            if string in var_stack:
                return var_stack[string]
            else:
                raise ValueError()
        else:
            pars = DataTypeParser()
            return pars.str_to_datatype(string)
