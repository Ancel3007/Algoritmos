from cilindro import Cilindro
from cubo import Cubo
from esfera import Esfera

def main():
    cilindro = Cilindro(5, " ", 7)
    print(f"El volumen del cilindro es de: {cilindro.calcular_volumen():.2f}")

    cubo = Cubo(10, " ")
    print(f"El volumen del cubo es de: {cubo.calcular_volumen():.2f}")

    esfera = Esfera(15, "")
    print(f"El volumen de la esfera es de: {esfera.calcular_volumen():.2f}")

if __name__ == "__main__":
    main()