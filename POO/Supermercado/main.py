from producto_perecedero import Producto_Perecedero
from producto_no_perecedero import Producto_No_Perecedero

def main():

    print("--------------IMPRESIÓN DE PRODUCTO PERECEDERO----------------")
    producto_perecedero = Producto_Perecedero(1054, "Arepa", 5000, 9, "15/09/2026")
    print(producto_perecedero)
    
    print("\n")
    
    print("--------------AUMENTO Y DISMINUCIÓN DE STOCK DE PRODUCTO PERECEDERO----------------")
    print(producto_perecedero.aumentar_stock())
    print(producto_perecedero.disminuir_stock())

    print("\n")

    print("--------------IMPRESIÓN DE PRODUCTO NO PERECEDERO----------------")
    producto_no_perecedero = Producto_No_Perecedero(5432, "Arroz", 3500, 25)
    print(producto_no_perecedero)
    
    print("\n")
    
    print("--------------AUMENTO Y DISMINUCIÓN DE STOCK DE PRODUCTO NO PERECEDERO----------------")
    print(producto_no_perecedero.aumentar_stock())
    print(producto_no_perecedero.disminuir_stock())

if __name__ == "__main__":
    main()