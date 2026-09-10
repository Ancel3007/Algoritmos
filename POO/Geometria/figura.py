from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, medida, pi):
        self.medida = medida
        self.pi = 3.1416

    @abstractmethod
    def calcular_volumen(self):
        pass