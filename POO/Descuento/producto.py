class Producto():
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        
    def descuento(self):
        while self.cantidad > 0:
            
            if self.cantidad < 10:
                return self.precio * 0.05
                
            elif self.cantidad > 10 and self.cantidad < 50:
                return self.precio * 0.10
                
            elif self.cantidad >= 49:
                return self.precio * 0.125
        
        else:
            print("No se pueden realizar descuentos con cantidades negativas o iguales a 0")