from administrativo import Administrativo
from desarrollador import Desarrollador
from gerente import Gerente


def main():
    administrativo = Administrativo('Ximena','8989',1000)

    print(administrativo)

    print(administrativo.salario)

    desarrollador = Desarrollador('Ana',6400,1100,'Chatear')
    print(desarrollador)
    print(desarrollador.calcular_bonificacion())

    gerente = Gerente('Lyne',2323, 8000)
    print(gerente.calcular_bonificacion())

if __name__ == "__main__":
    main()