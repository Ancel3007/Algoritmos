class Vehicle:
    def __init__(self, brand, color, plate):
        self.brand = brand
        self.color = color
        self.plate = plate
        self.speed = 0
        self.brake = 0
        
    def acelerar (self):
        self.speed += 10
        print(f"La {self.brand} aceleró a {self.speed} km/h")
        
    def desacelerar(self):
        self.brake = self.speed - 10
        print(f"La {self.brand} desaceleró a {self.brake} km/h")
        
#creacion de los objetos:
mi_vehiculo = Vehicle("Honda", "Roja", "XRE300")
mi_vehiculo.acelerar()
mi_vehiculo.acelerar()
mi_vehiculo.desacelerar()

#agrgar el atributo plate
#agregar metodo desacelerar
#subir a git