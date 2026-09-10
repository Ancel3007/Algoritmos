class cuenta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.__saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("No se pueden depositar valores negativos")

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__saldo -= cantidad
        else:
            print("No se pueden retirar valores positivos")

    def mostrar_saldo(self):
        print(f"El saldo de la cuenta: {self.numero} es de: {self.__saldo}")

cuenta1 = cuenta(1111, 1000)            
cuenta1.depositar(3000)
cuenta1.retirar(1500)
print(cuenta1)
cuenta1.mostrar_saldo()


