import tkinter as tk
from tkinter import ttk
from data_types import *
from command.generic import AbstractCommand
from parsers.argument_parser import ArgumentParser
from parsers.module_name_parser import ModuleNameParser


class ConsoleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CAS")

        # ТУТ ВСЯКОЕ ВСПОМОГАТЕЛЬНОЕ, несерьёзное
        self.var_stack = dict()
        self.available_types = ["INT", "NAT", "RAT", "POL"]
        self.type_codes = {Integer: "INT", Natural: "NAT", Rational: "RAT", Polynomial: "POL", bool: "BIN"}
        self.manager = CmdManager()
        self.loader = CMDLoader()

        # Цвета для светлой темы
        self.bg_color = "#e0f7fa"  # светлый фон
        self.text_color = "#004d40"  # темный текст
        self.font_size = ('Arial', 12)  # Шрифт для текста

        # Переменная для хранения последнего введенного значения
        self.last_input = ""

        # Настройка сетки для изменения размеров окна
        self.root.grid_columnconfigure(0, weight=3)  # Основное текстовое поле
        self.root.grid_columnconfigure(1, weight=0)  # Фиксированное правое поле
        self.root.grid_rowconfigure(0, weight=1)  # Текстовые области
        self.root.grid_rowconfigure(1, weight=0)  # Строка ввод

        # Создаем стиль для ползунков с помощью ttk
        style = ttk.Style()
        style.theme_use('clam')  # Устанавливаем тему
        style.configure("TScrollbar", background=self.bg_color, troughcolor=self.bg_color, arrowcolor=self.text_color,
                        bordercolor=self.bg_color)

        # Большое поле для вывода текста без переноса строк
        self.text_area = tk.Text(root, wrap=tk.NONE, width=60, height=20, state=tk.DISABLED, bg=self.bg_color,
                                 fg=self.text_color,
                                 insertbackground=self.text_color, font=self.font_size)
        self.text_area.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Создаем вертикальный ползунок для text_area
        text_scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.text_area.yview)
        self.text_area.config(yscrollcommand=text_scrollbar.set)
        text_scrollbar.grid(row=0, column=0, sticky="nse", padx=10)

        # Создаем горизонтальный ползунок для text_area
        text_h_scrollbar = ttk.Scrollbar(root, orient="horizontal", command=self.text_area.xview)
        self.text_area.config(xscrollcommand=text_h_scrollbar.set)
        text_h_scrollbar.grid(row=1, column=0, sticky="ew", padx=10)

        # Меньшее окно справа (без переноса строк) с увеличенной шириной
        self.right_area = tk.Text(root, wrap=tk.NONE, width=30, height=20, state=tk.DISABLED, bg=self.bg_color,
                                  fg=self.text_color,
                                  insertbackground=self.text_color, font=self.font_size)
        self.right_area.grid(row=0, column=1, sticky="nsew", padx=(0, 15),
                             pady=10)  # Уменьшен отступ слева и увеличен справа

        # Создаем вертикальный ползунок для right_area
        self.right_scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.right_area.yview)
        self.right_area.config(yscrollcommand=self.right_scrollbar.set)
        self.right_scrollbar.grid(row=0, column=1, sticky="nse", padx=(0, 15))  # Увеличен отступ справа

        # Создаем горизонтальный ползунок для right_area
        self.right_h_scrollbar = ttk.Scrollbar(root, orient="horizontal", command=self.right_area.xview)
        self.right_area.config(xscrollcommand=self.right_h_scrollbar.set)
        self.right_h_scrollbar.grid(row=1, column=1, sticky="ew", padx=(0, 15))  # Увеличен отступ справа

        # Поле для ввода текста пользователем
        self.input_field = tk.Entry(root, width=85, bg=self.bg_color, fg=self.text_color,
                                    insertbackground=self.text_color, font=self.font_size)
        self.input_field.grid(row=2, column=0, sticky="ew", padx=(10, 10), pady=(5, 2))

        # Кнопка для отправки текста
        self.send_button = tk.Button(root, text="Enter", command=self.send_input,
                                     bg=self.bg_color, fg=self.text_color, font=self.font_size)
        self.send_button.grid(row=2, column=1, sticky="e", padx=10, pady=(5, 2))

        # Привязка нажатия клавиши Enter к функции send_input
        self.input_field.bind("<Return>", self.send_input)

        self.print_help()

    def send_input(self, event=None):
        # Получаем текст от пользователя
        self.last_input = self.input_field.get()

        # Отображаем текст на текстовой области
        if self.last_input != '':
            self.display_text(f"Command executed: {self.last_input}")
            try:
                self.manager.process_cmd(self.last_input, self)
            except ValueError as e:
                self.display_text("Exception occurred:" + str(e.args[0]))

        self.update_right_area()
        # Очищаем поле ввода
        self.input_field.delete(0, tk.END)

    def display_text(self, text):
        # Добавляем текст в основную текстовую область
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, f"{text}\n")
        self.text_area.config(state=tk.DISABLED)

    def update_right_area(self):
        """Обновляет правую область информации новыми переменными."""
        self.right_area.config(state=tk.NORMAL)
        self.right_area.delete(1.0, tk.END)  # Очищаем содержимое
        for var_name, var_value in self.var_stack.items():
            var_type = self.type_codes[type(var_value)]
            self.right_area.insert(tk.END, f"{var_name}: [{var_type}] {var_value}\n")
        self.right_area.config(state=tk.DISABLED)

    def print_help(self):
        self.display_text("### Intro:\n"
                          "This program is a computer algebra system, its main feature is the ability to save values \n"
                          "into variables. The program supports 3 main commands: CMD, PUT, HLP. CMD allows you to \n"
                          "perform the specified algebraic transformation, their complete list can be obtained by \n"
                          "entering HLP LIST, and information about each individual command can be obtained by \n"
                          "entering HLP [MODULE_NAME]. The program converts strings entered by the user into various \n"
                          "data types automatically, without requiring explicit indication of the types. In this \n"
                          "regard, each data type has its own input rules.\n\n\n"
                          "### Data types:\n"
                          "1. Naturals: A sequence of digits, and only digits, that does not begin with zero, \n"
                          "unless it is exactly equal to zero. Example: 1000, 3000, 0.\n"
                          "2. Integers: + or - sign (required), followed by a valid natural number. Example: +1000, \n"
                          "-1000, +0\n"
                          "3. Rationals: The / sign separating the valid integer preceding it and the valid natural \n"
                          "number following it (not 0). Example: +100/10, -1/1, +21/1\n"
                          "4. Polynomials: A sequence of rational numbers (and here you can omit the / sign if the \n"
                          "division occurs by 1) separated by , (without spaces). The problem can be creating a \n"
                          "polynomial of degree 0; to do this, you need to put the letter P in front of the rational \n"
                          "number representing it.\n\n\n"
                          "### Commands:\n"
                          "The standard syntax for calling an algebraic module is CMD [Module name] [Variable being \n"
                          "written to or OUT keyword] | [A set of variables or explicitly specified values that \n"
                          "will be passed as arguments]\n"
                          "The easiest way to explain the program in detail is with the help of examples.\n\n\n"
                          "### Some basic examples:\n"
                          "PUT var1 50 - now the variable var1 contains the natural number 50.\n"
                          "PUT var2 +50 - now the variable var2 contains the integer 50. \n"
                          "PUT var3 +50/1 - now the variable var3 contains the rational number 50\n"
                          "PUT var4 P+50 - now the variable var4 contains the polynomial 50x^0\n"
                          "PUT varP +50,+20/3,-3 - now the variable varP contains the polynomial 50 + 20/3x - 3x^2\n"
                          "CMD ADD_NN_N varN | 50 30 - creates new variable varN (Natural number) equal to 50+30=80\n"
                          "CMD ADD_NN_N OUT | 50 30 - pints the result of the 50+30 operation to the console\n"
                          "CMD ADD_NN_N OUT | *varN *var1 - similarly, but the values will be taken from the\n"
                          "variables var1 and varN, you should pay attention to the * sign, it is required\n\n\n"
                          "### Loading scripts from file:\n"
                          "To load a sequence of commands from a file, you need to write SCR [file_name], it is also\n"
                          "possible to load commands under a condition, this condition is usually a Boolean variable.\n"
                          "In this case, the syntax is: SRF [file_name] *[variable]. An example of working with files\n"
                          "can be found in the repository (file test.txt). You can also add comments to files using "
                          "#.\n\n\n"
                          "### Basic troubleshooting:\n"
                          "Practice shows that the two main mistakes (on the user’s side) are: a lack of \n"
                          "understanding of what this or that module actually does (for example, running DIV_NN_Dk to\n"
                          "obtain the result of dividing natural numbers) and the incorrect format of the transferred\n"
                          "data (incorrect number of arguments or their incorrect type ). Both problems can be solved\n"
                          "by referring to the help for your module (HLP DIV_NN_Dk in this example)\n")


class CmdManager:
    def __init__(self):
        self.commands_dict = {
            "CMD": CMD(),
            "PUT": PUT(),
            "HLP": HLP(),
            "SCR": SCR(),
            "SRF": SRF()
        }

    def process_cmd(self, cmd_string: str, window):
        while cmd_string[-1] == " ":
            cmd_string = cmd_string[0:-1]
        while "  " in cmd_string or " |" in cmd_string or "| " in cmd_string:
            cmd_string = cmd_string.replace("  ", " ")
            cmd_string = cmd_string.replace(" |", "|")
            cmd_string = cmd_string.replace("| ", "|")
        if '|' in cmd_string:
            args = cmd_string.split('|')
            for i in range(len(args)):
                args[i] = args[i].split(' ')
            if len(args) == 0:
                raise ValueError("Empty string")
            command_tag = args[0][0]
            args[0] = args[0][1:]
        else:
            args = cmd_string.split(' ')
            if len(args) == 0:
                raise ValueError("Empty string")
            command_tag = args[0]
            args = args[1:]

        if command_tag not in self.commands_dict:
            raise ValueError("No such command")
        self.commands_dict[command_tag].execute(args, window)


class PUT(AbstractCommand):
    def execute(self, args, window: ConsoleApp):
        if len(args) != 2:
            raise ValueError("Invalid args for PUT command")
        pars = ArgumentParser()
        window.var_stack[args[0]] = pars.parse(args[1], window.var_stack)

    def reference(self) -> str:
        return "PUT [var_name] [value] - sets variable to given value"


class HLP(AbstractCommand):
    def execute(self, args, window: ConsoleApp):
        if len(args) == 0:
            return
        if len(args) != 1:
            raise ValueError("Invalid args for HLP command")
        name_parser = ModuleNameParser()
        if args[0] in name_parser.names:
            mod = name_parser.parse(args[0])
            window.display_text(mod.reference())

        if args[0] in window.manager.commands_dict:
            window.display_text(window.manager.commands_dict[args[0]].reference())
        if args[0] == "LIST":
            for value in name_parser.names.keys():
                parsed = name_parser.parse(value)
                window.display_text(value + ' : ' + parsed.reference().split('\n')[0])

    def reference(self) -> str:
        return ("HLP (optional: module_name OR cmd_name) \nEither prints general reference for program\n"
                "or if module_name is given prints reference for this specific module.")


class CMD(AbstractCommand):
    def execute(self, args, window: ConsoleApp):
        if len(args) != 2:
            raise ValueError("Invalid args for CMD command")
        cmd_name = args[0][0]
        args[0] = args[0][1:]
        name_parser = ModuleNameParser()
        type_parser = ArgumentParser()
        module = name_parser.parse(cmd_name)
        args_t = []
        for arg in args[1]:
            args_t.append(type_parser.parse(arg, window.var_stack))
        res = module.execute(args_t)
        if len(res) != len(args[0]):
            raise ValueError("Invalid args for CDM output")
        for i in range(len(args[0])):
            if args[0][i] == "OUT":
                window.display_text("Result #" + str(i) + ": " + str(res[i]))
            else:
                window.var_stack[args[0][i]] = res[i]

    def reference(self) -> str:
        return ("CMD [module_name] [var_name1] [var_name2] ... | [value1] [value2] ... \n"
                "Executes given module with given values and writes results to var_name1, var_name2")


class SCR(AbstractCommand):
    def execute(self, args, window: ConsoleApp):
        if len(args) != 1:
            raise ValueError("Invalid args for SCR command")
        file = open(args[0], 'r')
        text = file.read()
        file.close()
        window.loader.load(text)
        window.loader.run(window)

    def reference(self) -> str:
        return ("SCR [file_name] \n"
                "Load all commands from given file")


class SRF(AbstractCommand):
    def execute(self, args, window: ConsoleApp):
        if len(args) != 2:
            raise ValueError("Invalid args for SCR command")
        parser = ArgumentParser()
        res = parser.parse(args[1], window.var_stack)
        if not isinstance(res, bool):
            raise ValueError("Invalid args type for SCR command")

        if not res:
            return
        file = open(args[0], 'r')
        text = file.read()
        file.close()
        window.loader.load(text)
        window.loader.run(window)

    def reference(self) -> str:
        return ("SRF [file_name] [condition]\n"
                "Load all commands from given file if condition is TRUE")


class CMDLoader:
    def __init__(self):
        self.cmd_q = []
        self.running = False

    def load(self, cmd_block: str):
        split = cmd_block.split('\n')
        split_clear = []
        for st in split:
            if len(st) == 0:
                continue
            while st[0] in '\t ' and len(st) > 1:
                st = st[1:]
            if len(st) == 1 or st[0] == '#':
                continue
            split_clear.append(st)
        if self.running:
            self.cmd_q = [self.cmd_q[0]] + split_clear
        else:
            self.cmd_q = split_clear

    def run(self, window: ConsoleApp):
        if self.running:
            return
        self.running = True
        while len(self.cmd_q) > 0:
            window.manager.process_cmd(self.cmd_q[0], window)
            self.cmd_q = self.cmd_q[1:]

        window.update_right_area()
        self.running = False


# Создаем основное окно и запускаем приложение
if __name__ == "__main__":
    root = tk.Tk()
    app = ConsoleApp(root)
    root.mainloop()
