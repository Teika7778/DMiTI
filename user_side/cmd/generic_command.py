from abc import ABC, abstractmethod


# Базовый абстрактный класс для всех классов-функций
class AbstractCommand(ABC):
    @abstractmethod
    def execute(self, args, window):
        pass

    @abstractmethod
    def reference(self) -> str:
        pass