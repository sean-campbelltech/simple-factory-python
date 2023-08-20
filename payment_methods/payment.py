from abc import ABC, abstractmethod
from decimal import Decimal


# AbstractProduct
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: Decimal):
        pass
