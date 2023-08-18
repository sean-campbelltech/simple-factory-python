from abc import ABC, abstractmethod
from decimal import Decimal


class Payment(ABC):

    @abstractmethod
    def pay(self, amount: Decimal):
        pass
