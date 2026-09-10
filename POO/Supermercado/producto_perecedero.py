from producto import Producto

class Producto_Perecedero(Producto):
    def __init__(self, id, nombre, precio, stock, fecha_vencimiento):
        super().__init__(id, nombre, precio, stock)
        self.fecha_vencimiento = fecha_vencimiento

    def aumentar_stock(self):
        return super().aumentar_stock()
    
    def disminuir_stock(self):
        return super().disminuir_stock()
    
    def __str__(self):
        return f"{super().__str__()} - fecha de vencimiento: {self.fecha_vencimiento}"