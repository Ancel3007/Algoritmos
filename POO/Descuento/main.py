from producto import Producto

def main():
    
    producto1 = Producto(1425, "Tampico", 27, 3000)
    print(f"El descuento del producto: {producto1.nombre}, es de: {producto1.descuento()}")
    
    producto2 = Producto(7483, "Aloha", 53, 4500)
    print(f"El descuento del producto: {producto2.nombre}, es de: {producto2.descuento()}")

if __name__ == "__main__":
    main()