from abc import ABC, abstractmethod


class AbstractCommand(ABC):
    @abstractmethod
    def execute(self, args, window):
        pass

    @abstractmethod
    def reference(self) -> str:
        pass
