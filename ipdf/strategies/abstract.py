from abc import ABC, abstractmethod


class AbstractStrategy(ABC):
    def __init__(self, name):
        self.__name = name

    def name(self):
        return self.__name

    @abstractmethod
    def get_move(self):
        """You have to implement this method in your strategy"""