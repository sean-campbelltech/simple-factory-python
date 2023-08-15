from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount: float):
        pass