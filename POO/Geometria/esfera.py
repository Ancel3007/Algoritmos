from figura import Figura

class Esfera(Figura):
    def calcular_volumen(self):
        return (4 / 3) * self.pi * self.medida * self.medida * self.medida