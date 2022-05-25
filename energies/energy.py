from abc import ABCMeta, abstractmethod


class Energy:
    __metaclass__ = ABCMeta

    def __init__(self, gamma=1):
        self.gamma = gamma

    @abstractmethod
    def weight(self, i, j):
        pass

    @abstractmethod
    def calculate_energy_value(self, neurons):
        pass



