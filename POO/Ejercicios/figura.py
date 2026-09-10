class figura:
    def __init__(self, largo):
        self.largo=largo

class circulo(figura):
    def area_circulo(self):
        area_circulo=self.largo* 3.1416
        print(f"el area  del circulo es:{area_circulo}")
    def perimetro_circulo(self):
        perimetro_circulo=3.1416*self.largo*self.largo
        print(f"el perimetro del circulo es:{perimetro_circulo}")

class cuadrado(figura):
    def area_cuadrado(self):
        area_cuadrado=self.largo*self.largo
        print(f"el area del cuadrado es:{area_cuadrado}")
    def perimetro_cuadrado(self):
        perimetro_cuadrado=self.largo+self.largo+self.largo+self.largo
        print(f"el perimetro del cuadrado es:{perimetro_cuadrado}")

circulo1= circulo(5)
cuadrado1=cuadrado(5)
circulo1.area_circulo()
circulo1.perimetro_circulo()
cuadrado1.area_cuadrado()
cuadrado1.perimetro_cuadrado()

            
        