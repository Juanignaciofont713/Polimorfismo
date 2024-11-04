from .vehiculo import Vehiculo

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, capacidad_pasajeros):
        super().__init__(marca, modelo)
        self.capacidad_pasajeros = capacidad_pasajeros

    def describir(self):
        return f"{self.tipo_vehiculo()}: {self.marca} {self.modelo}, con capacidad para {self.capacidad_pasajeros} pasajeros"

    def tipo_vehiculo(self):
        return "Camioneta"