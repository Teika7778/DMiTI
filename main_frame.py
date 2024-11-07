import tkinter as tk
from tkinter import ttk
from data_types import *
from command.generic import AbstractCommand
from parsers.argument_parser import ArgumentParser
from parsers.module_name_parser import ModuleNameParser


class ConsoleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Консольное окно")

        # ТУТ ВСЯКОЕ ВСПОМОГАТЕЛЬНОЕ, несерьёзное
        self.var_stack = dict()
        self.available_types = ["INT", "NAT", "RAT", "POL"]
        self.type_codes = {Integer: "INT", Natural: "NAT", Rational: "RAT", Polynomial: "POL", bool: "BIN"}
        self.manager = CmdManager()

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
        self.send_button = tk.Button(root, text="Отправить", command=self.send_input,
                                     bg=self.bg_color, fg=self.text_color, font=self.font_size)
        self.send_button.grid(row=2, column=1, sticky="e", padx=10, pady=(5, 2))

        # Привязка нажатия клавиши Enter к функции send_input
        self.input_field.bind("<Return>", self.send_input)

    def send_input(self, event=None):
        # Получаем текст от пользователя
        self.last_input = self.input_field.get()

        # Отображаем текст на текстовой области
        if self.last_input != '':
            self.display_text(f"Command executed: {self.last_input}")
            self.manager.process_cmd(self.last_input, self)

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
            args[0] = args[0][1:]
        else:
            args = cmd_string.split(' ')
            if len(args) == 0:
                raise ValueError()
            command_tag = args[0]
            args = args[1:]

        if command_tag not in self.commands_dict:
            raise ValueError()
        self.commands_dict[command_tag].execute(args, window)


class PUT(AbstractCommand):
    def execute(self, args, window: ConsoleApp):
        if len(args) != 2:
            raise ValueError()
        pars = ArgumentParser()
        window.var_stack[args[0]] = pars.parse(args[1], window.var_stack)

    def reference(self) -> str:
        pass


class HLP(AbstractCommand):
    def execute(self, args, window: ConsoleApp):
        if len(args) != 1:
            raise ValueError()
        name_parser = ModuleNameParser()
        if args[0] in name_parser.names:
            mod = name_parser.parse(args[0])
            window.display_text(mod.reference())

    def reference(self) -> str:
        pass


class CMD(AbstractCommand):
    def execute(self, args, window: ConsoleApp):
        print(args)
        if len(args) != 2:
            raise ValueError()
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
            raise ValueError()
        for i in range(len(args[0])):
            window.var_stack[args[0][i]] = res[i]

    def reference(self) -> str:
        pass


# Создаем основное окно и запускаем приложение
if __name__ == "__main__":
    root = tk.Tk()
    app = ConsoleApp(root)
    root.mainloop()
