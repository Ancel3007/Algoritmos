from producto import Producto

class Producto_No_Perecedero(Producto):
    def aumentar_stock(self):
        return super().aumentar_stock()
    
    def disminuir_stock(self):
        return super().disminuir_stock()