from abc import ABC, abstractmethod


# Базовый абстрактный класс для всех классов-функций
class AbstractCommand(ABC):
    @abstractmethod
    def execute(self, args, var_stack):
        pass

    @abstractmethod
    def reference(self) -> str:
        pass