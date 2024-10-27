from abc import ABC, abstractmethod


# Базовый абстрактный класс для всех классов-функций
class AbstractModule(ABC):
    @abstractmethod
    def execute(self, args):
        pass

    @abstractmethod
    def reference(self) -> str:
        pass
