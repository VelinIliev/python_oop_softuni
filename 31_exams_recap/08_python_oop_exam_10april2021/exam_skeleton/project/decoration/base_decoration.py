from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    @abstractmethod
    def __init__(self, comfort: int, price: float):
        ...
        
