# Ejercicio 7

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print(f"Titular: {self.__titular}")
        print(f"Cantidad: {self.__cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad


#Ejercicio 8

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def es_titular_valido(self, edad):
        return 18 <= edad < 25

    def retirar(self, cantidad, edad):
        if self.es_titular_valido(edad):
            super().retirar(cantidad)
        else:
            print("Retirada no permitida: titular no válido")

    def mostrar(self):
        print("Cuenta Joven")
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Bonificación: {self.bonificacion}%")