class Producto():
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aumentar_stock(self):
        self.stock += 1
        return f"El stock ha aumentado una unidad a: {self.stock}"

    def disminuir_stock(self):
        self.stock -= 1
        return f"El stock ha disminuido una unidad a: {self.stock}"
    
    def __str__(self):
        return f"ID: {self.id} - nombre: {self.nombre} - precio: {self.precio} - stock: {self.stock}"