from abc import ABC, abstractmethod #Inicializa clases y funciones abstractas

class Empleado(ABC): #Crea una clase abstracta utilizando "ABC"
    def __init__(self, nombre, documento, salario): #Inicia la construcción del objeto (Parámetros)
        self.nombre = nombre
        self.documento = documento #Atributos
        self.__salario = salario

    @abstractmethod #Permite reutilizar funciones de una clase con un diferente método (Método Abstracto)
    def calcular_bonificacion(self):
        pass

    @property #Acceder a un atributo privado
    def salario(self):
        return self.__salario

    def mostrar_informacion(self): #Método
        print(f"Nombre: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Salario: {self.salario:,0.f}")
    
    def __str__(self): #Prueba unitaria
        return f"Nombre: {self.nombre} - Documento: {self.documento}"