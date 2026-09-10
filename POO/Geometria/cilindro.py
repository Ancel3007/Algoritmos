from figura import Figura

class Cilindro(Figura):
    def __init__(self, medida, pi, altura):
        super().__init__(medida, pi)
        self.altura = altura

    def calcular_volumen(self):
        return self.pi * self.medida * self.medida * self.altura
    